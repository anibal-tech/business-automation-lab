from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent

INPUT_FILE = SCRIPT_DIR / "sample_projects.csv"
OUTPUT_FILE = SCRIPT_DIR / "sample_status_report.md"

REQUIRED_COLUMNS = {
    "project_id",
    "project_name",
    "area",
    "status",
    "health",
    "progress_pct",
    "priority",
    "risk_level",
    "main_risk",
    "next_action",
    "owner",
    "due_date",
    "executive_attention",
}

STATUS_ORDER = ["On Track", "At Risk", "Delayed", "Not Started", "Completed"]
HEALTH_ORDER = ["Green", "Amber", "Red", "Gray"]
RISK_ORDER = ["Critical", "High", "Medium", "Low"]


def normalize_value(value: str) -> str:
    """Normalize text values for consistent reporting."""
    return value.strip()


def load_projects(file_path: Path) -> list[dict[str, str]]:
    """Load project records from a CSV file and validate required columns."""
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


def count_by_field(projects: list[dict[str, str]], field: str) -> Counter:
    """Count projects by a specific field."""
    return Counter(normalize_value(project[field]) for project in projects)


def parse_progress(value: str) -> float:
    """Parse progress percentage as a float."""
    try:
        return float(normalize_value(value))
    except ValueError as error:
        raise ValueError(f"Invalid progress value: {value}") from error


def is_at_risk_or_delayed(project: dict[str, str]) -> bool:
    """Determine whether a project is at risk or delayed."""
    status = normalize_value(project["status"])
    return status in {"At Risk", "Delayed"}


def is_high_or_critical_risk(project: dict[str, str]) -> bool:
    """Determine whether a project has high or critical risk."""
    risk_level = normalize_value(project["risk_level"]).title()
    return risk_level in {"Critical", "High"}


def requires_executive_attention(project: dict[str, str]) -> bool:
    """Determine whether a project requires executive attention."""
    return normalize_value(project["executive_attention"]).lower() == "yes"


def risk_sort_key(project: dict[str, str]) -> tuple[int, str, str]:
    """Sort projects by risk level, due date, and project ID."""
    risk_level = normalize_value(project["risk_level"]).title()
    risk_index = RISK_ORDER.index(risk_level) if risk_level in RISK_ORDER else 99
    return risk_index, project["due_date"], project["project_id"]


def status_sort_key(project: dict[str, str]) -> tuple[int, str, str]:
    """Sort projects by status, due date, and project ID."""
    status = normalize_value(project["status"])
    status_index = STATUS_ORDER.index(status) if status in STATUS_ORDER else 99
    return status_index, project["due_date"], project["project_id"]


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


def append_project_list(
    report: list[str],
    title: str,
    projects: list[dict[str, str]],
) -> None:
    """Append a formatted project list to the report."""
    report.append(f"## {title}")
    report.append("")

    if not projects:
        report.append("No projects found.")
        report.append("")
        return

    for project in projects:
        report.append(
            f"- **{project['project_id']}** {project['project_name']} "
            f"({project['area']}) - "
            f"Status: {project['status']} - "
            f"Health: {project['health']} - "
            f"Progress: {project['progress_pct']}% - "
            f"Risk: {project['risk_level']} - "
            f"Due: {project['due_date']}"
        )
        report.append(f"  - Main risk: {project['main_risk']}")
        report.append(f"  - Next action: {project['next_action']}")
        report.append(f"  - Owner: {project['owner']}")

    report.append("")


def build_report(projects: list[dict[str, str]]) -> str:
    """Build a Markdown executive status report from project data."""
    if not projects:
        raise ValueError("No projects found in the input file.")

    total_projects = len(projects)

    status_count = count_by_field(projects, "status")
    health_count = count_by_field(projects, "health")
    risk_count = Counter(
        normalize_value(project["risk_level"]).title()
        for project in projects
    )

    average_progress = (
        sum(parse_progress(project["progress_pct"]) for project in projects)
        / total_projects
    )

    at_risk_or_delayed_projects = [
        project for project in projects
        if is_at_risk_or_delayed(project)
    ]

    high_risk_projects = sorted(
        [
            project for project in projects
            if is_high_or_critical_risk(project)
        ],
        key=risk_sort_key,
    )

    executive_attention_projects = sorted(
        [
            project for project in projects
            if requires_executive_attention(project)
        ],
        key=risk_sort_key,
    )

    upcoming_projects = sorted(
        projects,
        key=lambda project: (project["due_date"], project["project_id"]),
    )[:5]

    report: list[str] = []

    report.append("# Executive Status Report")
    report.append("")
    report.append("## Executive Summary")
    report.append("")
    report.append(f"- Total projects: {total_projects}")
    report.append(f"- Average progress: {average_progress:.1f}%")
    report.append(f"- Projects on track: {status_count.get('On Track', 0)}")
    report.append(f"- Projects at risk or delayed: {len(at_risk_or_delayed_projects)}")
    report.append(f"- High or critical risk projects: {len(high_risk_projects)}")
    report.append(f"- Projects requiring executive attention: {len(executive_attention_projects)}")
    report.append("")

    append_count_section(report, "Projects by Status", status_count, STATUS_ORDER)
    append_count_section(report, "Projects by Health", health_count, HEALTH_ORDER)
    append_count_section(report, "Projects by Risk Level", risk_count, RISK_ORDER)

    append_project_list(report, "High and Critical Risk Projects", high_risk_projects)
    append_project_list(report, "Projects Requiring Executive Attention", executive_attention_projects)
    append_project_list(report, "Upcoming Due Dates", upcoming_projects)

    report.append("## Portfolio Detail")
    report.append("")
    report.append("| ID | Project | Status | Health | Progress | Risk | Owner | Due Date |")
    report.append("|---|---|---|---|---:|---|---|---|")

    for project in sorted(projects, key=status_sort_key):
        report.append(
            f"| {project['project_id']} | {project['project_name']} | "
            f"{project['status']} | {project['health']} | "
            f"{project['progress_pct']}% | {project['risk_level']} | "
            f"{project['owner']} | {project['due_date']} |"
        )

    report.append("")
    report.append("## Management Notes")
    report.append("")
    report.append(
        "This report was generated from fictional project data as part of a business automation experiment."
    )
    report.append("")
    report.append(
        "The purpose is to demonstrate how structured project information can be transformed into a concise executive status report for portfolio visibility, risk discussion, and decision support."
    )
    report.append("")
    report.append("## Privacy Notice")
    report.append("")
    report.append(
        "This example uses fictional data only. No private company data, customer information, credentials, financial information, or sensitive personal information are included."
    )

    return "\n".join(report)


def save_report(content: str, output_file: Path) -> None:
    """Save the generated report as a Markdown file."""
    output_file.write_text(content, encoding="utf-8")


def main() -> None:
    """Run the executive status report generator."""
    projects = load_projects(INPUT_FILE)
    report = build_report(projects)
    save_report(report, OUTPUT_FILE)
    print(f"Executive status report generated successfully: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
