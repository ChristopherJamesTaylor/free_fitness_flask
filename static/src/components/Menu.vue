<template>
    <div>
        <header class="site-header" role="banner" align="center">
            <h1>
                <a class="site-header_logo-link" href="\">
                    Free Fitness
                    <img src="../assets/profile.png" width="80" height="80">
                </a>
            </h1>
        </header>
        <br>
        <ul align="center">
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
                <a class="site-nav" href="/#/tdee">TDEE</a>
            </li>
            <li>
                <a class="site-nav" href="/#/gyms">Nearest Gym</a>
            </li>
            <v-avatar color="black">
                   <a href="/#/profile"> <v-icon black size="80">mdi-account-circle</v-icon> </a>
            </v-avatar>
            <li>
                <H1>
                Welcome <br/> {{users.data.user_details.first_name}} {{users.data.user_details.last_name}}
                </H1>
            </li>
        </ul>
    </div>
</template>
<script>
    export default {
        name: 'Menu',
        computed: {
          users(){
            // eslint-disable-next-line no-console
            console.log(this.$store.getters["login/listUsers"]);
            return this.$store.getters["login/listUsers"]
          }
        },
        data() {
            return {
                items: [
                    {title: 'Home'},
                    {title: 'Users'},
                    {title: 'Admin'},
                    {title: 'Setting'}
                ]
            }
        },
        methods: {
            getUser(){
               return this.$store.dispatch("login/listUsers");
            }
        }
    }
</script>

<style scoped>
    .profile{
        position: absolute;
        right:1px;
        padding-right: 300px;
        top: 1px;
        padding-top: 110px;
    }
    .avatar{
        right:1px;
    }
    .h1 a {
        color: inherit;
        text-decoration: none;
        font-weight: inherit;
    }

    .site-header {
        height: 65px;
        overflow: visible;
        top: 0;
    }

    a {
        color: black;
        cursor: pointer;
        text-decoration: none;
        font-weight: bold;
        text-transform: uppercase;
        display: block;
        font: 16px "lato";
    }

    li {
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

    .container {
        padding: 0;
    }


</style>

