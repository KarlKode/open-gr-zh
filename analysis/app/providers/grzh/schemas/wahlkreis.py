from decimal import Decimal

from pydantic_xml import BaseXmlModel, attr, element

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Wahlkreis"


class Wahlkreis(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    name: str = element("Name")
    sortierung: Decimal | None = element("Sortierung", nillable=True, default=None)
    inaktiv: bool | None = element("Inaktiv", nillable=True, default=None)
    altsystem_id: str = element("AltsystemID", default="")
    obj_guid: str = attr("OBJ_GUID")
    seq: str | None = attr("SEQ", nillable=True, default=None)
    idx: str | None = attr("IDX", nillable=True, default=None)
