from pydantic_xml import BaseXmlModel, attr, element

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Referendum"


class Referendum(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    name: str = element("Name")
    inaktiv: bool | None = element("Inaktiv", nillable=True, default=None)
    altsystem_id: str = element("AltsystemID", default="")
    obj_guid: str = attr("OBJ_GUID")
    seq: str | None = attr("SEQ", nillable=True, default=None)
    idx: str | None = attr("IDX", nillable=True, default=None)
