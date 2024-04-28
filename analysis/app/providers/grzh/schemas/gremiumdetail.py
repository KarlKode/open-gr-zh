import datetime

from pydantic_xml import BaseXmlModel, attr, element, wrapped

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Gremiumdetail"


class DateTimeFieldType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    start: datetime.datetime | None = element("Start", nillable=True, default=None)
    end: datetime.datetime | None = element("End", nillable=True, default=None)
    text: str | None = element("Text", nillable=True, default=None)


class Behoerdenmandat(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    kontakt_guid: str = element("KontaktGuid")
    vorname_name: str = element("VornameName")
    name: str = element("Name")
    vorname: str = element("Vorname")
    partei: str = element("Partei", default="")
    wahlkreis: str = element("Wahlkreis", default="")
    funktion: str = element("Funktion")
    dauer: DateTimeFieldType = element("Dauer")
    sitz: str = element("Sitz", default="")
    obj_guid: str = attr("OBJ_GUID")


class Sitzung(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    titel: str = element("Titel")
    datum: DateTimeFieldType = element("Datum")
    obj_guid: str = attr("OBJ_GUID")


class Gremiumdetail(BaseXmlModel, tag="Gremium", nsmap={"": __NAMESPACE__}):
    vater: str = element("Vater")
    name: str = element("Name")
    kurzname: str = element("Kurzname")
    bemerkung: str = element("Bemerkung", default="")
    gremiumstyp: str = element("Gremiumstyp")
    inaktiv: str = element("Inaktiv")
    sitzungen: list[Sitzung] = wrapped("Sitzungen", element("Sitzung", default=[]))
    behoerdenmitglieder: list[Behoerdenmandat] = wrapped("Behoerdenmitglieder", element("Behoerdenmandat", default=[]))
    obj_guid: str = attr("OBJ_GUID")
    seq: str | None = attr("SEQ", nillable=True, default=None)
    idx: str | None = attr("IDX", nillable=True, default=None)
