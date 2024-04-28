from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime
from xsdata_pydantic.fields import field

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Behoerdenmandat"


class DateTimeFieldType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "nillable": True,
        },
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "nillable": True,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
        },
    )


class Behoerdenmandat(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    vorname: str = field(
        metadata={
            "name": "Vorname",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    kontakt_guid: str = field(
        metadata={
            "name": "KontaktGuid",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    altsystem_id: str = field(
        metadata={
            "name": "AltsystemID",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    dauer: DateTimeFieldType = field(
        metadata={
            "name": "Dauer",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    gremium: str = field(
        metadata={
            "name": "Gremium",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    gremium_guid: str = field(
        metadata={
            "name": "GremiumGuid",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    gremiumstyp: str = field(
        metadata={
            "name": "Gremiumstyp",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    partei: str = field(
        metadata={
            "name": "Partei",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    partei_guid: str = field(
        metadata={
            "name": "ParteiGuid",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    titel: str = field(
        metadata={
            "name": "Titel",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    wahlkreis: str = field(
        metadata={
            "name": "Wahlkreis",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    wahlkreis_order: Optional[Decimal] = field(
        metadata={
            "name": "WahlkreisOrder",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "nillable": True,
        }
    )
    wohnkreis: str = field(
        metadata={
            "name": "Wohnkreis",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    funktion: str = field(
        metadata={
            "name": "Funktion",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "required": True,
        }
    )
    sitz: Optional[Decimal] = field(
        metadata={
            "name": "Sitz",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Behoerdenmandat",
            "nillable": True,
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


class Behordenmandat(Behoerdenmandat):
    class Meta:
        namespace = "http://www.cmiag.ch/cdws/Behoerdenmandat"

    model_config = ConfigDict(defer_build=True)
