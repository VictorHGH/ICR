# ICR - Documento de investigacion (LaTeX)

Repositorio academico para desarrollo del documento ICR, incluyendo estructura modular en LaTeX, bibliografia y recursos de apoyo.

## Contenido del repositorio

- `estructura/`: proyecto principal LaTeX.
- `estructura/icr.tex`: archivo maestro del documento.
- `estructura/bibliografia/`: archivos `.bib`.
- `estructura/imagenes/`: recursos graficos.
- `propuesta.md`: guia de redaccion para introduccion.
- `bibliografia_pdf/`: material de referencia en PDF.

## Requisitos

- TeX Live / MacTeX (con `xelatex` y `latexmk`)
- Herramienta BibTeX/Biber segun flujo de compilacion

## Compilar documento principal

Desde `estructura/`:

```bash
latexmk -xelatex -pdf icr.tex
```

Para limpiar archivos temporales:

```bash
latexmk -c
```

## Flujo recomendado

1. Editar secciones en carpetas modulares (`003_introduccion`, `004_marco_teorico_y_conceptual`, etc.).
2. Mantener referencias en `estructura/bibliografia/referencias.bib`.
3. Compilar con `latexmk` para resolver citas y tabla de contenido.

## Notas

- El archivo maestro declara `xelatex` como motor principal.
- Mantener nombres de rutas consistentes con `\import{...}{...}`.
