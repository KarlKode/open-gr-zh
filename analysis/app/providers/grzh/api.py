import asyncio
from collections.abc import AsyncIterable

import httpx

from app.providers.grzh.responses import SCHEMA_TYPES, SearchDetailResponse
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

URL = "https://www.gemeinderat-zuerich.ch/api"

FUNCTION_SEARCH = "search"
FUNCTION_SEARCHDETAIL = "searchdetails"


class GrzhApi:
    """API for the Gemeinderat Zürich."""

    def __init__(self) -> None:
        self.url = URL
        self.max_rows = 100
        self.language = "de-CH"

    async def search_ablaufschritt(self, q: str, limit: int | None = None) -> AsyncIterable[Ablaufschritt]:
        """
        Search for Ablaufschritt.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Ablaufschritt objects.
        """
        return self._search(Ablaufschritt, q, limit)

    async def get_ablaufschritt(self, guid: str) -> Ablaufschritt | None:
        """
        Get ablaufschritt by guid.

        :param guid: GUID of the ablaufschritt.
        :return: Ablaufschritt or None.
        """
        results = await self.search_ablaufschritt(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_abstimmung(self, q: str, limit: int | None = None) -> AsyncIterable[Abstimmung]:
        """
        Search for Abstimmung.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Abstimmung objects.
        """
        return self._search(Abstimmung, q, limit, max_rows=100)

    async def get_abstimmung(self, guid: str) -> Abstimmung | None:
        """
        Get abstimmung by guid.

        :param guid: GUID of the abstimmung.
        :return: Abstimmung or None.
        """
        results = await self.search_abstimmung(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_behoerdenmandat(self, q: str, limit: int | None = None) -> AsyncIterable[Behoerdenmandat]:
        """
        Search for Behoerdenmandat.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Behoerdenmandat objects.
        """
        return self._search(Behoerdenmandat, q, limit)

    async def get_behoerdenmandat(self, guid: str) -> Behoerdenmandat | None:
        """
        Get behoerdenmandat by guid.

        :param guid: GUID of the behoerdenmandat.
        :return: Behoerdenmandat or None.
        """
        results = await self.search_behoerdenmandat(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_departement(self, q: str, limit: int | None = None) -> AsyncIterable[Departement]:
        """
        Search for Departement.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Departement objects.
        """
        return self._search(Departement, q, limit)

    async def get_departement(self, guid: str) -> Departement | None:
        """
        Get departement by guid.

        :param guid: GUID of the departement.
        :return: Departement or None.
        """
        results = await self.search_departement(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_geschaeft(self, q: str, limit: int | None = None) -> AsyncIterable[Geschaeft]:
        """
        Search for Geschaeft.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Geschaeft objects.
        """
        return self._search(Geschaeft, q, limit)

    async def get_geschaeft(self, guid: str) -> Geschaeft | None:
        """
        Get geschaeft by guid.

        :param guid: GUID of the geschaeft.
        :return: Geschaeft or None.
        """
        results = await self.search_geschaeft(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_geschaeftsart(self, q: str, limit: int | None = None) -> AsyncIterable[Geschaeftsart]:
        """
        Search for Geschaeftsart.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Geschaeftsart objects.
        """
        return self._search(Geschaeftsart, q, limit)

    async def get_geschaeftsart(self, guid: str) -> Geschaeftsart | None:
        """
        Get geschaeftsart by guid.

        :param guid: GUID of the geschaeftsart.
        :return: Geschaeftsart or None.
        """
        results = await self.search_geschaeftsart(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_gremiumdetail(self, q: str, limit: int | None = None) -> AsyncIterable[Gremiumdetail]:
        """
        Search for Gremium detail.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Gremiumdetail objects.
        """
        return self._search(Gremiumdetail, q, limit)

    async def get_gremiumdetail(self, guid: str) -> Gremiumdetail | None:
        """
        Get gremiumdetail by guid.

        :param guid: GUID of the gremiumdetail.
        :return: Gremiumdetail or None.
        """
        results = await self.search_gremiumdetail(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_gremiumstyp(self, q: str, limit: int | None = None) -> AsyncIterable[Gremiumstyp]:
        """
        Search for Gremiumstyp.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Gremiumstyp objects.
        """
        return self._search(Gremiumstyp, q, limit)

    async def get_gremiumstyp(self, guid: str) -> Gremiumstyp | None:
        """
        Get gremiumstyp by guid.

        :param guid: GUID of the gremiumstyp.
        :return: Gremiumstyp or None.
        """
        results = await self.search_gremiumstyp(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_gremiumuebersicht(self, q: str, limit: int | None = None) -> AsyncIterable[Gremiumuebersicht]:
        """
        Search for Gremium uebersicht.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Gremiumuebersicht objects.
        """
        return self._search(Gremiumuebersicht, q, limit)

    async def get_gremiumuebersicht(self, guid: str) -> Gremiumuebersicht | None:
        """
        Get gremiumuebersicht by guid.

        :param guid: GUID of the gremiumuebersicht.
        :return: Gremiumuebersicht or None.
        """
        results = await self.search_gremiumuebersicht(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_kontakt(self, q: str, limit: int | None = None) -> AsyncIterable[Kontakt]:
        """
        Search for Kontakt.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Kontakt objects.
        """
        return self._search(Kontakt, q, limit)

    async def get_kontakt(self, guid: str) -> Kontakt | None:
        """
        Get kontakt by guid.

        :param guid: GUID of the kontakt.
        :return: Kontakt or None.
        """
        results = await self.search_kontakt(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_partei(self, q: str, limit: int | None = None) -> AsyncIterable[Partei]:
        """
        Search for Partei.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Partei objects.
        """
        return self._search(Partei, q, limit)

    async def get_partei(self, guid: str) -> Partei | None:
        """
        Get partei by guid.

        :param guid: GUID of the partei.
        :return: Partei or None.
        """
        results = await self.search_partei(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)


    async def search_pendentbei(self, q: str, limit: int | None = None) -> AsyncIterable[PendentBei]:
        """
        Search for PendentBei.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of PendentBei objects.
        """
        return self._search(PendentBei, q, limit)

    async def get_pendentbei(self, guid: str) -> PendentBei | None:
        """
        Get pendentBei by guid.

        :param guid: GUID of the pendentBei.
        :return: PendentBei or None.
        """
        results = await self.search_pendentbei(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_referendum(self, q: str, limit: int | None = None) -> AsyncIterable[Referendum]:
        """
        Search for Referendum.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Referendum objects.
        """
        return self._search(Referendum, q, limit)

    async def get_referendum(self, guid: str) -> Referendum | None:
        """
        Get referendum by guid.

        :param guid: GUID of the referendum.
        :return: Referendum or None.
        """
        results = await self.search_referendum(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_sitzung(self, q: str, limit: int | None = None) -> AsyncIterable[Sitzung]:
        """
        Search for Sitzung.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Sitzung objects.
        """
        return self._search(Sitzung, q, limit)

    async def get_sitzung(self, guid: str) -> Sitzung | None:
        """
        Get sitzung by guid.

        :param guid: GUID of the sitzung.
        :return: Sitzung or None.
        """
        results = await self.search_sitzung(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_wahlkreis(self, q: str, limit: int | None = None) -> AsyncIterable[Wahlkreis]:
        """
        Search for Wahlkreis.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Wahlkreis objects.
        """
        return self._search(Wahlkreis, q, limit)

    async def get_wahlkreis(self, guid: str) -> Wahlkreis | None:
        """
        Get wahlkreis by guid.

        :param guid: GUID of the wahlkreis.
        :return: Wahlkreis or None.
        """
        results = await self.search_wahlkreis(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def search_wohnkreis(self, q: str, limit: int | None = None) -> AsyncIterable[Wohnkreis]:
        """
        Search for Wohnkreis.

        :param q: The query string.
        :param limit: The maximum number of results to return.
        :return: A list of Wohnkreis objects.
        """
        return self._search(Wohnkreis, q, limit)

    async def get_wohnkreis(self, guid: str) -> Wohnkreis | None:
        """
        Get wohnkreis by guid.

        :param guid: GUID of the wohnkreis.
        :return: Wohnkreis or None.
        """
        results = await self.search_wohnkreis(f"OBJ_GUID adj \"{guid}\"", 1)
        return await anext(results, None)

    async def _search(self, t: SCHEMA_TYPES, q: str, limit: int | None = None, max_rows: int | None = None) -> AsyncIterable[SCHEMA_TYPES]:
        index = t.__name__.lower()
        if max_rows is None:
            max_rows = self.max_rows
        if limit is not None and limit < max_rows:
            max_rows = limit
        params = {
            "q": q,
            "m":max_rows,
            "l": self.language,
        }

        start = 1
        while True:
            params["s"] = start
            r = await self._get(index, FUNCTION_SEARCHDETAIL, params)
            r.raise_for_status()

            try:
                res = SearchDetailResponse[t.Hit].from_xml(r.content)
            except Exception as exc:
                raise exc
            for hit in res.hits:
                yield hit.obj

            start += len(res.hits)
            if start >= res.num_hits or (limit is not None and start >= limit):
                break

    async def _client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient()

    async def _get(self, index: str, function: str | None, params: dict[str, int | str]) -> httpx.Response:
        async with await self._client() as client:
            url_parts = [self.url, index]
            if function:
                url_parts.append(function)
            url = "/".join(url_parts)
            return await client.get(url, params=params, follow_redirects=True)


async def main() -> None:
    """Start main function."""
    api = GrzhApi()

    # ablaufschritt = await api.search_ablaufschritt("seq >= 0")
    # print(ablaufschritt)

    # res = await api.search_partei("seq >= 0", limit=10000)
    # parteien = []
    # async for r in res:
    #     print(r)
    #     parteien.append(r)
    # print(len(parteien))

    # res = await api.search_abstimmung("seq >= 0", limit=1000)
    # abstimmungen = []
    # async for r in res:
    #     print(r)
    #     abstimmungen.append(r)
    # print(len(abstimmungen))

    # res = await api.search_sitzung("seq >= 0", limit=10000)
    # sitzungen = []
    # async for r in res:
    #     print(r)
    #     sitzungen.append(r)
    # print(len(sitzungen))

    limit = 1000

    res = await api.search_ablaufschritt("seq >= 0", limit=limit)
    ablaufschritte = [res async for res in res]
    print(f"Ablaufschritte: {len(ablaufschritte)}")
    print(ablaufschritte)

    ablaufschritt = await api.get_ablaufschritt(ablaufschritte[0].obj_guid)
    print(f"Ablaufschritt: {ablaufschritt}")

    res = await api.search_abstimmung("seq >= 0", limit=limit)
    abstimmungen = [res async for res in res]
    print(f"Abstimmungen: {len(abstimmungen)}")

    abstimmung = await api.get_abstimmung(abstimmungen[0].obj_guid)
    print(f"Abstimmung: {abstimmung}")

    res = await api.search_behoerdenmandat("seq >= 0", limit=limit)
    behoerdenmandate = [res async for res in res]
    print(f"Behoerdenmandate: {len(behoerdenmandate)}")

    behoerdenmandat = await api.get_behoerdenmandat(behoerdenmandate[0].obj_guid)
    print(f"Behoerdenmandat: {behoerdenmandat}")

    res = await api.search_departement("seq >= 0", limit=limit)
    departemente = [res async for res in res]
    print(f"Departement: {len(departemente)}")

    departement = await api.get_departement(departemente[0].obj_guid)
    print(f"Departement: {departement}")

    res = await api.search_geschaeft("seq >= 0", limit=limit)
    geschaefte = [res async for res in res]
    print(f"Geschaefte: {len(geschaefte)}")

    geschaeft = await api.get_geschaeft(geschaefte[0].obj_guid)
    print(f"Geschaeft: {geschaeft}")

    res = await api.search_geschaeftsart("seq >= 0", limit=limit)
    geschaeftsarten = [res async for res in res]
    print(f"Geschaeftsarten: {len(geschaeftsarten)}")

    geschaeftsart = await api.get_geschaeftsart(geschaeftsarten[0].obj_guid)
    print(f"Geschaeftsart: {geschaeftsart}")

    res = await api.search_gremiumdetail("seq >= 0", limit=limit)
    gremiumdetails = [res async for res in res]
    print(f"Gremiumdetails: {len(gremiumdetails)}")

    gremiumdetail = await api.get_gremiumdetail(gremiumdetails[0].obj_guid)
    print(f"Gremiumdetail: {gremiumdetail}")

    res = await api.search_gremiumstyp("seq >= 0", limit=limit)
    gremiumstypen = [res async for res in res]
    print(f"Gremiumstypen: {len(gremiumstypen)}")

    gremiumstyp = await api.get_gremiumstyp(gremiumstypen[0].obj_guid)
    print(f"Gremiumstyp: {gremiumstyp}")

    res = await api.search_gremiumuebersicht("seq >= 0", limit=limit)
    gremiumuebersichten = [res async for res in res]
    print(f"Gremiumuebersichten: {len(gremiumuebersichten)}")

    gremiumuebersicht = await api.get_gremiumuebersicht(gremiumuebersichten[0].obj_guid)
    print(f"Gremiumuebersicht: {gremiumuebersicht}")

    res = await api.search_kontakt("seq >= 0", limit=limit)
    kontakte = [res async for res in res]
    print(f"Kontakte: {len(kontakte)}")

    kontakt = await api.get_kontakt(kontakte[0].obj_guid)
    print(f"Kontakt: {kontakt}")

    res = await api.search_partei("seq >= 0", limit=limit)
    parteien = [res async for res in res]
    print(f"Parteien: {len(parteien)}")

    partei = await api.get_partei(parteien[0].obj_guid)
    print(f"Partei: {partei}")

    res = await api.search_pendentbei("seq >= 0", limit=limit)
    pendentbeis = [res async for res in res]
    print(f"Pendentbeis: {len(pendentbeis)}")

    pendentbei = await api.get_pendentbei(pendentbeis[0].obj_guid)
    print(f"Pendentbei: {pendentbei}")

    res = await api.search_referendum("seq >= 0", limit=limit)
    referenden = [res async for res in res]
    print(f"Referenden: {len(referenden)}")

    referendum = await api.get_referendum(referenden[0].obj_guid)
    print(f"Referendum: {referendum}")

    res = await api.search_sitzung("seq >= 0", limit=limit)
    sitzungen = [res async for res in res]
    print(f"Sitzungen: {len(sitzungen)}")

    sitzung = await api.get_sitzung(sitzungen[0].obj_guid)
    print(f"Sitzung: {sitzung}")

    res = await api.search_wahlkreis("seq >= 0", limit=limit)
    wahlkreise = [res async for res in res]
    print(f"Wahlkreise: {len(wahlkreise)}")

    wahlkreis = await api.get_wahlkreis(wahlkreise[0].obj_guid)
    print(f"Wahlkreis: {wahlkreis}")

    res = await api.search_wohnkreis("seq >= 0", limit=limit)
    wohnkreise = [res async for res in res]
    print(f"Wohnkreise: {len(wohnkreise)}")

    wohnkreis = await api.get_wohnkreis(wohnkreise[0].obj_guid)
    print(f"Wohnkreis: {wohnkreis}")


if __name__ == "__main__":
    asyncio.run(main())
