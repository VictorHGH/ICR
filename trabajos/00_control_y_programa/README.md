# Control y programa

Usar esta carpeta para guardar cronogramas, versiones de la tabla de 10 semanas y documentos de seguimiento.

Archivo en esta carpeta:

- `tabla_de_objetivos.tex`: fuente de la tabla de 10 semanas.
- `tabla_de_objetivos.pdf`: PDF generado localmente; no se versiona porque los PDFs están ignorados.

Para regenerar el PDF:

```bash
latexmk -pdfxe tabla_de_objetivos.tex
```
