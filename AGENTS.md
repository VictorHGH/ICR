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
