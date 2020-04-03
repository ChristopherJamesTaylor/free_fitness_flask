<template>
    <v-toolbar>
        <v-toolbar-title><a href="/#/home">Free Fitness</a></v-toolbar-title>
         <v-img :src="image" heigh="80" width="80" contain/>
        <v-spacer/>
        <div>
            <v-menu offset-y>
                <template v-slot:activator="{ on }">
                    <v-btn
                            color="#64FFDA"
                            v-on="on"
                    >
                        Your Fitness
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
</template>

<script>
    export default {
        name: "mobileMenu",
        data() {
            return {
                items: [
                    {title: 'Fitness Plan'},
                    {title: 'Nutrition Plan'},
                    {title: 'Macros and TDEE'},
                    {title: 'Gym Finder'},
                    {title: 'Profile'},
                    {title: 'Logout'},
                ],
                image: require("../assets/profile.png"),
                mobileNav: false,
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
                } else if (item.title == 'Fitness Plan') {
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
                } else if (item.title == 'Nutrition Plan') {
                    document.location.replace('/#/nutrition')
                } else if (item.title == 'Macros and TDEE') {
                    document.location.replace('/#/macros')
                } else if (item.title == 'Gym Finder') {
                    document.location.replace('/#/gyms')
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