# Outline: Work Your Future Self Can Follow: An Introduction to Reproducible Research

50-minute undergraduate workshop · 15 slides · built on library-template.pptx

One line per slide: **title** — key point — source file(s).

## Opening (5 min)

1. **Work Your Future Self Can Follow: An Introduction to Reproducible Research** — Title slide with presenter name and DH Lab; template campus photo. — brief.md; library-template.pptx (image)
2. **Could You Pick Up Your Own Project After a Semester Away?** — Scenario: a student reopens a folder with `turnout_final_v2_AM.csv` and can't tell which file is final, what the columns mean, or who "AM" is. The main person you keep records for is future you. — Intro-to-FAIR.pdf (slides 50–52); TuringWay-overview-barriers.md ("Takes time"); TuringWay-overview-benefit.md (#6 Ensure continuity)

## What reproducibility is and why it matters (10 min) — Outcome 1

3. **Reproducible Means Same Data, Same Steps, Same Result** — Plain definition, with the data/analysis grid (reproducible vs. replicable, robust, generalisable). Researchers in other fields use the same definition (Nosek, in *Reproducibility and Transparency*, 2025). Reproducible doesn't have to mean public. — TuringWay-overview-definitions.md; images/definitions.png; articles/ReproducibilityAndTransparency.pdf
4. **Working Reproducibly Pays Off for You First** — Six benefits from the illustration (track history, collaborate, write efficiently, get credit, continuity, accuracy). Science as "a show-me enterprise, not a trust-me enterprise" (Nosek, 2025). — TuringWay-overview-benefit.md; images/added-advantages.png; articles/ReproducibilityAndTransparency.pdf

## The FAIR principles (12 min) — Outcome 2

5. **FAIR: Four Questions to Ask About Your Research Materials** — FAIR defined in plain language: Findable, Accessible, Interoperable, Reusable; written in 2016 to help both people and computers find and reuse research. Each principle as a question. — TuringWay-rdm-fair.md; images/fair-principles.png; Intro-to-FAIR.pdf (slide 7); articles/The Fair Guiding Principles.pdf (Wilkinson et al., 2016)
6. **Findable: Can Someone Locate Your Work?** — Metadata = information about your data (title, author, keywords, date). A persistent identifier such as a DOI is a permanent link, assigned when you deposit in a repository (e.g., Yale Dataverse, Zenodo). — TuringWay-rdm-fair.md; Intro-to-FAIR.pdf (slides 11–14, 23–28)
7. **Accessible: Can Someone Get It, and Do They Know How?** — Accessible isn't the same as open: "as open as possible, as closed as necessary." Sensitive materials can list a contact person, and the description stays visible even when the data can't be. Journals that rewarded open data saw sharing rise more than tenfold (Munafò et al., 2017). — TuringWay-rdm-fair.md; Intro-to-FAIR.pdf (slides 35, 38, 40–41); articles/A Manifesto for Reproducible Science.pdf
8. **Interoperable: Can It Work With Other Data and Tools?** — Use open formats any program can open (.csv rather than a file that needs a paid license). Use clear column names and a codebook explaining what each column and code means. — TuringWay-rdm-fair.md; Intro-to-FAIR.pdf (slides 49–58, 61–62)
9. **Reusable: Can Someone Use It for Something New?** — A README explaining why, how, and with what limits the material was collected. A license (e.g., CC BY) says how others may reuse it. Provenance = the documented history of where the data came from and what was done to it. — TuringWay-rdm-fair.md; Intro-to-FAIR.pdf (slides 68–73)

## Everyday habits: putting FAIR into practice (10 min) — Outcome 3

10. **Habit 1: File Names That Explain Themselves** — Before/after list (e.g., `Turnout Data GA Nov 2024.csv` → `2024-11-05_turnout-general_georgia-county.csv`). Names should be readable by people and computers and sort in a useful order (dates as year-month-day). Connects to Findable and Interoperable. — Intro-to-FAIR.pdf (slides 53–55, Jenny Bryan's rules as presented there)
11. **Habit 2: Version History Keeps Every Draft Without the Clutter** — Version control records what changed, when, by whom, and why, so you can go back. You already use it: Google Docs version history. It replaces `final_v2_REAL.docx` and supports Reusable (provenance). Git and GitHub are options you may meet later, not requirements. — TuringWay-vcs.md

## Activity (10 min)

12. **Activity: Could Someone Else Do This?** — In pairs, students look at a messy sample project folder and its first-pass README. They rename three files, add two lines to the README, and note which FAIR question each fix answers. The sample folder adapts the file names and turnout example from the FAIR deck. — Intro-to-FAIR.pdf (slides 50–56); TuringWay-rdm-fair.md

## Debrief, getting help, and wrap-up (3 min)

13. **Start Small: One Habit This Week, and Where to Get Help** — Debrief prompts. Pick one habit to start. Library contacts: DH Lab, StatLab, and the Research Data Management Librarian. — Intro-to-FAIR.pdf (slide 78); TuringWay-overview-barriers.md ("little steps")
14. **Further Reading** — The Turing Way handbook; Jenny Bryan's *How to Name Files*; Yale Library's Research Data Management guide; *A FAIRy Tale*; How to FAIR; re3data.org repository finder. — TuringWay-rdm-fair.md; Intro-to-FAIR.pdf (embedded links)
15. **Sources** — Full APA 7 citations for every source used, including the Turing Way chapters (CC BY 4.0) and image credits. — sources/articles/articles.txt; Turing Way file headers; images/images.md

## Flags for review

**[NEEDS SOURCE]:** None at the outline stage. Every planned claim maps to a file in sources/.

**Things to check before I build:**
- **Contacts on slide 13** come from the November 2025 FAIR deck (Jordan Bratt, Ted Ellsworth, Brandon Miliate). Please confirm they're still current.
- **Turing Way APA dates:** the excerpts give no publication dates, so I'll cite each chapter as (n.d.) with its URL. I won't add a date or the handbook's main DOI, because neither appears in sources/.
- **Article with no author:** "Reproducibility and transparency: What's going on and how can we help" (Nature Communications, 2025) has no listed author. Under APA, the title goes in the author position. On slides it will read "Nosek, quoted in *Reproducibility and Transparency* (2025)".
- **Statistic I'm not using:** TuringWay-overview-benefit.md reports reproducibility rates of about 40% (psychology) and 10% (cancer biology), but its two citations appear to be swapped. The figure also leans toward the "crisis" framing the brief asks to avoid, so I've left it out. I've also left out Wallach et al. (2018) and its biomedical statistics because they don't fit an undergraduate audience. It stays available for a speaker note if you want it.
- **Opening scenario** is a hypothetical teaching example built on the FAIR deck's "new grad student" example, not a factual claim.
- **Slide count:** 15, the top of the brief's 13–15 range. To fit, I didn't give the agenda its own slide. The learning outcomes go in the speaker notes for slide 2 and in the handout.

**Conflicts between brief and guidelines:** None found so far. One to watch at build time: the guidelines require body text of at least 24 pt. Some template layouts default to smaller body text. Following the guidelines, I'll override those to 24 pt, which also means some slides carry fewer words than the template allows.
