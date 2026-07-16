# Executive Status Report Generator

This automation generates an executive status report from a fictional project portfolio dataset.

## Purpose

The purpose of this automation is to demonstrate how structured project information can be transformed into a concise executive report.

Instead of manually consolidating project status, risks, progress, and next actions, the script reads a CSV file and generates a Markdown report focused on portfolio visibility, risk discussion, and decision support.

## Input

The input file is:

```text
sample_projects.csv
```

The dataset includes fictional project information such as:

- Project ID
- Project name
- Business area
- Status
- Health
- Progress percentage
- Priority
- Risk level
- Main risk
- Next action
- Owner
- Due date
- Executive attention flag

## Output

The script generates or updates:

```text
sample_status_report.md
```

## How to Run

From the repository root, run:

```bash
python automations/executive-status-report/generate_status_report.py
```

On Windows, you can also use:

```bash
py automations\executive-status-report\generate_status_report.py
```

## Business Value

This type of automation can help teams:

- Reduce manual executive reporting effort
- Improve portfolio visibility
- Identify projects at risk
- Highlight critical or high-risk items
- Support stakeholder alignment
- Standardize status updates
- Improve decision-making conversations
- Connect project execution with business impact

## Executive Reporting Focus

The generated report includes:

- Portfolio summary
- Projects grouped by status
- Projects grouped by health
- Projects grouped by risk level
- High and critical risk projects
- Projects requiring executive attention
- Upcoming due dates
- Portfolio detail table

## Technical Notes

The script uses only Python standard library modules:

- `csv`
- `collections`
- `pathlib`

No external dependencies are required for the current version.

## Privacy Notice

This example uses fictional data only.

No private company data, customer information, credentials, financial information, tokens, or sensitive personal information should be included.
