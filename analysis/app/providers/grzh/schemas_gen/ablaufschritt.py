from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata_pydantic.fields import field

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Ablaufschritt"


class Ablaufschritt(BaseModel):
    class Meta:
        namespace = "http://www.cmiag.ch/cdws/Ablaufschritt"

    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    inaktiv: Optional[bool] = field(
        metadata={
            "name": "Inaktiv",
            "type": "Element",
            "nillable": True,
        }
    )
    ablaufschritt_nr: str = field(
        metadata={
            "name": "AblaufschrittNr",
            "type": "Element",
            "required": True,
        }
    )
    obj_guid: str = field(
        metadata={
            "name": "OBJ_GUID",
            "type": "Attribute",
            "required": True,
        }
    )
    seq: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEQ",
            "type": "Attribute",
        },
    )
    idx: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDX",
            "type": "Attribute",
        },
    )
