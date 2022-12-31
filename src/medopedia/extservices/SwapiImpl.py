import httpx
import json

from src.medopedia.extapi.interface import MedopediaAPI


class SwapiImpl(MedopediaAPI):
    def search_for_character(self, search: str) -> str:
        url = "https://swapi.dev/api"
        full_url = url + "/people/?search=" + search

        print(full_url)
        response = httpx.get(full_url, timeout=None)
        print("<<< Request Duration: " + response.elapsed.__str__() + ">>>")
        formatted_json = json.dumps(json.loads(response.text), indent=2)
        return formatted_json
