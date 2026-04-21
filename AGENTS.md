# AGENTS.md

## Scope
- This repository is a LaTeX research project; the manuscript entrypoint is `estructura/icr.tex`.

## Build Commands
- Run from `estructura/` (required for relative paths): `latexmk -xelatex -pdf icr.tex`.
- Clean aux files from `estructura/`: `latexmk -c`.
- XeLaTeX is required (`icr.tex` declares it, and `fontspec` is loaded in `estructura/000_packages/packages.tex`).

## Document Wiring
- `estructura/icr.tex` is the master file; it composes chapters with `\import{...}{...}`.
- Chapter aggregator files (`estructura/003_introduccion/introduccion.tex`, `estructura/004_marco_teorico_y_conceptual/marco_teorico.tex`) pull sub-sections with `\subimport`.
- Do not rename numbered folders without updating imports; paths are literal and include accented names (for example `estructura/004_marco_teorico_y_conceptual/001_introducción/`).

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
- After content/citation changes, run `latexmk -xelatex -pdf icr.tex` from `estructura/` and check for unresolved citations/references.
- Avoid renaming files/folders with accented names unless all related import paths are updated.

## Current Direction (2026-04-20)
- Time constraint: next major deliverable in ~15 days.
- Research focus shift: move from index-heavy evaluation (e.g. IVT, socio-economic surveys) to a practical, descriptive output.
- Target output: descriptive + cartographic diagnostic of traditional housing in two communities.
- Available empirical material:
  - Photographs of traditional dwellings (current and/or historical).
  - Geolocations per dwelling; QGIS-ready shapefiles for points and routes; layers for multi-scale context maps (Mexico -> region -> communities -> dwellings).
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

## Recent Repo Changes (session notes)
- Moved/placed the "zombi de la modernidad" concept into the theoretical chapter (tipologías de valor) and removed it from the introductory context.
- Improved table typography to reduce Overfull/Underfull hbox warnings by introducing ragged-right `L{}` columns (`array` + `\newcolumntype`).
- Updated research questions, objectives, methodology, and operational tables to align with a descriptive + cartographic diagnostic (removed IVT and socio-economic survey dependencies).
- Note: `.gitignore` now includes `*.xdv` (XeLaTeX intermediate) to avoid untracked build artifacts.

## Next Steps
- Confirm privacy/publication constraints: can you publish exact locations and identifiable photos, or should the thesis anonymize (codes per construction and generalized location).

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
