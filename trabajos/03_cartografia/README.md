# Cartografía

Organizar aquí todo el material de QGIS, capas fuente y mapas exportados.

## Proyecto QGIS activo

- Abrir `01_qgis_proyecto/mapa_general_icr.qgz`.
- El proyecto se guardó con rutas relativas para poder moverlo entre computadoras junto con este repositorio.
- No usar como fuente principal `trabajos/mapas/mapaGeneral/Mapa general nuevo.qgz`; quedó como copia local anterior.
- Capas fuente necesarias para los layouts actuales están dentro de `02_capas_fuente/`.
- `02_capas_fuente/puntos_construcciones/construcciones_tradicionales.gpkg` contiene la capa interna `Viviendas` con puntos exactos; no publicar coordenadas exactas.
- `02_capas_fuente/contexto/regiones/mexico_entidades_federativas.gpkg` sustituye al `00ent.shp` local anterior.
- `02_capas_fuente/contexto/inegi_13_hidalgo/02_gpkg_trabajo/vialidades_cardonal_13e.gpkg` contiene una derivada ligera de `13e` solo para Cardonal; se usa en `PL-03` para mostrar calles a escala comunitaria.
- `02_capas_fuente/contexto/inegi_13_hidalgo/02_gpkg_trabajo/inegi_13_hidalgo_contexto.gpkg` contiene `servicios_linea_13sil`, usado en `PL-04` para comparar terracerías, veredas, carreteras y puentes de INEGI.
- `02_capas_fuente/contexto/osm/caminos_osm_el_deca_el_buena.gpkg` contiene caminos vectoriales descargados de OpenStreetMap para el entorno El Deca-El Buena; en `PL-04` se usa como capa complementaria debajo de los caminos INEGI.

## Qué debe salir de esta carpeta

- Mapa de contexto regional.
- Mapa de comunidades.
- Mapa de construcciones con ubicación generalizada.
- Mapa interno de construcciones registradas y cuatro casos seleccionados (`PL-04`); antes de uso público, generalizar ubicaciones o confirmar autorización.
- Mapa de recorridos.
- Mapa o esquema de relación con materiales locales.

## Criterios

- Guardar coordenadas exactas solo para análisis interno.
- Exportar para ICR con puntos generalizados.
- Nombrar mapas con número y escala: `01_contexto_regional`, `02_comunidades`, etc.
- Usar `02_capas_fuente/contexto/inegi_13_hidalgo/` como base INEGI de contexto para Hidalgo.
- Revisar `02_capas_fuente/contexto/topografia_hidalgo/` antes de usar capas topográficas; las curvas de nivel y vegetación actuales están incompletas.
- El MDE original `13_Hidalgo_r15m_v4.tif` no se versiona por tamaño; se versionan sus derivados útiles para Cardonal.
- Distinguir en textos y mapas entre perímetros geoestadísticos de localidad y adscripción comunitaria declarada por habitantes; `C-02`, `C-04` y un punto gris cercano quedan fuera del polígono oficial, pero son reconocidos localmente como de `El Deca`.
