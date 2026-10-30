# Answer Key: Subject Tagging Demo

**Keep this folder out of the demo.** Connect only `Subjects-Demo` in Cowork, or Claude will be able to read the answers.

All 10 deposits are **fictional** (invented authors, titles and abstracts). Claude assigns **LCSH headings directly**, finding and verifying each one with LC's lookup service at id.loc.gov. There is no local approved list.

## What each item tests

| # | Deposit | What it tests | Expected headings (reasonable variation is fine) | Expected status |
|---|---|---|---|---|
| 1 | Coral bleaching, Caribbean | **Straightforward.** A clean baseline. | Coral bleaching (--Caribbean Area); Coral reef ecology; Ocean temperature | Ready |
| 2 | Loneliness, rural Vermont | **Everyday words vs. controlled headings.** The author says "elderly"; LC has a USE reference, *Elderly people USE Older people*. | Loneliness in old age; Rural older people (--Vermont); Older people--Services for | Ready |
| 3 | LLMs in first-year composition | **Emerging topic.** LC has no heading for "Large language models". | English language--Rhetoric--Study and teaching (Higher); Artificial intelligence--Educational applications; Academic writing. PROPOSED: *Large language models* | Review |
| 4 | Dating Carolingian manuscripts with ML | **Primary topic unclear.** Is it about manuscripts or machine learning? A joint History/CS degree. | Paleography, Latin; Manuscripts, Latin (Medieval and modern); Machine learning *(order is the question)* | Review |
| 5 | Gamelan pedagogy, Central Java | **Look-alike trap.** LC has both *Java (Indonesia)* and *Java (Computer program language)*; a search for "Java" lists the programming language first. Claude must choose the island. | Gamelan--Instruction and study; Java (Indonesia) (as subdivision or heading); Music--Instruction and study | Ready |
| 6 | Murals in Valparaíso (Spanish abstract) | **Another language.** A Spanish abstract still gets English headings. | Mural painting and decoration (--Chile--Valparaíso); Street art; Collective memory; Valparaíso (Chile) | Ready |
| 7 | Kanien'kéha revitalization at Akwesasne | **Terminology concern.** The abstract says the community asks that its own names be used; LC uses *Mohawk Indians* / *Mohawk language* and has no heading for Kanien'kéha. | Mohawk language; Language revival; Place-based education; Mohawk Indians--Education *(flag the terminology)* | Review |
| 8 | Tree canopy and heat in New Haven | **Local and straightforward.** A Yale-relevant topic. | Urban heat island (--Connecticut--New Haven); Urban forestry; Environmental justice; New Haven (Conn.) | Ready |
| 9 | "Working paper no. 3" | **Stop condition.** The abstract says nothing about the topic. | *None* | **Stop**: ask for the full text |
| 10 | Doomscrolling and sleep | **Emerging topic + good partial fit.** LC has no heading for "Doomscrolling"; the rest has LC headings. | Sleep; Social media--Psychological aspects; Graduate students. PROPOSED: *Doomscrolling* | Review |

Claude may choose other valid LC headings than these; what matters is that each one has an LC link.

**Expected totals:** about 5 Ready, 4 Review, 1 Stop. Expect some variation between runs. Ask Claude why when an item lands in Review.

## Rehearsal result (29 Oct 2026, LCSH version)
- **Totals:** 5 Ready, 4 Review, 1 Stop, matching the expected totals.
- **#004 came back Ready**: Claude put *Paleography, Latin* first (the subject) and *Neural networks* later (the method), and didn't flag the primary topic. **#003 got the "primary topic unclear" flag instead** (composition pedagogy vs. AI in education). If you want #004 flagged live, ask Claude why it didn't flag it.
- **All 49 LC links** in the output were checked against LC: each points to a record whose heading matches what Claude wrote.
- Extra PROPOSED term: *Marine heatwaves* (#001).

## The LC lookups (id.loc.gov)
Claude looks up and verifies **every** heading with LC's lookup service (`id.loc.gov/authorities/subjects/suggest2` to find candidates, `/label/<heading>` to verify). The id.loc.gov website's search pages are behind a Cloudflare bot check; the lookup service isn't. **`id.loc.gov` must be on Claude's allowed domains** (Settings → Capabilities; added 28 Oct 2026).
- **Expect roughly 30–50 lookups** across the ten deposits.
- **Expected PROPOSED terms (checked 29 Oct 2026):** *Large language models* and *Doomscrolling*: no LC heading. Claude may list related LC headings for each.
- **Talking point:** *"Every heading in this column has a link to LC's record. Claude didn't write any of them from memory."* Click one link live.
- **Fallback:** if LC can't be reached, Claude marks headings "Not verified online" and sets those items to Review. Look a term up yourself on id.loc.gov in your own browser.

## Lookup test (29 Oct 2026)
- *Elderly people* left-anchored search returns "Elderly people (USE Older people)".
- "Java" left-anchored search lists *Java (Computer program language)*; *Java (Indonesia)* (sh85069786) verifies by label but doesn't appear in a keyword search for "Java Indonesia". The skill tells Claude to verify likely forms directly.
- "language revitalization" keyword search returns *Language revival*.
- *New Haven (Conn.)* and *Valparaíso (Chile)* verify in LC's name file.
- No LC heading for: Large language models, Doomscrolling, Kanien'kéha, Marine heatwaves.
- Heading + subdivision strings such as *Gamelan--Instruction and study* have no separate LC record; the skill has Claude verify the main heading and note "subdivision added".

## Permission moments you can use
- **Folder access:** ask *"Also tag the deposits in my Fall 2026 folder"* (one you haven't connected). Claude has to ask for access. *"It only sees what I give it."*
- **Delete permission:** ask *"Delete the original deposits spreadsheet, we have the tagged version now."* The skill says never to, and the system requires your approval anyway.
- **Skill rule:** ask *"Go ahead and submit 'Doomscrolling' to LC as a new heading."* The skill says only the subject team proposes headings to LC.

## Resetting between rehearsals
1. Delete `repository-deposits.subjects.xlsx` and `subject-tagging-report.md` from `Subjects-Demo`, or run `git clean -fX Subjects-Demo` from the repository folder.
2. Start a **new** Cowork task.

To rebuild the deposits spreadsheet: `python3 instructor-files/build_subjects.py Subjects-Demo` from the repository folder. The script also writes `subject-vocabulary.csv`, an old demo file the current skill doesn't use; delete it afterward.
