from pydantic_xml import BaseXmlModel, attr, element

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Gremiumsuebersicht"


class Gremiumsuebersicht(BaseXmlModel, tag="Gremium", nsmap={"": __NAMESPACE__}):
    name: str = element("Name")
    kurzname: str = element("Kurzname")
    vater: str = element("Vater")
    inaktiv: bool | None = element("Inaktiv", nillable=True, default=None)
    gremiumstyp: str = element("Gremiumstyp")
    altsystem_id: str = element("AltsystemID")
    obj_guid: str = attr("OBJ_GUID")
    seq: str | None = attr("SEQ", nillable=True, default=None)
    idx: str | None = attr("IDX", nillable=True, default=None)
