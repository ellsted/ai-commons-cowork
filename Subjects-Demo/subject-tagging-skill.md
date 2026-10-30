# Subject Tagging Policy: Institutional Repository Deposits

Use this policy when assigning subject headings to theses, dissertations, working papers, and other items deposited in our institutional repository.

## How to decide what a work is about
- Read the **title and abstract**. Decide what the work is *about*, not just which methods it uses.
- **Author keywords are hints, not headings.** Authors use everyday language ("elderly", "LLMs"); our catalog uses Library of Congress Subject Headings (LCSH).
- An abstract in another language still gets English headings.

## Assigning headings
- Assign **2–4 LCSH headings** per item, with the most central topic first.
- **Every heading must come from LC.** Find it on id.loc.gov (see below) and use the authorized form exactly as LC gives it. Don't write a heading from memory.
- If an author's word is an LC **USE reference** (for example, *Elderly people USE Older people*), use the heading LC points to.
- Some LC headings look alike but mean different things, such as *Java (Indonesia)*, the island, and *Java (Computer program language)*. Check that the heading you choose matches the work's meaning.
- When a work focuses on a particular place, add the place as its own heading or as a geographic subdivision (e.g. `Urban heat island--Connecticut--New Haven`), using LC's form of the place name.
- You may add a standard subdivision such as `--Study and teaching` or `--Psychological aspects` to a heading. LC doesn't create separate records for most of these combinations, so verify the main heading and note "subdivision added".
- If a central concept has **no LC heading**, don't force a poor fit and don't invent a heading. List the concept as **PROPOSED**, with the term you would suggest. The subject team decides whether to propose it to LC.

## Looking up headings at the Library of Congress
Use LC's lookup service at id.loc.gov, not the website's search pages (they sit behind a bot check). Running a command to fetch these addresses is fine. URL-encode the terms.
- **Find candidates:** `https://id.loc.gov/authorities/subjects/suggest2?q=<term>&searchtype=keyword`. Also try `searchtype=left-anchored`, which shows USE references.
- **Verify a heading:** `https://id.loc.gov/authorities/subjects/label/<heading>` redirects to the record if the heading exists, and returns "not found" if it doesn't.
- **Place names** are in LC's name file: use the same two addresses with `/authorities/names/` instead of `/authorities/subjects/`.
- Give a link for every assigned heading, in the form `https://id.loc.gov/authorities/subjects/<id>.html` (or `/names/` for places).
- For each PROPOSED term, record **"No LC heading found"** and up to 3 related LC headings with links, for the subject librarian to consider. Don't assign them.
- **If a bot check, CAPTCHA, or "verify you are human" page appears, don't try to solve it.** Mark the affected headings "Not verified online", set the item to Review, and finish the rest of the work.
- If the service can't be reached, say so in the report. **Don't answer from memory** about whether LC has a heading.
- Use only id.loc.gov for this check, not other websites.

## Flag for the subject librarian (don't decide these yourself)
- **Primary topic unclear:** a work sits between disciplines and the first heading could reasonably go either way. Give both options and say why.
- **Terminology concerns:** the author or community has asked for terms that differ from LC's headings. Keep the LC heading, note the preferred term, and flag it. Don't substitute.
- **Not enough information:** if the title and abstract don't say what the work is about, **assign nothing** for that item and ask for the full text or the author's input.

## Output
1. A new spreadsheet named `repository-deposits.subjects.xlsx` with columns:
   Deposit ID · Title · Assigned headings (LCSH) · LC links · PROPOSED (no LC heading) · Author keywords (unchanged) · Status · Note for subject librarian
   - **Status** is one of: **Ready** (every heading verified, no flags) / **Review** (has a flag, a PROPOSED term, or an unverified heading) / **Stop** (not enough information)
2. A short report, `subject-tagging-report.md`: totals by status, then each Review and Stop item with the reason.

## Never
- Change or delete `repository-deposits.xlsx`.
- Submit a heading proposal to LC, or add headings to any local list. Only the subject team does that.
- Publish, upload, or send anything. This is a draft for review.
