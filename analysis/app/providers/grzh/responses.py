from decimal import Decimal
from typing import TypeVar

from pydantic_xml import BaseXmlModel, attr, element

from app.providers.grzh.schemas.ablaufschritt import Ablaufschritt
from app.providers.grzh.schemas.abstimmung import Abstimmung
from app.providers.grzh.schemas.behoerdenmandat import Behoerdenmandat
from app.providers.grzh.schemas.departement import Departement
from app.providers.grzh.schemas.geschaeft import Geschaeft
from app.providers.grzh.schemas.geschaeftsart import Geschaeftsart
from app.providers.grzh.schemas.gremiumdetail import Gremiumdetail as Gremiumdetail
from app.providers.grzh.schemas.gremiumstyp import Gremiumstyp
from app.providers.grzh.schemas.gremiumsuebersicht import Gremiumsuebersicht as Gremiumuebersicht
from app.providers.grzh.schemas.kontakt import Kontakt
from app.providers.grzh.schemas.partei import Partei
from app.providers.grzh.schemas.pendentbei import PendentBei
from app.providers.grzh.schemas.referendum import Referendum
from app.providers.grzh.schemas.sitzung import Sitzung
from app.providers.grzh.schemas.wahlkreis import Wahlkreis
from app.providers.grzh.schemas.wohnkreis import Wohnkreis

SCHEMA_TYPES = Ablaufschritt | Abstimmung | Behoerdenmandat | Departement | Geschaeft | Partei | Gremiumdetail | Gremiumstyp | Gremiumuebersicht | Kontakt | PendentBei | Referendum | Sitzung | Wahlkreis | Wohnkreis

class SearchDetailResponseBaseHit(BaseXmlModel, nsmap={'': 'http://www.cmiag.ch/cdws/searchDetailResponse'}):
    guid: str = attr("Guid")
    id: int = attr("SEQ")
    relevance: Decimal = attr("Relevance")
    snippet: str | None = element("Snippet", nillable=True, default=None)
    obj: SCHEMA_TYPES


class SearchDetailResponseAblaufschrittHit(SearchDetailResponseBaseHit):
    obj: Ablaufschritt = element("Ablaufschritt")


Ablaufschritt.Hit = SearchDetailResponseAblaufschrittHit


class SearchDetailResponseAbstimmungHit(SearchDetailResponseBaseHit):
    obj: Abstimmung = element("Abstimmung")


Abstimmung.Hit = SearchDetailResponseAbstimmungHit


class SearchDetailResponseBehoerdenmandatHit(SearchDetailResponseBaseHit):
    obj: Behoerdenmandat = element("Behordenmandat")


Behoerdenmandat.Hit = SearchDetailResponseBehoerdenmandatHit


class SearchDetailResponseDepartementHit(SearchDetailResponseBaseHit):
    obj: Departement = element("Departement")


Departement.Hit = SearchDetailResponseDepartementHit


class SearchDetailResponseGeschaeftHit(SearchDetailResponseBaseHit):
    obj: Geschaeft = element("Geschaeft")


Geschaeft.Hit = SearchDetailResponseGeschaeftHit


class SearchDetailResponseGeschaeftsartHit(SearchDetailResponseBaseHit):
    obj: Geschaeftsart = element("Geschaeftsart")


Geschaeftsart.Hit = SearchDetailResponseGeschaeftsartHit


class SearchDetailResponseGremiumdetailHit(SearchDetailResponseBaseHit):
    obj: Gremiumdetail = element("Gremium")


Gremiumdetail.Hit = SearchDetailResponseGremiumdetailHit


class SearchDetailResponseGremiumstypHit(SearchDetailResponseBaseHit):
    obj: Gremiumstyp = element("Gremiumstyp")


Gremiumstyp.Hit = SearchDetailResponseGremiumstypHit


class SearchDetailResponseGremiumsuebersichtHit(SearchDetailResponseBaseHit):
    obj: Gremiumuebersicht = element("Gremium")


Gremiumuebersicht.Hit = SearchDetailResponseGremiumsuebersichtHit


class SearchDetailResponseKontaktHit(SearchDetailResponseBaseHit):
    obj: Kontakt = element("Kontakt")


Kontakt.Hit = SearchDetailResponseKontaktHit


class SearchDetailResponseParteiHit(SearchDetailResponseBaseHit):
    obj: Partei = element("Partei")


Partei.Hit = SearchDetailResponseParteiHit


class SearchDetailResponsePendentBeiHit(SearchDetailResponseBaseHit):
    obj: PendentBei = element("PendentBei")


PendentBei.Hit = SearchDetailResponsePendentBeiHit


class SearchDetailResponseReferendumHit(SearchDetailResponseBaseHit):
    obj: Referendum = element("Referendum")


Referendum.Hit = SearchDetailResponseReferendumHit


class SearchDetailResponseSitzungHit(SearchDetailResponseBaseHit):
    obj: Sitzung = element("Sitzung")


Sitzung.Hit = SearchDetailResponseSitzungHit


class SearchDetailResponseWahlkreisHit(SearchDetailResponseBaseHit):
    obj: Wahlkreis = element("Wahlkreis")


Wahlkreis.Hit = SearchDetailResponseWahlkreisHit


class SearchDetailResponseWohnkreisHit(SearchDetailResponseBaseHit):
    obj: Wohnkreis = element("Wohnkreis")


Wohnkreis.Hit = SearchDetailResponseWohnkreisHit


SearchDetailResponseHit = (
        SearchDetailResponseAblaufschrittHit
        | SearchDetailResponseAbstimmungHit
        | SearchDetailResponseBehoerdenmandatHit
        | SearchDetailResponseDepartementHit
        | SearchDetailResponseGeschaeftHit
        | SearchDetailResponseGeschaeftsartHit
        | SearchDetailResponseGremiumdetailHit
        | SearchDetailResponseGremiumstypHit
        | SearchDetailResponseGremiumsuebersichtHit
        | SearchDetailResponseKontaktHit
        | SearchDetailResponseParteiHit
        | SearchDetailResponsePendentBeiHit
        | SearchDetailResponseReferendumHit
        | SearchDetailResponseSitzungHit
        | SearchDetailResponseWahlkreisHit
        | SearchDetailResponseWohnkreisHit
)


#T = TypeVar("T")

class SearchDetailResponse[T](BaseXmlModel, tag="SearchDetailResponse", nsmap={'': 'http://www.cmiag.ch/cdws/searchDetailResponse'}):
    id: int = attr("IDXSEQ")
    q: str = attr("q")
    language: str = attr("l")
    start: int = attr("s")
    max_results: int = attr("m")
    num_hits: int = attr("numHits")
    index: str = attr("indexName")
    hits: list[T] = element("Hit")
