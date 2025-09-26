from __future__ import annotations
from typing import List, Optional, Union, TYPE_CHECKING
"""
======================================================================
 Project: Gedcom-X
 File:    Person.py
 Author:  David J. Cartwright
 Purpose: Python Object representation of GedcomX Person Type

 Created: 2025-08-25
 Updated:
   - 2025-08-31: _as_dict_ to only create entries in dict for fields that hold data
   - 2025-09-03: _from_json_ refactor
   - 2025-09-09: added schema_class
   
======================================================================
"""

"""
======================================================================
GEDCOM Module Types
======================================================================
"""
if TYPE_CHECKING:
    from .source_description import SourceDescription

from .attribution import Attribution
from .qualifier import Qualifier

from .resource import Resource
from .schemas import extensible

from .uri import URI
from .logging_hub import hub, logging
"""
======================================================================
Logging
======================================================================
"""
log = logging.getLogger("gedcomx")
serial_log = "gedcomx.serialization"
#=====================================================================

from collections.abc import Sized

class KnownSourceReference(Qualifier):
    CharacterRegion = "http://gedcomx.org/CharacterRegion"
    RectangleRegion = "http://gedcomx.org/RectangleRegion"
    TimeRegion = "http://gedcomx.org/TimeRegion"
    Page = "http://gedcomx.org/Page"
    
    @property
    def description(self):
        descriptions = {
            self.CharacterRegion: (
                "A region of text in a digital document, in the form of a,b where a is the index of the start "
                "character and b is the index of the end character. The meaning of this qualifier is undefined "
                "if the source being referenced is not a digital document."
            ),
            self.RectangleRegion: (
                "A rectangular region of a digital image. The value of the qualifier is interpreted as a series "
                "of four comma-separated numbers. If all numbers are less than 1, it is interpreted as x1,y1,x2,y2, "
                "representing percentage-based coordinates of the top-left and bottom-right corners. If any number is "
                "more than 1, it is interpreted as x,y,w,h where x and y are coordinates in pixels, and w and h are "
                "the width and height of the rectangle in pixels."
            ),
            self.TimeRegion: (
                "A region of time in a digital audio or video recording, in the form of a,b where a is the starting "
                "point in milliseconds and b is the ending point in milliseconds. This qualifier's meaning is undefined "
                "if the source is not a digital audio or video recording."
            ),
            self.Page: (
                "A single page in a multi-page document, represented as a 1-based integer. This always references the "
                "absolute page number, not any custom page number. This qualifier is undefined if the source is not a "
                "multi-page document."
            )
        }
        return descriptions.get(self, "No description available.")

@extensible()
class SourceReference:
    identifier = 'http://gedcomx.org/v1/SourceReference'
    version = 'http://gedcomx.org/conceptual-model/v1'
    
    def __init__(self,
                 description: Union[URI, SourceDescription] = None,
                 descriptionId: Optional[str] = None,
                 attribution: Optional[Attribution] = None,
                 qualifiers: Optional[List[Qualifier]] = None
                 ) -> None:
        
        self.description = description
        self.descriptionId = descriptionId
        self.attribution = attribution
        self.qualifiers = qualifiers if qualifiers and isinstance(qualifiers, list) else [] 

    def add_qualifier(self, qualifier: Qualifier):
        if isinstance(qualifier, (Qualifier,KnownSourceReference)):
            if self.qualifiers:
                #TODO Prevent Duplicates
                for current_qualifier in self.qualifiers:
                    if qualifier == current_qualifier:
                        return
            self.qualifiers.append(qualifier)
            return
        raise ValueError("The 'qualifier' must be type 'Qualifier' or 'KnownSourceReference', not " + str(type(qualifier))) 
    
    def append(self, text_to_add: str):
        raise ValueError
        if text_to_add and isinstance(text_to_add, str):
            if self.descriptionId is None:
                self.descriptionId = text_to_add
            else:
                self.descriptionId += text_to_add
        else:
            raise ValueError("The 'text_to_add' must be a non-empty string.")
    
    @property    
    def _as_dict_(self):
        with hub.use(serial_log):
            log.debug(f"Serializing 'SourceReference' with 'descriptionId': '{self.descriptionId}'")
            type_as_dict = {}
            if self.description is not None:
                type_as_dict['description']= URI(target=self.description)._as_dict_ if self.description is not None else None
            if self.descriptionId is not None:
                type_as_dict['descriptionId']= self.descriptionId.replace("\n"," ").replace("\r"," ") if self.descriptionId else None
            if self.attribution is not None:
                type_as_dict['attribution'] = self.attribution._as_dict_ if self.attribution else None
            if self.qualifiers is not None and self.qualifiers != []:
                type_as_dict['qualifiers'] = [qualifier.__as_dict__ for qualifier in self.qualifiers] if (self.qualifiers and len(self.qualifiers) > 0) else None
            log.debug(f"'SourceReference' serialized with fields: {type_as_dict.keys()}") 
            if type_as_dict == {}: log.warning("serializing and empty 'SourceReference'")  
        return type_as_dict if type_as_dict != {} else None
      
    @classmethod
    def _from_json_(cls, data: dict, context=None) -> "SourceReference":
        ref = {}

        # Scalars
        if (descriptionId := data.get("descriptionId")) is not None:
            ref["descriptionId"] = descriptionId

        # Objects (description could be URI or SourceDescription)
        if (description := data.get("description")) is not None:
            # if description is just a string, assume URI
            if isinstance(description, str):
                ref["description"] = URI(description)
            elif isinstance(description, dict):
                print(">>",description)
                ref["description"] = Resource._from_json_(description, context)
                assert False
        else:
            pass #TODO
            #print(ref["descriptionId"])

        if (attribution := data.get("attribution")) is not None:
            ref["attribution"] = Attribution._from_json_(attribution, context)

        if (qualifiers := data.get("qualifiers")) is not None:
            ref["qualifiers"] = [Qualifier._from_json_(q, context) for q in qualifiers]

        return cls(**ref)
  
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False  

        return (
            self.description._uri == other.description._uri
        )
