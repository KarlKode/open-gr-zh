from pydantic_xml import BaseXmlModel, attr, element

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Geschaeftsart"


class Geschaeftsart(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    name: str = element("Name")
    inaktiv: bool | None = element("Inaktiv", nillable=True, default=None)
    obj_guid: str = attr("OBJ_GUID")
    seq: str | None = attr("SEQ", nillable=True, default=None)
    idx: str | None = attr("IDX", nillable=True, default=None)

