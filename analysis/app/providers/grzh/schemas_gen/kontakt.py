from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime
from xsdata_pydantic.fields import field

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Kontakt"


class Adresse(BaseModel):
    model_config = ConfigDict(defer_build=True)
    adressart: str = field(
        metadata={
            "name": "Adressart",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    strasse: str = field(
        metadata={
            "name": "Strasse",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    plz: str = field(
        metadata={
            "name": "PLZ",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    ort: str = field(
        metadata={
            "name": "Ort",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
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
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "nillable": True,
        },
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "nillable": True,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
        },
    )


class Geschaeft(BaseModel):
    model_config = ConfigDict(defer_build=True)
    grnr: str = field(
        metadata={
            "name": "GRNr",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    grnr_sort: str = field(
        metadata={
            "name": "GRNrSort",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    titel: str = field(
        metadata={
            "name": "Titel",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    ratsgeschaeftsart: str = field(
        metadata={
            "name": "Ratsgeschaeftsart",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
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


class Interessenbindung(BaseModel):
    model_config = ConfigDict(defer_build=True)
    bezeichnung: str = field(
        metadata={
            "name": "Bezeichnung",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
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


class SozialeMedien(BaseModel):
    model_config = ConfigDict(defer_build=True)
    adresse: str = field(
        metadata={
            "name": "Adresse",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    typ: str = field(
        metadata={
            "name": "Typ",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
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


class Behoerdenmandat(BaseModel):
    model_config = ConfigDict(defer_build=True)
    gremium_name: str = field(
        metadata={
            "name": "GremiumName",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    gremium_kurzname: str = field(
        metadata={
            "name": "GremiumKurzname",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    gremium_guid: str = field(
        metadata={
            "name": "GremiumGuid",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    gremium_typ: str = field(
        metadata={
            "name": "GremiumTyp",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    gremium_inaktiv: Optional[bool] = field(
        metadata={
            "name": "GremiumInaktiv",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "nillable": True,
        }
    )
    funktion: str = field(
        metadata={
            "name": "Funktion",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    dauer: DateTimeFieldType = field(
        metadata={
            "name": "Dauer",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    sitznummer: str = field(
        metadata={
            "name": "Sitznummer",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
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


class Parteizugehoerigkeit(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partei: str = field(
        metadata={
            "name": "Partei",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    partei_guid: str = field(
        metadata={
            "name": "ParteiGuid",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    funktion: str = field(
        metadata={
            "name": "Funktion",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    dauer: DateTimeFieldType = field(
        metadata={
            "name": "Dauer",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
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
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
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
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
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


class Konakt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    altsystem_id: str = field(
        metadata={
            "name": "AltsystemID",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    name_vorname: str = field(
        metadata={
            "name": "NameVorname",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    vorname: str = field(
        metadata={
            "name": "Vorname",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    partei: str = field(
        metadata={
            "name": "Partei",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    partei_guid: str = field(
        metadata={
            "name": "ParteiGuid",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    fraktion: str = field(
        metadata={
            "name": "Fraktion",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    wahlkreis: str = field(
        metadata={
            "name": "Wahlkreis",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    wohnkreis: str = field(
        metadata={
            "name": "Wohnkreis",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    beruf: str = field(
        metadata={
            "name": "Beruf",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    jahrgang: Optional[Decimal] = field(
        metadata={
            "name": "Jahrgang",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "nillable": True,
        }
    )
    todesjahr: Optional[Decimal] = field(
        metadata={
            "name": "Todesjahr",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "nillable": True,
        }
    )
    geschlecht: str = field(
        metadata={
            "name": "Geschlecht",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    bild: DocumentFieldType = field(
        metadata={
            "name": "Bild",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    email_geschaeft: str = field(
        metadata={
            "name": "EmailGeschaeft",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    email_privat: str = field(
        metadata={
            "name": "EmailPrivat",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    telefon_geschaeft: str = field(
        metadata={
            "name": "TelefonGeschaeft",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    telefon_privat: str = field(
        metadata={
            "name": "TelefonPrivat",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    telefon_mobile_geschaeft: str = field(
        metadata={
            "name": "TelefonMobileGeschaeft",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    telefon_mobile_privat: str = field(
        metadata={
            "name": "TelefonMobilePrivat",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    fax_geschaeft: str = field(
        metadata={
            "name": "FaxGeschaeft",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    fax_privat: str = field(
        metadata={
            "name": "FaxPrivat",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    homepage_geschaeft: str = field(
        metadata={
            "name": "HomepageGeschaeft",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    homepage_privat: str = field(
        metadata={
            "name": "HomepagePrivat",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    adressen: "Konakt.Adressen" = field(
        metadata={
            "name": "Adressen",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    parteizugehoerigkeit: "Konakt.Parteizugehoerigkeit" = field(
        metadata={
            "name": "Parteizugehoerigkeit",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    interessenbindung: "Konakt.Interessenbindung" = field(
        metadata={
            "name": "Interessenbindung",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    behoerdenmandat: "Konakt.Behoerdenmandat" = field(
        metadata={
            "name": "Behoerdenmandat",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    soziale_medien: "Konakt.SozialeMedien" = field(
        metadata={
            "name": "SozialeMedien",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    erstunterzeichner: "Konakt.Erstunterzeichner" = field(
        metadata={
            "name": "Erstunterzeichner",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            "required": True,
        }
    )
    mitunterzeichner: "Konakt.Mitunterzeichner" = field(
        metadata={
            "name": "Mitunterzeichner",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Kontakt",
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

    class Adressen(BaseModel):
        model_config = ConfigDict(defer_build=True)
        adresse: List[Adresse] = field(
            default_factory=list,
            metadata={
                "name": "Adresse",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            },
        )

    class Parteizugehoerigkeit(BaseModel):
        model_config = ConfigDict(defer_build=True)
        parteizugehoerigkeit: List[Parteizugehoerigkeit] = field(
            default_factory=list,
            metadata={
                "name": "Parteizugehoerigkeit",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            },
        )

    class Interessenbindung(BaseModel):
        model_config = ConfigDict(defer_build=True)
        interessenbindung: List[Interessenbindung] = field(
            default_factory=list,
            metadata={
                "name": "Interessenbindung",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            },
        )

    class Behoerdenmandat(BaseModel):
        model_config = ConfigDict(defer_build=True)
        behoerdenmandat: List[Behoerdenmandat] = field(
            default_factory=list,
            metadata={
                "name": "Behoerdenmandat",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            },
        )

    class SozialeMedien(BaseModel):
        model_config = ConfigDict(defer_build=True)
        kommunikation: List[SozialeMedien] = field(
            default_factory=list,
            metadata={
                "name": "Kommunikation",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            },
        )

    class Erstunterzeichner(BaseModel):
        model_config = ConfigDict(defer_build=True)
        geschaeft: List[Geschaeft] = field(
            default_factory=list,
            metadata={
                "name": "Geschaeft",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            },
        )

    class Mitunterzeichner(BaseModel):
        model_config = ConfigDict(defer_build=True)
        geschaeft: List[Geschaeft] = field(
            default_factory=list,
            metadata={
                "name": "Geschaeft",
                "type": "Element",
                "namespace": "http://www.cmiag.ch/cdws/Kontakt",
            },
        )


class Kontakt(Konakt):
    class Meta:
        namespace = "http://www.cmiag.ch/cdws/Kontakt"

    model_config = ConfigDict(defer_build=True)
