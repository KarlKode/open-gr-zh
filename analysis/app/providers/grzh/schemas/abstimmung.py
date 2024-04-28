from decimal import Decimal

from pydantic_xml import BaseXmlModel, attr, element, wrapped

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Abstimmung"


class Stimmabgabe(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    kontakt_guid: str = element("KontaktGuid")
    name: str = element("Name")
    vorname: str = element("Vorname")
    partei: str = element("Partei")
    fraktion: str = element("Fraktion", default="")
    spezialfunktion: str = element("Spezialfunktion", default="")
    geschlecht: str = element("Geschlecht", default="")
    alter: Decimal | None = element("Alter", nillable=True, default=None)
    abstimmungsverhalten: str = element("Abstimmungsverhalten", default="")
    obj_guid: str = attr("OBJ_GUID")


class Abstimmung(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    sitzung_guid: str = element("SitzungGuid")
    sitzung_titel: str = element("SitzungTitel")
    sitzung_datum: str = element("SitzungDatum")
    traktandum_guid: str = element("TraktandumGuid")
    traktandum_nr: str = element("TraktandumNr")
    traktandum_titel: str = element("TraktandumTitel")
    geschaeft_guid: str = element("GeschaeftGuid")
    geschaeft_titel: str = element("GeschaeftTitel")
    geschaeft_gr_nr: str = element("GeschaeftGrNr")
    geschaeft_ratsgeschaeftsart: str = element("GeschaeftRatsgeschaeftsart")
    abstimmungstitel: str = element("Abstimmungstitel")
    nummer: str = element("Nummer")
    abstimmungstyp: str = element("Abstimmungstyp")
    anzahl_ja: Decimal | None = element("Anzahl_Ja", nillable=True, default=None)
    anzahl_nein: Decimal | None = element("Anzahl_Nein", nillable=True, default=None)
    anzahl_enthaltung: Decimal | None = element("Anzahl_Enthaltung", nillable=True, default=None)
    anzahl_abwesend: Decimal | None = element("Anzahl_Abwesend", nillable=True, default=None)
    anzahl_a: Decimal | None = element("Anzahl_A", nillable=True, default=None)
    anzahl_b: Decimal | None = element("Anzahl_B", nillable=True, default=None)
    anzahl_c: Decimal | None = element("Anzahl_C", nillable=True, default=None)
    anzahl_d: Decimal | None = element("Anzahl_D", nillable=True, default=None)
    anzahl_e: Decimal | None = element("Anzahl_E", nillable=True, default=None)
    schlussresultat: str = element("Schlussresultat", default="")
    stimmabgaben: list[Stimmabgabe] = wrapped("Stimmabgaben", element("Stimmabgabe"))
    obj_guid: str = attr("OBJ_GUID")
    seq: str | None = attr("SEQ", nillable=True, default=None)
    idx: str | None = attr("IDX", nillable=True, default=None)
