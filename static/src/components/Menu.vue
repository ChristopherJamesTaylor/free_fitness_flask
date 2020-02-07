<template>
    <div>
        <header class="site-header" role="banner" align="center">
            <h1>
                <a class="site-header_logo-link" >
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
                   <a href="/#/profile" @click="getUserDetails"> <v-icon black size="80">mdi-account-circle</v-icon> </a>
            </v-avatar>
            <li>
                <v-toolbar-title>
                Welcome <br/> {{users}}
                </v-toolbar-title>
            </li>
            <li>
                <a>Logout</a>
            </li>
        </ul>
    </div>
</template>
<script>
    export default {
        name: 'Menu',
        computed: {
          users(){
              return sessionStorage.getItem('user')
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
            },
            getUserDetails(){
               let data = {
                   'username': sessionStorage.getItem('user'),
               };
               // eslint-disable-next-line no-console
               console.log("The data is:", data);
               this.$store.dispatch("user/getUser", data).then((response) => {
                    if (response){
                    // eslint-disable-next-line no-console
                    console.log("success");
                    // eslint-disable-next-line no-console
                    console.log(response);
                    return response.data
                } else {
                    // eslint-disable-next-line no-console
                    console.log("error");
                    this.snackbar = true;
                    return 'hi'
                    }
                })
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

