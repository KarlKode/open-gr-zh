from pydantic_xml import BaseXmlModel, attr, element

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Partei"

class Partei(BaseXmlModel, nsmap={'': __NAMESPACE__}):
    name: str = element("Name")
    kuerzel: str = element("Kuerzel")
    inaktiv: bool | None = element("Inaktiv", nillable=True)
    altsystem_id: str = element("AltsystemID")
    obj_guid: str = attr("OBJ_GUID")
    seq: str | None = attr("SEQ", nillable=True)
    idx: str | None = attr("IDX", nillable=True)

