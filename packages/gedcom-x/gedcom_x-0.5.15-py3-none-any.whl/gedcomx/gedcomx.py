DEBUG = False

import json
import random
import string
import orjson

from functools import lru_cache
from typing import Any, Dict, List, Optional, Union, Generic, TypeVar, Iterable

"""
======================================================================
 Project: Gedcom-X
 File:    GedcomX.py
 Author:  David J. Cartwright
 Purpose: Object for working with Gedcom-X Data

 Created: 2025-07-25
 Updated:
    - 2025-08-31: _as_dict_ to only create entries in dict for fields that hold data,
    id_index functionality, will be used for resolution of Resources
    - 2025-09-03: _from_json_ refactor
    - 2025-09-09: added schema_class
   
======================================================================
"""

"""
======================================================================
GEDCOM Module Types
======================================================================
"""
from .agent import Agent
from .attribution import Attribution
from .document import Document
from .event import Event
from .group import Group
from .identifier import make_uid
from .logging_hub import logging, hub, ChannelConfig
from .person import Person
from .place_description import PlaceDescription
from .relationship import Relationship, RelationshipType
from .resource import Resource
from .schemas import extensible
from .source_description import ResourceType, SourceDescription
from .textvalue import TextValue
from .uri import URI
#=====================================================================

log = logging.getLogger("gedcomx")
serial_log = "gedcomx.serialization"
deserial_log = "gedcomx.serialization"



T = TypeVar("T")

class TypeCollection(Generic[T]):
    """
    A typed, indexable, iterable container with small indexes on id/name/uri.
    The class name stays 'Collection'; the element type is carried in `item_type`.
    """
    def __init__(self, item_type: type[T]):
        self.item_type: type[T] = item_type
        self._items: list[T] = []
        self._id_index: dict[Any, T] = {}
        self._name_index: dict[str, list[T]] = {}
        self._uri_index: dict[str, T] = {}
        self._uri = URI(path=f"/{item_type.__name__}s/")

    # --- core container protocol ---
    def __iter__(self):
        return iter(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def __contains__(self, item: object) -> bool:
        return item in self._items

    def __repr__(self) -> str:
        return f"Collection<{self.item_type.__name__}>({len(self)} items)"

    # --- indexing helpers ---
    def _update_indexes(self, item: T) -> None:
        if hasattr(item, "id") and getattr(item, "id") is not None:
            self._id_index[getattr(item, "id")] = item

        u = getattr(item, "uri", None)
        if u is not None and getattr(u, "value", None):
            self._uri_index[u.value] = item

        names = getattr(item, "names", None)
        if names:
            for nm in names:
                name_value = nm.value if isinstance(nm, TextValue) else getattr(nm, "value", None)
                if isinstance(name_value, str) and name_value:
                    self._name_index.setdefault(name_value, []).append(item)

    def _remove_from_indexes(self, item: T) -> None:
        if hasattr(item, "id"):
            self._id_index.pop(getattr(item, "id"), None)

        u = getattr(item, "uri", None)
        if u is not None and getattr(u, "value", None):
            self._uri_index.pop(u.value, None)

        names = getattr(item, "names", None)
        if names:
            for nm in names:
                name_value = nm.value if isinstance(nm, TextValue) else getattr(nm, "value", None)
                if isinstance(name_value, str):
                    lst = self._name_index.get(name_value)
                    if lst and item in lst:
                        lst.remove(item)
                        if not lst:
                            self._name_index.pop(name_value, None)

    # --- lookups ---
    def byId(self, id_: Any) -> T | None:
        return self._id_index.get(id_)

    def byUri(self, uri: Union[URI, str]) -> T | None:
        key = uri.value if isinstance(uri, URI) else str(uri) # type: ignore
        return self._uri_index.get(key)

    def byName(self, sname: str | None) -> list[T] | None:
        if not sname:
            return None
        return self._name_index.get(sname.strip(), None)

    # --- mutation ---
    def append(self, item: T) -> None:
        if not isinstance(item, self.item_type):
            raise TypeError(f"Expected {self.item_type.__name__}, got {type(item).__name__} {item}")

        # ensure/normalize item.uri
        u = getattr(item, "uri", None)
        if u is None:
            setattr(item, "uri", URI(path=f"/{self.item_type.__name__}s/", fragment=getattr(item, "id", None)))
        else:
            if not getattr(u, "path", None):
                u.path = f"/{self.item_type.__name__}s/"

        self._items.append(item)
        self._update_indexes(item)

    def extend(self, items: Iterable[T]) -> None:
        for it in items:
            self.append(it)

    def remove(self, item: T) -> None:
        if item not in self._items:
            raise ValueError("Item not found in the collection.")
        self._items.remove(item)
        self._remove_from_indexes(item)

    # --- convenience / serialization ---
    

    def __call__(self, **kwargs) -> list[T]:
        out: list[T] = []
        for item in self._items:
            for k, v in kwargs.items():
                if not hasattr(item, k) or getattr(item, k) != v:
                    break
            else:
                out.append(item)
        return out

    @property
    def _items_as_dict(self) -> dict:
        # {"Persons": [ ... ]}
        return {f"{self.item_type.__name__}s": [it._as_dict_ for it in self._items]}

    @property
    def _as_dict_(self) -> dict:
        # {"persons": [ ... ]}
        return {f"{self.item_type.__name__.lower()}s": [it._as_dict_ for it in self._items]}

    @property
    def json(self) -> str:
        return json.dumps(self._as_dict_, indent=4)


@extensible()
class GedcomX:
    """
    Main GedcomX Object representing a Genealogy. Stores collections of Top Level Gedcom-X Types.
    complies with GEDCOM X Conceptual Model V1 (http://gedcomx.org/conceptual-model/v1)

    Parameters
    ----------
    id : str
        Unique identifier for this Genealogy.
    attribution : Attribution Object
        Attribution information for the Genealogy
    filepath : str
        Not Implimented.
    description : str
        Description of the Genealogy: ex. 'My Family Tree'

    Raises
    ------
    ValueError
        If `id` is not a valid UUID.
    """
    version = 'http://gedcomx.org/conceptual-model/v1'

    def __init__(self, id: Optional[str] = None,
                 attribution: Optional[Attribution] = None,
                 filepath: Optional[str] = None,
                 description: Optional[str] = None,
                 persons: Optional[TypeCollection[Person]] = None,
                 relationships: Optional[TypeCollection[Relationship]] = None,
                 sourceDescriptions: Optional[TypeCollection[SourceDescription]] = None,
                 agents:  Optional[TypeCollection[Agent]] = None,
                 places: Optional[TypeCollection[PlaceDescription]] = None) -> None:
        
        self.id = id
        self.attribution = attribution
        self._filepath = None
        
        self.description = description
        self.sourceDescriptions = TypeCollection(SourceDescription)
        if sourceDescriptions: self.sourceDescriptions.extend(sourceDescriptions)
        self.persons = TypeCollection(Person)
        if persons: self.persons.extend(persons)
        self.relationships = TypeCollection(Relationship)
        if relationships: self.relationships.extend(relationships)      
        self.agents = TypeCollection(Agent)
        if agents: self.agents.extend(agents) 
        self.events = TypeCollection(Event)
        self.documents = TypeCollection(Document)
        self.places = TypeCollection(PlaceDescription)
        if places: self.places.extend(places)
        self.groups = TypeCollection(Group)

        self.relationship_table = {}

        #self.default_id_generator = make_uid

    @property
    def contents(self):
        return {
            "source_descriptions": len(self.sourceDescriptions),
            "persons": len(self.persons),
            "relationships": len(self.relationships),
            "agents": len(self.agents),
            "events": len(self.events),
            "documents": len(self.documents),
            "places": len(self.places),
            "groups": len(self.groups),
        }
            
    def add(self,gedcomx_type_object):
        if gedcomx_type_object:
            if isinstance(gedcomx_type_object,Person):
                self.add_person(gedcomx_type_object)
            elif isinstance(gedcomx_type_object,SourceDescription):
                self.add_source_description(gedcomx_type_object)
            elif isinstance(gedcomx_type_object,Agent):
                self.add_agent(gedcomx_type_object)
            elif isinstance(gedcomx_type_object,PlaceDescription):
                self.add_place_description(gedcomx_type_object)
            elif isinstance(gedcomx_type_object,Event):
                self.add_event(gedcomx_type_object)
            elif isinstance(gedcomx_type_object,Relationship):
                self.add_relationship(gedcomx_type_object)
            else:
                raise ValueError(f"I do not know how to add an Object of type {type(gedcomx_type_object)}")
        else:
            Warning("Tried to add a None type to the Geneology")

    def add_source_description(self,sourceDescription: SourceDescription):
        if sourceDescription and isinstance(sourceDescription,SourceDescription):
            if sourceDescription.id is None:
                assert False
            self.sourceDescriptions.append(item=sourceDescription)
            self.lastSourceDescriptionAdded = sourceDescription
        else:
            raise ValueError(f"When adding a SourceDescription, value must be of type SourceDescription, type {type(sourceDescription)} was provided")

    def add_person(self,person: Person):
        """Add a Person object to the Genealogy

        Args:
            person: Person Object

        Returns:
            None

        Raises:
            ValueError: If `person` is not of type Person.
        """
        if person and isinstance(person,Person):
            if person.id is None:
                person.id =self.make_id()
            self.persons.append(item=person)
        else:
            raise ValueError(f'person must be a Person Object not type: {type(person)}')
        
    def add_relationship(self,relationship: Relationship):
        if relationship and isinstance(relationship,Relationship):
            if isinstance(relationship.person1,Resource) and isinstance(relationship.person2,Resource):
                self.relationships.append(relationship)
                return
            elif isinstance(relationship.person1,Person) and isinstance(relationship.person2,Person):

                if relationship.person1:
                    if relationship.person1.id is None:
                        relationship.person1.id = self.make_id()
                    if not self.persons.byId(relationship.person1.id):
                        self.persons.append(relationship.person1)
                    if relationship.person1.id not in self.relationship_table:
                        self.relationship_table[relationship.person1.id] = []
                    self.relationship_table[relationship.person1.id].append(relationship)
                    relationship.person1._add_relationship(relationship)
                else:
                    pass
                
                if relationship.person2:
                    if relationship.person2.id is None:
                        relationship.person2.id = self.make_id() #TODO
                    if not self.persons.byId(relationship.person2.id):
                        self.persons.append(relationship.person2)
                    if relationship.person2.id not in self.relationship_table:
                        self.relationship_table[relationship.person2.id] = []
                    self.relationship_table[relationship.person2.id].append(relationship)
                    relationship.person2._add_relationship(relationship)
                else:
                    pass

                self.relationships.append(relationship)
        else:
            raise ValueError()
    
    def add_place_description(self,placeDescription: PlaceDescription):
        if placeDescription and isinstance(placeDescription,PlaceDescription):
            if placeDescription.id is None:
                Warning("PlaceDescription has no id")
            self.places.append(placeDescription)

    def add_agent(self,agent: Agent):
        if isinstance(agent,Agent) and agent is not None:
            if self.agents.byId(agent.id) is not None:  
                log.info(f"Did not add agent with Duplicate ID: {agent.id}")  
                return False  
            self.agents.append(agent)
        else:
            raise ValueError()
    
    def add_event(self,event_to_add: Event):
        if event_to_add and isinstance(event_to_add,Event):
            if event_to_add.id is None: event_to_add.id = make_uid()
            for current_event in self.events:
                if event_to_add == current_event:
                    print("DUPLICATE EVENT")
                    print(event_to_add._as_dict_)
                    print(current_event._as_dict_)
                    
                    return
            self.events.append(event_to_add)
        else:
            raise ValueError

    @lru_cache(maxsize=65536)
    def get_person_by_id(self,id: str):
        filtered = [person for person in self.persons if getattr(person, 'id') == id]
        if filtered: return filtered[0]
        return None
     
    @lru_cache(maxsize=65536)
    def source_by_id(self,id: str):
        filtered = [source for source in self.sourceDescriptions if getattr(source, 'id') == id]
        if filtered: return filtered[0]
        return None        

    @property
    def id_index(self) -> Dict[Any,Union[SourceDescription,Person,Relationship,Agent,Event,Document,PlaceDescription,Group]]:
        combined = {**self.sourceDescriptions._id_index,
                    **self.persons._id_index,
                    **self.relationships._id_index,
                    **self.agents._id_index,
                    **self.events._id_index,
                    **self.documents._id_index,
                    **self.places._id_index,
                    **self.groups._id_index
        }
        #for i in combined.keys():
        #    combined[i] = str(type(combined[i]).__name__)
        return combined

    @property
    def _as_dict(self) -> dict[str, Any]:
        from .serialization import Serialization
        return Serialization.serialize(self)
        
    @property
    def json(self) -> bytes:
        """
        JSON Representation of the GedcomX Genealogy.

        Returns:
            str: JSON Representation of the GedcomX Genealogy in the GEDCOM X JSON Serialization Format
        """
        return orjson.dumps(self._as_dict,option= orjson.OPT_INDENT_2 | orjson.OPT_APPEND_NEWLINE)

    @lru_cache(maxsize=65536)
    def _resolve(self,resource_reference: Union[URI,Resource]):
        #TODO indept URI search, URI index in collections
        if resource_reference:
            if isinstance(resource_reference,Resource):
                log.warning(f"Resource: {resource_reference}")
                ref_id = resource_reference.resource
                ref_id = ref_id.partition("#")[2] if ref_id else None
                ref = self.id_index.get(ref_id,None)
            elif isinstance(resource_reference,URI):
                ref_id = resource_reference.value
                ref_id = ref_id.partition("#")[2] if ref_id else None
                ref = self.id_index.get(ref_id,None)    
            else:
                raise TypeError()
            
            if ref is None: log.warning(f"Failed to locate object with id: {ref_id} from {type(resource_reference).__name__}")
            else: log.info(f"Found id: {ref_id} of type {type(ref).__name__}")
            return ref
        else: log.info(f"_resolve was passed a NoneType as a reference.")

    