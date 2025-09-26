
// Subscriptions

PubSub.subscribe(mapEvent.MAP_SOURCES_LOADED, add_basemap_layers);
PubSub.subscribe(mapEvent.MAP_SOURCES_LOADED, add_layers);


// Subscriber Functions

function add_basemap_layers(msg) {
    const layers = map.getStyle().layers;
    // Find the index of the first symbol layer in the map style
    let beforeLayer;
    for (let i = 0; i < layers.length; i++) {
        if (layers[i].type === "symbol") {
            firstSymbolId = layers[i].id;
            break;
        }
    }
    const basemap_layers = JSON.parse(document.getElementById("mapengine_basemap_layers").textContent);
    for (const basemap_layer of basemap_layers) {
        map.addLayer(
            {
                id: basemap_layer.layer_id,
                type: basemap_layer.type,
                source: basemap_layer.layer_id,
            },
            beforeLayer
        );
        map.setLayoutProperty(basemap_layer.layer_id, "visibility", "none");
    }
    return logMessage(msg);
}

function add_layers(msg)
{
  const layers = JSON.parse(document.getElementById("mapengine_layers").textContent);
  const layers_at_startup = JSON.parse(document.getElementById("mapengine_layers_at_startup").textContent);
  for (const layer of layers) {
    map.addLayer(layer);
    const isStartupLayer = layers_at_startup.some(startup_layer => layer.id === startup_layer);
    if (isStartupLayer) {
      map.setLayoutProperty(layer.id, "visibility", "visible");
    } else {
      map.setLayoutProperty(layer.id, "visibility", "none");
    }

    if (map_store.cold.debug) {
      map.on("click", layer.id, function (e) {
        console.log(`${layer.id}:`, e.features[0].properties.name, e.features[0]);
      });
    }
  }
  PubSub.publish(mapEvent.MAP_LAYERS_LOADED);
  return logMessage(msg);
}

// Helper Functions

function turn_off_layer(layer_id) {
  const layerExists = map.getStyle().layers.some(layer => layer.id === layer_id);
  if (!layerExists) {
    throw new Error(`There are no layers starting with '${layer_id}' registered in map.`);
  }
  map.setLayoutProperty(layer_id, "visibility", "none");
}

function turn_on_layer(layer_id) {
  const layerExists = map.getStyle().layers.some(layer => layer.id === layer_id);
  if (!layerExists) {
    throw new Error(`There are no layers starting with '${layer_id}' registered in map.`);
  }
  map.setLayoutProperty(layer_id, "visibility", "visible");
}
