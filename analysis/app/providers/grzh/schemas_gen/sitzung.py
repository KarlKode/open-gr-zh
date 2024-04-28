from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime
from xsdata_pydantic.fields import field

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Sitzung"


class Abstimmung(BaseModel):
    model_config = ConfigDict(defer_build=True)
    abstimmungstitel: str = field(
        metadata={
            "name": "Abstimmungstitel",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    abstimmungsnummer: Optional[Decimal] = field(
        metadata={
            "name": "Abstimmungsnummer",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "nillable": True,
        }
    )
    schlussresultat: str = field(
        metadata={
            "name": "Schlussresultat",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
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


class DateTimeFieldType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "nillable": True,
        },
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "nillable": True,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
        },
    )


class PersonWortmeldung(BaseModel):
    model_config = ConfigDict(defer_build=True)
    kontakt_guid: str = field(
        metadata={
            "name": "KontaktGuid",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    partei: str = field(
        metadata={
            "name": "Partei",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    spezialfunktion: str = field(
        metadata={
            "name": "Spezialfunktion",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
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


class RenditionType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    extension: str = field(
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "required": True,
        }
    )
    ansicht: str = field(
        metadata={
            "name": "Ansicht",
            "type": "Attribute",
            "required": True,
        }
    )


class VersionType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    rendition: List[RenditionType] = field(
        default_factory=list,
        metadata={
            "name": "Rendition",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
        },
    )
    nr: Decimal = field(
        metadata={
            "name": "Nr",
            "type": "Attribute",
            "required": True,
        }
    )


class DocumentFieldType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    version: List[VersionType] = field(
        default_factory=list,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
        },
    )
    id: str = field(
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    file_name: str = field(
        metadata={
            "name": "FileName",
            "type": "Attribute",
            "required": True,
        }
    )


class Audio(BaseModel):
    model_config = ConfigDict(defer_build=True)
    titel: str = field(
        metadata={
            "name": "Titel",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    file: DocumentFieldType = field(
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    kategorie: str = field(
        metadata={
            "name": "Kategorie",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
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


class Dokument(BaseModel):
    model_config = ConfigDict(defer_build=True)
    titel: str = field(
        metadata={
            "name": "Titel",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    file: DocumentFieldType = field(
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    kategorie: str = field(
        metadata={
            "name": "Kategorie",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
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


class Unterlage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    beschluss: Optional[bool] = field(
        metadata={
            "name": "Beschluss",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "nillable": True,
        }
    )
    dokumente: "Unterlage.Dokumente" = field(
        metadata={
            "name": "Dokumente",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
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

    class Dokumente(BaseModel):
        model_config = ConfigDict(defer_build=True)
        dokument: Optional[Dokument] = field(
            default=None,
            metadata={
                "name": "Dokument",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            },
        )


class Wortmeldung(BaseModel):
    model_config = ConfigDict(defer_build=True)
    subtraktandum: str = field(
        metadata={
            "name": "Subtraktandum",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    sortierung: Optional[Decimal] = field(
        metadata={
            "name": "Sortierung",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "nillable": True,
        }
    )
    level: Optional[Decimal] = field(
        metadata={
            "name": "Level",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "nillable": True,
        }
    )
    aufzeichnung: "Wortmeldung.Aufzeichnung" = field(
        metadata={
            "name": "Aufzeichnung",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    personen_wortmeldung: "Wortmeldung.PersonenWortmeldung" = field(
        metadata={
            "name": "PersonenWortmeldung",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
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

    class Aufzeichnung(BaseModel):
        model_config = ConfigDict(defer_build=True)
        dokument: Optional[Audio] = field(
            default=None,
            metadata={
                "name": "Dokument",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            },
        )

    class PersonenWortmeldung(BaseModel):
        model_config = ConfigDict(defer_build=True)
        person_wortmeldung: List[PersonWortmeldung] = field(
            default_factory=list,
            metadata={
                "name": "PersonWortmeldung",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            },
        )


class Traktandum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    geschaeft_guid: str = field(
        metadata={
            "name": "GeschaeftGuid",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    geschaeft_altsystem_id: str = field(
        metadata={
            "name": "GeschaeftAltsystemID",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    grnr: str = field(
        metadata={
            "name": "GRnr",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    titel: str = field(
        metadata={
            "name": "Titel",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    traktandennummer: str = field(
        metadata={
            "name": "Traktandennummer",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    traktandierungscode: str = field(
        metadata={
            "name": "Traktandierungscode",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    traktandierungscode_erlaeuterungen: str = field(
        metadata={
            "name": "TraktandierungscodeErlaeuterungen",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    unterlagen: "Traktandum.Unterlagen" = field(
        metadata={
            "name": "Unterlagen",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    wortmeldungen: "Traktandum.Wortmeldungen" = field(
        metadata={
            "name": "Wortmeldungen",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            "required": True,
        }
    )
    abstimmungen: "Traktandum.Abstimmungen" = field(
        metadata={
            "name": "Abstimmungen",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Sitzung",
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

    class Unterlagen(BaseModel):
        model_config = ConfigDict(defer_build=True)
        unterlage: List[Unterlage] = field(
            default_factory=list,
            metadata={
                "name": "Unterlage",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            },
        )

    class Wortmeldungen(BaseModel):
        model_config = ConfigDict(defer_build=True)
        wortmeldung: List[Wortmeldung] = field(
            default_factory=list,
            metadata={
                "name": "Wortmeldung",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            },
        )

    class Abstimmungen(BaseModel):
        model_config = ConfigDict(defer_build=True)
        abstimmung: List[Abstimmung] = field(
            default_factory=list,
            metadata={
                "name": "Abstimmung",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Sitzung",
            },
        )


class Sitzung(BaseModel):
    class Meta:
        namespace = "http://www.cmiag.ch/cdws/Sitzung"

    model_config = ConfigDict(defer_build=True)
    titel: str = field(
        metadata={
            "name": "Titel",
            "type": "Element",
            "required": True,
        }
    )
    datum: DateTimeFieldType = field(
        metadata={
            "name": "Datum",
            "type": "Element",
            "required": True,
        }
    )
    beginn: str = field(
        metadata={
            "name": "Beginn",
            "type": "Element",
            "required": True,
        }
    )
    ende: str = field(
        metadata={
            "name": "Ende",
            "type": "Element",
            "required": True,
        }
    )
    ende_nach_mitternacht: str = field(
        metadata={
            "name": "EndeNachMitternacht",
            "type": "Element",
            "required": True,
        }
    )
    video_url: str = field(
        metadata={
            "name": "VideoURL",
            "type": "Element",
            "required": True,
        }
    )
    traktanden: "Sitzung.Traktanden" = field(
        metadata={
            "name": "Traktanden",
            "type": "Element",
            "required": True,
        }
    )
    dokumente: "Sitzung.Dokumente" = field(
        metadata={
            "name": "Dokumente",
            "type": "Element",
            "required": True,
        }
    )
    sitzungsaufzeichnung: "Sitzung.Sitzungsaufzeichnung" = field(
        metadata={
            "name": "Sitzungsaufzeichnung",
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

    class Traktanden(BaseModel):
        model_config = ConfigDict(defer_build=True)
        traktandum: List[Traktandum] = field(
            default_factory=list,
            metadata={
                "name": "Traktandum",
                "type": "Element",
            },
        )

    class Dokumente(BaseModel):
        model_config = ConfigDict(defer_build=True)
        dokument: List[Dokument] = field(
            default_factory=list,
            metadata={
                "name": "Dokument",
                "type": "Element",
            },
        )

    class Sitzungsaufzeichnung(BaseModel):
        model_config = ConfigDict(defer_build=True)
        dokument: Optional[Audio] = field(
            default=None,
            metadata={
                "name": "Dokument",
                "type": "Element",
            },
        )
