<template>
  <div>

    <header class="site-header" role="banner">
            <h1>
              <a class="site-header_logo-link" href="\">
                Free Fitness
                <img src="../assets/profile.png" width="80" height="80">
              </a>
            </h1>
    </header>
      <br>
      <ul>
           <li>
            <a class="site-nav" href="/#/fitnessplan">Your Fitness Plan</a>
          </li>
          <li>
            <a class="site-nav" href="/#/nutrition">Nutrition</a>
          </li>
          <li>
            <a class="site-nav" href="/#/macros">Macros</a>
          </li>
          <li>
            <a  class="site-nav" href="/#/tdee">TDEE</a>
          </li>
          <li>
            <a  class="site-nav" href="/#/gyms">Nearest Gym</a>
          </li>
          </ul>
  </div>
</template>

<script>
    export default {
      name: 'Menu',
      data () {
        return {
          items: [
            {title: 'Home'},
            {title: 'Users'},
            {title: 'Admin'},
            {title: 'Setting'}
          ]
        }
      }
    }
</script>

<style scoped>
.h1 a{
  color: inherit;
  text-decoration: none;
  font-weight: inherit;
}

.site-header{
  height: 65px;
  overflow: visible;
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
  font: 60px "Source Code Pro";
  }
.site-nav {
  padding: 3px 10px;
}
.container{
    padding: 0;
}



</style>

