import requests
from typing import List

def fetch_pubmed_ids(query: str) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": 100}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["esearchresult"]["idlist"]

def fetch_details(ids: List[str]) -> str:
    id_str = ",".join(ids)
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {"db": "pubmed", "id": id_str, "retmode": "xml"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text
