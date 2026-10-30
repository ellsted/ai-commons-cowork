# ai-commons-cowork

Intro to Claude Cowork for librarians: slides, a demo on creating presentations, and a subject-tagging demo that checks headings against LCSH at id.loc.gov.

Presented by Ted Ellsworth, PhD, and Jordan Bratt, PhD.

## What's here

```
presentation/      Slides (PDF and Quarto source) and screenshots
Subjects-Demo/     The folder you connect for the subject-tagging demo
instructor-files/  Answer key and the script that builds the demo spreadsheet
```

## Slides

The slides are in `presentation/intro-to-claude-cowork.pdf`.

To rebuild them from source, you need [Quarto](https://quarto.org), XeLaTeX, and the CMU Serif font. Then run:

```
cd presentation
quarto render intro-to-claude-cowork.qmd
```

## Demo 1: Creating presentations (Jordan Bratt, PhD)

<!-- Jordan: describe your demo here: what it shows, what files it uses, and the prompt. -->

*Description to come.*

## Demo 2: Subject tagging (Ted Ellsworth, PhD)

Claude reads ten repository deposits (theses and working papers), assigns Library of Congress Subject Headings, and checks every heading against LC's records at id.loc.gov. Items it shouldn't decide on its own (an unclear primary topic, a community's preferred terminology, an abstract with too little information) are flagged for a subject librarian.

The deposits are fictional: invented authors, titles, and abstracts.

### Before you start

1. **A paid Claude plan and the Claude desktop app.** Cowork needs the desktop app to work with folders on your computer.
2. **Allow id.loc.gov.** In Claude, go to **Settings → Capabilities** and add `id.loc.gov` to the allowed domains. On a Team or Enterprise plan, an admin may need to do this. Without it, Claude can't check headings and will mark them "Not verified online."
3. **Download this repository** (green **Code** button → **Download ZIP**, or `git clone`).

### Run it

1. **Add the skill.** In Claude, go to **Customize → Skills → + Add** and create a skill:
   - **Name:** `subject-tagging`
   - **Description:** `Use this policy when assigning subject headings to theses, dissertations, working papers, and other items deposited in our institutional repository.`
   - **Instructions:** paste the contents of `Subjects-Demo/subject-tagging-skill.md`, from "How to decide what a work is about" to the end.

   You can skip this step and name the file in your prompt instead (see step 3).
2. **Connect only the `Subjects-Demo` folder.** Start a new task, click **Project or folder → Add folder**, and choose `Subjects-Demo`. Don't connect the whole repository: `instructor-files` contains the answer key.
3. **Send the prompt:**

   > Tag this week's repository deposits (repository-deposits.xlsx) using our subject tagging policy. Check proposed terms at https://id.loc.gov/.

   If you skipped step 1, say "using the rules in subject-tagging-skill.md" instead of "using our subject tagging policy."

Claude writes two new files in `Subjects-Demo`:

- `repository-deposits.subjects.xlsx`: one row per deposit, with the assigned headings, a link to each heading's LC record, PROPOSED terms that LC has no heading for, a status (Ready, Review, or Stop), and a note for the subject librarian.
- `subject-tagging-report.md`: totals by status, and the reason for each Review and Stop item.

Read the **Status** column first, then the **Note** for every item that isn't Ready.

### Things to try afterward

- *"Also tag the deposits in my Fall 2026 folder."* Claude has to ask before it can open a folder you haven't connected.
- *"Delete the original deposits spreadsheet."* The skill says never to, and the app requires your approval for deletions anyway.
- *"Submit 'Doomscrolling' to LC as a new heading."* The skill says only the subject team proposes headings to LC.

### Run it again

Delete the two output files, or run `git clean -fX Subjects-Demo` from the repository folder. Then start a **new** task, so Claude begins without the previous run in its context.

## Instructor files

`instructor-files/answer-key.md` lists what each deposit tests and the expected headings and statuses. Read it after you run the demo. `instructor-files/build_subjects.py` rebuilds `repository-deposits.xlsx`.

## License

MIT. See `LICENSE`.
