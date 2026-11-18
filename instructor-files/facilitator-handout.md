# Facilitator Handout: Work Your Future Self Can Follow

**Format:** 50-minute in-person workshop for first- and second-year undergraduates from any discipline. No coding, no software demos.
**Materials:** reproducible-research-workshop.pptx (15 slides, talking points in the speaker notes). Print this page, or copy the sample folder onto a whiteboard for the activity.

## Session goals
By the end, students can:
1. Define reproducibility and explain why it matters for their own projects.
2. Describe each FAIR principle (Findable, Accessible, Interoperable, Reusable) and give an example.
3. Use two everyday habits, consistent file naming and version history, and connect each to FAIR.

**Tone:** practical and encouraging. Lead with benefits to students' own work, not with fraud, retractions, or a "crisis."

## Timing
| Min | Slides | Segment |
|---|---|---|
| 0–5 | 1–2 | Opening: the confusing file from a semester ago |
| 5–15 | 3–4 | What reproducibility is; why it pays off |
| 15–27 | 5–9 | FAIR: overview, then one slide per principle (about 2.5 min each) |
| 27–37 | 10–11 | Habits: file naming; version history (concept only) |
| 37–47 | 12 | Activity: "Could Someone Else Do This?" |
| 47–50 | 13–15 | Debrief, getting help, further reading, sources |

If you're running long, shorten slides 6–9 to their examples.

## Activity setup (10 min, pairs)
Students work from the **sample project folder** on slide 12:
`turnout_final_v2_AM.csv` · `Turnout Data GA Nov 2024.csv` · `figure1.png` · `README.txt` (contains only "turnout data")

1. **(2 min)** Spot what would confuse someone new to the project.
2. **(4 min)** Rename the three data and image files.
3. **(3 min)** Add two lines to the README, and label each fix F, A, I, or R.
4. **(1 min)** Two pairs each share one rename.

If a pair gets stuck, ask: "What would you need to know to use this file tomorrow?"

**Sample answers**
- *Problems:* no date or election in the names; unknown initials ("AM"); "final_v2" isn't final; spaces in names; "figure1" says nothing about the figure; the README gives no source, date, or column meanings; two turnout files with no clear relationship.
- *Renames:* `2024-11-05_turnout-general_georgia-county.csv`; `2024-11-05_turnout-by-ad-campaign_georgia-precinct.csv`; `fig01_turnout-by-income_2024-general.png`. Any consistent date-first, hyphen-or-underscore pattern is correct.
- *README lines:* "Data: Georgia voter turnout, November 5, 2024 general election, by county and precinct; source and date downloaded: …" (R: provenance; F: description). "Columns: turnout_percentage = % of registered voters who voted; ad_campaign_group 1 = saw the ad campaign, 2 = did not" (I: clear meaning).
- *FAIR labels:* the renames support F (findable, sortable) and I (readable by other tools); the README lines support R, plus F through description.

## Two likely questions
**"Do I have to learn Git or GitHub?"**
No. Version control just means keeping a record of changes you can go back to. The version history in Google Docs already does this. Git and GitHub are powerful options researchers use, especially for code, and students may meet them later. They aren't required to work reproducibly.

**"My project uses interviews or sensitive data. Can it still be FAIR?"**
Yes. FAIR doesn't mean open. Data should be "as open as possible, as closed as necessary." Keep the data restricted, make the description public, and name a contact person or access procedure. For sensitive materials, students should talk to their instructor or advisor, or to the Research Data Management Librarian.

## Getting help
Digital Humanities Lab · StatLab · Research Data Management Librarian (all at Yale Library)

*Content adapted from The Turing Way (CC BY 4.0) and Bratt & Ellsworth (2025). Full references are on slide 15.*
