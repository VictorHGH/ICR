# OpenStreetMap - caminos El Deca / El Buena

Esta carpeta contiene caminos vectoriales descargados de OpenStreetMap para el entorno de El Deca y El Buena, Cardonal, Hidalgo.

## Capas

- `caminos_osm_el_deca_el_buena.gpkg`: GeoPackage con la capa interna `Caminos OSM El Deca-El Buena`.

## Uso en QGIS

- La capa se usa en `PL-04_Construcciones_Registradas` como complemento de las capas INEGI.
- En el layout se dibuja debajo de `Vialidades INEGI`, `Puentes INEGI`, `Carreteras INEGI`, `Terracerias INEGI` y `Veredas INEGI`.
- Su función no es reemplazar la cartografía oficial, sino mostrar accesos que la capa INEGI no representa con la misma cercanía a las construcciones registradas.

## Interpretación

- Los trazos OSM se leen como cartografía colaborativa y deben contrastarse con observación de campo, relato local y capas oficiales.
- Para `C-02`, `C-04` y un punto gris cercano, los caminos OSM quedan mucho más cerca de los puntos que las capas INEGI disponibles.
- No publicar coordenadas exactas de construcciones en productos públicos sin autorización o generalización espacial.
