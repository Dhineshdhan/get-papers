# get-papers

## Description
CLI tool to fetch PubMed research papers with non-academic authors from pharma/biotech companies.

## Usage

```bash
poetry install
poetry run get-papers-list "cancer immunotherapy" -f results.csv --debug
```

## Features
- Filters non-academic authors by heuristic
- Outputs CSV or prints to terminal
- Uses PubMed API

## Tools Used
- [Poetry](https://python-poetry.org/)
- [Typer](https://typer.tiangolo.com/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## Development Note

This project was developed with assistance from OpenAI's GPT-4, a large language model. GPT-4 was used to guide architecture, generate boilerplate, and optimize the CLI interface and parsing logic.
