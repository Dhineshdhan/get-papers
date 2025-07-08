import argparse
from get_papers.pubmed import fetch_pubmed_ids, fetch_details
from get_papers.filters import parse_papers
from get_papers.csv_writer import write_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("-f", "--file", help="Output CSV file")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    try:
        if args.debug:
            print(f"Fetching IDs for query: {args.query}")
        ids = fetch_pubmed_ids(args.query)
        if not ids:
            print("No results found.")
            return

        if args.debug:
            print(f"Found {len(ids)} papers.")

        xml = fetch_details(ids)
        papers = parse_papers(xml)

        if args.file:
            write_csv(args.file, papers)
            print(f"Saved to {args.file}")
        else:
            for paper in papers:
                print(paper)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
