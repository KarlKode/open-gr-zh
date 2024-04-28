from typing import List, Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime
from xsdata_pydantic.fields import field

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Gremiumdetail"


class DateTimeFieldType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
            "nillable": True,
        },
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
            "nillable": True,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
        },
    )


class Behoerdenmandat(BaseModel):
    model_config = ConfigDict(defer_build=True)
    kontakt_guid: str = field(
        metadata={
            "name": "KontaktGuid",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
            "required": True,
        }
    )
    vorname_name: str = field(
        metadata={
            "name": "VornameName",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
            "required": True,
        }
    )
    vorname: str = field(
        metadata={
            "name": "Vorname",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
            "required": True,
        }
    )
    partei: str = field(
        metadata={
            "name": "Partei",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
            "required": True,
        }
    )
    wahlkreis: str = field(
        metadata={
            "name": "Wahlkreis",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
            "required": True,
        }
    )
    funktion: str = field(
        metadata={
            "name": "Funktion",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
            "required": True,
        }
    )
    dauer: DateTimeFieldType = field(
        metadata={
            "name": "Dauer",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
            "required": True,
        }
    )
    sitz: str = field(
        metadata={
            "name": "Sitz",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
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


class Sitzung(BaseModel):
    model_config = ConfigDict(defer_build=True)
    titel: str = field(
        metadata={
            "name": "Titel",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
            "required": True,
        }
    )
    datum: DateTimeFieldType = field(
        metadata={
            "name": "Datum",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Gremiumdetail",
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


class Gremium(BaseModel):
    class Meta:
        namespace = "http://www.cmiag.ch/cdws/Gremiumdetail"

    model_config = ConfigDict(defer_build=True)
    vater: str = field(
        metadata={
            "name": "Vater",
            "type": "Element",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    kurzname: str = field(
        metadata={
            "name": "Kurzname",
            "type": "Element",
            "required": True,
        }
    )
    bemerkung: str = field(
        metadata={
            "name": "Bemerkung",
            "type": "Element",
            "required": True,
        }
    )
    gremiumstyp: str = field(
        metadata={
            "name": "Gremiumstyp",
            "type": "Element",
            "required": True,
        }
    )
    inaktiv: str = field(
        metadata={
            "name": "Inaktiv",
            "type": "Element",
            "required": True,
        }
    )
    sitzungen: "Gremium.Sitzungen" = field(
        metadata={
            "name": "Sitzungen",
            "type": "Element",
            "required": True,
        }
    )
    behoerdenmitglieder: "Gremium.Behoerdenmitglieder" = field(
        metadata={
            "name": "Behoerdenmitglieder",
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

    class Sitzungen(BaseModel):
        model_config = ConfigDict(defer_build=True)
        sitzung: List[Sitzung] = field(
            default_factory=list,
            metadata={
                "name": "Sitzung",
                "type": "Element",
            },
        )

    class Behoerdenmitglieder(BaseModel):
        model_config = ConfigDict(defer_build=True)
        behoerdenmandat: List[Behoerdenmandat] = field(
            default_factory=list,
            metadata={
                "name": "Behoerdenmandat",
                "type": "Element",
            },
        )
