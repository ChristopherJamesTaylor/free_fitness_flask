<template>
    <v-container fluid>
        <v-toolbar>
        <v-toolbar-title class="site-header_logo-link" role="banner">
            <a href="/#/home">Free Fitness</a>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <div>
            <v-img :src="image" heigh="80" width="80" contain/>
        </div>
        <v-spacer></v-spacer>
        <div>
            <a class="site-nav" href="/#/fitnessplan" @click="getFitnessPlan">Your Fitness Plan</a>
        </div>
        <v-spacer></v-spacer>
        <div>
            <a class="site-nav" href="/#/nutrition">Nutrition</a>
        </div>
        <v-spacer></v-spacer>
        <div>
            <a class="site-nav" href="/#/macros">Macros and TDEE</a>
        </div>
        <v-spacer></v-spacer>
        <div>
            <a class="site-nav" href="/#/gyms">Nearest Gym</a>
        </div>
        <v-spacer></v-spacer>
        <div>
            Welcome <br/> {{users}}
        </div>
        <v-spacer></v-spacer>
        <div>
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
        </div>
    </v-toolbar>
    </v-container>
</template>

<script>
    export default {
        name: "desktopMenu",
        computed: {
            users() {
                if (sessionStorage.getItem('user') == null) {
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
                ],
                image: require("../assets/profile.png"),
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
                if (item.title == 'Logout') {
                    this.logout();
                } else if (item.title == 'Profile') {
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
                    'personID': sessionStorage.getItem('personID')
                };
                this.$store.dispatch("fitness/getFitnessPlan", data).then((response) => {
                    if (response) {
                        // eslint-disable-next-line no-console
                        console.log(response);
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