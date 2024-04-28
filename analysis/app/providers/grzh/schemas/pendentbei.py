from pydantic_xml import BaseXmlModel, attr, element

__NAMESPACE__ = "http://www.cmiag.ch/cdws/PendentBei"


class PendentBei(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    name: str = element("Name")
    inaktiv: bool | None = element("Inaktiv", nillable=True, default=None)
    alt_system_id: str = element("AltsystemID", default="")
    obj_guid: str = attr("OBJ_GUID")
    seq: str | None = attr("SEQ", nillable=True, default=None)
    idx: str | None = attr("IDX", nillable=True, default=None)
