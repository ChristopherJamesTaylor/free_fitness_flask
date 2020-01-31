<template xmlns:position="http://www.w3.org/1999/xhtml">
  <div>
      <Menu></Menu>
      <div class="image">
        <img :src="images" :alt="images" height="800" width="1500"/>
      </div>
  </div>
</template>

<script>
    import Menu from './Menu'
export default {
      name: 'Home',
      components: {Menu},
      data () {
        return {
          images: require('../assets/DSC00439.jpg')
        }
      }
    }
</script>

<style scoped>
</style>
