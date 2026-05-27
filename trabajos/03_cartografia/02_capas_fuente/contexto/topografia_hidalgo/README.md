# Topografia Hidalgo

Revision de `trabajos/mapas/Hidalgo topografia/` para identificar capas utiles en la cartografia de la ICR.

## Estado de la carpeta fuente

La carpeta fuente contiene archivos parciales de varias capas. Para que un shapefile sea utilizable como capa espacial debe contar, como minimo, con `.shp`, `.shx` y `.dbf`. En esta carpeta varias capas aparecen incompletas.

## Capas de interes para la ICR

| Capa | Interes | Estado actual | Decision |
|---|---|---|---|
| `curva_nivel250_l` | Curvas de nivel | Incompleta: solo hay `.prj`, `.sbn` y `.shp.xml`; falta `.shp`, `.shx` y `.dbf` | No usable por ahora |
| `vegetacion250_a` | Vegetacion | Incompleta: hay `.dbf` y `.shp.xml`, pero falta `.shp` y `.shx` | No usable por ahora |
| `camino250_l` | Caminos | Incompleta: falta `.shx`; ademas la capa INEGI `13sil` ya cubre caminos y otros servicios lineales | No copiar por ahora |
| `canal250_l` | Canales | Legible, pero sin `.dbf` ni `.prj` en la carpeta | Secundaria; preferir `13sil` si basta |
| `conducto250_l` | Conductos | Legible, pero sin `.dbf` ni `.prj` en la carpeta | No prioritaria para la ICR |
| `via_ferrea250_l` | Via ferrea | Legible, pero sin `.dbf` ni `.prj` en la carpeta | Usar solo si aparece en el contexto regional |
| `aerodromo250_a`, `pista_aviaci250_l` | Infraestructura aeroportuaria | Legibles, pero no relevantes para el diagnostico de construcciones | No usar por ahora |
| `ins_diversa250_p`, `rasgo_arqueo250_p` | Puntos diversos / arqueologicos | Incompletas o secundarias | No usar por ahora |

## CRS probable

Los metadatos y archivos `.prj` presentes indican `MEXICO_ITRF_2008_LCC`, equivalente practico al CRS usado por INEGI para estas capas. En QGIS corresponde al flujo de trabajo con `EPSG:6372` cuando se integra con el Marco Geoestadistico.

## Recomendacion

- No copiar estas capas al GeoPackage de trabajo hasta conseguir los archivos completos.
- Para curvas de nivel, volver a descargar la capa topografica completa de INEGI o usar un modelo de elevacion/curvas ya completas.
- Para vegetacion, volver a descargar `vegetacion250_a` completa o buscar una capa de uso de suelo y vegetacion completa.
- Mientras tanto, usar `02_capas_fuente/contexto/inegi_13_hidalgo/02_gpkg_trabajo/inegi_13_hidalgo_contexto.gpkg` para limites, localidades, servicios lineales, areas y puntos de referencia.

## Fuentes web revisadas

- INEGI, Topografia: `https://www.inegi.org.mx/temas/topografia/`.
- INEGI, Informacion topografica 1:50 000: `https://www.inegi.org.mx/programas/topografia/50000/`.
- INEGI, Descarga tu mapa: `https://www.inegi.org.mx/descarga-mapa/`.
- INEGI, Uso de suelo y vegetacion 2019: `https://www.inegi.org.mx/programas/usyv/2019/`.
- INEGI, Modelos Digitales de Elevacion: `https://www.inegi.org.mx/programas/mde/`.
- INEGI, Continuo de Elevaciones Mexicano: `https://www.inegi.org.mx/app/geo2/elevacionesmex/`.

## Hallazgos de busqueda web

- El paquete oficial `Descarga tu mapa` para Hidalgo en QGIS esta disponible en `https://www.inegi.org.mx/contenidos/descarga-mapa/proyectos-sig/hgo-QGis.zip`. Se reviso en temporal y contiene `Hidalgo.qgz` y `mapa_base.gpkg`; no contiene curvas de nivel ni vegetacion detallada.
- El servicio WMS/WMTS de INEGI permite usar el mapa base topografico en QGIS. Es util para ver relieve y posible representacion topografica como fondo, pero no sustituye una capa vectorial editable de curvas de nivel.
- La pagina de Uso de suelo y vegetacion 2019 ofrece capas descargables por recorte mediante el servicio de INEGI. El flujo genera CAPTCHA, por lo que la descarga final debe completarse manualmente en navegador.
- Para curvas de nivel editables, la alternativa mas robusta es descargar un MDE/CEM de INEGI y generar curvas en QGIS, o localizar el paquete topografico completo donde `curva_nivel250_l` incluya `.shp`, `.shx`, `.dbf` y `.prj`.
