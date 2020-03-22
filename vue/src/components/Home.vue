<template xmlns:position="http://www.w3.org/1999/xhtml">
    <v-container fluid>
        <Menu></Menu>
        <v-img :src="images" :alt="images" contain/>
        <Footer></Footer>
    </v-container>
</template>

<script>
    import Menu from './Menu'
    import Footer from "./footer";

    export default {
        name: 'Home',
        components: {Footer, Menu},
        data() {
            return {
                images: require('../assets/DSC00439.jpg')
            }
        }
    }
</script>

<style scoped>
    .text {
        color: black;
        cursor: pointer;
        text-decoration: none;
        font-weight: bold;
        text-transform: uppercase;
        display: block;
        font: 16px "lato";
    }
</style>
