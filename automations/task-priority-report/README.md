# Task Priority Report Automation

This automation generates a simple task priority report from a fictional CSV dataset.

## Purpose

The goal is to demonstrate how a repetitive business review process can be transformed into a simple automated report.

Instead of manually reviewing a list of tasks and preparing a summary, the script reads structured data and generates a Markdown report with key indicators.

## Input

The input file is:

```text
sample_tasks.csv
```

The dataset includes fictional task information such as:

- Task area
- Request description
- Priority
- Status
- Owner
- Due date

## Output

The script generates or updates:

```text
outputs/sample_report.md
```

## How to Run

From the repository root or from this folder, run:

```bash
python automations/task-priority-report/generate_report.py
```

or:

```bash
cd automations/task-priority-report
python generate_report.py
```

## Business Value

This type of automation can help teams:

- Identify high-priority tasks
- Improve operational visibility
- Reduce manual reporting effort
- Standardize recurring updates
- Support management review routines
- Detect workload concentration by area or status

## Technical Notes

The script uses only Python standard library modules:

- `csv`
- `collections`
- `pathlib`

No external dependencies are required for the current version.

## Privacy Notice

This example uses fictional data only.

No private company data, customer information, credentials, tokens, or sensitive personal information should be included.
