<template>
    <v-container fluid>
        <div>
            <header class="site-header" role="banner" align="center">
                <h1>
                    <a class="site-header_logo-link" href="/#/home">
                        Free Fitness
                        <img src="../assets/profile.png" width="80" height="80">
                    </a>
                </h1>
            </header>
            <v-spacer></v-spacer>
            <ul align="center">
                <li>
                    <a class="site-nav" href="/#/fitnessplan" @click="getFitnessPlan">Your Fitness Plan</a>
                </li>
                <li>
                    <a class="site-nav" href="/#/nutrition">Nutrition</a>
                </li>
                <li>
                    <a class="site-nav" href="/#/macros">Macros and TDEE</a>
                </li>
                <li>
                    <a class="site-nav" href="/#/gyms">Nearest Gym</a>
                </li>
                <li>
                    <v-toolbar-title>
                        Welcome <br/> {{users}}
                    </v-toolbar-title>
                </li>
                <li>
                <v-menu offset-y>
                    <template v-slot:activator="{ on }">
                        <v-btn
                                color="#64FFDA"
                                v-on="on"
                        >
                           Profile and Logout
                        </v-btn>
                    </template>
                    <v-list>
                        <v-list-item
                                v-for="(item, index) in items"
                                :key="index"
                                @click="routing(item)"
                        >
                            <v-list-item-title>{{ item.title }}</v-list-item-title>
                        </v-list-item>
                    </v-list>
                </v-menu>
                </li>
            </ul>
        </div>
    </v-container>
</template>
<script>
    export default {
        name: 'Menu',
        computed: {
            users() {
                if(sessionStorage.getItem('user') == null){
                   document.location.replace('/');
                }
                return sessionStorage.getItem('user')
            },
        },
        data() {
            return {
                items: [
                    {title: 'Profile'},
                    {title: 'Logout'},
                ]
            }
        },
        methods: {
            getUser() {
                return this.$store.dispatch("login/listUsers");
            },
            logout() {
                sessionStorage.clear();
                document.location.replace('/');
            },
            routing(item) {
                if(item.title == 'Logout'){
                    this.logout();
                }
                else if(item.title == 'Profile'){
                    this.getUserDetails();
                }
            },
            getUserDetails() {
                let data = {
                    'username': sessionStorage.getItem('user'),
                };
                this.$store.dispatch("user/getUser", data).then((response) => {
                    if (response) {
                        // eslint-disable-next-line no-console
                        console.log("success");
                        // eslint-disable-next-line no-console
                        console.log(response);
                        document.location.replace('/#/profile');
                    } else {
                        // eslint-disable-next-line no-console
                        console.log("error");
                        this.snackbar = true;
                        return 'hi'
                    }
                })
            },
            getFitnessPlan() {
                let data = {
                    'personID': sessionStorage.getItem('id'),
                };
                this.$store.dispatch("user/getFitnessPlan", data).then((response) => {
                    if (response['exists']) {
                        document.location.replace('/#/currentfitnessplan');
                    } else {
                        document.location.replace('/#/fitnessplan');
                    }
                })
            },
        }
    }
</script>

<style scoped>
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

</style>

