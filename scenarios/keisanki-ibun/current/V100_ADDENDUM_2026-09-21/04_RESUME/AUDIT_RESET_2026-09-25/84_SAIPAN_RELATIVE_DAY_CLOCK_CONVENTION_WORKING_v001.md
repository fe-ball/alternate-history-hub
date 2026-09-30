# Saipan relative-day clock convention
## 2026-09-30

Status: **SELECTED WORKING NOTATION RULE / NOT AUTHORITY / NO CANONICAL CLOCK ADVANCE**

Authority remains Branch B v100.
Canonical machine clock remains 1944-06-16T14:15.

Purpose:
reduce chronology errors caused by mixing:
- Japanese/local calendar dates;
- U.S. source dates / West Longitude Date labels;
- historical Saipan chronology;
- Branch chronology after divergence.

## 1. Primary operational clock

For Saipan ground / local-sea events use:

**B-D+n hh:mm**

where:
- B = current Branch;
- D+0 = Branch Saipan assault day / H-hour reference;
- n = elapsed local operational days after Branch H-hour.

Calendar date is secondary metadata.

Example:
- `B-D+5 evening (Branch local 20 Jun)`.

Do not write only `20 Jun evening` in new operational files when the relative day matters.

## 2. Historical comparison clock

Use:

**H-D+n**

for the historical Saipan campaign.

Historical source dates remain tagged separately:
- `H-D+2 / source says 17 Jun WLD`;
- do not silently convert WLD / local dates.

When Branch and history share the same assault-day start, the counters may initially align.
After event divergence, do not assume that an event occurring on B-D+n corresponds to the same historical event.

## 3. Dual-reference form

When historical comparison matters, use:

**B-D+n (Branch local date; comparator H-D+m / source-date label)**

Example:
- `B-D+5 18:00 (Branch 20 Jun; historical comparator H-D+5)`.

If the historical event being cited occurred on another relative day:
- write both explicitly.

## 4. Operation prefixes

Do not use bare D+ in cross-campaign files.

Use:
- `SAI B-D+` for Saipan Branch;
- `SAI H-D+` for historical Saipan;
- `ATTU B-D+` for Attu Branch;
- etc.

This prevents an Attu / Saipan / carrier-operation D+ clock from being merged accidentally.

## 5. Source-date guard

U.S. Navy communiques and operational records may use source-specific date conventions.

Rule:
- preserve the source label;
- compare by event sequence / elapsed time;
- only convert to Branch local date when the conversion is independently closed.

## 6. Existing files

Do not mass-rewrite files 01-83.

Going forward:
- handoff summaries should show B-D+n first;
- calendar date remains in parentheses;
- when revisiting an old event, add the relative label in the new audit file rather than silently changing old prose.

## 7. Current anchor

For the present thick-counterlanding work:
- Saipan assault = **SAI B-D+0**;
- current relief / thick-intervention problem = approximately **SAI B-D+5 evening/night**;
- all future 20/21-Jun references should carry that relative label.

This is a notation correction only.
