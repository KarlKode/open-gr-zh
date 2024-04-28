from typing import Optional

from pydantic_xml import BaseXmlModel, attr, element

__NAMESPACE__ = "http://www.cmiag.ch/cdws/Gremiumstyp"


class Gremiumstyp(BaseXmlModel, nsmap={"": __NAMESPACE__}):
    name: str = element("Name")
    inaktiv: Optional[bool] = element("Inaktiv", nillable=True, default=None)
    obj_guid: str = attr("OBJ_GUID")
    seq: Optional[str] = attr("SEQ", nillable=True, default=None)
    idx: Optional[str] = attr("IDX", nillable=True, default=None)
