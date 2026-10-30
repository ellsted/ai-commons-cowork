"""Regenerate the subject tagging demo inputs (all items fictional).
Usage: python3 build_subjects.py <output folder>"""
import sys, os, csv
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

out = sys.argv[1]

DEPOSITS = [
("DEP-2026-001", "Thermal stress and coral bleaching on Caribbean reefs, 2005-2023",
 "Alvarez, Marisol", "Ecology & Evolutionary Biology", "Dissertation",
 "This dissertation examines how repeated marine heatwaves have affected reef-building corals across twelve Caribbean monitoring sites between 2005 and 2023. Combining satellite sea-surface temperature records with annual diver surveys, I estimate the thermal thresholds at which bleaching begins and identify which coral species recover. Bleaching events became more frequent and more severe over the study period, and reefs with higher herbivorous fish populations recovered faster. I conclude with recommendations for prioritizing reef protection in a warming ocean.",
 "coral reefs; marine heatwaves; climate change; Caribbean"),
("DEP-2026-002", "Alone on the back roads: loneliness among elderly residents of rural Vermont",
 "Okonkwo, Daniel", "School of Public Health", "Master's thesis",
 "Social isolation is a growing public health concern for the elderly, particularly in rural areas with limited transportation and services. Drawing on interviews with 38 residents aged 70 and over in three Vermont counties, this thesis describes how loneliness is experienced and managed. Participants relied heavily on churches, general stores, and informal phone networks. Loss of a driver's license was the single strongest predictor of reported loneliness. I discuss implications for rural aging services and volunteer transportation programs.",
 "elderly; loneliness; rural health; Vermont"),
("DEP-2026-003", "Large language models as writing partners in first-year composition",
 "Hartley, Simone", "English", "Dissertation",
 "Since 2023, students have increasingly used large language models such as chatbots to brainstorm, draft, and revise academic essays. This study follows four sections of a first-year composition course in which students were explicitly permitted to use these tools and asked to document their use. Through analysis of drafts, reflective memos, and instructor feedback, I identify three patterns of use: idea generation, sentence-level revision, and wholesale drafting. Students who used the tools mainly for revision showed the greatest gains in argument quality.",
 "LLMs; ChatGPT; generative AI; composition pedagogy; academic writing"),
("DEP-2026-004", "Dating Carolingian manuscripts with machine learning",
 "Lindqvist, Johan", "History / Computer Science (joint)", "Dissertation",
 "Many early medieval Latin manuscripts can only be dated approximately, based on expert judgment of their script. This dissertation trains a convolutional neural network on 4,200 digitized pages of Carolingian minuscule with secure dates, then applies it to 310 undated manuscripts. The model dates pages to within 25 years in 81% of test cases and highlights letter forms that drive its predictions. The final chapters compare model predictions with paleographers' estimates and discuss what each approach can and cannot tell us about scribal training.",
 "paleography; Carolingian minuscule; neural networks; digital humanities; medieval manuscripts"),
("DEP-2026-005", "Learning by ear: gamelan pedagogy in Central Java",
 "Prasetyo, Wulan", "Music", "Dissertation",
 "Gamelan ensembles in Central Java have traditionally been taught orally, by imitation and repetition rather than notation. Based on eighteen months of fieldwork in Surakarta and Yogyakarta, this dissertation documents how teachers in village ensembles, conservatories, and university programs transmit repertoire today. I show that notation is increasingly used as a memory aid but rarely replaces listening, and that younger teachers blend traditional and conservatory methods. I argue that these hybrid approaches are sustaining, not eroding, the tradition.",
 "Java; gamelan; music education; oral tradition; ethnomusicology"),
("DEP-2026-006", "Muros que recuerdan: memoria colectiva y murales comunitarios en Valparaíso",
 "Fuentes, Catalina", "Spanish & Portuguese", "Dissertation",
 "Esta tesis analiza cómo los murales comunitarios de los cerros de Valparaíso, Chile, funcionan como espacios de memoria colectiva tras el estallido social de 2019. A partir de entrevistas con muralistas y vecinos, y del registro fotográfico de 140 murales, se estudia cómo las comunidades negocian qué historias se pintan, quién las pinta y cómo se protegen frente al borrado municipal. Se propone que el muralismo barrial constituye un archivo vivo y disputado de la historia reciente del país.",
 "muralismo; memoria colectiva; arte urbano; Valparaíso; Chile"),
("DEP-2026-007", "Speaking with the land: Kanien'kéha revitalization and land-based learning at Akwesasne",
 "Thompson, Rebecca", "Linguistics", "Master's thesis",
 "This thesis documents a community-led immersion program in which Kanien'kehá:ka (Mohawk) youth learn Kanien'kéha through seasonal, land-based activities such as planting, fishing, and medicine gathering. Working with program elders and teachers, I recorded lesson sessions over two years and analyzed how vocabulary for plants, places, and kinship is taught in context. Learners retained land-related vocabulary far better than words taught in the classroom. The thesis was prepared in consultation with the community, which asks that its own names for the people and language be used.",
 "Kanien'kéha; Kanien'kehá:ka; language revitalization; land-based education; Akwesasne"),
("DEP-2026-008", "Shade and justice: tree canopy, heat, and neighborhood inequality in New Haven",
 "Reyes, Marcus", "School of the Environment", "Master's project",
 "Summer surface temperatures in New Haven, Connecticut vary by more than 10°F between neighborhoods. Using satellite thermal imagery, city tree inventories, and census data, this project maps the relationship between tree canopy cover, surface heat, and household income. The hottest, least-shaded neighborhoods are disproportionately low-income and have the lowest rates of street-tree planting. I propose a planting prioritization index for the city's urban forestry program and discuss its fit with existing environmental justice commitments.",
 "urban heat; tree canopy; environmental justice; New Haven"),
("DEP-2026-009", "Working paper no. 3",
 "Ibrahim, Yusuf", "Economics", "Working paper",
 "This paper extends the framework developed in the author's previous working papers. Additional robustness checks are reported and an alternative specification is discussed. Results are broadly consistent with earlier findings.",
 "robustness; specification"),
("DEP-2026-010", "Doomscrolling and sleep quality among graduate students",
 "Mehta, Priya", "Psychology", "Master's thesis",
 "Doomscrolling, the habit of compulsively scrolling through negative news and social media content, has become a common late-night behavior. This thesis surveys 412 graduate students about their phone use in the hour before bed and their sleep quality over two weeks. Students who reported nightly doomscrolling slept an average of 47 minutes less and reported higher anxiety the following day. A brief intervention that moved phones out of the bedroom improved sleep for most participants. Implications for graduate student wellness programs are discussed.",
 "doomscrolling; sleep; social media; graduate students; anxiety"),
]

VOCAB = [
# heading, type, note
("Coral reef ecology", "Topical", ""),
("Coral bleaching", "Topical", ""),
("Coral reef conservation", "Topical", ""),
("Ocean temperature", "Topical", ""),
("Older people", "Topical", "Use for: Elderly, Aged, Seniors"),
("Rural older people", "Topical", ""),
("Loneliness", "Topical", ""),
("Loneliness in old age", "Topical", ""),
("Older people--Services for", "Topical", ""),
("Artificial intelligence--Educational applications", "Topical", ""),
("English language--Rhetoric--Study and teaching (Higher)", "Topical", ""),
("Academic writing", "Topical", ""),
("Paleography, Latin", "Topical", ""),
("Manuscripts, Latin (Medieval and modern)", "Topical", ""),
("Manuscripts, Medieval", "Topical", ""),
("Machine learning", "Topical", ""),
("Neural networks (Computer science)", "Topical", ""),
("Digital humanities", "Topical", ""),
("Gamelan", "Topical", ""),
("Gamelan--Instruction and study", "Topical", ""),
("Music--Instruction and study", "Topical", ""),
("Java (Computer program language)", "Topical", "The programming language. For the island, see Java (Indonesia)"),
("Street art", "Topical", ""),
("Mural painting and decoration", "Topical", ""),
("Collective memory", "Topical", ""),
("Mohawk Indians", "Topical", ""),
("Mohawk Indians--Education", "Topical", ""),
("Mohawk language", "Topical", ""),
("Language revival", "Topical", ""),
("Place-based education", "Topical", ""),
("Urban heat island", "Topical", ""),
("Urban forestry", "Topical", ""),
("Trees in cities", "Topical", ""),
("Environmental justice", "Topical", ""),
("Sleep", "Topical", ""),
("Sleep deprivation", "Topical", ""),
("Graduate students", "Topical", ""),
("Social media--Psychological aspects", "Topical", ""),
("Internet--Psychological aspects", "Topical", ""),
("Public libraries", "Topical", ""),
("Caribbean Area", "Geographic", ""),
("Vermont", "Geographic", ""),
("Java (Indonesia)", "Geographic", "The island. For the programming language, see Java (Computer program language)"),
("Valparaíso (Chile)", "Geographic", ""),
("Chile", "Geographic", ""),
("New Haven (Conn.)", "Geographic", ""),
("Connecticut", "Geographic", ""),
("New York (State)", "Geographic", ""),
]

os.makedirs(out, exist_ok=True)
wb = Workbook(); ws = wb.active; ws.title = "Deposits"
hdr = ["Deposit ID", "Title", "Author", "Department", "Item type", "Abstract", "Author keywords"]
ws.append(hdr)
for r in DEPOSITS: ws.append(list(r))
widths = [15, 45, 20, 26, 16, 90, 40]
for i, w in enumerate(widths): ws.column_dimensions[chr(65 + i)].width = w
for c in ws[1]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="00356B")
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
ws.freeze_panes = "B2"
wb.save(os.path.join(out, "repository-deposits.xlsx"))

with open(os.path.join(out, "subject-vocabulary.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["Heading", "Type", "Note"])
    for v in VOCAB: w.writerow(v)
print(len(DEPOSITS), "deposits;", len(VOCAB), "vocabulary headings")
