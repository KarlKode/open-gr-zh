from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, ConfigDict
from xsdata_pydantic.fields import field

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Abstimmung"


class Stimmabgabe(BaseModel):
    model_config = ConfigDict(defer_build=True)
    kontakt_guid: str = field(
        metadata={
            "name": "KontaktGuid",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Abstimmung",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Abstimmung",
            "required": True,
        }
    )
    vorname: str = field(
        metadata={
            "name": "Vorname",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Abstimmung",
            "required": True,
        }
    )
    partei: str = field(
        metadata={
            "name": "Partei",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Abstimmung",
            "required": True,
        }
    )
    fraktion: str = field(
        metadata={
            "name": "Fraktion",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Abstimmung",
            "required": True,
        }
    )
    spezialfunktion: str = field(
        metadata={
            "name": "Spezialfunktion",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Abstimmung",
            "required": True,
        }
    )
    geschlecht: str = field(
        metadata={
            "name": "Geschlecht",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Abstimmung",
            "required": True,
        }
    )
    alter: Optional[Decimal] = field(
        metadata={
            "name": "Alter",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Abstimmung",
            "nillable": True,
        }
    )
    abstimmungsverhalten: str = field(
        metadata={
            "name": "Abstimmungsverhalten",
            "type": "Element",
            "namespace": "http://www.cmiag.ch/cdws/Abstimmung",
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


class Abstimmung(BaseModel):
    class Meta:
        namespace = "http://www.cmiag.ch/cdws/Abstimmung"

    model_config = ConfigDict(defer_build=True)
    sitzung_guid: str = field(
        metadata={
            "name": "SitzungGuid",
            "type": "Element",
            "required": True,
        }
    )
    sitzung_titel: str = field(
        metadata={
            "name": "SitzungTitel",
            "type": "Element",
            "required": True,
        }
    )
    sitzung_datum: str = field(
        metadata={
            "name": "SitzungDatum",
            "type": "Element",
            "required": True,
        }
    )
    traktandum_guid: str = field(
        metadata={
            "name": "TraktandumGuid",
            "type": "Element",
            "required": True,
        }
    )
    traktandum_nr: str = field(
        metadata={
            "name": "TraktandumNr",
            "type": "Element",
            "required": True,
        }
    )
    traktandum_titel: str = field(
        metadata={
            "name": "TraktandumTitel",
            "type": "Element",
            "required": True,
        }
    )
    geschaeft_guid: str = field(
        metadata={
            "name": "GeschaeftGuid",
            "type": "Element",
            "required": True,
        }
    )
    geschaeft_titel: str = field(
        metadata={
            "name": "GeschaeftTitel",
            "type": "Element",
            "required": True,
        }
    )
    geschaeft_gr_nr: str = field(
        metadata={
            "name": "GeschaeftGrNr",
            "type": "Element",
            "required": True,
        }
    )
    geschaeft_ratsgeschaeftsart: str = field(
        metadata={
            "name": "GeschaeftRatsgeschaeftsart",
            "type": "Element",
            "required": True,
        }
    )
    abstimmungstitel: str = field(
        metadata={
            "name": "Abstimmungstitel",
            "type": "Element",
            "required": True,
        }
    )
    nummer: str = field(
        metadata={
            "name": "Nummer",
            "type": "Element",
            "required": True,
        }
    )
    abstimmungstyp: str = field(
        metadata={
            "name": "Abstimmungstyp",
            "type": "Element",
            "required": True,
        }
    )
    anzahl_ja: Optional[Decimal] = field(
        metadata={
            "name": "Anzahl_Ja",
            "type": "Element",
            "nillable": True,
        }
    )
    anzahl_nein: Optional[Decimal] = field(
        metadata={
            "name": "Anzahl_Nein",
            "type": "Element",
            "nillable": True,
        }
    )
    anzahl_enthaltung: Optional[Decimal] = field(
        metadata={
            "name": "Anzahl_Enthaltung",
            "type": "Element",
            "nillable": True,
        }
    )
    anzahl_abwesend: Optional[Decimal] = field(
        metadata={
            "name": "Anzahl_Abwesend",
            "type": "Element",
            "nillable": True,
        }
    )
    anzahl_a: Optional[Decimal] = field(
        metadata={
            "name": "Anzahl_A",
            "type": "Element",
            "nillable": True,
        }
    )
    anzahl_b: Optional[Decimal] = field(
        metadata={
            "name": "Anzahl_B",
            "type": "Element",
            "nillable": True,
        }
    )
    anzahl_c: Optional[Decimal] = field(
        metadata={
            "name": "Anzahl_C",
            "type": "Element",
            "nillable": True,
        }
    )
    anzahl_d: Optional[Decimal] = field(
        metadata={
            "name": "Anzahl_D",
            "type": "Element",
            "nillable": True,
        }
    )
    anzahl_e: Optional[Decimal] = field(
        metadata={
            "name": "Anzahl_E",
            "type": "Element",
            "nillable": True,
        }
    )
    schlussresultat: str = field(
        metadata={
            "name": "Schlussresultat",
            "type": "Element",
            "required": True,
        }
    )
    stimmabgaben: "Abstimmung.Stimmabgaben" = field(
        metadata={
            "name": "Stimmabgaben",
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

    class Stimmabgaben(BaseModel):
        model_config = ConfigDict(defer_build=True)
        stimmabgabe: List[Stimmabgabe] = field(
            default_factory=list,
            metadata={
                "name": "Stimmabgabe",
                "type": "Element",
            },
        )
