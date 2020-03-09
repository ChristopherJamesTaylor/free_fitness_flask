<template>
      <v-content>
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.2.0/dist/leaflet.css">
            <router-view></router-view>
      </v-content>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang="sass">
      $color-pack: false
      @import '~vuetify/src/styles/main.sass'

</style>
