# AI-Assisted Status Report Prompt Pack

## Purpose

This document provides a set of original, fictional, and reusable prompt templates for generating AI-assisted status reports, executive updates, RAID summaries, action plans, and stakeholder communications.

The goal is to demonstrate how generative AI can support documentation, reporting, knowledge management, and operational efficiency without replacing human judgment.

This prompt pack is part of a professional portfolio and does not include course materials, proprietary content, confidential business information, or real company data.

## When to Use This Prompt Pack

Use these prompts for:

- Weekly executive status updates
- Project portfolio summaries
- RAID summary interpretation
- Risk narrative drafting
- Decision support notes
- Stakeholder communication drafts
- Action plan generation
- Meeting follow-up summaries
- Benefits realization updates
- Operational reporting

## Responsible AI Guidelines

Before using AI to generate status reports, follow these principles:

- Use fictional, anonymized, or sanitized data.
- Do not include confidential information.
- Do not include customer data.
- Do not include credentials, tokens, API keys, or access details.
- Do not include private financial information.
- Validate AI-generated outputs before sharing.
- Keep humans responsible for final decisions.
- Treat AI output as a draft, not as an approved report.
- Separate facts from assumptions.
- Clearly identify risks, decisions, and next actions.

## Input Quality Principles

AI output quality depends heavily on input quality.

Good inputs should include:

- Reporting period
- Audience
- Project or portfolio name
- Overall status
- Key accomplishments
- Risks and issues
- Dependencies
- Decisions required
- Upcoming milestones
- Owners
- Due dates
- Business impact
- Executive attention items

Avoid vague inputs such as:

```text
Create a project update.
```

Prefer structured inputs such as:

```text
Create an executive update for the weekly portfolio review using the following project status, risks, issues, decisions required, and next actions.
```

## Recommended Prompt Structure

A strong prompt should include:

```text
Role:
Context:
Task:
Input data:
Output format:
Constraints:
Review notes:
```

Example:

```text
Role: Act as a delivery manager preparing an executive update.
Context: The audience is senior leadership.
Task: Summarize the portfolio status.
Input data: Use only the information provided below.
Output format: Executive summary, risks, decisions required, next actions.
Constraints: Do not invent information. Flag missing information.
Review notes: Keep the tone concise, professional, and business-oriented.
```

---

# Prompt 1: Executive Status Summary

## Use Case

Generate a concise executive status update from structured project or portfolio data.

## Prompt Template

```text
Role:
Act as a Delivery Manager preparing a concise executive status update for senior stakeholders.

Context:
The audience needs a clear view of current status, business impact, risks, decisions required, and next actions.

Task:
Using only the information provided below, create an executive status report.

Input:
[Paste project or portfolio status input here]

Output format:
1. Executive Summary
2. Overall Status
3. Key Accomplishments
4. Risks and Issues
5. Decisions Required
6. Next Actions
7. Items Requiring Executive Attention

Constraints:
- Do not invent facts.
- Do not add names, dates, or risks that are not present in the input.
- If information is missing, include a "Missing Information" section.
- Keep the tone professional, clear, and business-oriented.
- Use bullet points where helpful.
```

---

# Prompt 2: RAID to Executive Update

## Use Case

Transform RAID information into a leadership-ready summary.

## Prompt Template

```text
Role:
Act as a PMO Lead preparing an executive RAID summary.

Context:
The audience needs visibility into top risks, critical issues, blocked dependencies, overdue actions, and decisions required.

Task:
Analyze the RAID input below and produce an executive summary.

Input:
[Paste RAID log or RAID summary here]

Output format:
1. RAID Executive Summary
2. Top Risks
3. Critical Issues
4. Blocked Dependencies
5. Overdue or High-Priority Actions
6. Escalations Required
7. Decisions Needed
8. Recommended Next Steps

Constraints:
- Use only the provided input.
- Prioritize items by business impact and urgency.
- Do not exaggerate or minimize risk.
- Clearly identify ownership and due dates when available.
- Flag missing owners or missing due dates.
```

---

# Prompt 3: Weekly Portfolio Digest

## Use Case

Create a weekly portfolio update from multiple project summaries.

## Prompt Template

```text
Role:
Act as a Technical Program Manager preparing a weekly portfolio digest.

Context:
The audience includes business stakeholders, delivery leaders, technical owners, and PMO representatives.

Task:
Create a weekly portfolio digest using the input below.

Input:
[Paste project updates here]

Output format:
1. Portfolio Health Summary
2. Projects On Track
3. Projects At Risk
4. Delayed Projects
5. Key Milestones Completed
6. Upcoming Milestones
7. Cross-Project Dependencies
8. Decisions Required
9. Executive Attention Items

Constraints:
- Keep the update concise.
- Do not include unnecessary technical detail.
- Highlight business impact.
- Separate facts from assumptions.
- Do not invent missing data.
```

---

# Prompt 4: Risk Narrative Draft

## Use Case

Turn raw risk information into a clear risk narrative for stakeholders.

## Prompt Template

```text
Role:
Act as a delivery leader documenting risk in a clear and actionable way.

Context:
The risk needs to be communicated to stakeholders without creating unnecessary alarm.

Task:
Convert the risk information below into a concise risk narrative.

Input:
[Paste risk details here]

Output format:
1. Risk Statement
2. Business Impact
3. Probability
4. Impact Level
5. Mitigation Plan
6. Owner
7. Due Date
8. Escalation Needed
9. Recommended Message for Leadership

Constraints:
- Keep the language factual.
- Do not blame individuals or teams.
- Do not invent mitigation actions.
- Flag missing information.
```

---

# Prompt 5: Action Plan Generator

## Use Case

Generate an action plan from project issues, risks, or meeting notes.

## Prompt Template

```text
Role:
Act as a project delivery manager creating a clear action plan.

Context:
The team needs ownership, due dates, and follow-up structure.

Task:
Create an action plan based on the input below.

Input:
[Paste issue summary, meeting notes, or RAID items here]

Output format:
| Action | Owner | Due Date | Priority | Related Risk or Issue | Expected Outcome |
|---|---|---|---|---|---|

Also include:
1. Immediate Actions
2. Follow-Up Actions
3. Items Requiring Escalation
4. Missing Information

Constraints:
- Use only provided names, owners, and dates.
- If owner or date is missing, mark as "To be assigned".
- Keep actions specific and measurable.
```

---

# Prompt 6: Stakeholder Communication Draft

## Use Case

Create a professional stakeholder update from a project status summary.

## Prompt Template

```text
Role:
Act as a delivery manager drafting a stakeholder communication.

Context:
The message should be clear, professional, concise, and suitable for business stakeholders.

Task:
Draft a stakeholder update using the information below.

Input:
[Paste status summary here]

Output format:
Subject:
Opening:
Current Status:
Key Updates:
Risks or Issues:
Decisions Required:
Next Steps:
Closing:

Constraints:
- Do not include confidential information.
- Do not overpromise.
- Keep the message calm and action-oriented.
- Make decision points explicit.
- Avoid technical jargon unless necessary.
```

---

# Prompt 7: Decision Support Note

## Use Case

Prepare a concise decision note when leadership input is required.

## Prompt Template

```text
Role:
Act as a Technical Program Manager preparing a decision support note.

Context:
Leadership needs to understand the decision, options, risks, and recommended path.

Task:
Create a decision support note using the input below.

Input:
[Paste decision context here]

Output format:
1. Decision Needed
2. Background
3. Options Considered
4. Recommended Option
5. Business Impact
6. Technical Impact
7. Risks
8. Dependencies
9. Deadline for Decision
10. Consequence of No Decision

Constraints:
- Do not invent options.
- Clearly state assumptions.
- Keep the recommendation balanced and practical.
- Highlight timing impact.
```

---

# Prompt 8: Meeting Follow-Up Summary

## Use Case

Convert meeting notes into a structured follow-up summary.

## Prompt Template

```text
Role:
Act as a PMO analyst summarizing a project meeting.

Context:
The team needs a clear summary of decisions, actions, risks, and next steps.

Task:
Summarize the meeting notes below.

Input:
[Paste meeting notes here]

Output format:
1. Meeting Summary
2. Decisions Made
3. Open Questions
4. Action Items
5. Risks and Issues
6. Dependencies
7. Next Meeting Focus

Action item format:
| Action | Owner | Due Date | Notes |
|---|---|---|---|

Constraints:
- Do not invent decisions.
- If a due date is missing, mark it as "To be confirmed".
- If an owner is missing, mark it as "To be assigned".
- Keep the summary concise and useful.
```

---

# Prompt 9: Benefits Realization Update

## Use Case

Summarize expected benefits, actual benefits, gaps, and management attention items.

## Prompt Template

```text
Role:
Act as a portfolio manager preparing a benefits realization update.

Context:
Leadership needs to understand whether expected benefits are being realized.

Task:
Create a benefits realization summary using the input below.

Input:
[Paste benefits tracking data here]

Output format:
1. Benefits Summary
2. Expected vs Actual Benefits
3. Largest Gaps
4. Benefits On Track
5. Benefits At Risk
6. Owners and Next Actions
7. Executive Attention Items

Constraints:
- Use only provided benefit values.
- Do not create financial numbers.
- Highlight gaps clearly.
- Include owners and due dates when available.
- Flag missing data.
```

---

# Prompt 10: Operational Readiness Summary

## Use Case

Summarize operational readiness before BAU handover.

## Prompt Template

```text
Role:
Act as a Service Delivery Manager preparing an operational readiness summary.

Context:
The audience needs to decide whether the solution is ready for Business As Usual support.

Task:
Create an operational readiness summary using the input below.

Input:
[Paste operational readiness checklist or handover notes here]

Output format:
1. Readiness Summary
2. Support Model Status
3. Monitoring and Alerts
4. Known Issues
5. Access Readiness
6. Runbooks and Documentation
7. Training and Knowledge Transfer
8. SLA or KPI Impact
9. BAU Handover Status
10. Conditions Before Approval

Constraints:
- Do not mark the solution ready unless the input supports it.
- Clearly list conditions, gaps, and owners.
- Keep the tone factual and practical.
```

## Sample Files

Sample input and output files are available here:

- [Sample status input](../examples/sample-status-input.md)
- [Sample AI-generated status output](../examples/sample-ai-generated-status-output.md)

## Final Principle

AI-assisted reporting should improve clarity, speed, and consistency.

It should not replace accountability, business judgment, stakeholder ownership, or final human review.
