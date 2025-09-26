import logging
import mimetypes
import re
import xml.etree.ElementTree as ET

from typing import Any, Mapping
from typing import Iterable, Callable, TypeVar, Hashable, List, Optional

import math
import shutil

"""
======================================================================
 Project: Gedcom-X
 File:    converter.py
 Author:  David J. Cartwright
 Purpose: convert gedcom versions

 Created: 2025-08-25
 Updated:
   - 2025-09-01: added docs and fixed imports for lowercase module names
   
======================================================================
"""

"""
======================================================================
GEDCOM Module Types
======================================================================
"""

from .address import Address
from .agent import Agent
from .attribution import Attribution
from .conclusion import Conclusion
from .coverage import Coverage
from .date import Date, date_to_timestamp
from .document import Document
from .evidence_reference import EvidenceReference
from .exceptions import TagConversionError, ConversionErrorDump
from .event import Event, EventType, EventRole, EventRoleType
from .fact import Fact, FactType, FactQualifier
#from .gedcom import Gedcom
from .gedcom.records.element import Element
from .gedcom.gedcom5x import Gedcom5x
from .gedcomx import GedcomX
from .gender import Gender, GenderType
from .group import Group
from .identifier import Identifier, IdentifierType
from .logging_hub import hub, ChannelConfig
from .name import Name, NameType, NameForm, NamePart, NamePartType, NamePartQualifier
from .note import Note
from .online_account import OnlineAccount
from .person import Person
from .place_description import PlaceDescription
from .place_reference import PlaceReference
from .qualifier import Qualifier
from .relationship import Relationship, RelationshipType
from .resource import Resource
from .schemas import fact_from_even_tag
from .source_citation import SourceCitation
from .source_description import SourceDescription, ResourceType
from .source_reference import SourceReference, KnownSourceReference
# from .subject import Subject
from .textvalue import TextValue
#from .topleveltypecollection import TopLevelTypeCollection
from .uri import URI
from .logging_hub import hub, logging
from .identifier import make_uid
"""
======================================================================
Logging
======================================================================
"""
log = logging.getLogger("gedcomx")
serial_log = "gedcomx.serialization"
convert_log = "gedcomx.convert.GEDCOM5x"
#=====================================================================



hub.start_channel(
    ChannelConfig(
        name=convert_log,
        path=f"logs/{convert_log}.log",
        level=logging.DEBUG,
        rotation="size:10MB:3",   # rotate by size, keep 3 backups
    ))

T = TypeVar("T")
K = TypeVar("K", bound=Hashable)

class GedcomConverter():
    def __init__(self) -> None:
        self.gedcomx: GedcomX = GedcomX()
        self.object_map: dict[Any, Any] = {-1:self.gedcomx}
        self.missing_handler_count = {}
    
    type_name_type = {
        'aka': NameType.AlsoKnownAs
    }

    personal_events = ["BARM", "BASM", "BLES", "CHRA", "CONF", "CENS", "CREM", "EMIG", "GRAD", "NATU", "ORDN", "RETI", "WILL"]

    @property
    def ignored_tags(self):
        return self.missing_handler_count if self.missing_handler_count != {} else None

    def clean_str(self, text: str | None) -> str:
        # Regular expression to match HTML/XML tags
        if text is None or text.strip() == '':
            return ""
        clean_text = re.sub(r'<[^>]+>', '', text)
        
        return clean_text
    
    def parse_gedcom5x_record(self,record: Element):
        if record is not None: 
            with hub.use(convert_log):
                log.debug(f"{record.tag} with id: {record.xref} and value {record.value} has {len(record.subRecords())} subRecords")
                handler_name = 'handle_' + record.tag.lower() 
                if record.tag in self.personal_events:
                    self.handle_pevent(record)
                elif hasattr(self,handler_name):                                            
                    log.info(f'Using {handler_name} to pars Record: {record.describe()}')         
                    handler = getattr(self,handler_name)            
                    handler(record)
                    if record.tag != 'FAM' and (sub_records := record.subRecords()) is not None:
                        for sub_record in sub_records:
                            log.debug(sub_record.describe())
                            self.parse_gedcom5x_record(sub_record)

                else:
                    if record.tag in self.missing_handler_count:
                        self.missing_handler_count[record.tag] += 1
                    else:
                        self.missing_handler_count[record.tag] = 1
                    log.error(f'Failed Parsing Record: {record.describe()}')        
        else:
            assert False
    
    def handle__apid(self, record: Element):
        if isinstance(self.object_map[record.level-1], SourceReference):
            self.object_map[record.level-1].description.add_identifier(Identifier(type=IdentifierType.Other, value=[URI.from_url('APID://' + record.value if record.value else '')])) # type: ignore
        elif isinstance(self.object_map[record.level-1], SourceDescription):
            self.object_map[record.level-1].add_identifier(Identifier(type=IdentifierType.Other,value=[URI.from_url('APID://' + record.value if record.value else '')])) # type: ignore
        else:
            self.convert_exception_dump(record=record)

    def handle__meta(self, record: Element):
        if isinstance(self.object_map[record.level-1], SourceDescription):
            gxobject = Note(text=self.clean_str(record.value if record.value else 'Warning: This NOTE had not content.'))
            self.object_map[record.level-1].add_note(gxobject)
            
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle__wlnk(self, record: Element):
        return self.handle_sour(record)

    def handle_addr(self, record: Element):
        if isinstance(self.object_map[record.level-1], Agent):
            # TODO CHeck if URL?
            if record.value is not None and self.clean_str(record.value):
                gxobject = Address(value=self.clean_str(record.value))
            else:
                gxobject = Address()
            self.object_map[record.level-1].address = gxobject
            self.object_map[record.level] = gxobject
        else:
            raise ValueError(f"I do not know how to handle an 'ADDR' tag for a {type(self.object_map[record.level-1])}")
    
    def handle_adr1(self, record: Element):
        if isinstance(self.object_map[record.level-1], Address):
            if record.value is not None and self.clean_str(record.value):
                self.object_map[record.level-1].street = self.clean_str(record.value)
            else:
                self.convert_exception_dump(record=record)     
        else:
            self.convert_exception_dump(record=record)
    
    def handle_adr2(self, record: Element):
        if isinstance(self.object_map[record.level-1], Address):
            if record.value is not None and self.clean_str(record.value):
                self.object_map[record.level-1].street2 = self.clean_str(record.value)        
            else:
                self.convert_exception_dump(record=record)     
        else:
            self.convert_exception_dump(record=record)
    
    def handle_adr3(self, record: Element):
        if isinstance(self.object_map[record.level-1], Address):
            if record.value is not None and self.clean_str(record.value):
                self.object_map[record.level-1].street3 = self.clean_str(record.value)  
            else:
                self.convert_exception_dump(record=record)     
        else:
            self.convert_exception_dump(record=record)
    
    def handle_adr4(self, record: Element):
        if isinstance(self.object_map[record.level-1], Address):
            if record.value is not None and self.clean_str(record.value):
                self.object_map[record.level-1].street4 = self.clean_str(record.value)        
        else:
            self.convert_exception_dump(record=record)
    
    def handle_adr5(self, record: Element):
        if isinstance(self.object_map[record.level-1], Address):
            if record.value is not None and self.clean_str(record.value):
                self.object_map[record.level-1].street5 = self.clean_str(record.value)        
        else:
            self.convert_exception_dump(record=record)
    
    def handle_adr6(self, record: Element):
        if isinstance(self.object_map[record.level-1], Address):
            if record.value is not None and self.clean_str(record.value):
                self.object_map[record.level-1].street5 = self.clean_str(record.value)        
        else:
            self.convert_exception_dump(record=record)
        
    def handle_phon(self, record: Element):
        if isinstance(self.object_map[record.level-1], Agent):
            if record.value is not None and self.clean_str(record.value):
                self.object_map[record.level-1].phones.append(self.clean_str(record.value))        
        else:
            self.convert_exception_dump(record=record)
    
    def handle_email(self, record: Element):
        if isinstance(self.object_map[record.level-1], Agent):
            if record.value is not None and self.clean_str(record.value):
                self.object_map[record.level-1].emails.append(self.clean_str(record.value))        
        else:
            self.convert_exception_dump(record=record)
    
    def handle_fax(self, record: Element):
        if isinstance(self.object_map[record.level-1], Agent):
            if record.value is not None and self.clean_str(record.value):
                self.object_map[record.level-1].emails.append('FAX:' + (self.clean_str(record.value) if record.value is not None else ''))        
        else:
            self.convert_exception_dump(record=record)

    def handle_adop(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Fact(type=FactType.Adoption)
            self.object_map[record.level-1].add_fact(gxobject)

            
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_auth(self, record: Element):
        if isinstance(self.object_map[record.level-1], SourceDescription):
            if record.value is not None and self.gedcomx.agents.byName(record.value):
                gxobject = self.gedcomx.agents.byName(record.value)[0]
            else:
                gxobject = Agent(names=[TextValue(record.value)])
                self.gedcomx.add_agent(gxobject)
            
            self.object_map[record.level-1].author = gxobject
            
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_bapm(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Fact(type=FactType.Baptism)
            self.object_map[record.level-1].add_fact(gxobject)

            
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_birt(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Fact(type=FactType.Birth)
            self.object_map[record.level-1].add_fact(gxobject)
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_buri(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Fact(type=FactType.Burial)
            self.object_map[record.level-1].add_fact(gxobject)

            
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_caln(self, record: Element):
        if isinstance(self.object_map[record.level-1], SourceReference):
            self.object_map[record.level-1].description.add_identifier(Identifier(type=IdentifierType.Other,value=[URI.from_url('Call Number:' + record.value if record.value else '')])) # type: ignore
        elif isinstance(self.object_map[record.level-1], SourceDescription):
            self.object_map[record.level-1].add_identifier(Identifier(type=IdentifierType.Other,value=[URI.from_url('Call Number:' + record.value if record.value else '')])) # type: ignore
        elif isinstance(self.object_map[record.level-1], Agent):
            pass
            # TODO Why is GEDCOM so shitty? A callnumber for a repository?
        else:
            self.convert_exception_dump(record=record)

    def handle_chan(self, record: Element):
        if isinstance(self.object_map[record.level-1], SourceDescription):
            date = record.subRecord('DATE')
            if date is not None:
                self.object_map[record.level-1].created = Date(date.value)
        elif isinstance(self.object_map[record.level-1], Agent):
            if self.object_map[record.level-1].attribution is None:
                gxobject = Attribution()
                self.object_map[record.level-1].attribution = gxobject
                self.object_map[record.level] = gxobject
            else:
                self.convert_exception_dump(record=record)
        elif isinstance(self.object_map[record.level-1], Person):
            if self.object_map[record.level-1].attribution is None:
                gxobject = Attribution()
                self.object_map[record.level-1].attribution = gxobject
                self.object_map[record.level] = gxobject
            else:
                self.convert_exception_dump(record=record)
        else:
            self.convert_exception_dump(record=record)

    def handle_chr(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Fact(type=FactType.Christening)
            self.object_map[record.level-1].add_fact(gxobject)

            
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_city(self, record: Element):
        if isinstance(self.object_map[record.level-1], Address):
            if record.value is not None:
                self.object_map[record.level-1].city = self.clean_str(record.value)
            else: raise ValueError('Record had no value')
        else:
            raise ValueError(f"I do not know how to handle an 'CITY' tag for a {type(self.object_map[record.level-1])}")
        
    def handle_conc(self, record: Element):
        obj_map = sorted(self.object_map.items(), reverse=True)
        obj_map = dict(obj_map)
        for k in obj_map:
            log.debug(f"{k}\t{obj_map[k]}\t{str(obj_map[k])}")
            print(f"{k}\t{obj_map[k]}\t{str(obj_map[k])}")
        print(f"{record.describe()}")
        log.debug(f"{record.describe()}")
        if isinstance(self.object_map[record.level-1], Note):
            gxobject = self.clean_str(str(record.value))
            self.object_map[record.level-1].append(gxobject)
        elif isinstance(self.object_map[record.level-1], Agent):
            gxobject = str(record.value)
            self.object_map[record.level-1]._append_to_name(gxobject)
        elif isinstance(self.object_map[record.level-1], Qualifier):
            gxobject = str(record.value)
            self.object_map[record.level-1]._append(gxobject)
        elif isinstance(self.object_map[record.level-1], TextValue):
            #gxobject = TextValue(value=self.clean_str(record.value))
            self.object_map[record.level-1]._append_to_value(record.value)
        elif isinstance(self.object_map[record.level-1], SourceReference):
            self.object_map[record.level-1].append(record.value)
        elif isinstance(self.object_map[record.level-1], Fact):
            self.object_map[record.level-1].notes[0].text += record.value
        elif isinstance(self.object_map[record.level-1], str):
            self.object_map[record.level-1] = self.object_map[record.level-1] = record.value
            
        else:
            self.convert_exception_dump(record=record)

    def handle_cont(self, record: Element):
        if isinstance(self.object_map[record.level-1], Note):
            gxobject = str(" " + record.value if record.value else '')
            self.object_map[record.level-1].append(gxobject)
        elif isinstance(self.object_map[record.level-1], Agent):
            gxobject = str(" " + record.value if record.value else '')
        elif isinstance(self.object_map[record.level-1], Qualifier):
            gxobject = str(" " + record.value if record.value else '')
            self.object_map[record.level-1]._append(gxobject)
        elif isinstance(self.object_map[record.level-1], TextValue):
            #gxobject = TextValue(value="\n" + record.value)
            self.object_map[record.level-1]._append_to_value(record.value if record.value else '\n')
        elif isinstance(self.object_map[record.level-1], SourceReference):
            self.object_map[record.level-1].append(record.value)
        elif isinstance(self.object_map[record.level-1], Address):
            self.object_map[record.level-1]._append(record.value)
        elif isinstance(self.object_map[record.level-1], str):
            self.object_map[record.level-1] = self.object_map[record.level-1] = record.value
        else:
            self.convert_exception_dump(record=record)
    
    def handle_crea(self, record: Element):
        if isinstance(self.object_map[record.level-1], SourceDescription):
            date = record.subRecord('DATE')
            if  date is not None and date != []:
                self.object_map[record.level-1].created = Date(original=date[0].value)
            else: raise ValueError('DATE had not value')                     
            
        elif isinstance(self.object_map[record.level-1], Agent):
            if self.object_map[record.level-1].attribution is None:
                gxobject = Attribution()
                self.object_map[record.level-1].attribution = gxobject
                
                self.object_map[record.level] = gxobject
            else:
                log.info(f"[{record.tag}] Attribution already exists for SourceDescription with id: {self.object_map[record.level-1].id}")
        else:
            raise ValueError(f"Could not handle '{record.tag}' tag in record {record.describe()}, last stack object {self.object_map[record.level-1]}")
    
    def handle__crea(self, record: Element):
        if isinstance(self.object_map[record.level-1], SourceDescription):
            if  record.value is not None:
                self.object_map[record.level-1].created = Date(original=record.value)
            else: raise ValueError('DATE had not value')   

    def handle_ctry(self, record: Element):
        if isinstance(self.object_map[record.level-1], Address):
            if record.value is not None:
                self.object_map[record.level-1].country = self.clean_str(record.value)
            else:
                raise ValueError('Recrod had no value')
        else:
            raise ValueError(f"I do not know how to handle an '{record.tag}' tag for a {type(self.object_map[record.level-1])}")
     
    def handle_data(self, record: Element) -> None:
        if record.value != '' and record.value == 'None':
            assert False
        self.object_map[record.level] = self.object_map[record.level-1]

    def handle_date(self, record: Element):
        if record.parent is not None and record.parent.tag == 'PUBL':
            #gxobject = Date(original=record.value) #TODO Make a parser for solid timestamps
            #self.object_map[0].published = gxobject
            #self.object_map[0].published = date_to_timestamp(record.value) if record.value else None 
            self.object_map[0].published = record.value    
            #
            #self.object_map[record.level] = gxobject
        elif isinstance(self.object_map[record.level-1], Event):
            self.object_map[record.level-1].date = Date(original=record.value)
        elif isinstance(self.object_map[record.level-1], Fact):
            self.object_map[record.level-1].date = Date(original=record.value)
        elif record.parent is not None and record.parent.tag == 'DATA' and isinstance(self.object_map[record.level-2], SourceReference):
            gxobject = Note(text='Date: ' + record.value if record.value else '')
            self.object_map[record.level-2].description.add_note(gxobject)
            
            self.object_map[record.level] = gxobject
        elif isinstance(self.object_map[record.level-1], SourceDescription):
            
            self.object_map[record.level-1].ctreated = record.value #TODO String to timestamp
        elif isinstance(self.object_map[record.level-1], Attribution):
            if record.parent is not None and record.parent.tag == 'CREA':
                self.object_map[record.level-1].created = record.value #TODO G7
            elif record.parent is not None and record.parent.tag == "CHAN":
                self.object_map[record.level-1].modified = record.value #TODO G7
            elif (created := self.object_map[record.level-1].created) is None:
                self.object_map[record.level-1].created = record.value
        elif isinstance(self.object_map[0], Attribution):
            if self.object_map[0].created is not None:
                self.object_map[0].created = record.value
            else:
                log.warning('Attribution already had created date')
        elif record.parent is not None and record.parent.tag in ['CREA','CHAN']:
            pass
        

        else:
            self.convert_exception_dump(record=record)

    def handle_deat(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Fact(type=FactType.Death)
            self.object_map[record.level-1].add_fact(gxobject)

            
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_pevent(self, record: Element):
        # EVEN (Fact) specific to INDI (Person)
        if (fact_type := fact_from_even_tag(record.tag)) is not None:
            if isinstance(self.object_map[record.level-1], Person):
                gxobject = Fact(type=fact_type)
                self.object_map[record.level-1].add_fact(gxobject)
                self.object_map[record.level] = gxobject

    def handle_even(self, record: Element):
        # TODO If events in a @S, check if only 1 person matches?
        # TODO, how to deal with and diferentiate Events
        if record.value and (not record.value.strip() == ''):
            values = [value.strip() for value in record.value.split(",")]
            for value in values:
                if (fact_type := fact_from_even_tag(value)) is not None:
                    if isinstance(self.object_map[record.level-1], Person):
                        gxobject = Fact(type=fact_type)
                        self.object_map[record.level-1].add_fact(gxobject)
                        self.object_map[record.level] = gxobject

                    elif isinstance(self.object_map[record.level-1], SourceDescription):
                        gxobject = Event(type=fact_type,sources=[self.object_map[record.level-1]])
                        self.gedcomx.add_event(gxobject)
                        self.object_map[record.level] = gxobject
                    else:
                        self.convert_exception_dump(record=record)
                else:
                    log.warning(f"EVEN type is not known {record.describe()}")
                    gxobject = Event(roles=[EventRole(person=self.object_map[record.level],type=EventRoleType.Principal)])
                    self.gedcomx.add_event(gxobject)
                    self.object_map[record.level] = gxobject
                  
        else:
            if (even_type := record.subRecord('TYPE')) is not None:
                
                if possible_fact := FactType.guess(even_type.value):
                    gxobject = Fact(type=possible_fact)
                    self.object_map[record.level-1].add_fact(gxobject)                   
                    self.object_map[record.level] = gxobject
                    return
                elif EventType.guess(even_type.value):
                    if isinstance(self.object_map[record.level-1], Person):
                        gxobject = Event(type=EventType.guess(even_type.value), roles=[EventRole(person=self.object_map[record.level-1], type=EventRoleType.Principal)])
                        self.gedcomx.add_event(gxobject)
                        
                        self.object_map[record.level] = gxobject
                    return
                else:
                    if isinstance(self.object_map[record.level-1], Person):
                        gxobject = Event(type=None, roles=[EventRole(person=self.object_map[record.level-1], type=EventRoleType.Principal)])
                        gxobject.add_note(Note(subject='Event', text=record.value))
                        self.gedcomx.add_event(gxobject)
                        
                        self.object_map[record.level] = gxobject
                        return
                        
                    else:
                        assert False

    def handle_exid(self,record: Element):
        if record.value:
            gxobject = Identifier(type=IdentifierType.External,value=[URI._from_json_(record.value) if record.value else URI()]) # type: ignore
            self.object_map[record.level-1].add_identifier(gxobject)       
            self.object_map[record.level] = gxobject
        else: raise ValueError('Record had no value')

    def handle_fam(self, record: Element) -> None:
        if record.tag != 'FAM' or record.level != 0:
            raise ValueError("Invalid record: Must be a level 0 FAM record")

        husband, wife, children = None, None, []

        husband_record = record.subRecords('HUSB')
        if husband_record is not None:
            
            id = husband_record[0].xref if len(husband_record) > 0 else None
            if id:
                husband = self.gedcomx.get_person_by_id(id)
            

        wife_record = record.subRecords('WIFE')
        if wife_record:
            
            id = wife_record[0].xref if len(wife_record) > 0 else None
            if id:
                wife = self.gedcomx.get_person_by_id(id)
            

        children_records = record.subRecords('CHIL')
        if children_records:
            for child_record in children_records:
                id = child_record.xref
                if id:
                    child = self.gedcomx.get_person_by_id(id)
                    if child:
                        children.append(child)

        if husband:
            
            for child in children:
                relationship = Relationship(person1=husband, person2=child, type=RelationshipType.ParentChild)
                self.gedcomx.add_relationship(relationship)
        if wife:
            
            for child in children:
                relationship = Relationship(person1=wife, person2=child, type=RelationshipType.ParentChild)
                self.gedcomx.add_relationship(relationship)
        if husband and wife:
            
            relationship = Relationship(person1=husband, person2=wife, type=RelationshipType.Couple)
            self.gedcomx.add_relationship(relationship)
            self.object_map[record.level] = relationship
        
        if (marr_record := record.subRecord('MARR')) is not None:
            self.handle_marr(marr_record)
    
    def handle_famc(self, record: Element) -> None:
        #TODO
        return

    def handle_fams(self, record: Element) -> None:
        #TODO
        return

    def handle_file(self, record: Element):
        if record.value and record.value.strip() != '':
            #raise ValueError(f"I did not expect the 'FILE' tag to have a value: {record.value}")
            #TODO Handle files referenced here
            ...
        elif isinstance(self.object_map[record.level-1], SourceDescription):
            ...
        self.object_map[record.level-1].resourceType = ResourceType.DigitalArtifact
           
    def handle_form(self, record: Element):
        if record.parent is not None and record.parent.tag == 'FILE' and isinstance(self.object_map[record.level-2], SourceDescription):
            if record.value and record.value.strip() != '':
                mime_type, _ = mimetypes.guess_type('placehold.' + record.value)
                if mime_type:
                    self.object_map[record.level-2].mediaType = mime_type
                else:
                    log.error(f"Could not determing mime type from {record.value}")
        elif isinstance(self.object_map[record.level-1], PlaceDescription):
            self.object_map[record.level-1].names.append(TextValue(value=record.value))
        elif record.parent is not None and record.parent.tag == 'TRAN':
            pass #TODO
        else:
            log.error(f"raise TagConversionError(record=record,levelstack=self.object_map")

    def handle_fsid(self,record: Element):
        if record.value:
            gxobject = Identifier(type=IdentifierType.FamilySearchId,value=[URI._from_json_(record.value) if record.value else URI()]) # type: ignore
            self.object_map[record.level-1].add_identifier(gxobject)       
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_givn(self, record: Element):
        if isinstance(self.object_map[record.level-1], Name):
            given_name = NamePart(value=record.value, type=NamePartType.Given)
            self.object_map[record.level-1]._add_name_part(given_name)
        else:
            self.convert_exception_dump(record=record)

    def handle_head(self, record: Element):
        gxobject = Attribution()
        self.gedcomx.attribution = gxobject
        self.object_map[record.level] = gxobject

    def handle_indi(self, record: Element):
        person = self.gedcomx.persons.byId(record.xref)
        if person is None:
            log.warning('Had to create person with id {recrod.xref}')
            if isinstance(record.xref,str):
                person = Person(id=record.xref)
                self.gedcomx.add_person(person)
            else:
                self.convert_exception_dump(record=record)  
        self.object_map[record.level] = person

    def handle_immi(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Fact(type=FactType.Immigration)
            self.object_map[record.level-1].add_fact(gxobject)

            
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_map(self, record: Element):
        if isinstance(self.object_map[record.level-1],PlaceReference):
            self.object_map[record.level] = self.object_map[record.level-1].description
        else:
            self.convert_exception_dump(record=record)

    def handle_marr(self, record: Element):
        """
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Fact(type=FactType.Marriage)
            self.object_map[record.level-1].add_fact(gxobject)

            
            self.object_map[record.level] = gxobject
        """

        if (add_fact := getattr(self.object_map[record.level-1],'add_fact',None)) is not None:
            gxobject = Fact(type=FactType.Marriage)
            add_fact(gxobject)
            self.object_map[record.level] = gxobject       
        else:
            self.convert_exception_dump(record=record)

    def handle_lati(self, record: Element):
        if isinstance(self.object_map[record.level-1], PlaceDescription):
            self.object_map[record.level-1].latitude = record.value
        else:
            self.convert_exception_dump(record=record)

    def handle_long(self, record: Element):
        if isinstance(self.object_map[record.level-1], PlaceDescription):
            self.object_map[record.level-1].longitude = record.value
        else:
            self.convert_exception_dump(record=record)

    def handle__link(self,record: Element):
        if isinstance(self.object_map[record.level-1], SourceReference):
            gxobject = Identifier([URI.from_url(record.value)],IdentifierType.External) # type: ignore
            self.object_map[record.level-1].description.add_identifier(gxobject)
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle__milt(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Fact(type=FactType.MilitaryService)
            self.object_map[record.level-1].add_fact(gxobject)
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_name(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Name.simple(record.value if record.value else 'WARNING: NAME had no value')
            #gxobject = Name(nameForms=[NameForm(fullText=record.value)], type=NameType.BirthName)
            self.object_map[record.level-1].add_name(gxobject)
            self.object_map[record.level] = gxobject
        elif isinstance(self.object_map[record.level-1], Agent):
            gxobject = TextValue(value=record.value)
            self.object_map[record.level-1].add_name(gxobject)    
        else:
            self.convert_exception_dump(record=record)

    def handle_note(self, record: Element):
        if isinstance(self.object_map[record.level-1], SourceDescription):
            gxobject = Note(text=self.clean_str(record.value))
            self.object_map[record.level-1].add_note(gxobject)

            
            self.object_map[record.level] = gxobject
        elif isinstance(self.object_map[record.level-1], SourceReference):
            if self.object_map[record.level-1].description is not None:
                gxobject = Note(text=self.clean_str(record.value))
                self.object_map[record.level-1].description.add_note(gxobject)
                self.object_map[record.level] = gxobject
            else:
                log.error('SourceReference does not have description')

            
            
        elif isinstance(self.object_map[record.level-1], Conclusion):
            gxobject = Note(text=record.value)
            self.object_map[record.level-1].add_note(gxobject)

            
            self.object_map[record.level] = gxobject
        elif isinstance(self.object_map[record.level-1], Agent):
            gxobject = Note(text=record.value)
            self.object_map[record.level-1].add_note(gxobject)           
            self.object_map[record.level] = gxobject
        elif isinstance(self.object_map[record.level-1], Attribution):
            if self.object_map[record.level-1].changeMessage is None:
                gxobject = record.value
                self.object_map[record.level-1].changeMessage = gxobject
            else:
                gxobject = self.object_map[record.level-1].changeMessage + '' + record.value
                self.object_map[record.level-1].changeMessage = gxobject
            
            self.object_map[record.level] = gxobject
        elif isinstance(self.object_map[record.level-1], Note):
            gxobject = Note(text=self.clean_str(record.value))
            self.object_map[record.level-2].add_note(gxobject)          
            self.object_map[record.level] = gxobject

        else:
            self.convert_exception_dump(record=record)

    def handle_nsfx(self, record: Element):
        if isinstance(self.object_map[record.level-1], Name):
            surname = NamePart(value=record.value, type=NamePartType.Suffix)
            self.object_map[record.level-1]._add_name_part(surname)
        else:
            self.convert_exception_dump(record=record)

    def handle_occu(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Fact(type=FactType.Occupation)
            self.object_map[record.level-1].add_fact(gxobject)

            
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_obje(self, record: Element):
        self.handle_sour(record)

    def handle_page(self, record: Element):
        if isinstance(self.object_map[record.level-1], SourceReference):
            #self.object_map[record.level-1].descriptionId = record.value
            gx_object = Qualifier(name=KnownSourceReference.Page,value=record.value)
            self.object_map[record.level-1].add_qualifier(gx_object)
            self.object_map[record.level] = gx_object
        else:
            self.convert_exception_dump(record=record)

    def handle_plac(self, record: Element):
        if isinstance(self.object_map[record.level-1], Agent):
            gxobject = Address(value=record.value)
            self.object_map[record.level-1].add_address(gxobject)
            self.object_map[record.level] = gxobject
        elif isinstance(self.object_map[record.level-1], Event):
            if self.gedcomx.places.byName(record.value):
                self.object_map[record.level-1].place = PlaceReference(original=record.value, description=self.gedcomx.places.byName(record.value)[0])
            else:
                place_des = PlaceDescription(names=[TextValue(value=record.value)])
                self.gedcomx.add_place_description(place_des)
                self.object_map[record.level-1].place = PlaceReference(original=record.value, description=place_des)
                if (record.subRecords() is not None) and len(record.subRecords()) > 0:
                    self.object_map[record.level]= place_des

        elif isinstance(self.object_map[record.level-1], Fact):
            if self.gedcomx.places.byName(record.value):
                self.object_map[record.level-1].place = PlaceReference(original=record.value, description=self.gedcomx.places.byName(record.value)[0])
            else:
                place_des = PlaceDescription(names=[TextValue(value=record.value)])
                self.gedcomx.add_place_description(place_des)
                self.object_map[record.level-1].place = PlaceReference(original=record.value, description=place_des)
            self.object_map[record.level] = self.object_map[record.level-1].place
        elif isinstance(self.object_map[record.level-1], SourceDescription):
            if (place := self.gedcomx.places.byName(record.value)) is not None:
                self.object_map[record.level-1].place = place
            else:
                place = PlaceDescription(names=[TextValue(value=record.value)])
                self.gedcomx.add_place_description(place)
                self.object_map[record.level-1].place = PlaceReference(original=record.value, description=place)
            gxobject = Note(text='Place: ' + record.value if record.value else 'WARNING: NOTE had no value')
            self.object_map[record.level-1].add_note(gxobject)
            
            self.object_map[record.level] = place
        else:
            self.convert_exception_dump(record=record)

    def handle_post(self, record: Element):
        if isinstance(self.object_map[record.level-1], Address):
            self.object_map[record.level-1].postalCode = self.clean_str(record.value)
        else:
            self.convert_exception_dump(record=record) 
    
    def handle_publ(self, record: Element):
        if isinstance(self.object_map[record.level-1], SourceDescription):
            if record.value == None or record.value.strip() == '':
                #check for date
                if (date := record['DATE']) is not None:
                    self.object_map[record.level-1].published = date
            else:
                if record.value and self.gedcomx.agents.byName(record.value):
                    gxobject = self.gedcomx.agents.byName(record.value)[0]
                else:
                    gxobject = Agent(names=[TextValue(record.value)])
                    self.gedcomx.add_agent(gxobject)
                self.object_map[record.level-1].publisher = gxobject
                self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_prob(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Fact(type=FactType.Probate)
            self.object_map[record.level-1].add_fact(gxobject)

            
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_uid(self, record: Element):
        if isinstance(self.object_map[record.level-1], Agent):
            gxobject = Identifier(value=[URI('UID:' + record.value)] if record.value else [URI('WARNING: NOTE had no value')],type=IdentifierType.Primary) # type: ignore
            self.object_map[record.level-1].add_identifier(gxobject) #NOTE GC7 
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_refn(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person) or isinstance(self.object_map[record.level-1], SourceDescription):
            gxobject = Identifier(value=[URI.from_url('Reference Number:' + record.value)] if record.value else [],type=IdentifierType.External)
            self.object_map[record.level-1].add_identifier(gxobject)
            
            self.object_map[record.level] = gxobject
        elif isinstance(self.object_map[record.level-1], Agent):
            gxobject = Identifier(value=[URI('Reference Number:' + record.value)] if record.value else [],type=IdentifierType.External)
            self.object_map[record.level-1].add_identifier(gxobject) #NOTE GC7
            
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_repo(self, record: Element):
        if record.level == 0:
            if record.value is not None and self.gedcomx.agents.byName(record.value):
                gxobject = self.gedcomx.agents.byId(record.xref)
            else:
                gxobject = Agent(id=record.xref,names = [TextValue(record.value)] if record.value else [])
                self.gedcomx.add_agent(gxobject)            
            self.object_map[record.level] = gxobject
        elif isinstance(self.object_map[record.level-1], SourceDescription):
            if self.gedcomx.agents.byId(record.xref) is not None:            
                # TODO WHere and what to add this to?
                gxobject = self.gedcomx.agents.byId(record.xref)
                self.object_map[record.level-1].repository = gxobject
                self.object_map[record.level] = gxobject
            else:
                self.convert_exception_dump(record=record)
        else:
            self.convert_exception_dump(record=record)
        self.object_map[record.level] = gxobject

    def handle_resi(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            gxobject = Fact(type=FactType.Residence)
            if record.value and record.value.strip() != '':
                gxobject.add_note(Note(text=record.value))
            self.object_map[record.level-1].add_fact(gxobject)

            
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_rin(self, record: Element):
        if isinstance(self.object_map[record.level-1], SourceDescription):
            self.object_map[record.level-1].add_identifier = Identifier(Type=IdentifierType.External,value=record.value)
            self.object_map[record.level-1].add_note(Note(text=f"Source had RIN: of {record.value}"))

        else:
            raise ValueError(f"Could not handle 'RIN' tag in record {record.describe()}, last stack object {type(self.object_map[record.level-1])}")
        
    def handle_sex(self, record: Element):
        if isinstance(self.object_map[record.level-1], Person):
            if record.value == 'M':
                gxobject = Gender(type=GenderType.Male)
            elif record.value == 'F':
                gxobject = Gender(type=GenderType.Female)
            else:
                gxobject = Gender(type=GenderType.Unknown)
            self.object_map[record.level-1].gender = gxobject
            self.object_map[record.level] = gxobject
        else:
            self.convert_exception_dump(record=record)

    def handle_sour(self, record: Element):
        if record.level == 0 and (record.tag in ['SOUR','OBJE','_WLNK']):
            
            if (gxobject := self.gedcomx.sourceDescriptions.byId(record.xref)) is None:
                log.debug(f"SourceDescription with id: {record.xref} was not found. Creating a new SourceDescription")
                log.debug(f"Creating SourceDescription from {record.tag} {record.describe()}")
                gxobject = SourceDescription(id=record.xref)
                self.object_map[record.level-1].add_source_description(gxobject)
            else:
                log.debug(f"Found SourceDescription with id:{record.xref}")
            
        elif (add_method := getattr(self.object_map[record.level-1],"add_source_reference",None)) is not None:
            if (source_description := self.gedcomx.sourceDescriptions.byId(record.xref)) is not None:
                gxobject = SourceReference(descriptionId=record.xref, description=source_description)
                add_method(gxobject)
            else:
                log.error(f"Could not find source with id: {record.xref}, Creating Place Holder Description")
                gxobject = SourceDescription(id=record.xref)
                gxobject._place_holder = True
                gxobject = SourceReference(descriptionId=record.xref, description=gxobject)

        elif record.tag == 'OBJE' and isinstance(self.object_map[record.level-1],SourceReference): #TODO Flesh out OBJECTs/FILES
            if (source_description := self.gedcomx.sourceDescriptions.byId(record.xref)) is not None:
                gxobject = SourceReference(descriptionId=record.xref, description=source_description)
                self.object_map[record.level-1].description.add_source_reference(gxobject)
            else:
                self.convert_exception_dump(record=record)
        elif isinstance(self.object_map[record.level-1],Attribution): #TODO Flesh out OBJECTs/FILES
            if (creator := self.object_map[record.level-1].creator) is not None:
                creator.add_name(record.value)
                return
            else:
                if record.value is not None and self.gedcomx.agents.byName(record.value):
                    gxobject = self.gedcomx.agents.byId(record.xref)
                else:
                    gxobject = Agent(names=[TextValue(value=record.value)])
                    self.gedcomx.add_agent(gxobject)
                    self.object_map[record.level-1].creator = gxobject
                
                #self.convert_exception_dump(record=record,note=f"creator existed {creator}")
        else:
            self.convert_exception_dump(record=record)
            
        self.object_map[record.level] = gxobject
          
    def handle_stae(self, record: Element):
        if isinstance(self.object_map[record.level-1], Address):
            self.object_map[record.level-1].stateOrProvince = self.clean_str(record.value)
        else:
            raise ValueError(f"I do not know how to handle an 'STAE' tag for a {type(self.object_map[record.level-1])}")

    def handle_subm(self, record: Element):
        if record.value is not None and self.gedcomx.agents.byName(record.value):
            gxobject = self.gedcomx.agents.byId(record.xref)
        else:
            gxobject = Agent(id=record.xref)

        if isinstance(self.object_map[record.level-1], Attribution):
            self.object_map[record.level-1].creator = gxobject
        elif isinstance(self.object_map[record.level-1], Gedcom5x):
            self.object_map[record.level-1].add_agent(gxobject)
        else:
            self.convert_exception_dump(record=record)
        self.object_map[record.level] = gxobject
        




    def handle_surn(self, record: Element):
        if isinstance(self.object_map[record.level-1], Name):
            surname = NamePart(value=record.value, type=NamePartType.Surname)
            self.object_map[record.level-1]._add_name_part(surname)
        else:
            self.convert_exception_dump(record=record)

    def handle_text(self, record: Element):
        if record.parent is not None and record.parent.tag == 'DATA':
            if isinstance(self.object_map[record.level-2], SourceReference):
                gxobject = TextValue(value=record.value)
                self.object_map[record.level-2].description.add_description(gxobject)
                
                self.object_map[record.level] = gxobject
        elif isinstance(self.object_map[record.level-1], SourceDescription):
            gxobject = Document(text=record.value)
            self.object_map[record.level-1].analysis = gxobject
        else:
            assert False

    def handle_titl(self, record: Element):
        if isinstance(self.object_map[record.level-1], SourceDescription):
            
            gxobject = TextValue(value=self.clean_str(record.value))
            self.object_map[record.level-1].add_title(gxobject)
            self.object_map[record.level] = gxobject
        
        elif record.parent is not None and record.parent.tag == 'FILE' and isinstance(self.object_map[record.level-2], SourceDescription):
            gxobject = TextValue(value=record.value)
            self.object_map[record.level-2].add_title(gxobject)

            
            self.object_map[record.level] = gxobject
        elif self.object_map[record.level] and isinstance(self.object_map[record.level], Name):
            gxobject = NamePart(value=record.value, qualifiers=[NamePartQualifier.Title])

            self.object_map[record.level]._add_name_part(gxobject)
        else:
            log.error(f"self.convert_exception_dump(record=record)")

    def handle_tran(self, record: Element):
        pass

    def handle_type(self, record: Element):
        # peek to see if event or fact
        if isinstance(self.object_map[record.level-1], Event):
            if EventType.guess(record.value):
                self.object_map[record.level-1].type = EventType.guess(record.value)                
            else:
                log.warning(f"Could not determine type of event with value '{record.value}'")  
            # add as a note anyway, guess works of text in the string    
            self.object_map[record.level-1].add_note(Note(text=self.clean_str(record.value)))
        elif isinstance(self.object_map[record.level-1], Fact):
            if not self.object_map[record.level-1].type:
                self.object_map[0].type = FactType.guess(record.value)
        elif isinstance(self.object_map[record.level-1], Identifier):
            
            self.object_map[record.level-1].values.append(self.clean_str(record.value))
            self.object_map[record.level-1].type = IdentifierType.Other # type: ignore

        elif record.parent is not None and record.parent.tag == 'FORM':
            if not self.object_map[0].mediaType:
                self.object_map[0].mediaType = record.value
        elif isinstance(self.object_map[record.level-1], Name):
            self.object_map[record.level-1].type = GedcomConverter.type_name_type.get(record.value,NameType.Other)

        else:
            raise TagConversionError(record,self.object_map)

    def handle__url(self, record: Element):
        if isinstance(self.object_map[record.level-2], SourceDescription):
            self.object_map[record.level-2].about = URI.from_url(record.value) if record.value else None
        else:
            raise ValueError(f"Could not handle '_URL' tag in record {record.describe()}, last stack object {self.object_map[record.level-1]}")
            
    def handle_www(self, record: Element):
        if isinstance(self.object_map[record.level-1], Agent):
            self.object_map[record.level-1].homepage = self.clean_str(record.value)
        elif isinstance(self.object_map[record.level-2], SourceReference):
            self.object_map[record.level-2].description.add_identifier(Identifier(value=[URI.from_url(record.value)] if record.value else []))
        else:
            raise ValueError(f"Could not handle 'WWW' tag in record {record.describe()}, last stack object {self.object_map[record.level-1]}")

    def parse_gedcom5x_fam_record(self, record: Element):
        log.info(f"Parsing family recrods")
        with open('./logs/gedcomx.convert.families.json', 'a') as f:
            for fam in record._flatten_subrecords(record):
                f.write(fam.describe() + "\n")

    def print_counts_table(self, counts: Mapping[Any, int]) -> None:
        """
        Pretty-print {key: int} as columns, largest count first.
        Column count adapts to terminal width and number of items.
        """
        items = [(str(k), int(v)) for k, v in counts.items()]
        if not items:
            print("(empty)")
            return

        # Sort: by value desc, then key asc for stable ordering
        items.sort(key=lambda kv: (-kv[1], kv[0]))

        # Cell formatting widths
        key_w = max(len(k) for k, _ in items)
        num_w = max(len(str(v)) for _, v in items)
        cell_fmt = f"{{k:<{key_w}}}  {{v:>{num_w}}}"  # e.g., 'Surname        123'
        cell_width = key_w + 2 + num_w + 2            # +2 padding between columns

        # Decide number of columns: fit to terminal, but also scale with item count
        term_cols = shutil.get_terminal_size(fallback=(100, 24)).columns
        fit_cols = max(1, term_cols // cell_width)
        sqrt_cols = max(1, int(math.sqrt(len(items))))  # more cols when many items
        cols = max(1, min(len(items), max(fit_cols, sqrt_cols)))

        rows = math.ceil(len(items) / cols)

        # Print row-wise, reading items column-major so columns stay balanced
        for r in range(rows):
            line = []
            for c in range(cols):
                i = c * rows + r
                if i < len(items):
                    k, v = items[i]
                    cell = cell_fmt.format(k=k, v=v)
                    line.append(cell.ljust(cell_width))
            print("".join(line).rstrip())

    def has_duplicates(self,seq) -> bool:
        """Fast True/False check (works for hashable items)."""
        return len(seq) != len(set(seq))

    def find_duplicates(self, seq):
        """Return duplicate items once each, in the order they first repeat."""
        seen, dups = set(), []
        for x in seq:
            if x in seen and x not in dups:
                dups.append(x)
            seen.add(x)
        return dups
      
    def unique(self, seq: Iterable[T], key: Optional[Callable[[T], K]] = None) -> List[T]:
        """
        Return a list with duplicates removed, keeping the first occurrence.
        If `key` is provided, it’s used to compute a hashable identity for each item.
        """
        
        seen: set[K] = set()
        out: List[T] = []
        for item in seq:
            k = item if key is None else key(item)
            if k not in seen:
                seen.add(k)
                out.append(item)
        return out

    def convert_exception_dump(self,record,note: Optional[str] = None):
        obj_map = sorted(self.object_map.items(), reverse=True)
        obj_map = dict(obj_map)
        if note: print(note)
        for k in obj_map:
            log.debug(f"{k}\t{obj_map[k]}\t{str(obj_map[k])}\t{type(obj_map[k])}")
            print(f"{k}\t{obj_map[k]}\t{str(obj_map[k])}\t{type(obj_map[k])}")
        print(f"{record.describe()}")
        log.debug(f"{record.describe()}")
        raise ConversionErrorDump()

    def Gedcom5x_GedcomX(self, gedcom5x: Gedcom5x):
        #print(f'Parsing GEDCOM Version {gedcom5x.version}')
        
        individual_ids = set()
        source_ids = set()
        repository_ids = set()
        family_ids = set()

        with hub.use(convert_log):
            if gedcom5x:
                log.debug(f"Priming TopLevel Type id's")
                for object in gedcom5x.objects:
                    source_ids.add(object.xref)
                    gx_obj = SourceDescription(id=object.xref,type=ResourceType.DigitalArtifact)
                    self.gedcomx.add_source_description(gx_obj)
                olen = len(self.gedcomx.sourceDescriptions)
                log.debug(f"Primed {olen} SourceDescriptions from GEDCOM5 Objects")

                for source in gedcom5x.sources:
                    source_ids.add(source.xref)
                    gx_obj = SourceDescription(id=source.xref)
                    self.gedcomx.add_source_description(gx_obj)
                log.debug(f"Primed {len(self.gedcomx.sourceDescriptions)-olen} SourceDescriptions from GEDCOM5 Sources")
                
                for repo in gedcom5x.repositories:
                    repository_ids.add(repo.xref)
                    gx_obj = Agent(id=repo.xref)
                    self.gedcomx.add_agent(gx_obj)
                
                for individual in gedcom5x.individuals:
                    individual_ids.add(individual.xref)
                    gx_obj = Person(id=individual.xref)
                    self.gedcomx.add_person(gx_obj)
                
                for family in gedcom5x.families:
                    family_ids.add(family.xref)
                    self.handle_fam(family)
                
                # Now Parse Zero Level Recrods
                for header in gedcom5x.header:
                    self.parse_gedcom5x_record(header)
                for source in gedcom5x.sources:
                    self.parse_gedcom5x_record(source)
                for object in gedcom5x.objects:
                    self.parse_gedcom5x_record(object)
                for individual in gedcom5x.individuals:
                    self.parse_gedcom5x_record(individual)
                for repo in gedcom5x.repositories:
                    self.parse_gedcom5x_record(repo)
                for family in gedcom5x.families:
                    self.parse_gedcom5x_record(family)

                #clean up notes, and TextValue descriptions:
                for sd in self.gedcomx.sourceDescriptions:
                    log.debug(f"Removing dupliate notes in SourceDescriptions")
                    sd.notes = self.unique(sd.notes,key=lambda n: n._key())
                    log.debug(f"Removing dupliate descriptions in SourceDescriptions")
                    sd.descriptions = self.unique(sd.descriptions,key=lambda n: n._key())

        self.print_counts_table(self.missing_handler_count)
        
        return self.gedcomx
