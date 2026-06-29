from pathlib import Path

from qgis.PyQt.QtGui import QColor
from qgis.core import (
    QgsApplication,
    QgsCategorizedSymbolRenderer,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsFeature,
    QgsFields,
    QgsField,
    QgsGeometry,
    QgsLayoutItemLabel,
    QgsLayoutItemLegend,
    QgsLayoutItemMap,
    QgsPalLayerSettings,
    QgsProject,
    QgsRendererCategory,
    QgsSingleSymbolRenderer,
    QgsSymbol,
    QgsVectorFileWriter,
    QgsVectorLayer,
    QgsVectorLayerSimpleLabeling,
    QgsWkbTypes,
)
from qgis.PyQt.QtCore import QVariant


ROOT = Path(__file__).resolve().parents[3]
PROJECT_PATH = ROOT / "trabajos/03_cartografia/01_qgis_proyecto/mapa_general_icr.qgz"
POINTS_PATH = ROOT / "trabajos/03_cartografia/02_capas_fuente/puntos_construcciones/construcciones_tradicionales.gpkg"
OSM_PATH = ROOT / "trabajos/03_cartografia/02_capas_fuente/contexto/osm/caminos_osm_el_deca_el_buena.gpkg"
REGIONS_PATH = ROOT / "trabajos/03_cartografia/02_capas_fuente/contexto/regiones/icr_capas_derivadas.gpkg"
OUT_DIR = ROOT / "trabajos/03_cartografia/02_capas_fuente/recorridos_y_area"
OUT_PATH = OUT_DIR / "recorridos_area_registro_2025.gpkg"


def layer_from_gpkg(path, layer_name, display_name):
    layer = QgsVectorLayer(f"{path}|layername={layer_name}", display_name, "ogr")
    if not layer.isValid():
        raise RuntimeError(f"No se pudo abrir la capa {layer_name}: {path}")
    return layer


def transform_geom(geom, source_crs, target_crs):
    transformed = QgsGeometry(geom)
    transformed.transform(QgsCoordinateTransform(source_crs, target_crs, QgsProject.instance()))
    return transformed


def polygon_parts(geom):
    multi = geom.asMultiPolygon()
    if multi:
        return [QgsGeometry.fromPolygonXY(part) for part in multi]
    polygon = geom.asPolygon()
    if polygon:
        return [QgsGeometry.fromPolygonXY(polygon)]
    return []


def write_layer(layer, layer_name):
    options = QgsVectorFileWriter.SaveVectorOptions()
    options.driverName = "GPKG"
    options.layerName = layer_name
    options.actionOnExistingFile = (
        QgsVectorFileWriter.CreateOrOverwriteLayer
        if OUT_PATH.exists()
        else QgsVectorFileWriter.CreateOrOverwriteFile
    )
    error, message, _, _ = QgsVectorFileWriter.writeAsVectorFormatV3(
        layer,
        str(OUT_PATH),
        QgsProject.instance().transformContext(),
        options,
    )
    if error != QgsVectorFileWriter.NoError:
        raise RuntimeError(f"Error al escribir {layer_name}: {message}")


def make_memory_layer(name, wkb_type, crs, fields):
    uri = f"{QgsWkbTypes.displayString(wkb_type)}?crs={crs.authid()}"
    layer = QgsVectorLayer(uri, name, "memory")
    provider = layer.dataProvider()
    provider.addAttributes(fields)
    layer.updateFields()
    return layer


def style_line_layer(layer):
    colors = {
        "R1": "#d7191c",
        "R2": "#2c7bb6",
        "R3": "#fdae61",
    }
    categories = []
    for key, color in colors.items():
        symbol = QgsSymbol.defaultSymbol(layer.geometryType())
        symbol.setColor(QColor(color))
        symbol.setWidth(1.0)
        categories.append(QgsRendererCategory(key, symbol, key))
    layer.setRenderer(QgsCategorizedSymbolRenderer("recorrido", categories))


def style_area_layer(layer):
    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor(158, 202, 225, 80))
    symbol.symbolLayer(0).setStrokeColor(QColor("#2171b5"))
    symbol.symbolLayer(0).setStrokeWidth(0.6)
    layer.setRenderer(QgsSingleSymbolRenderer(symbol))


def configure_viviendas_labels(layer):
    settings = QgsPalLayerSettings()
    settings.fieldName = "clave_registro"
    settings.isExpression = False
    settings.enabled = True
    labeling = QgsVectorLayerSimpleLabeling(settings)
    layer.setLabeling(labeling)
    layer.setLabelsEnabled(True)
    layer.triggerRepaint()


def project_layer(project, name):
    matches = project.mapLayersByName(name)
    return matches[0] if matches else None


def update_layout_labels(layout, replacements):
    for item in layout.items():
        if not isinstance(item, QgsLayoutItemLabel):
            continue
        text = item.text()
        if text in replacements:
            item.setText(replacements[text])
        else:
            for old, new in replacements.items():
                if old in text:
                    text = text.replace(old, new)
            item.setText(text)


def layer_extent_in_project(layer, project):
    transform = QgsCoordinateTransform(layer.crs(), project.crs(), project)
    return transform.transformBoundingBox(layer.extent())


def configure_layout_map(layout, project, layers, extent_layers):
    maps = [item for item in layout.items() if isinstance(item, QgsLayoutItemMap)]
    main_map = None
    for item in maps:
        if item.displayName() == "Map 2":
            main_map = item
            break
    if not main_map and maps:
        main_map = maps[-1]
    if not main_map:
        return

    selected_layers = [layer for layer in layers if layer is not None]
    main_map.setLayers(selected_layers)
    main_map.setKeepLayerSet(True)

    extent = None
    for layer in extent_layers:
        if layer is None:
            continue
        layer_extent = layer_extent_in_project(layer, project)
        if extent is None:
            extent = layer_extent
        else:
            extent.combineExtentWith(layer_extent)
    if extent is not None:
        extent.scale(1.18)
        main_map.setExtent(extent)
    main_map.storeCurrentLayerStyles()
    for item in layout.items():
        if isinstance(item, QgsLayoutItemLegend):
            item.setLinkedMap(main_map)
            item.setAutoUpdateModel(True)
            item.setLegendFilterByMapEnabled(True)
            item.updateLegend()


def create_or_replace_layout(project, source_name, new_name, replacements, layers, extent_layers):
    manager = project.layoutManager()
    existing = manager.layoutByName(new_name)
    if existing:
        manager.removeLayout(existing)
    source = manager.layoutByName(source_name)
    if not source:
        raise RuntimeError(f"No se encontro el layout base {source_name}")
    new_layout = manager.duplicateLayout(source, new_name)
    update_layout_labels(new_layout, replacements)
    configure_layout_map(new_layout, project, layers, extent_layers)
    return new_layout


def add_or_replace_project_layer(project, layer):
    for old in project.mapLayersByName(layer.name()):
        project.removeMapLayer(old.id())
    project.addMapLayer(layer)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if OUT_PATH.exists():
        OUT_PATH.unlink()

    app = QgsApplication([], False)
    QgsApplication.initQgis()

    target_crs = QgsCoordinateReferenceSystem("EPSG:6372")
    points = layer_from_gpkg(POINTS_PATH, "Viviendas", "Viviendas")
    osm = layer_from_gpkg(OSM_PATH, "Caminos OSM El Deca-El Buena", "Caminos OSM")
    communities = layer_from_gpkg(REGIONS_PATH, "comunidades_estudio_poligonos", "Comunidades de estudio")

    # Build community route areas.
    deca_geom = None
    buena_parts = []
    for feature in communities.getFeatures():
        name = feature["NOMGEO"]
        geom = transform_geom(feature.geometry(), communities.crs(), target_crs)
        if name == "El Deca":
            deca_geom = geom
        elif name == "El Buena":
            buena_parts.extend(polygon_parts(geom))

    if not deca_geom or not buena_parts:
        raise RuntimeError("No se encontraron las geometrias de El Deca y El Buena.")

    buena_parts = sorted(buena_parts, key=lambda g: g.area(), reverse=True)
    buena_grande = buena_parts[0]
    buena_chico = buena_parts[1] if len(buena_parts) > 1 else buena_parts[0].buffer(80, 12)

    point_geoms = []
    deca_point_buffers = []
    for feature in points.getFeatures():
        geom = transform_geom(feature.geometry(), points.crs(), target_crs)
        point_geoms.append(geom)
        if feature.id() in (1, 2, 3, 4):
            deca_point_buffers.append(geom.buffer(120, 12))

    deca_route_area = QgsGeometry.unaryUnion([deca_geom.buffer(90, 12)] + deca_point_buffers)
    buena_grande_route_area = buena_grande.buffer(100, 12)
    buena_chico_route_area = buena_chico.buffer(100, 12)

    route_specs = [
        ("R1", "Recorrido 1: El Deca", "Mayo de 2025", deca_route_area),
        ("R2", "Recorrido 2: El Buena, poligono mayor", "Mayo de 2025", buena_grande_route_area),
        ("R3", "Recorrido 3: El Buena, poligono menor", "Mayo de 2025", buena_chico_route_area),
    ]

    route_fields = QgsFields()
    route_fields.append(QgsField("recorrido", QVariant.String))
    route_fields.append(QgsField("descripcion", QVariant.String))
    route_fields.append(QgsField("fecha", QVariant.String))
    route_fields.append(QgsField("fuente", QVariant.String))
    route_layer = make_memory_layer("recorridos_aproximados_2025", QgsWkbTypes.MultiLineString, target_crs, route_fields)
    route_provider = route_layer.dataProvider()

    for road in osm.getFeatures():
        road_geom = transform_geom(road.geometry(), osm.crs(), target_crs)
        if road_geom.isEmpty():
            continue
        for key, desc, date, area in route_specs:
            if not road_geom.intersects(area):
                continue
            clipped = road_geom.intersection(area)
            if clipped.isEmpty():
                continue
            out = QgsFeature(route_layer.fields())
            out.setGeometry(clipped)
            out.setAttributes([key, desc, date, "OpenStreetMap, trazo aproximado sobre caminos existentes"])
            route_provider.addFeature(out)

    route_layer.updateExtents()
    write_layer(route_layer, "recorridos_aproximados_2025")

    area_fields = QgsFields()
    area_fields.append(QgsField("nombre", QVariant.String))
    area_fields.append(QgsField("criterio", QVariant.String))
    area_layer = make_memory_layer("area_registro_aproximada", QgsWkbTypes.Polygon, target_crs, area_fields)
    area_provider = area_layer.dataProvider()
    area_geom = QgsGeometry.unaryUnion([geom.buffer(140, 12) for geom in point_geoms]).convexHull().buffer(120, 18)
    area_feature = QgsFeature(area_layer.fields())
    area_feature.setGeometry(area_geom)
    area_feature.setAttributes([
        "Area aproximada de registro de construcciones tradicionales",
        "Envolvente generalizada de las construcciones visualizadas; no representa limites prediales ni coordenadas publicas exactas.",
    ])
    area_provider.addFeature(area_feature)
    area_layer.updateExtents()
    write_layer(area_layer, "area_registro_aproximada")

    project = QgsProject.instance()
    if not project.read(str(PROJECT_PATH)):
        raise RuntimeError(f"No se pudo abrir el proyecto: {PROJECT_PATH}")

    for point_layer_name in ("Viviendas", "Material / sistema constructivo"):
        for candidate in project.mapLayersByName(point_layer_name):
            if candidate.fields().indexOf("clave_registro") != -1:
                configure_viviendas_labels(candidate)

    routes_project_layer = layer_from_gpkg(OUT_PATH, "recorridos_aproximados_2025", "Recorridos aproximados 2025")
    area_project_layer = layer_from_gpkg(OUT_PATH, "area_registro_aproximada", "Area aproximada de registro")
    style_line_layer(routes_project_layer)
    style_area_layer(area_project_layer)
    add_or_replace_project_layer(project, area_project_layer)
    add_or_replace_project_layer(project, routes_project_layer)

    # Refresh layer handles after adding/replacing them in the project.
    routes_project_layer = project_layer(project, "Recorridos aproximados 2025")
    area_project_layer = project_layer(project, "Area aproximada de registro")
    osm_layer = project_layer(project, "OpenStreetMap")
    shade_layer = project_layer(project, "Sombreado relieve Cardonal")
    community_layer = project_layer(project, "Comunidades de estudio base") or project_layer(project, "Comunidad El Buena")
    osm_roads_layer = project_layer(project, "Caminos OSM")
    point_layer = project_layer(project, "Material / sistema constructivo") or project_layer(project, "Viviendas")

    # QgsLayoutItemMap expects the list in draw priority order; thematic layers first
    # so they are not hidden below the OSM/WMS background.
    base_context_layers = [point_layer, osm_roads_layer, shade_layer, osm_layer]
    create_or_replace_layout(
        project,
        "PL-04_Construcciones_Registradas",
        "PL-06_Recorridos_Documentacion_2025",
        {
            "PL-04": "PL-06",
            "4 / 7": "6 / 7",
            "Siguiente:\nPL-05": "Siguiente:\nPL-07",
            "Plano anterior:\nPL-03 Comunidades": "Plano anterior:\nPL-05 Materiales",
            "Registro de construcciones y corpus seleccionado": "Recorridos aproximados de documentacion en campo",
            "Construcciones registradas": "Recorridos de documentacion 2025",
            "PL-04. Construcciones registradas y casos seleccionados": "PL-06. Recorridos aproximados de documentacion, mayo de 2025",
            "INEGI; registro de campo; elaboracion propia": "OpenStreetMap; registro de campo; elaboracion propia",
            "Uso interno; ubicaciones no publicas": "Recorridos aproximados; no representan tracks GPS exactos",
        },
        [routes_project_layer] + base_context_layers,
        [routes_project_layer],
    )
    create_or_replace_layout(
        project,
        "PL-04_Construcciones_Registradas",
        "PL-07_Area_Registro_Constructivo",
        {
            "PL-04": "PL-07",
            "4 / 7": "7 / 7",
            "Siguiente:\nPL-05": "Siguiente:\n--",
            "Plano anterior:\nPL-03 Comunidades": "Plano anterior:\nPL-06 Recorridos",
            "Registro de construcciones y corpus seleccionado": "Area aproximada de registro y riqueza constructiva",
            "Construcciones registradas": "Area aproximada de registro",
            "PL-04. Construcciones registradas y casos seleccionados": "PL-07. Area aproximada donde se identifico diversidad constructiva",
            "INEGI; registro de campo; elaboracion propia": "OpenStreetMap; registro de campo; elaboracion propia",
            "Uso interno; ubicaciones no publicas": "Area generalizada; no representa coordenadas ni limites prediales exactos",
        },
        [point_layer, area_project_layer, osm_roads_layer, shade_layer, osm_layer],
        [area_project_layer],
    )

    project.write(str(PROJECT_PATH))
    QgsApplication.exitQgis()


if __name__ == "__main__":
    main()
    QgsCategorizedSymbolRenderer,
    QgsLayoutItemLabel,
    QgsLayoutItemMap,
    QgsRendererCategory,
