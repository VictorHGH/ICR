# INEGI Hidalgo 2019

Capas de contexto tomadas del Marco Geoestadistico INEGI, septiembre 2019, solo para el estado de Hidalgo (`13`).

## Organizacion

- `00_documentacion/`: documentos y catalogos basicos copiados desde la descarga original.
- `01_shp_originales/`: copia limpia de las capas `shp` utiles para la ICR; no incluye archivos `._*`.
- `02_gpkg_trabajo/inegi_13_hidalgo_contexto.gpkg`: GeoPackage de trabajo con las mismas capas seleccionadas.

## CRS

- Las capas INEGI usan Mexico ITRF2008 / LCC.
- En QGIS se identifican como `EPSG:6372`.
- No usar `Definir CRS de capa` para convertirlas. Si se necesita otro CRS, usar `Exportar > Guardar como...`.

## Capas seleccionadas

| Capa original | Capa en GeoPackage | Uso en la ICR |
|---|---|---|
| `13ent` | `limite_estatal_13ent` | Limite estatal de Hidalgo |
| `13mun` | `municipios_13mun` | Limites municipales |
| `13l` | `localidades_poligono_13l` | Localidades urbanas y rurales amanzanadas |
| `13lpr` | `localidades_rurales_punto_13lpr` | Localidades rurales puntuales |
| `13sil` | `servicios_linea_13sil` | Caminos, rios, carreteras, corrientes de agua y otros servicios lineales |
| `13sia` | `servicios_area_13sia` | Cuerpos de agua, areas verdes y otros servicios de area |
| `13sip` | `servicios_punto_13sip` | Templos, escuelas, plazas, servicios y otros puntos de referencia |
| `13cd` | `caserio_disperso_13cd` | Contexto de caserio disperso |
| `13ar` | `ageb_rural_13ar` | AGEB rurales, solo si se necesita escala geoestadistica |

## Capas no copiadas por ahora

- `13e`: ejes de vialidad; muy pesada, usar solo si hace falta detalle vial.
- `13m`: manzanas; demasiado detallada para los mapas previstos.
- `13fm`: frentes de manzana; no necesaria para la ICR.
- `13a`: AGEB urbanas; secundaria para el enfoque rural actual.
- `13pe` y `13pem`: poligonos externos; no necesarios por ahora.

## Fuente original

La descarga original se conserva en `trabajos/mapas/13_hidalgo/`.
