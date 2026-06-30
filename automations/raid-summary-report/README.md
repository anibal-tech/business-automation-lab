# RAID Summary Report Automation

This automation generates an executive RAID summary report from a fictional CSV dataset.

RAID stands for:

- Risks
- Actions
- Issues
- Dependencies

## Purpose

The purpose of this automation is to demonstrate how a RAID log can be transformed into a concise management report.

Instead of manually reviewing risks, actions, issues, and dependencies, the script reads structured data and generates a Markdown report with key indicators, escalation items, and priority focus areas.

## Input

The input file is:

```text
sample_raid_log.csv
```

The dataset includes fictional RAID information such as:

- Item ID
- Type
- Description
- Priority
- Status
- Owner
- Due date
- Business impact
- Response plan
- Escalation requirement
- Last update

## Output

The script generates or updates:

```text
outputs/sample_raid_summary_report.md
```

## How to Run

From the repository root, run:

```bash
python automations/raid-summary-report/generate_raid_report.py
```

On Windows, you can also use:

```bash
py automations\raid-summary-report\generate_raid_report.py
```

## Business Value

This type of automation can help teams:

- Improve visibility of delivery risks
- Identify critical issues quickly
- Track blocked dependencies
- Highlight overdue or high-priority actions
- Support executive reporting
- Standardize RAID governance updates
- Reduce manual reporting effort

## Technical Notes

The script uses only Python standard library modules:

- `csv`
- `collections`
- `pathlib`

No external dependencies are required for the current version.

## Privacy Notice

This example uses fictional data only.

No private company data, customer information, credentials, tokens, financial data, or sensitive personal information should be included.
