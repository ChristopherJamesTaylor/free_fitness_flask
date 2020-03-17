<template>
    <div>
        <Menu></Menu>
        <div id="app" class="container">
        <div class="row">
            <div class="col-md-9">
                <!-- The map goes here -->
                <div id="map" class="map">


                        <!-- label and input elements go here -->
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div
                            class="form-check"
                            v-for="layer in layers"
                            :key="layer.id"
                    >
                <label class="form-check-label">
                    <input
                            class="form-check-input"
                            type="checkbox"
                            v-model="layer.active"
                            @change="layerChanged(layer.id, layer.active)"
                    />
                    {{ layer.name }}
                </label>
                <!-- The layer checkboxes go here -->
            </div>
        </div>
    </div>
    </div>
</template>
<script>
    import L from 'leaflet';
    import Menu from "./Menu";

    export default {
        name: "Gym",
        components: {Menu},
        data() {
            return {
                map: null,
                tileLayer: null,
                layers: [
                    {
                        id: 0,
                        name: 'Restaurants',
                        active: false,
                        features: []
                    }
                ],
            }
        },
  mounted() {
    this.initMap();
    this.initLayers();
  },
  methods: {
    layerChanged(layerId, active) {
      const layer = this.layers.find(layer => layer.id === layerId);

      layer.features.forEach((feature) => {
        if (active) {
          feature.leafletObject.addTo(this.map);
        } else {
          feature.leafletObject.removeFrom(this.map);
        }
      });
    },
    initLayers() {
      this.layers.forEach((layer) => {
        const markerFeatures = layer.features.filter(feature => feature.type === 'marker');
        const polygonFeatures = layer.features.filter(feature => feature.type === 'polygon');

        markerFeatures.forEach((feature) => {
          feature.leafletObject = L.marker(feature.coords)
            .bindPopup(feature.name);
        });

        polygonFeatures.forEach((feature) => {
          feature.leafletObject = L.polygon(feature.coords)
            .bindPopup(feature.name);
        });
      });
    },
    initMap() {
      this.map = L.map('map').setView([38.63, -90.23], 12);
      this.tileLayer = L.tileLayer(
        'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png',
        {
          maxZoom: 18,
          attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>',
        }
      );

      this.tileLayer.addTo(this.map);
    },
  },
    }
</script>

<style scoped>
    .map {
        height: 600px;
    }
</style>