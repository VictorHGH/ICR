# AGENTS.md

## Scope
- This repository is a LaTeX ICR project; ICR means `Idónea Comunicación de Resultados`, the institutional name for this final document. Do not call it `tesis` unless referring to external bibliography or other institutions' documents.
- The manuscript entrypoint is `estructura/icr.tex`.

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

## QGIS Project And MCP Setup
- Active portable QGIS project: `trabajos/03_cartografia/01_qgis_proyecto/mapa_general_icr.qgz`.
- The active QGIS project was saved with relative path storage; keep cartographic sources under `trabajos/03_cartografia/02_capas_fuente/` so the project can move between computers.
- Do not use `trabajos/mapas/mapaGeneral/Mapa general nuevo.qgz` as the active project; it was the older local project location before portability cleanup.
- Start QGIS first, load the active project, and then start/restart opencode so MCP tools can connect.
- Expected QGIS MCP socket when working: `127.0.0.1:9876`.
- `opencode.json` is configured with a local MCP server named `qgis` using `uvx --from git+https://github.com/nkarasiak/qgis-mcp.git qgis-mcp-server`.
- On a new computer, install `uv`/`uvx` first. A typical install is `curl -LsSf https://astral.sh/uv/install.sh | sh`, then ensure `uvx` is on `PATH`.
- If `uvx` is not found by opencode, run `which uvx` and either add that directory to `PATH` before launching opencode or change the first command entry in `opencode.json` from `uvx` to the absolute path reported by `which uvx`.
- The QGIS-side MCP plugin must also be installed and enabled in the active QGIS profile. In this machine it lives under `/home/victorhgh/.local/share/QGIS/QGIS4/profiles/default/python/plugins/qgis_mcp_plugin/`; on another computer use the equivalent QGIS profile plugin folder or install it from the `qgis-mcp` project instructions.
- If MCP fails, diagnose in this order: QGIS is open, the plugin is enabled, the plugin server is listening on `127.0.0.1:9876`, `uvx` works in the shell, then restart opencode.

## Current QGIS/Cartography State (updated 2026-06-03)
- Active project file: `trabajos/03_cartografia/01_qgis_proyecto/mapa_general_icr.qgz`.
- Current QGIS version used: `QGIS 4.0.2-Norrköping`.
- Current layouts in the active project:
  - `PL-01_Contexto_Mexico_Hidalgo`: Mexico context with Hidalgo highlighted in red; uses a dedicated duplicated layer named `Hidalgo` so its legend does not drift when other maps restyle the Hidalgo boundary layer.
  - `PL-02_Hidalgo_Cardonal`: Hidalgo/Cardonal context with Valle del Mezquital; native legend; municipality table split into two native attribute tables (`VM_NUM <= 14` and `VM_NUM >= 15`) with larger type.
  - `PL-03_Cardonal_Comunidades`: Cardonal community context with `El Deca / El Buena` polygons and perimeter labels.
  - `PL-04_Construcciones_Registradas`: local map of registered constructions and the four selected ICR cases; includes INEGI roads plus vector OSM roads as complementary access traces.
  - `PL-05_Relacion_Materiales_Territorio`: materials-territory map using vector vegetation (`Uso suelo / vegetación`), shaded relief, roads, community contours, and the four selected systems. The locator should visually reference the main map of `PL-04`.
- Layout maps are locked and store their own layer sets/styles. If a layer style is changed globally, re-store current layer styles in the affected layout map before saving.
- Save the QGIS project after every substantial layout edit because a prior QGIS crash lost memory-layer layout work.
- Persistent derived GeoPackage: `trabajos/03_cartografia/02_capas_fuente/contexto/regiones/icr_capas_derivadas.gpkg`.
- Persistent Mexico context layer: `trabajos/03_cartografia/02_capas_fuente/contexto/regiones/mexico_entidades_federativas.gpkg`.
- Persistent construction points layer: `trabajos/03_cartografia/02_capas_fuente/puntos_construcciones/construcciones_tradicionales.gpkg` with internal layer `Viviendas`.
- Persistent INEGI Hidalgo source layers: `trabajos/03_cartografia/02_capas_fuente/contexto/inegi_13_hidalgo/01_shp_originales/` and working package `02_gpkg_trabajo/inegi_13_hidalgo_contexto.gpkg`.
- Persistent Cardonal street layer: `trabajos/03_cartografia/02_capas_fuente/contexto/inegi_13_hidalgo/02_gpkg_trabajo/vialidades_cardonal_13e.gpkg`; derived from raw INEGI `13e` ejes de vialidad filtered to `CVE_MUN = 015`; used in `PL-03`.
- Persistent OSM roads layer: `trabajos/03_cartografia/02_capas_fuente/contexto/osm/caminos_osm_el_deca_el_buena.gpkg`, internal layer `Caminos OSM El Deca-El Buena`; downloaded from Overpass for the El Deca/El Buena area and used in `PL-04` as complementary road/access evidence.
- Persistent vegetation vector layer for `PL-05`: `trabajos/03_cartografia/02_capas_fuente/materiales/uso_suelo_vegetacion_cardonal/usv_serieV_f1411_vegetacion.gpkg`, internal layer `Uso suelo vegetacion Serie V`, shown in QGIS as `Uso suelo / vegetación` and categorized by `TIP_ECOV`.
- `PL-04` road layers: `Vialidades INEGI`, `Puentes INEGI`, `Carreteras INEGI`, `Terracerias INEGI`, `Veredas INEGI`, and `Caminos OSM`. The OSM layer is drawn below INEGI road layers so it reads as complementary rather than replacing official data.
- `PL-04` uses exact/internal construction points; public ICR export still needs location generalization or privacy approval before publication.
- Persistent topographic derivatives: `trabajos/03_cartografia/02_capas_fuente/contexto/topografia_hidalgo/mde_cem_15m/derivados/`.
- The original full Hidalgo MDE `13_Hidalgo_r15m_v4.tif` is intentionally not versioned because it is about 169 MB; use the committed Cardonal derivatives instead or reacquire the original from INEGI if a new derivative is needed.
- `trabajos/mapas/` is now treated as a local raw/source dump and is ignored by Git; do not make the active QGIS project depend on it.
- `trabajos/Fotos/` is ignored as a local raw photo dump. Case-level public selections live under `trabajos/02_fichas/*/fotografias_publicables/`.
- There is one leftover empty memory layer from the crash named `El Deca`; it is not needed by the layouts. Remove it only if the user approves cleanup.
- Current active layouts are `PL-01` through `PL-05`. Earlier planning mentioned a possible 7-map package; only 5 layouts are built now. The remaining two should be defined only if the final ICR needs them, likely as access/route context and operational synthesis/ficha cartografica.

## Current Cartographic Interpretation Notes (updated 2026-06-03)
- All 10 registered construction points fall inside the municipality of Cardonal according to the official municipal layer.
- `C-02`, `C-04`, and one additional gray registered point fall outside the official INEGI locality polygons for `El Deca`/`El Buena`, but the owners identify as belonging to `El Deca`; record this as a distinction between official geo-statistical perimeter and local community affiliation.
- In manuscript language, use `adscripción comunitaria` or `pertenencia comunitaria` for this local recognition, and distinguish it from `perímetro geoestadístico de localidad`.
- The manuscript now states that maps triangulate official cartography, collaborative OSM cartography, and local accounts rather than treating a boundary or road layer as exhaustive proof of community belonging.
- OSM vector roads are much closer to the `C-02`/`C-04` access traces than INEGI 13sil roads; approximate distances found: gray point `~4.3 m`, `C-04` `~17.1 m`, `C-02` `~22.8 m` from nearest OSM road.
- Keep this interpretive point in the diagnosis: INEGI locality limits and road layers are institutional representations; they do not fully capture territory lived through ownership, family relations, daily access, memory, and local recognition.

## Current Direction (updated 2026-05-19)
- Research focus is now an ICR-style, practical, descriptive output aligned with Guerrero Baca 2025 research-structure guidance and Guerrero Baca-oriented ICR patterns: concrete case, diagnostic core, fichas, cartography, criteria, and an operational product.
- The manuscript now makes the structure explicit: problemática, objeto de estudio, unidad de análisis, categorías, evidencia, procedimiento, producto and alcance.
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
  - No final field revisit is planned; work only with the existing photographs, geolocations, maps, and spoken accounts.
  - Do not present a website as the operational product for now; it was previously considered but needs a better plan and approval before reintroducing it.

## Current Structural Alignment
- Active alignment source from advisor: `bibliografia_pdf/(2025)_(Propuesta_de_estructura_de_investigacion)_(Guerrero_Baca).pdf`, cited in the manuscript as `guerrerobaca2025propuesta`.
- New introduction subsection: `estructura/003_introduccion/008_estructura_de_investigacion/estructura_de_investigacion.tex`.
- Active introduction aggregator: `estructura/003_introduccion/introduccion.tex`.
- Active objectives file imported by the manuscript: `estructura/003_introduccion/006_objetivos/objetivos.tex`.
- Note: `estructura/003_introduccion/006_objetivos/008.1_objetivo_general/` and `008.2_objetivos_especificos/` exist, but they are not imported by the current aggregator unless `objetivos.tex` is changed to subimport them. Keep `objetivos.tex` coherent first.
- Methodology now includes:
  - categorical, qualitative analysis fields instead of indices.
  - a step-by-step procedure from corpus matrix to fichas, cartography, comparative synthesis, and documentation criteria.
  - a matriz de congruencia linking questions, objectives, techniques, and products.

## Recent Repo Changes (session notes)
- Rebuilt and saved QGIS layouts `PL-01`, `PL-02`, and `PL-03` after a QGIS crash.
- Corrected `PL-01` so Hidalgo has its own red highlighted layer and matching legend entry.
- Adjusted `PL-02` so the Valle del Mezquital municipality table is split into two larger native QGIS attribute tables.
- Saved a portable QGIS project at `trabajos/03_cartografia/01_qgis_proyecto/mapa_general_icr.qgz` and moved project dependencies away from the local `trabajos/mapas/` dump where possible.
- Updated MCP guidance: opencode uses `uvx` to launch `qgis-mcp-server`; the QGIS plugin must be installed/enabled separately in QGIS.
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
- Added and imported `estructura/003_introduccion/008_estructura_de_investigacion/estructura_de_investigacion.tex` to make the advisor's research-structure logic explicit.
- Updated `estructura/005_metodologia/metodologia.tex` with categories of analysis, step-by-step procedure, and a congruence matrix.
- Cleaned `estructura/003_introduccion/007_justificacion/justificacion.tex` so it does not promise workshops, tourism outputs, restoration, or valuation methods beyond the current descriptive/cartographic scope.
- Updated `estructura/000_packages/packages.tex` with `\setlength{\headheight}{30pt}` to remove the `fancyhdr` headheight warning.
- Last successful manuscript build: `latexmk -pdfxe icr.tex` from `estructura/`; output was 47 pages. No critical errors, no undefined citations, and no undefined references. Remaining warnings are minor `Underfull \vbox` typography messages.
- Generated a separate 10-week planning table in `trabajos/00_control_y_programa/tabla_de_objetivos.tex`; regenerate its PDF from that folder with `latexmk -pdfxe tabla_de_objetivos.tex`.
- Removed duplicate untracked `trabajos/tabla_de_objetivos.tex`; keep only `trabajos/00_control_y_programa/tabla_de_objetivos.tex`.
- Completed local bibliography sidecar summaries in `bibliografia_pdf/`: 78 PDFs and 78 matching `.md` files. `bibliografia_pdf/` remains ignored by Git.
- Removed generated local bibliography concatenation files `bibliografia_pdf/junto.txt` and `bibliografia_pdf/todo_junto.txt`; individual `.md` summaries are the source of truth.
- Created an operational work folder tree under `trabajos/` for filling the remaining empirical material:
  - `01_corpus_y_datos/` for the master corpus matrix.
  - `02_fichas/` for one folder per construction (`C-01` to `C-04`).
  - `03_cartografia/` for QGIS project files, source layers, and exported maps.
  - `04_fotografias/` for originals, public selections, internal images, and existing before/after pairs.
  - `05_relatos/` for audios, transcriptions, and case summaries.
  - `06_tablas_y_sintesis/` for comparative tables and pending matrices.
  - `07_figuras_para_icr/` for final ICR-ready figures only.
  - `08_pendientes_y_revision/` for active checklists.
- Latest pushed commits on `main`:
  - `297ada9` `[Updated] map selected ICR cases`
  - `110fa33` `[Updated] refine PL-03 community map`
  - `408775a` `[Updated] save QGIS portable project`
  - `77b1b27` `[Updated] add portable QGIS workspace`
- Current status after those commits: manuscript is aligned to a non-web, descriptive + cartographic diagnostic and to the advisor-provided Guerrero Baca 2025 structure. `PL-04` and `PL-05` are now built; decide whether the two remaining possible maps are needed before creating more layouts.

## Latest Session Changes (2026-06-03)
- Replaced Helvetica/Sans Serif/Arial references in QGIS labels/layout items with `Liberation Sans`; local font availability confirmed with `fc-match 'Liberation Sans'`.
- Created `PL-04_Construcciones_Registradas` from `PL-03`, then user-adjusted visual details; final map shows all registered constructions and highlights `C-01` to `C-04`.
- Corrected `PL-04` locator to show the previous `PL-03` community context instead of an incorrect CRS-shifted view.
- Added INEGI `13sil` road/service-line variants as separate layers for visual comparison: `Puentes INEGI`, `Carreteras INEGI`, `Terracerias INEGI`, `Veredas INEGI`; the empty `INEGI 13sil - brechas/peatonales` layer remains loaded but is not useful.
- Downloaded OSM vector roads from Overpass and saved them under `trabajos/03_cartografia/02_capas_fuente/contexto/osm/`; `Caminos OSM` is now used in `PL-04` as a complementary access layer below INEGI roads.
- Updated `estructura/006_caso_de_estudio_y_corpus/caso_de_estudio_y_corpus.tex` and `estructura/007_diagnostico_descriptivo_y_cartografico/diagnostico_descriptivo_y_cartografico.tex` to explain the difference between official locality perimeters and local community affiliation.
- Created and refined `PL-05_Relacion_Materiales_Territorio`. Main map uses communities as visible contours over vegetation so the material-territory reading remains clear; the locator uses the `PL-04` main-map layer set/styles as prior-reference context.
- Removed the temporary `Comunidad El Deca (ref)` and `Comunidad El Buena (ref)` memory layers from `PL-05`; the layout now depends only on persistent layers. The old unused memory layer `El Deca` remains loaded and should only be removed with user approval.
- Completed `trabajos/01_corpus_y_datos/matriz_corpus_C01_C04.md` with community, system, use, materials, qualitative physical state, visible/related changes, spoken-account synthesis, public-photo folder, and generalized location by community for `C-01` to `C-04`.
- Filled the base case fichas in `trabajos/02_fichas/*/README.md` from the corpus matrix. Each ficha now includes identification, materials, physical state, changes, relato, photo folders, cartography, brief interpretation, and remaining ampliation-only notes.
- Decided not to use a single coded physical-state field because it would flatten the material, morphological, social, and narrative depth of each traditional construction. Use qualitative descriptions instead.
- For `C-02`, use `piedra local / tepetate`: respect the community term `tepetate`, but avoid claiming a petrographic classification because no petrographic analysis will be done.
- Public ICR location handling for the four cases is generalized by community; exact coordinates remain internal in QGIS only.
- Latest pushed commits include `9e8fd5a [Updated] add PL-05 materials map` and `137f1dc [Updated] complete corpus matrix`.

## Next Steps
- First action in the next session: create/fill `trabajos/06_tablas_y_sintesis/cuadro_comparativo_sistemas.md` from the completed matrix and fichas. Compare systems, materials, use, physical state, changes, relato themes, territorial relation, and conservation implications.
- Step 1: Complete `trabajos/06_tablas_y_sintesis/cuadro_comparativo_sistemas.md`.
- Step 2: Complete or revise `trabajos/06_tablas_y_sintesis/matriz_pendientes_por_caso.md`; most base data is complete, so remaining notes should focus on optional ficha ampliation, public-image selection, and manuscript insertion.
- Step 3: Expand `estructura/007_diagnostico_descriptivo_y_cartografico/diagnostico_descriptivo_y_cartografico.tex` using the matrix, fichas, and maps `PL-04`/`PL-05`.
- Step 4: Refine `estructura/008_producto_operativo/producto_operativo.tex` as a non-web operational product: ficha fields, map package, comparative synthesis, privacy levels, and documentation criteria.
- Step 5: Decide whether maps `PL-06` and `PL-07` are actually needed. Do not create them automatically; likely options are access/route context and operational synthesis/ficha cartografica.
- Step 6: Keep checking coherence across questions, objectives, methodology, diagnostic chapter, product chapter, and conclusions after each content update.

## Immediate User Prompt For Next Session
- Start by saying: "La matriz y las fichas base ya están completas. El siguiente paso es hacer el cuadro comparativo de sistemas en `trabajos/06_tablas_y_sintesis/cuadro_comparativo_sistemas.md` y luego pasar ese contenido al capítulo de diagnóstico."
- If the user wants to continue writing, work from the completed fichas and matrix; do not ask again for data already captured unless a contradiction appears.
- Do not expose exact coordinates, owners, or sensitive identifying information in the manuscript.

## Confirmed Inputs (2026-04-21)
- The field record includes several traditional constructions, but the ICR will analyze 4 selected cases/systems because they are the most original examples found in morphology and traditional materials. Do not write as if only four constructions were registered in total.
- Case count for the diagnostic corpus: 4 selected traditional construction cases (photos + location + at least one spoken account).
- Unit of analysis wording: prefer \emph{construcciones} (not \emph{viviendas}), since what remains standing are mainly kitchens or storage buildings.
- Provisional construction systems to classify (goal: 4 systems across 2 communities):
  - Penca de maguey: muros con entramado de quiote de lechuguilla y recubrimiento de pencas de maguey.
  - Piedra "tepetate" (nombre local): muros a hueso con ese tipo de piedra (pendiente confirmar material exacto).
  - Bajareque: entramado de lechuguilla, relleno con "castillo" y recubrimiento con tierra.
  - Órganos: cerramientos/muros con cactus "órgano" formando un entorno cerrado pero vivo.
- Common observed condition: floors are usually compacted earth; roofs are often replaced with corrugated sheets (various materials).
- Privacy/publication: for internal presentations you will use exact locations; for the published ICR/output you will generalize locations and anonymize constructions as needed.

## Current Corpus Placeholders
- `C-01`: penca de maguey; corresponds to `Viviendas` `fid=10`, `id=11`; community El Buena; used as pulque-related bodega; key themes are maintenance of pencas, lunar cutting knowledge, decline of pulque consumption, and material adequacy through floor/roof changes.
- `C-02`: piedra local / tepetate; corresponds to `Viviendas` `fid=3`, `id=4`; community El Deca by local affiliation; use as bodega/corral context after former habitation; keep `tepetate` as community term and avoid petrographic certainty.
- `C-03`: bajareque; corresponds to `Viviendas` `fid=5`, `id=6`; community El Buena; kitchen with fogon; highest morphological permanence; key themes are taste, affective attachment, risk of demolition after user dies, and `castillo` as locally available infill.
- `C-04`: órganos; corresponds to `Viviendas` `fid=2`, `id=3`; community El Deca by local affiliation; kitchen/storage space; treat as living or semi-living enclosure, not a conventional building; key themes are transplant timing after full moon, size selection, local abundance, and partial replacement after organ death.
- The `Viviendas` GeoPackage now has helper fields `caso_icr`, `sistema_icr`, and `seleccion_icr` for these four selected cases. Use `seleccion_icr = 1` to symbolize the diagnostic corpus; other points are registered constructions but not the four selected systems.

## Data To Request First
- Do not request the base corpus fields again; they are already captured in the matrix and fichas.
- If more detail is needed, ask only targeted optional questions: floor description, whether there are before/after photos, or which photo from each `fotografias_publicables/` folder should be used in the manuscript.
- Continue using cautious naming for `piedra local / tepetate`; use `bajareque` consistently for `C-03`.

## Writing Guidance For Next Sessions
- Use `construcciones tradicionales` as the default unit; avoid reverting to `viviendas` unless discussing prior literature.
- Use `ICR` or `Idónea Comunicación de Resultados` for this project document; avoid calling it `tesis` in manuscript/workflow text.
- Keep the tone human and direct, not like a generic methods manual.
- Avoid adding mini-summaries called `Conclusión de la sección` inside every subsection.
- Do not reintroduce IVT, socioeconomic surveys, measured architectural drawings, or synthetic indices unless the user explicitly changes the scope.
- The practical contribution is documentation and organization: fichas, maps, typology, basic preventive criteria, and a clear structure for continuing the record later.
- Do not reintroduce a website/catalog-web product unless the user explicitly asks for it after developing a stronger plan.
- Protect privacy in public outputs: no exact coordinates, no identifiable owners, and no sensitive photographs without explicit authorization.
