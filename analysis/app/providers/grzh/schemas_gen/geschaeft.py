from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime
from xsdata_pydantic.fields import field

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Geschaeft"


class DateTimeFieldType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "nillable": True,
        },
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "nillable": True,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
        },
    )


class Departement(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
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


class Einreicher(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    partei: str = field(
        metadata={
            "name": "Partei",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    ist_gremium: Optional[bool] = field(
        metadata={
            "name": "IstGremium",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
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


class Gremium(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
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


class Verweis(BaseModel):
    model_config = ConfigDict(defer_build=True)
    titel: str = field(
        metadata={
            "name": "Titel",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    grnr: str = field(
        metadata={
            "name": "GRNr",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
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
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    datum: DateTimeFieldType = field(
        metadata={
            "name": "Datum",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    beginn: str = field(
        metadata={
            "name": "Beginn",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    ende: str = field(
        metadata={
            "name": "Ende",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
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


class VersionType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    rendition: List[RenditionType] = field(
        default_factory=list,
        metadata={
            "name": "Rendition",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
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
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
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


class Traktandum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    traktandennummer: str = field(
        metadata={
            "name": "Traktandennummer",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    titel: str = field(
        metadata={
            "name": "Titel",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    sitzung: "Traktandum.Sitzung" = field(
        metadata={
            "name": "Sitzung",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
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
        sitzung: Optional[Sitzung] = field(
            default=None,
            metadata={
                "name": "Sitzung",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            },
        )


class Dokument(BaseModel):
    model_config = ConfigDict(defer_build=True)
    titel: str = field(
        metadata={
            "name": "Titel",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    file: DocumentFieldType = field(
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
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


class Aufgabe(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ablaufschritt_name: str = field(
        metadata={
            "name": "AblaufschrittName",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    traktandum_guid: str = field(
        metadata={
            "name": "TraktandumGuid",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    sitzung_guid: str = field(
        metadata={
            "name": "SitzungGuid",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    ablaufschritt_nr: str = field(
        metadata={
            "name": "AblaufschrittNr",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    datum: DateTimeFieldType = field(
        metadata={
            "name": "Datum",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    frist_bis: DateTimeFieldType = field(
        metadata={
            "name": "FristBis",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    beschlussnummer: str = field(
        metadata={
            "name": "Beschlussnummer",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    dokumente: "Aufgabe.Dokumente" = field(
        metadata={
            "name": "Dokumente",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    protokolleintrag: str = field(
        metadata={
            "name": "Protokolleintrag",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    protokolleintrag_html: str = field(
        metadata={
            "name": "ProtokolleintragHTML",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            "required": True,
        }
    )
    erstellt_am: str = field(
        metadata={
            "name": "ErstelltAm",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
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
        dokument: List[Dokument] = field(
            default_factory=list,
            metadata={
                "name": "Dokument",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Geschaeft",
            },
        )


class Geschaeft(BaseModel):
    class Meta:
        namespace = "http://www.cmiag.ch/cdws/Geschaeft"

    model_config = ConfigDict(defer_build=True)
    grnr: str = field(
        metadata={
            "name": "GRNr",
            "type": "Element",
            "required": True,
        }
    )
    grnr_sort: str = field(
        metadata={
            "name": "GRNrSort",
            "type": "Element",
            "required": True,
        }
    )
    titel: str = field(
        metadata={
            "name": "Titel",
            "type": "Element",
            "required": True,
        }
    )
    geschaeftsart: str = field(
        metadata={
            "name": "Geschaeftsart",
            "type": "Element",
            "required": True,
        }
    )
    geschaeftsstatus: str = field(
        metadata={
            "name": "Geschaeftsstatus",
            "type": "Element",
            "required": True,
        }
    )
    dringlich: Optional[bool] = field(
        metadata={
            "name": "Dringlich",
            "type": "Element",
            "nillable": True,
        }
    )
    vorberatende_kommission: "Geschaeft.VorberatendeKommission" = field(
        metadata={
            "name": "VorberatendeKommission",
            "type": "Element",
            "required": True,
        }
    )
    weitere_vorberatende_kommissionen: "Geschaeft.WeitereVorberatendeKommissionen" = field(
        metadata={
            "name": "WeitereVorberatendeKommissionen",
            "type": "Element",
            "required": True,
        }
    )
    federfuehrendes_departement: "Geschaeft.FederfuehrendesDepartement" = (
        field(
            metadata={
                "name": "FederfuehrendesDepartement",
                "type": "Element",
                "required": True,
            }
        )
    )
    mitbeteiligte_departemente: "Geschaeft.MitbeteiligteDepartemente" = field(
        metadata={
            "name": "MitbeteiligteDepartemente",
            "type": "Element",
            "required": True,
        }
    )
    beginn: DateTimeFieldType = field(
        metadata={
            "name": "Beginn",
            "type": "Element",
            "required": True,
        }
    )
    pendent_bei: str = field(
        metadata={
            "name": "PendentBei",
            "type": "Element",
            "required": True,
        }
    )
    referendum: str = field(
        metadata={
            "name": "Referendum",
            "type": "Element",
            "required": True,
        }
    )
    ablaufschritte: "Geschaeft.Ablaufschritte" = field(
        metadata={
            "name": "Ablaufschritte",
            "type": "Element",
            "required": True,
        }
    )
    erstunterzeichner: "Geschaeft.Erstunterzeichner" = field(
        metadata={
            "name": "Erstunterzeichner",
            "type": "Element",
            "required": True,
        }
    )
    mitunterzeichner: "Geschaeft.Mitunterzeichner" = field(
        metadata={
            "name": "Mitunterzeichner",
            "type": "Element",
            "required": True,
        }
    )
    anzahl_mitunterzeichnende: Optional[Decimal] = field(
        metadata={
            "name": "AnzahlMitunterzeichnende",
            "type": "Element",
            "nillable": True,
        }
    )
    verweis_zu: "Geschaeft.VerweisZu" = field(
        metadata={
            "name": "VerweisZu",
            "type": "Element",
            "required": True,
        }
    )
    verweis_von: "Geschaeft.VerweisVon" = field(
        metadata={
            "name": "VerweisVon",
            "type": "Element",
            "required": True,
        }
    )
    traktanden: "Geschaeft.Traktanden" = field(
        metadata={
            "name": "Traktanden",
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

    class VorberatendeKommission(BaseModel):
        model_config = ConfigDict(defer_build=True)
        gremium: Optional[Gremium] = field(
            default=None,
            metadata={
                "name": "Gremium",
                "type": "Element",
            },
        )

    class WeitereVorberatendeKommissionen(BaseModel):
        model_config = ConfigDict(defer_build=True)
        gremium: List[Gremium] = field(
            default_factory=list,
            metadata={
                "name": "Gremium",
                "type": "Element",
            },
        )

    class FederfuehrendesDepartement(BaseModel):
        model_config = ConfigDict(defer_build=True)
        departement: Optional[Departement] = field(
            default=None,
            metadata={
                "name": "Departement",
                "type": "Element",
            },
        )

    class MitbeteiligteDepartemente(BaseModel):
        model_config = ConfigDict(defer_build=True)
        departement: List[Departement] = field(
            default_factory=list,
            metadata={
                "name": "Departement",
                "type": "Element",
            },
        )

    class Ablaufschritte(BaseModel):
        model_config = ConfigDict(defer_build=True)
        aufgabe: List[Aufgabe] = field(
            default_factory=list,
            metadata={
                "name": "Aufgabe",
                "type": "Element",
            },
        )

    class Erstunterzeichner(BaseModel):
        model_config = ConfigDict(defer_build=True)
        kontakt_gremium: Optional[Einreicher] = field(
            default=None,
            metadata={
                "name": "KontaktGremium",
                "type": "Element",
            },
        )

    class Mitunterzeichner(BaseModel):
        model_config = ConfigDict(defer_build=True)
        kontakt_gremium: List[Einreicher] = field(
            default_factory=list,
            metadata={
                "name": "KontaktGremium",
                "type": "Element",
            },
        )

    class VerweisZu(BaseModel):
        model_config = ConfigDict(defer_build=True)
        geschaeft: List[Verweis] = field(
            default_factory=list,
            metadata={
                "name": "Geschaeft",
                "type": "Element",
            },
        )

    class VerweisVon(BaseModel):
        model_config = ConfigDict(defer_build=True)
        geschaeft: List[Verweis] = field(
            default_factory=list,
            metadata={
                "name": "Geschaeft",
                "type": "Element",
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
