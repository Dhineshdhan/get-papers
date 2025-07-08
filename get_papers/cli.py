import typer
from get_papers.pubmed import fetch_pubmed_ids, fetch_details
from get_papers.filters import parse_papers
from get_papers.csv_writer import write_csv

app = typer.Typer()

@app.command()
def get_papers_list(query: str, file: str = None, debug: bool = False):
    """
    Fetch PubMed papers with at least one non-academic author
    and optionally save the results to a CSV file.
    """
    try:
        if debug:
            typer.echo(f"📡 Fetching IDs for query: {query}")
        ids = fetch_pubmed_ids(query)

        if not ids:
            typer.echo("❌ No results found for the query.")
            raise typer.Exit()

        if debug:
            typer.echo(f"✅ Found {len(ids)} PubMed papers.")

        xml = fetch_details(ids)
        papers = parse_papers(xml)

        if debug:
            typer.echo(f"🧪 Filtered papers with non-academic authors: {len(papers)}")

        if not papers:
            typer.echo("⚠️ No qualifying papers found (with non-academic authors). Exiting.")
            raise typer.Exit()

        if file:
            write_csv(file, papers)
            typer.echo(f"💾 Saved results to '{file}'")
        else:
            for paper in papers:
                typer.echo(paper)

    except Exception as e:
        typer.echo(f"❌ Error: {e}", err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
