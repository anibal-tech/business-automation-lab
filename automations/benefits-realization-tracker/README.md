# Benefits Realization Tracker

This automation generates a benefits realization report from a fictional project benefits dataset.

## Purpose

The purpose of this automation is to demonstrate how expected benefits, actual benefits, gaps, ownership, and executive comments can be transformed into a concise management report.

Instead of tracking benefits manually across scattered notes or spreadsheets, the script reads a structured CSV file and generates a Markdown report focused on value realization, accountability, and executive visibility.

## Input

The input file is:

```text
sample_benefits.csv
```

The dataset includes fictional benefits information such as:

- Benefit ID
- Initiative
- Responsible area
- Benefit category
- Expected benefit
- Actual benefit
- Status
- Owner
- Target date
- Executive comment

## Output

The script generates or updates:

```text
sample_benefits_report.md
```

## How to Run

From the repository root, run:

```bash
python automations/benefits-realization-tracker/generate_benefits_report.py
```

On Windows, you can also use:

```bash
py automations\benefits-realization-tracker\generate_benefits_report.py
```

## Business Value

This type of automation can help teams:

- Track expected vs. actual benefits
- Identify benefit gaps
- Improve accountability by area and owner
- Support executive reporting
- Connect initiatives with measurable value
- Highlight benefits at risk
- Improve portfolio governance
- Standardize benefits realization conversations

## Executive Reporting Focus

The generated report includes:

- Total expected benefit
- Total actual benefit
- Benefit gap
- Overall realization percentage
- Benefits grouped by status
- Benefits grouped by responsible area
- Benefits grouped by category
- Benefits requiring attention
- Largest benefit gaps
- Upcoming target dates
- Benefit detail table

## Technical Notes

The script uses only Python standard library modules:

- `csv`
- `collections`
- `pathlib`

No external dependencies are required for the current version.

## Privacy Notice

This example uses fictional data only.

No private company data, customer information, financial information, credentials, tokens, or sensitive personal information should be included.
