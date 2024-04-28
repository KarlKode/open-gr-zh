import datetime
from decimal import Decimal

from pydantic_xml import BaseXmlModel, attr, element, wrapped

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Kontakt"


class Adresse(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    addressart: str = element("Adressart", default="")
    strasse: str = element("Strasse", default="")
    plz: str = element("PLZ", default="")
    ort: str = element("Ort", default="")
    obj_guid: str = attr("OBJ_GUID")


class DateTimeFieldType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    start: datetime.datetime | None = element("Start", nillable=True, default=None)
    end: datetime.datetime | None = element("End", nillable=True, default=None)
    text: str = element("Text")


class Geschaeft(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    grnr: str = element("GRNr")
    grnr_sort: str = element("GRNrSort")
    titel: str = element("Titel")
    ratsgeschaeftsart: str = element("Ratsgeschaeftsart")
    obj_guid: str = attr("OBJ_GUID")


class Interessenbindung(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    bezeichnung: str = element("Bezeichnung")
    obj_guid: str = attr("OBJ_GUID")


class RenditionType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    extension: str = attr("Extension")
    ansicht: str = attr("Ansicht")


class SozialeMedien(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    adresse: str = element("Adresse", default="")
    typ: str = element("Typ", default="")
    obj_guid: str = attr("OBJ_GUID")


class Behoerdenmandat(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    gremium_name: str = element("GremiumName")
    gremium_kurzname: str = element("GremiumKurzname")
    gremium_guid: str = element("GremiumGuid")
    gremium_typ: str = element("GremiumTyp")
    gremium_inaktiv: bool | None = element("GremiumInaktiv", nillable=True, default=None)
    funktion: str = element("Funktion")
    dauer: DateTimeFieldType = element("Dauer")
    sitznummer: str = element("Sitznummer", default="")
    obj_guid: str = attr("OBJ_GUID")


class Parteizugehoerigkeit(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    partei: str = element("Partei")
    partei_guid: str = element("ParteiGuid")
    funktion: str = element("Funktion")
    dauer: DateTimeFieldType = element("Dauer")
    obj_guid: str = attr("OBJ_GUID")


class VersionType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    rendition: list[RenditionType] = element("Rendition")
    nr: Decimal = attr("Nr")


class DocumentFieldType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    version: list[VersionType] = element("Version", default=[])
    id: str = attr("ID")
    file_name: str = attr("FileName")


class Kontakt(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    altsystem_id: str = element("AltsystemID", default="")
    name_vorname: str = element("NameVorname")
    name: str = element("Name")
    vorname: str = element("Vorname")
    partei: str = element("Partei", default="")
    partei_guid: str = element("ParteiGuid", default="")
    fraktion: str = element("Fraktion", default="")
    wahlkreis: str = element("Wahlkreis", default="")
    wohnkreis: str = element("Wohnkreis", default="")
    beruf: str = element("Beruf", default="")
    jahrgang: Decimal | None = element("Jahrgang", nillable=True, default=None)
    todesjahr: Decimal | None = element("Todesjahr", nillable=True, default=None)
    geschlecht: str = element("Geschlecht", default="")
    bild: DocumentFieldType = element("Bild")
    email_geschaeft: str = element("EmailGeschaeft", default="")
    email_privat: str = element("EmailPrivat", default="")
    telefon_geschaeft: str = element("TelefonGeschaeft", default="")
    telefon_privat: str = element("TelefonPrivat", default="")
    telefon_mobile_geschaeft: str = element("TelefonMobileGeschaeft", default="")
    telefon_mobile_privat: str = element("TelefonMobilePrivat", default="")
    fax_geschaeft: str = element("FaxGeschaeft", default="")
    fax_privat: str = element("FaxPrivat", default="")
    homepage_geschaeft: str = element("HomepageGeschaeft", default="")
    homepage_privat: str = element("HomepagePrivat", default="")
    adressen: list[Adresse] = wrapped("Adressen", element("Adresse", default=[]))
    parteizugehoerigkeit: list[Parteizugehoerigkeit] = wrapped("Parteizugehoerigkeit", element("Parteizugehoerigkeit", default=[]))
    interessenbindung: list[Interessenbindung] = wrapped("Interessenbindung", element("Interessenbindung", default=[]))
    behoerdenmandat: list[Behoerdenmandat] = wrapped("Behoerdenmandat", element("Behoerdenmandat"))
    soziale_medien: list[SozialeMedien] = wrapped("SozialeMedien", element("Kommunikation", default=[]))
    erstunterzeichner: list[Geschaeft] = wrapped("Erstunterzeichner", element("Geschaeft", default=[]))
    mitunterzeichner: list[Geschaeft] = wrapped("Mitunterzeichner", element("Geschaeft", default=[]))
    obj_guid: str = attr("OBJ_GUID")
    seq: str | None = attr("SEQ", nillable=True, default=None)
    idx: str | None = attr("IDX", nillable=True, default=None)
