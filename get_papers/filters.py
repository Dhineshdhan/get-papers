from bs4 import BeautifulSoup
from typing import List, Dict
import re

# Expanded keywords list for non-academic affiliations
NON_ACADEMIC_KEYWORDS = [
    "Inc", "Ltd", "Pharma", "Biotech", "Therapeutics", "Corporation", "LLC",
    "Technologies", "Diagnostics", "Medical", "Labs", "Research", "GmbH",
    "Company", "Industry", "Pvt", "S.A.", "S.r.l", "Holdings", "Corp", "Co.", "Limited"
]

def is_non_academic(affiliation: str) -> bool:
    return any(keyword.lower() in affiliation.lower() for keyword in NON_ACADEMIC_KEYWORDS)

def parse_papers(xml_data: str) -> List[Dict]:
    soup = BeautifulSoup(xml_data, features="xml")
    papers = []

    for article in soup.find_all("PubmedArticle"):
        pmid_tag = article.find("PMID")
        title_tag = article.find("ArticleTitle")
        pub_date_tag = article.find("PubDate")

        pmid = pmid_tag.text if pmid_tag else ""
        title = title_tag.text if title_tag else ""
        pub_date_str = pub_date_tag.get_text(" ") if pub_date_tag else ""

        authors = article.find_all("Author")
        non_acad_authors = []
        companies = set()
        email = None

        for auth in authors:
            aff = auth.find("AffiliationInfo")
            aff_text = aff.Affiliation.text if aff and aff.Affiliation else ""
            if is_non_academic(aff_text):
                # Debug print
                print(f"🧾 Matched affiliation: {aff_text}")

                lastname = auth.LastName.text if auth.LastName else ""
                firstname = auth.ForeName.text if auth.ForeName else ""
                full_name = f"{firstname} {lastname}".strip()
                non_acad_authors.append(full_name)
                companies.add(aff_text)

                if not email:
                    match = re.search(r"[\w\.-]+@[\w\.-]+", aff_text)
                    if match:
                        email = match.group(0)

        if non_acad_authors:
            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date_str,
                "Non-academic Author(s)": ", ".join(non_acad_authors),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": email or "N/A",
            })

    return papers
