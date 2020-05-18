<template>
    <v-container fluid class="banner">
        <v-toolbar flat light short>
            <v-toolbar-title class="site-header_logo-link">
                Free Fitness
            </v-toolbar-title>
            <v-img src="../assets/profile.png" width="80" height="80" contain />
        </v-toolbar>
    </v-container>
</template>

<script>
    export default {
        name: "LoginBanner"
    }
</script>

<style scoped>

.site-header_logo-link {
  display: inline-block;
  word-break: break-word;
  font-weight: bold;
  text-transform: uppercase;
  font: 30px "Source Code Pro";
  }
</style>