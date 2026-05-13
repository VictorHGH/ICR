# AGENTS.md

## Scope
- This repository is a LaTeX research project; the manuscript entrypoint is `estructura/icr.tex`.

## Build Commands
- Run from `estructura/` (required for relative paths): `latexmk -pdfxe icr.tex`.
- Clean aux files from `estructura/`: `latexmk -c`.
- XeLaTeX is required (`icr.tex` declares it, and `fontspec` is loaded in `estructura/000_packages/packages.tex`).
- Avoid `latexmk -xelatex -pdf icr.tex`; in this project it can try the wrong PDF flow. The confirmed working command is `latexmk -pdfxe icr.tex`.

## Document Wiring
- `estructura/icr.tex` is the master file; it composes chapters with `\import{...}{...}`.
- Chapter aggregator files (`estructura/003_introduccion/introduccion.tex`, `estructura/004_marco_teorico_y_conceptual/marco_teorico.tex`) pull sub-sections with `\subimport`.
- Do not rename numbered folders without updating imports; paths are literal and include accented names (for example `estructura/004_marco_teorico_y_conceptual/001_introducción/`).
- Current imported chapter sequence in `estructura/icr.tex` includes:
  - `001_portada`
  - `002_titulo`
  - `003_introduccion`
  - `004_marco_teorico_y_conceptual`
  - `005_metodologia`
  - `006_caso_de_estudio_y_corpus`
  - `007_diagnostico_descriptivo_y_cartografico`
  - `008_producto_operativo`
  - `009_conclusiones`

## Bibliography
- Active bibliography source: `estructura/bibliografia/referencias.bib` via `\bibliography{./bibliografia/referencias}`.
- Citation stack is `natbib` + `agsm` (`estructura/000_packages/packages.tex`); keep citation commands compatible.
- `estructura/bibliografia/referencias2.bib` exists but is not used by the current master file.
- Add new references in `estructura/bibliografia/referencias.bib` only.

## Inclusion Gotchas
- `estructura/007_mapa_de_actores/mapa_de_actores.tex` and `estructura/008_limites_y_alcances/limites_y_alcances.tex` are present but not imported in `estructura/icr.tex`.
- If you edit those files, also add their `\import` lines in `estructura/icr.tex` or they will not appear in the PDF.
- If you create a new subsection file, wire it in the chapter aggregator with `\subimport` or it will not be rendered.

## Repo Hygiene
- `.gitignore` excludes LaTeX build artifacts and PDFs (`*.aux`, `*.bbl`, `*.fdb_latexmk`, `*.pdf`, etc.); avoid committing generated outputs.
- `bibliografia_pdf/` is reference material and is ignored.
- Never edit `estructura/icr.bbl` manually (generated file).

## Editing Workflow
- For normal content updates, edit only `.tex` files and `estructura/bibliografia/referencias.bib`.
- After content/citation changes, run `latexmk -pdfxe icr.tex` from `estructura/` and check for unresolved citations/references.
- Avoid renaming files/folders with accented names unless all related import paths are updated.

## Current Direction (updated 2026-05-08)
- Research focus is now an ICR-style, practical, descriptive output aligned with Guerrero Baca-oriented theses/ICR patterns: concrete case, diagnostic core, fichas, cartography, criteria, and an operational product.
- Research focus shift: move from index-heavy evaluation (e.g. IVT, socio-economic surveys) to a practical, descriptive output.
- Target output: descriptive + cartographic diagnostic of four traditional constructions in two communities, plus fichas, maps, comparative synthesis, and basic documentation/conservation criteria.
- Available empirical material:
  - Photographs of four traditional constructions (current and/or historical).
  - Geolocations per construction; QGIS-ready shapefiles for points and routes; layers for multi-scale context maps (Mexico -> region -> communities -> constructions).
  - Audio/spoken accounts from inhabitants about lived experience and changes.
  - Literature summaries: `bibliografia_pdf/` contains PDFs and per-PDF `.md` summaries (folder is git-ignored).
- Current constraints:
  - No architectural measured drawings/levantamientos.
  - No socio-economic surveys.
  - Prefer to avoid constructing synthetic indices (e.g. IVT) in results.
- Near-term storyline:
  - Demonstrate richness of local knowledge by identifying multiple construction systems (goal: 4 systems across 2 communities).
  - Argue that each system responds to material availability/proximity.
  - If safe/feasible: one final field revisit to capture changes since ~3 years and enable before/after comparison.
  - Do not present a website as the operational product for now; it was previously considered but needs a better plan and approval before reintroducing it.

## Recent Repo Changes (session notes)
- Moved/placed the "zombi de la modernidad" concept into the theoretical chapter (tipologías de valor) and removed it from the introductory context.
- Improved table typography to reduce Overfull/Underfull hbox warnings by introducing ragged-right `L{}` columns (`array` + `\newcolumntype`).
- Updated research questions, objectives, methodology, and operational tables to align with a descriptive + cartographic diagnostic (removed IVT and socio-economic survey dependencies).
- Note: `.gitignore` now includes `*.xdv` (XeLaTeX intermediate) to avoid untracked build artifacts.
- Reviewed local `bibliografia_pdf/` summaries and consolidated bibliography keys in `estructura/bibliografia/referencias.bib`.
- Integrated additional sources into the theoretical chapter, including Rapoport, Torres Zárate, Martín Galindo, Lárraga, Rodríguez-Ruiz/Gándara, Thompson, and relevant heritage-law entries.
- Removed repetitive internal mini-conclusions from theoretical subsections; keep only the chapter-level conclusion in `004_marco_teorico_y_conceptual/007_conclusion_marco/conclusion_marco.tex`.
- Added new manuscript chapters and imported them in `estructura/icr.tex`:
  - `estructura/006_caso_de_estudio_y_corpus/caso_de_estudio_y_corpus.tex`
  - `estructura/007_diagnostico_descriptivo_y_cartografico/diagnostico_descriptivo_y_cartografico.tex`
  - `estructura/008_producto_operativo/producto_operativo.tex`
  - `estructura/009_conclusiones/conclusiones.tex`
- Reoriented the objective, questions, methodology, and conclusions toward four documented constructions, fichas, cartography, spoken accounts, and operational documentation criteria.
- Updated `estructura/000_packages/packages.tex` with `\setlength{\headheight}{30pt}` to remove the `fancyhdr` headheight warning.
- Last successful build: `latexmk -pdfxe icr.tex` from `estructura/`; output was 42 pages. No critical errors, no undefined citations, and no undefined references. Remaining warnings are minor `Underfull` typography messages and two BibTeX `empty publisher` warnings for older entries.
- Latest pushed commits on `main`:
  - `d962daf` `[Updated] streamline marco teorico closures`
  - `2c9e2ee` `[Updated] restructure manuscript for web catalog`
  - `385bc6b` `[Updated] fix fancyhdr headheight warning`
  - `592e373` `[Updated] persist session guidance notes`
- Current correction after those commits: remove the website/catalog-web framing from the manuscript. Keep the product as fichas, maps, comparative synthesis, and criteria until the website plan is better developed and approved.

## Next Steps
- First action in the next session: ask the user for the missing field data before expanding the diagnosis. Do not invent or fill empirical ficha content without user-provided data.
- Fill the empirical diagnosis for `C-01` to `C-04` with real field data: community, use, materials, state, observed changes, associated spoken account, photographs, and generalized location.
- Select which photographs can be published and which must remain internal.
- Prepare maps for the diagnostic chapter: regional context, communities, generalized construction locations, routes, and relation to local materials.
- Expand `007_diagnostico_descriptivo_y_cartografico/diagnostico_descriptivo_y_cartografico.tex` from placeholders into actual fichas for `C-01`, `C-02`, `C-03`, and `C-04`.
- Refine `008_producto_operativo/producto_operativo.tex` as a non-web operational product: ficha fields, map package, comparative synthesis, privacy levels, and documentation criteria.
- Keep checking coherence across questions, objectives, methodology, diagnostic chapter, product chapter, and conclusions after each content update.

## Confirmed Inputs (2026-04-21)
- Case count: 4 traditional constructions documented (photos + location + at least one spoken account).
- Unit of analysis wording: prefer \emph{construcciones} (not \emph{viviendas}), since what remains standing are mainly kitchens or storage buildings.
- Provisional construction systems to classify (goal: 4 systems across 2 communities):
  - Penca de maguey: muros con entramado de quiote de lechuguilla y recubrimiento de pencas de maguey.
  - Piedra "tepetate" (nombre local): muros a hueso con ese tipo de piedra (pendiente confirmar material exacto).
  - Bajareque (tipo "pajareque"): entramado de lechuguilla, relleno con "castillo" y recubrimiento con tierra.
  - Órganos: cerramientos/muros con cactus "órgano" formando un entorno cerrado pero vivo.
- Common observed condition: floors are usually compacted earth; roofs are often replaced with corrugated sheets (various materials).
- Privacy/publication: for internal presentations you will use exact locations; for the published thesis/output you will generalize locations and anonymize constructions as needed.

## Current Corpus Placeholders
- `C-01`: penca de maguey; needs final community, photos, location handling, state, use, and spoken account summary.
- `C-02`: piedra local or "tepetate"; keep the wording cautious because material characterization is pending.
- `C-03`: bajareque or "pajareque"; document entramado, relleno, recubrimiento, maintenance/loss, and related narratives.
- `C-04`: órganos; treat as living or semi-living enclosure/cerramiento, not necessarily a conventional building.

## Data To Request First
- For each construction `C-01` to `C-04`, ask for: community, current or remembered use, observed materials, physical state, visible changes, associated spoken account summary, photograph selection/publication permission, and location handling (exact internal vs generalized public).
- Ask whether there are before/after photographs for any case, especially if a final field revisit is possible.
- Ask which maps already exist as QGIS outputs and which still need to be exported for the thesis.
- Confirm cautious naming for `tepetate` and `pajareque/bajareque` before writing final diagnostic language.

## Writing Guidance For Next Sessions
- Use `construcciones tradicionales` as the default unit; avoid reverting to `viviendas` unless discussing prior literature.
- Keep the tone human and direct, not like a generic methods manual.
- Avoid adding mini-summaries called `Conclusión de la sección` inside every subsection.
- Do not reintroduce IVT, socioeconomic surveys, measured architectural drawings, or synthetic indices unless the user explicitly changes the scope.
- The practical contribution is documentation and organization: fichas, maps, typology, basic preventive criteria, and a clear structure for continuing the record later.
- Do not reintroduce a website/catalog-web product unless the user explicitly asks for it after developing a stronger plan.
- Protect privacy in public outputs: no exact coordinates, no identifiable owners, and no sensitive photographs without explicit authorization.
