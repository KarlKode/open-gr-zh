import datetime
from decimal import Decimal

from pydantic_xml import BaseXmlModel, attr, element

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Behoerdenmandat"


class DateTimeFieldType(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    start: datetime.datetime | None = element("Start", nillable=True, default=None)
    end: datetime.datetime | None = element("End", nillable=True, default=None)
    text: str | None = element("Text", nillable=True, default=None)


class Behoerdenmandat(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    name: str = element("Name")
    vorname: str = element("Vorname")
    kontakt_guid: str = element("KontaktGuid")
    altsystem_id: str = element("AltsystemID")
    dauer: DateTimeFieldType = element("Dauer")
    gremium: str = element("Gremium")
    gremium_guid: str = element("GremiumGuid")
    gremiumstyp: str = element("Gremiumstyp")
    partei: str = element("Partei", default="")
    partei_guid: str = element("ParteiGuid", default="")
    titel: str = element("Titel", default="")
    wahlkreis: str = element("Wahlkreis", default="")
    wahlkreis_order: Decimal | None = element("WahlkreisOrder", nillable=True, default=None)
    wohnkreis: str = element("Wohnkreis", default="")
    funktion: str = element("Funktion")
    sitz: Decimal | None = element("Sitz", nillable=True, default=None)
    obj_guid: str = attr("OBJ_GUID")
    seq: str | None = attr("SEQ", nillable=True, default=None)
    idx: str | None = attr("IDX", nillable=True, default=None)
