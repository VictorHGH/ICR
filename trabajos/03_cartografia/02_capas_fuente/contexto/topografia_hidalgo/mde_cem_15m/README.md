# MDE CEM 15 m Hidalgo

Fuente: INEGI, Continuo de Elevaciones Mexicano 4.0.

## Archivos base

- `13_Hidalgo_r15m_v4.tif`: Modelo Digital de Elevacion para Hidalgo, resolucion 15 m.
- `continuonacional_r15_v4.txt`: metadato del producto.
- `continuonacional_r15_v4.xml`: metadato XML.
- `metadatos_continuonacional_r15_v4.txt`: resumen de metadatos.

## Informacion tecnica

- Producto: Continuo de Elevaciones Mexicano 4.0.
- Resolucion: 15 m.
- CRS original: `EPSG:6365`, Mexico ITRF2008, coordenadas geograficas.
- Elevacion minima en Hidalgo: 33 m.
- Elevacion maxima en Hidalgo: 3384 m.
- NoData: -32768.

## Derivados para la ICR

Carpeta: `derivados/`

- `cardonal_limite.gpkg`: limite municipal de Cardonal extraido de la base INEGI Hidalgo.
- `mde_cardonal_15m_utm14n.tif`: MDE recortado al municipio de Cardonal y reproyectado a `EPSG:6369`.
- `sombreado_cardonal_15m.tif`: sombreado de relieve derivado del MDE recortado.
- `curvas_nivel_cardonal_100m.gpkg`: curvas de nivel cada 100 m, con atributo `elev_m`.
- `curvas_nivel_cardonal_50m.gpkg`: curvas de nivel cada 50 m, con atributo `elev_m`.
- `curvas_nivel_cardonal_20m.gpkg`: curvas de nivel cada 20 m, con atributo `elev_m`.
- `curvas_nivel_cardonal_10m.gpkg`: curvas de nivel cada 10 m, con atributo `elev_m`.
- `curvas_nivel_cardonal_5m.gpkg`: curvas de nivel cada 5 m, con atributo `elev_m`.

## Uso en la ICR

Usar `sombreado_cardonal_15m.tif` como fondo de relieve suave y elegir las curvas segun el nivel de acercamiento del mapa:

- `100m`: contexto municipal o regional, cuando importa la forma general del relieve.
- `50m`: mapa municipal con mas detalle, sin saturar la lectura.
- `20m`: acercamiento a comunidades, rutas o zonas de estudio.
- `10m`: mapa de detalle alrededor de construcciones o relacion inmediata con ladera, barranca, terrazas o disponibilidad de materiales.
- `5m`: acercamiento fino a localidad o entorno inmediato del caso, cuando la separacion de `10m` deja demasiado espacio visual entre curvas.

Para composiciones impresas, activar solo una capa de curvas por mapa. Las curvas de `10m` y `5m` deben usarse con simbolo delgado o transparencia porque el MDE base tiene resolucion de 15 m y la densidad visual aumenta rapidamente. La capa de `5m` es util para interpretacion morfologica local, pero no sustituye un levantamiento topografico de precision.
