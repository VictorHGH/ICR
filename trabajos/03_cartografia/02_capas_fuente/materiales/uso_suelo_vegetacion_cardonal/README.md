# Uso de suelo y vegetacion Cardonal

Fuente: INEGI, `Mapa municipal de uso del suelo y vegetacion, Cardonal, Hidalgo`, UPC `794551158456`.

## Archivos

- `13015.tif`: raster georreferenciado de uso de suelo y vegetacion.
- `13015.tfw`: archivo de georreferencia auxiliar.
- `13015.tif.aux.xml`: estadisticas y metadatos auxiliares GDAL/QGIS.
- `usv_serieV_f1411_vegetacion.gpkg`: capa vectorial derivada del SHP INEGI Serie V `f1411_usv250s5v.shp`, cargada en QGIS como `Uso suelo / vegetación`.

## Informacion tecnica

- Municipio: Cardonal, Hidalgo.
- Escala del producto cartografico: 1:50 000.
- Cobertura temporal: 2024.
- Edicion: 2025.
- CRS del TIFF: `EPSG:6369`, Mexico ITRF2008 / UTM zone 14N.
- Resolucion aproximada: 4.23 m por pixel.
- La capa vectorial Serie V se usa con categorias `TIP_ECOV`; en el encuadre de `PL-05` se redujo la leyenda a clases visibles para mantener lectura cartografica.

## Uso en la ICR

Este raster sirve como contexto ambiental para mostrar la relacion entre las construcciones documentadas, las comunidades de El Deca y El Buena, y las unidades de uso de suelo/vegetacion del municipio.

Para `PL-05` se prefirio la capa vectorial `Uso suelo / vegetación` sobre el TIFF RGB porque permite una leyenda categorizada legible por tipo ecologico. El mapa debe leerse como relacion interpretativa materiales-territorio, no como localizacion exacta de extraccion de materiales.

No usar este TIFF para generar curvas de nivel; para curvas se requiere un raster de elevacion (MDE/DEM/CEM).
