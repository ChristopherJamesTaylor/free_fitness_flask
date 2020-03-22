<template>
    <div>
        <Menu></Menu>
        <div align="center">
            <v-btn class="center" rounded color="#64FFDA" @click="getCoords"
            >Find Gyms
            </v-btn>
        </div>
        <br/>
        <v-container :align-content-center="true">
            <div id="app" class="container" >
            <div class="row" >
                <div class="col-md-12" >
                    <!-- The map goes here -->
                    <div id="map" class="map">
                    </div>
                </div>
            </div>
        </div>
        </v-container>
    </div>
</template>

<script>
    import Menu from "./Menu";
    import L from "leaflet";

    export default {
        name: "GymFinder",
        components: {Menu},
        data() {
            return {
                error: '',
                lat: '',
                lon: '',
                lmap: null,
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
            this.myFunction();
            this.initMap();
            this.initLayers();
        },
        methods: {
            myFunction: function () {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(this.showPosition);
                } else {
                    this.error = "Geolocation is not supported.";

                }
            },
            showPosition: function (position) {
                this.lat = position.coords.latitude;
                this.lon = position.coords.longitude;
                this.map.setView([this.lat, this.lon], 12);
            },
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
            //[38.63, -90.23]
            initMap() {
                this.map = L.map('map').setView([this.lat
                    , this.lon], 12);
                this.tileLayer = L.tileLayer(
                    'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png',
                    {
                        maxZoom: 18,
                        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>',
                    }
                );

                this.tileLayer.addTo(this.map);
            },
            getCoords() {
                let data = {
                    'lat': this.lat,
                    'long': this.lon,
                };
                this.$store.dispatch("gym/getGyms", data).then((response) => {
                    if (response) {
                        // eslint-disable-next-line no-console
                        console.log(response);
                        for (let i = 0; i < response['results'].length; i++) {
                            // eslint-disable-next-line no-console
                            console.log(response[i]);
                            L.marker([response.results[i].geometry.location.lat, response.results[i].geometry.location.lng], {iconUrl:response.results[i].icon}).addTo(this.map).bindPopup(response.results[i].name + '<br/>' + response.results[i].vicinity);
                        }
                    } else {
                        // eslint-disable-next-line no-console
                        console.log("error");
                    }
                })
            },
        }
    }
</script>

<style scoped>
    .map {
        height: 600px;
    }
</style>