from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent

INPUT_FILE = SCRIPT_DIR / "sample_raid_log.csv"
OUTPUT_FILE = REPO_ROOT / "outputs" / "sample_raid_summary_report.md"

REQUIRED_COLUMNS = {
    "item_id",
    "type",
    "description",
    "priority",
    "status",
    "owner",
    "due_date",
    "business_impact",
    "response_plan",
    "escalation_required",
    "last_update",
}

TYPE_ORDER = ["Risk", "Action", "Issue", "Dependency"]
PRIORITY_ORDER = ["Critical", "High", "Medium", "Low"]
STATUS_ORDER = [
    "New",
    "Open",
    "In Progress",
    "Blocked",
    "Escalated",
    "Resolved",
    "Closed",
    "Deferred",
]


def normalize_value(value: str) -> str:
    """Normalize text values for consistent reporting."""
    return value.strip()


def load_raid_items(file_path: Path) -> list[dict[str, str]]:
    """Load RAID items from a CSV file and validate required columns."""
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


def count_by_field(items: list[dict[str, str]], field: str) -> Counter:
    """Count items by a specific field."""
    return Counter(normalize_value(item[field]) for item in items)


def is_open_item(item: dict[str, str]) -> bool:
    """Determine whether a RAID item is still open."""
    status = normalize_value(item["status"]).lower()
    return status not in {"resolved", "closed"}


def requires_escalation(item: dict[str, str]) -> bool:
    """Determine whether a RAID item requires escalation."""
    return normalize_value(item["escalation_required"]).lower() == "yes"


def is_priority_focus_item(item: dict[str, str]) -> bool:
    """Determine whether an item should be highlighted as critical or high priority."""
    priority = normalize_value(item["priority"]).title()
    return priority in {"Critical", "High"}


def priority_sort_key(item: dict[str, str]) -> tuple[int, str, str]:
    """Sort by priority, due date, and item ID."""
    priority = normalize_value(item["priority"]).title()
    priority_index = PRIORITY_ORDER.index(priority) if priority in PRIORITY_ORDER else 99
    return priority_index, item["due_date"], item["item_id"]


def append_count_section(
    report: list[str],
    title: str,
    counter: Counter,
    ordered_values: list[str],
) -> None:
    """Append a count section to the Markdown report."""
    report.append(f"## {title}")
    report.append("")

    for value in ordered_values:
        report.append(f"- {value}: {counter.get(value, 0)}")

    extra_values = sorted(set(counter.keys()) - set(ordered_values))
    for value in extra_values:
        report.append(f"- {value}: {counter[value]}")

    report.append("")


def append_item_list(
    report: list[str],
    title: str,
    items: list[dict[str, str]],
) -> None:
    """Append a formatted RAID item list."""
    report.append(f"## {title}")
    report.append("")

    if not items:
        report.append("No items found.")
        report.append("")
        return

    for item in items:
        report.append(
            f"- **{item['item_id']}** [{item['type']}] "
            f"{item['description']} - "
            f"Priority: {item['priority']} - "
            f"Status: {item['status']} - "
            f"Owner: {item['owner']} - "
            f"Due: {item['due_date']}"
        )
        report.append(f"  - Business impact: {item['business_impact']}")
        report.append(f"  - Response plan: {item['response_plan']}")

    report.append("")


def build_report(items: list[dict[str, str]]) -> str:
    """Build a Markdown executive RAID summary report."""
    total_items = len(items)

    type_count = count_by_field(items, "type")
    priority_count = count_by_field(items, "priority")
    status_count = count_by_field(items, "status")

    open_items = [item for item in items if is_open_item(item)]
    escalation_items = [item for item in items if requires_escalation(item)]
    blocked_items = [
        item for item in items
        if normalize_value(item["status"]).lower() == "blocked"
    ]
    priority_focus_items = sorted(
        [item for item in items if is_priority_focus_item(item)],
        key=priority_sort_key,
    )

    report: list[str] = []

    report.append("# RAID Summary Report")
    report.append("")
    report.append("## Executive Summary")
    report.append("")
    report.append(f"- Total RAID items: {total_items}")
    report.append(f"- Open items: {len(open_items)}")
    report.append(f"- Critical priority items: {priority_count.get('Critical', 0)}")
    report.append(f"- High priority items: {priority_count.get('High', 0)}")
    report.append(f"- Items requiring escalation: {len(escalation_items)}")
    report.append(f"- Blocked items: {len(blocked_items)}")
    report.append("")

    append_count_section(report, "Items by Type", type_count, TYPE_ORDER)
    append_count_section(report, "Items by Priority", priority_count, PRIORITY_ORDER)
    append_count_section(report, "Items by Status", status_count, STATUS_ORDER)

    append_item_list(report, "Critical and High Priority Items", priority_focus_items)
    append_item_list(report, "Items Requiring Escalation", escalation_items)
    append_item_list(report, "Blocked Items", blocked_items)

    report.append("## Management Notes")
    report.append("")
    report.append(
        "This report was generated from fictional sample RAID data as part of a business automation experiment."
    )
    report.append("")
    report.append(
        "The purpose is to demonstrate how structured RAID information can be transformed into an executive summary for delivery governance, escalation management, and decision support."
    )
    report.append("")

    report.append("## Privacy Notice")
    report.append("")
    report.append(
        "This example uses fictional data only. No private company data, customer information, credentials, tokens, or sensitive personal information are included."
    )

    return "\n".join(report)


def save_report(content: str, output_file: Path) -> None:
    """Save the generated report as a Markdown file."""
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(content, encoding="utf-8")


def main() -> None:
    """Run the RAID summary report automation."""
    items = load_raid_items(INPUT_FILE)
    report = build_report(items)
    save_report(report, OUTPUT_FILE)
    print(f"RAID summary report generated successfully: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
