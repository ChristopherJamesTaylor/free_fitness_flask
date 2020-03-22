<template>
    <v-container fluid class="banner">
        <header class="site-header" role="banner">
            <h1>
              <a class="site-header_logo-link">
                Free Fitness
                <img src="../assets/profile.png" width="80" height="80">
              </a>
            </h1>
    </header>
    </v-container>
</template>

<script>
    export default {
        name: "LoginBanner"
    }
</script>

<style scoped>
.h1 a{
  color: inherit;
  text-decoration: none;
  font-weight: inherit;
}

.site-header{
  height: 100px;
  top: 0;
}
a{
  color: black;
  cursor: pointer;
  text-decoration: none;
  font-weight: bold;
  text-transform: uppercase;
  display: block;
  font: 16px "lato";
}
li{
  display: inline-block;
  margin-bottom: 0;
  vertical-align: middle;
  padding: 40px;

}
.site-header_logo-link {
  display: inline-block;
  word-break: break-word;
  font: 50px "Source Code Pro";
  }
.site-nav {
  padding: 3px 10px;
}
.container{
    padding: 0;
}
</style>