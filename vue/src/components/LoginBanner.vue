<template>
    <div>
        <desktop-login-banner v-if="layoutDesktop"></desktop-login-banner>
        <mobile-login-banner v-if="layoutMobile"></mobile-login-banner>
    </div>
</template>

<script>
    import desktopLoginBanner from "./desktopLoginBanner";
    import mobileLoginBanner from "./mobileLoginBanner";
    export default {
        name: "LoginBanner",
        components: {desktopLoginBanner, mobileLoginBanner},
        computed: {
            layoutMobile(){
                return this.$vuetify.breakpoint.mdAndDown;
            },
            layoutDesktop(){
            return this.$vuetify.breakpoint.mdAndUp;
            },
        },
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