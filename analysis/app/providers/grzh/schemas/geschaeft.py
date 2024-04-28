import datetime
from decimal import Decimal

from pydantic_xml import BaseXmlModel, attr, element, wrapped

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Geschaeft"


class DateTimeFieldType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    start: datetime.datetime | None = element("Start", nillable=True, default=None)
    end: datetime.datetime | None = element("End", nillable=True, default=None)
    text: str | None = element("Text", nillable=True, default=None)


class Departement(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    name: str = element("Name")
    obj_guid: str = attr("OBJ_GUID")


class Einreicher(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    name: str = element("Name")
    partei: str = element("Partei")
    ist_gremium: bool | None = element("IstGremium", nillable=True, default=None)
    obj_guid: str = attr("OBJ_GUID")


class Gremium(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    name: str = element("Name")
    obj_guid: str = attr("OBJ_GUID")


class RenditionType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    extension: str = attr("Extension")
    ansicht: str = attr("Ansicht")


class Verweis(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    titel: str = element("Titel")
    grnr: str = element("GRNr")
    obj_guid: str = attr("OBJ_GUID")


class Sitzung(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    titel: str = element("Titel")
    datum: DateTimeFieldType = element("Datum")
    beginn: str = element("Beginn")
    ende: str = element("Ende")
    obj_guid: str = attr("OBJ_GUID")


class VersionType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    rendition: list[RenditionType] = element("Rendition")
    nr: Decimal = attr("Nr")


class DocumentFieldType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    version: list[VersionType] = element("Version")
    id: str = attr("ID")
    file_name: str = attr("FileName")


class Traktandum(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    traktandennummer: str = element("Traktandennummer")
    titel: str = element("Titel")
    sitzung: Sitzung = wrapped("Sitzung", element("Sitzung"))
    obj_guid: str = attr("OBJ_GUID")

class Dokument(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    titel: str = element("Titel")
    file: DocumentFieldType = element("File")
    obj_guid: str = attr("OBJ_GUID")


class Aufgabe(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    ablaufschritt_name: str = element("AblaufschrittName")
    traktandum_guid: str = element("TraktandumGuid")
    sitzung_guid: str = element("SitzungGuid")
    ablaufschritt_nr: str = element("AblaufschrittNr")
    datum: DateTimeFieldType = element("Datum")
    frist_bis: DateTimeFieldType = element("FristBis")
    beschlussnummer: str = element("Beschlussnummer")
    dokumente: list[Dokument] = wrapped("Dokumente", element("Dokument"))
    protokolleintrag: str = element("Protokolleintrag")
    protokolleintrag_html: str = element("ProtokolleintragHTML")
    erstellt_am: str = element("ErstelltAm")
    obj_guid: str = attr("OBJ_GUID")


class Geschaeft(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    grnr: str = element("GRNr")
    grnr_sort: str = element("GRNrSort", default="")
    titel: str = element("Titel")
    geschaeftsart: str = element("Geschaeftsart")
    geschaeftsstatus: str = element("Geschaeftsstatus")
    dringlich: bool | None = element("Dringlich", nillable=True, default=None)
    vorberatende_kommision: Gremium | None = wrapped("VorberatendeKommision", element("Gremium", nillable=True, default=None))
    weitere_vorberatende_kommissionen: list[Gremium] = wrapped("VorberatendeKommision", element("Gremium", default=[]))
    federfuehrendes_departement: Departement | None = wrapped("FederfuehrendesDepartement", element("Departement", nillable=True, default=None))
    mitbeteiligte_departemente: list[Departement] = wrapped("MitbeteiligteDepartemente", element("Departement", default=[]))
    beginn: DateTimeFieldType = element("Beginn", default="")
    pendent_bei: str = element("PendentBei", default="")
    referendumsstatus: str = element("Referendumsstatus", default="")
    referendum: str = element("Referendum", default="")
    ablaufschritte: list[Aufgabe] = wrapped("Ablaufschritte", element("Aufgabe", default=[]))
    erstunterzeichner: Einreicher | None = wrapped("Erstunterzeichner", element("KontaktGremium", nillable=True, default=None))
    mitunterzeichner: list[Einreicher] = wrapped("Mitunterzeichner", element("KontaktGremium", default=[]))
    anzahl_mitunterzeichnende: Decimal | None = element("AnzahlMitunterzeichnende", nillable=True, default=None)
    verweis_zu: list[Verweis] = wrapped("VerweisZu", element("Geschaeft", default=[]))
    verweis_von: list[Verweis] = wrapped("VerweisVon", element("Geschaeft", default=[]))
    traktanden: list[Traktandum] = wrapped("Traktanden", element("Traktandum", default=[]))
    obj_guid: str = attr("OBJ_GUID")
    seq: str | None = attr("SEQ", nillable=True, default=None)
    idx: str | None = attr("IDX", nillable=True, default=None)
