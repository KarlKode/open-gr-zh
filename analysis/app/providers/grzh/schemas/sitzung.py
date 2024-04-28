import datetime
from decimal import Decimal

from pydantic_xml import BaseXmlModel, attr, element, wrapped

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Sitzung"


class Abstimmung(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    abstimmungstitel: str = element("Abstimmungstitel")
    abstimmungsnummer: Decimal | None = element("Abstimmungsnummer", nillable=True, default=False)
    schlussresultat: str = element("Schlussresultat", default="")
    obj_guid: str = attr("OBJ_GUID")


class DateTimeFieldType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    start: datetime.datetime | None = element("Start", nillable=True, default=None)
    end: datetime.datetime | None = element("End", nillable=True, default=None)
    text: str | None = element("Text", nillable=True, default=None)


class PersonWortmeldung(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    kontakt_guid: str = element("KontaktGuid")
    name: str = element("Name")
    partei: str = element("Partei")
    spezialfunktion: str = element("Spezialfunktion")
    obj_guid: str = attr("OBJ_GUID")


class RenditionType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    extension: str = attr("Extension")
    ansicht: str = attr("Ansicht")


class VersionType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    rendition: list[RenditionType] = element("Rendition", default=[])
    nr: Decimal = attr("Nr")


class DocumentFieldType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    version: list[VersionType] = element("Version")
    id: str = attr("ID")
    file_name: str = attr("FileName")


class Dokument(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    titel: str = element("Titel")
    file: DocumentFieldType = element("File")
    kategorie: str = element("Kategorie", default="")
    obj_guid: str = attr("OBJ_GUID")


class Audio(Dokument):
    pass


class Unterlage(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    beschluss: bool | None = element("Beschluss", nillable=True, default=None)
    dokumente: Dokument | None = wrapped("Dokumente", element("Dokument", nillable=True, default=None))
    obj_guid: str = attr("OBJ_GUID")


class Wortmeldung(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    subtraktandum: str = element("Subtraktandum", default="")
    sortierung: Decimal | None = element("Sortierung", nillable=True, default=None)
    level: Decimal | None = element("Level", nillable=True, default=None)
    aufzeichnung: Audio | None = wrapped("Aufzeichnung", element("Dokument", nillable=True, default=None))
    personen_wortmeldung: list[PersonWortmeldung] = wrapped("PersonenWortmeldung", element("PersonenWortmeldung", default=[]))
    obj_guid: str = attr("OBJ_GUID")


class Traktandum(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    geschaeft_guid: str = element("GeschaeftGuid", default="")
    geschaeft_altsystem_id: str = element("GeschaeftAltsystemID", default="")
    grnr: str = element("GRnr", default="")
    titel: str = element("Titel")
    traktandennummer: str = element("Traktandennummer")
    traktandierungscode: str = element("Traktandierungscode", default="")
    traktandierungscode_erlaeuterungen: str = element("TraktandierungscodeErlaeuterungen", default="")
    unterlagen: list[Unterlage] = wrapped("Unterlagen", element("Unterlage", default=[]))
    wortmeldungen: list[Wortmeldung] = wrapped("Wortmeldungen", element("Wortmeldung", default=[]))
    abstimmungen: list[Abstimmung] = wrapped("Abstimmungen", element("Abstimmung", default=[]))
    obj_guid: str = attr("OBJ_GUID")


class Traktanden(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    traktanden: list[Traktandum] = element("Traktandum", default=[])


class Sitzung(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    titel: str = element("Titel")
    datum: DateTimeFieldType = element("Datum")
    beginn: str = element("Beginn", default="")
    ende: str = element("Ende", default="")
    ende_nach_mitternacht: str = element("EndeNachMitternacht", default="")
    video_url: str = element("VideoURL", default="")
    #traktanden: list[Traktandum] = element("Traktanden", default=[])
    traktanden: list[Traktandum] = wrapped("Traktanden", element("Traktandum", default=[]))
    #traktanden: Traktanden = element("Traktanden")
    dokumente: list[Dokument] = wrapped("Dokumente", element("Dokument", default=[]))
    sitzungsaufzeichnung: Audio | None = wrapped("Sitzungsaufzeichnung", element("Dokument", nillable=True, default=None))
    obj_guid: str = attr("OBJ_GUID")
    seq: str | None = attr("SEQ", nillable=True, default=None)
    idx: str | None = attr("IDX", nillable=True, default=None)
