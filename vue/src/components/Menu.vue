<template>
    <div>
        <DesktopMenu v-if="layoutDesktop"></DesktopMenu>
        <MobileMenu v-if="layoutMobile"></MobileMenu>
    </div>
</template>
<script>
    import DesktopMenu from "./desktopMenu";
    import MobileMenu from "./mobileMenu";
    export default {
        name: 'Menu',
        components: {MobileMenu, DesktopMenu},
        computed: {
            layoutMobile(){
                return this.$vuetify.breakpoint.mdAndDown;
            },
            layoutDesktop(){
            return this.$vuetify.breakpoint.mdAndUp;
            },
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

