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

## Demo 1: Workshop Slides (Jordan Bratt, PhD)

Claude builds a slide deck for a 50-minute informational workshop that introduces undergraduates without coding experience to reproducible research. Claude works from a written brief, openly licensed source material, and a branded template. It writes an outline and waits for approval before building any slides, follows the rules in `presentation-guidelines.md`, credits every source as its license requires, and flags any claim the sources don't support instead of inventing a citation.

The source materials are excerpts and illustrations from *The Turing Way* (The Turing Way Community; illustrations by Scriberia; CC BY 4.0) and open-access articles, each with its license and attribution at the top of the file. 

### Before you start

1. **A paid Claude plan and the Claude desktop app.** Cowork needs the desktop app to work with folders on your computer.
2. **Download this repository** (green **Code** button → **Download ZIP**, or `git clone`).

No skill and no network settings are needed. Everything Claude uses is in the folder, and the guidelines are named in the prompt.

### What's in the folder

```
Presentations-Demo/
  brief.md                      This presentation: audience, outcomes, structure, deliverables
  presentation-guidelines.md    Rules for every deck: accessibility, sources, attribution, files, process
  library-template.pptx         Branded template: colors, fonts, logo, layouts
  sources/
    turing-way-*.md             Excerpts from The Turing Way, with attribution and slide credit
    Intro-to-FAIR.pdf           Slides for a workshop on FAIR Principles
    articles/                   Open-access articles, with attribution and slide credit
    images/
      images.md                 What each image shows, where it belongs, and its credit line
      *.png                     Scriberia illustrations from The Turing Way

```

### Run it

1. **Connect only the `Presentations-Demo` folder.** Start a new task, click **Project or folder → Add folder**, and choose `Presentations-Demo`. Don't connect the whole repository: `instructor-files` contains a sample of the finished deck.
2. **Send the prompt:**

   > Using brief.md and the materials in sources/, create a slide deck for an undergraduate reproducible research workshop. Follow the rules in presentation-guidelines.md and use library-template.pptx. First write outline.md and stop so I can review it. After I approve, build reproducible-research-workshop.pptx with speaker notes, and a one-page facilitator-handout.md.

3. **Review the outline.** Claude stops after writing `outline.md`. Check that each slide names its source file and that any `[NEEDS SOURCE]` flags are listed. Ask for one change, such as "Introduce the opening scenario earlier," then approve.
4. **Iterate on one slide.** After the deck is built, send one follow-up, such as "Slide 7 is too dense; split it into two."

Claude writes three new files in `Presentations-Demo/outputs`:

- `outline.md`: one line per slide, with its title, key point, and source file.
- `reproducible-research-workshop.pptx`: the deck, with speaker notes, alt text, credit lines, and a sources slide in APA style.
- `facilitator-handout.md`: one page for whoever teaches the session, with goals, timing, the "Could Someone Else Do This?" activity and its answers, and likely student questions.

At the end of the run, Claude lists every `[NEEDS SOURCE]` flag, any conflict between the brief and the guidelines, and anything it couldn't do. Read that list first. Then open the deck and spot-check one slide: Is the image right for the topic? Is the alt text accurate? Is the credit line there?

### Things to try afterward

- *"Also use the slides in my Desktop folder."* Claude has to ask before it can open a folder you haven't connected.
- *"Add a slide with the latest statistics on the reproducibility crisis."* Nothing in `sources/` supports it, so Claude should mark it `[NEEDS SOURCE]` rather than invent a citation.
- *"Overwrite past-workshop-deck.pptx with the new version."* The guidelines say never to overwrite existing files.

### Run it again

Delete the three output files. Then start a **new** task, so Claude begins without the previous run in its context.

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
