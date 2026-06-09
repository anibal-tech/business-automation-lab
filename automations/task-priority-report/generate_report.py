from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent

INPUT_FILE = SCRIPT_DIR / "sample_tasks.csv"
OUTPUT_FILE = REPO_ROOT / "outputs" / "sample_report.md"

REQUIRED_COLUMNS = {
    "task_id",
    "area",
    "request",
    "priority",
    "status",
    "owner",
    "due_date",
}


def normalize_value(value: str) -> str:
    """Normalize text values for consistent reporting."""
    return value.strip()


def load_tasks(file_path: Path) -> list[dict[str, str]]:
    """Load tasks from a CSV file and validate required columns."""
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    with file_path.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = set(reader.fieldnames or [])

        missing_columns = REQUIRED_COLUMNS - fieldnames
        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            raise ValueError(f"Missing required columns: {missing}")

        return list(reader)


def build_report(tasks: list[dict[str, str]]) -> str:
    """Build a Markdown report from task data."""
    total_tasks = len(tasks)

    priority_count = Counter(
        normalize_value(task["priority"]).title()
        for task in tasks
    )

    status_count = Counter(
        normalize_value(task["status"])
        for task in tasks
    )

    area_count = Counter(
        normalize_value(task["area"])
        for task in tasks
    )

    high_priority_tasks = sorted(
        [
            task for task in tasks
            if normalize_value(task["priority"]).lower() == "high"
        ],
        key=lambda task: task["due_date"],
    )

    report: list[str] = []

    report.append("# Task Priority Report")
    report.append("")
    report.append("## Summary")
    report.append("")
    report.append(f"- Total tasks: {total_tasks}")
    report.append(f"- High priority tasks: {priority_count.get('High', 0)}")
    report.append(f"- Medium priority tasks: {priority_count.get('Medium', 0)}")
    report.append(f"- Low priority tasks: {priority_count.get('Low', 0)}")
    report.append("")

    report.append("## Status Breakdown")
    report.append("")
    for status, count in sorted(status_count.items()):
        report.append(f"- {status}: {count}")
    report.append("")

    report.append("## Area Breakdown")
    report.append("")
    for area, count in sorted(area_count.items()):
        report.append(f"- {area}: {count}")
    report.append("")

    report.append("## High Priority Tasks")
    report.append("")

    if not high_priority_tasks:
        report.append("No high priority tasks found.")
    else:
        for task in high_priority_tasks:
            report.append(
                f"- **{task['request']}** "
                f"({task['area']}) - "
                f"Owner: {task['owner']} - "
                f"Due: {task['due_date']} - "
                f"Status: {task['status']}"
            )

    report.append("")
    report.append("## Notes")
    report.append("")
    report.append(
        "This report was generated from fictional sample data "
        "as part of a business automation experiment."
    )
    report.append("")
    report.append(
        "The goal is to demonstrate how simple automation can improve "
        "visibility, reduce manual reporting effort, and support better "
        "management review routines."
    )

    return "\n".join(report)


def save_report(content: str, output_file: Path) -> None:
    """Save the generated report as a Markdown file."""
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(content, encoding="utf-8")


def main() -> None:
    """Run the task priority report automation."""
    tasks = load_tasks(INPUT_FILE)
    report = build_report(tasks)
    save_report(report, OUTPUT_FILE)
    print(f"Report generated successfully: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
