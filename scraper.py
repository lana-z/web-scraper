import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    citations = soup.find_all("sup", class_="reference")
    return len(citations)


def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    citations = soup.find_all("sup", class_="reference")
    report = ""
    
    for citation in citations:
        parent_element = citation.find_parent("p")
        if parent_element:
            report += f"{parent_element.text}\n\n"
    
    return report


url = "https://en.wikipedia.org/wiki/Neurology"

print(get_citations_needed_report(url))
print(f"Total citations: {get_citations_needed_count(url)}\n")