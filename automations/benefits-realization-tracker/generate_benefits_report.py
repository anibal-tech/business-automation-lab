from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent

INPUT_FILE = SCRIPT_DIR / "sample_benefits.csv"
OUTPUT_FILE = SCRIPT_DIR / "sample_benefits_report.md"

REQUIRED_COLUMNS = {
    "benefit_id",
    "initiative",
    "area",
    "benefit_category",
    "expected_benefit_usd",
    "actual_benefit_usd",
    "status",
    "owner",
    "target_date",
    "executive_comment",
}

STATUS_ORDER = ["On Track", "At Risk", "Delayed", "Not Started", "Realized"]


def normalize_value(value: str) -> str:
    """Normalize text values for consistent reporting."""
    return value.strip()


def parse_amount(value: str) -> float:
    """Parse a numeric amount from text."""
    try:
        return float(normalize_value(value))
    except ValueError as error:
        raise ValueError(f"Invalid numeric value: {value}") from error


def format_money(value: float) -> str:
    """Format a numeric value as USD currency."""
    sign = "-" if value < 0 else ""
    return f"{sign}${abs(value):,.0f}"


def format_percent(value: float) -> str:
    """Format a numeric value as a percentage."""
    return f"{value:.1f}%"


def calculate_realization(expected: float, actual: float) -> float:
    """Calculate benefit realization percentage."""
    if expected == 0:
        return 0.0
    return (actual / expected) * 100


def load_benefits(file_path: Path) -> list[dict[str, str]]:
    """Load benefits from a CSV file and validate required columns."""
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


def count_by_field(benefits: list[dict[str, str]], field: str) -> Counter:
    """Count benefits by a specific field."""
    return Counter(normalize_value(benefit[field]) for benefit in benefits)


def aggregate_by_field(
    benefits: list[dict[str, str]],
    field: str,
) -> dict[str, dict[str, float]]:
    """Aggregate expected and actual benefits by a field."""
    result: dict[str, dict[str, float]] = defaultdict(
        lambda: {"expected": 0.0, "actual": 0.0}
    )

    for benefit in benefits:
        key = normalize_value(benefit[field])
        result[key]["expected"] += parse_amount(benefit["expected_benefit_usd"])
        result[key]["actual"] += parse_amount(benefit["actual_benefit_usd"])

    return dict(result)


def benefit_gap(benefit: dict[str, str]) -> float:
    """Calculate actual minus expected benefit."""
    expected = parse_amount(benefit["expected_benefit_usd"])
    actual = parse_amount(benefit["actual_benefit_usd"])
    return actual - expected


def requires_attention(benefit: dict[str, str]) -> bool:
    """Determine whether a benefit requires management attention."""
    status = normalize_value(benefit["status"])
    return status in {"At Risk", "Delayed", "Not Started"}


def gap_sort_key(benefit: dict[str, str]) -> tuple[float, str, str]:
    """Sort benefits by largest negative gap, target date, and benefit ID."""
    return benefit_gap(benefit), benefit["target_date"], benefit["benefit_id"]


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


def append_aggregate_table(
    report: list[str],
    title: str,
    aggregates: dict[str, dict[str, float]],
    key_label: str,
) -> None:
    """Append an aggregate table to the report."""
    report.append(f"## {title}")
    report.append("")
    report.append(f"| {key_label} | Expected Benefit | Actual Benefit | Gap | Realization |")
    report.append("|---|---:|---:|---:|---:|")

    for key in sorted(aggregates):
        expected = aggregates[key]["expected"]
        actual = aggregates[key]["actual"]
        gap = actual - expected
        realization = calculate_realization(expected, actual)

        report.append(
            f"| {key} | {format_money(expected)} | {format_money(actual)} | "
            f"{format_money(gap)} | {format_percent(realization)} |"
        )

    report.append("")


def append_benefit_list(
    report: list[str],
    title: str,
    benefits: list[dict[str, str]],
) -> None:
    """Append a formatted benefit list to the report."""
    report.append(f"## {title}")
    report.append("")

    if not benefits:
        report.append("No benefits found.")
        report.append("")
        return

    for benefit in benefits:
        expected = parse_amount(benefit["expected_benefit_usd"])
        actual = parse_amount(benefit["actual_benefit_usd"])
        gap = actual - expected
        realization = calculate_realization(expected, actual)

        report.append(
            f"- **{benefit['benefit_id']}** {benefit['initiative']} "
            f"({benefit['area']}) - "
            f"Status: {benefit['status']} - "
            f"Expected: {format_money(expected)} - "
            f"Actual: {format_money(actual)} - "
            f"Gap: {format_money(gap)} - "
            f"Realization: {format_percent(realization)} - "
            f"Target: {benefit['target_date']}"
        )
        report.append(f"  - Executive comment: {benefit['executive_comment']}")

    report.append("")


def build_report(benefits: list[dict[str, str]]) -> str:
    """Build a Markdown benefits realization report."""
    if not benefits:
        raise ValueError("No benefits found in the input file.")

    total_expected = sum(
        parse_amount(benefit["expected_benefit_usd"])
        for benefit in benefits
    )
    total_actual = sum(
        parse_amount(benefit["actual_benefit_usd"])
        for benefit in benefits
    )
    total_gap = total_actual - total_expected
    overall_realization = calculate_realization(total_expected, total_actual)

    status_count = count_by_field(benefits, "status")
    area_aggregates = aggregate_by_field(benefits, "area")
    category_aggregates = aggregate_by_field(benefits, "benefit_category")

    attention_benefits = sorted(
        [benefit for benefit in benefits if requires_attention(benefit)],
        key=gap_sort_key,
    )

    largest_gaps = sorted(benefits, key=gap_sort_key)[:5]

    upcoming_targets = sorted(
        benefits,
        key=lambda benefit: (benefit["target_date"], benefit["benefit_id"]),
    )[:5]

    report: list[str] = []

    report.append("# Benefits Realization Report")
    report.append("")
    report.append("## Executive Summary")
    report.append("")
    report.append(f"- Total benefits tracked: {len(benefits)}")
    report.append(f"- Total expected benefit: {format_money(total_expected)}")
    report.append(f"- Total actual benefit: {format_money(total_actual)}")
    report.append(f"- Total benefit gap: {format_money(total_gap)}")
    report.append(f"- Overall realization: {format_percent(overall_realization)}")
    report.append(f"- Benefits requiring attention: {len(attention_benefits)}")
    report.append("")

    append_count_section(report, "Benefits by Status", status_count, STATUS_ORDER)
    append_aggregate_table(report, "Benefits by Responsible Area", area_aggregates, "Area")
    append_aggregate_table(report, "Benefits by Category", category_aggregates, "Category")

    append_benefit_list(report, "Benefits Requiring Attention", attention_benefits)
    append_benefit_list(report, "Largest Benefit Gaps", largest_gaps)
    append_benefit_list(report, "Upcoming Target Dates", upcoming_targets)

    report.append("## Benefit Detail")
    report.append("")
    report.append(
        "| ID | Initiative | Area | Category | Status | Expected | Actual | Gap | Owner | Target Date |"
    )
    report.append("|---|---|---|---|---|---:|---:|---:|---|---|")

    for benefit in sorted(benefits, key=lambda item: (item["target_date"], item["benefit_id"])):
        expected = parse_amount(benefit["expected_benefit_usd"])
        actual = parse_amount(benefit["actual_benefit_usd"])
        gap = actual - expected

        report.append(
            f"| {benefit['benefit_id']} | {benefit['initiative']} | "
            f"{benefit['area']} | {benefit['benefit_category']} | "
            f"{benefit['status']} | {format_money(expected)} | "
            f"{format_money(actual)} | {format_money(gap)} | "
            f"{benefit['owner']} | {benefit['target_date']} |"
        )

    report.append("")
    report.append("## Management Notes")
    report.append("")
    report.append(
        "This report was generated from fictional benefits realization data as part of a business automation experiment."
    )
    report.append("")
    report.append(
        "The purpose is to demonstrate how expected benefits, actual benefits, ownership, gaps, and executive comments can be transformed into a concise management report for portfolio governance and value realization."
    )
    report.append("")
    report.append("## Privacy Notice")
    report.append("")
    report.append(
        "This example uses fictional data only. No private company data, customer information, financial information, credentials, or sensitive personal information are included."
    )

    return "\n".join(report)


def save_report(content: str, output_file: Path) -> None:
    """Save the generated report as a Markdown file."""
    output_file.write_text(content, encoding="utf-8")


def main() -> None:
    """Run the benefits realization report generator."""
    benefits = load_benefits(INPUT_FILE)
    report = build_report(benefits)
    save_report(report, OUTPUT_FILE)
    print(f"Benefits realization report generated successfully: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
