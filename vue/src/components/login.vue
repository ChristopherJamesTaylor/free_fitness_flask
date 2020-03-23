<template>
    <v-container fluid>
        <div class="login-body">
            <LoginBanner/>
            <div class="login">
                <h1>Login</h1>
                <v-text-field
                        v-model="name"
                        label="Username or Email"
                        required
                />

                <v-text-field
                        v-model="password"
                        type="password"
                        label="Password"
                        required
                />

                <v-btn
                        :disabled="!valid"
                        color="blue"
                        class="mr-4"
                        v-on:click="login"
                >
                    Login
                </v-btn>
                <div>
                    <br>
                    <hr>
                    <br>
                    <p>DON'T HAVE AN ACCOUNT?</p>
                    <v-btn
                            color=" light green"
                            href="/#/registration"
                    >Register
                    </v-btn>
                </div>
            </div>
        </div>
        <div class="text-center ma-2">
            <v-snackbar
                    v-model="snackbar"
            >
                {{ text }}
                <v-btn
                        color="pink"
                        text
                        @click="snackbar = false"
                >
                    Close
                </v-btn>
            </v-snackbar>
        </div>
    </v-container>
</template>
<script>
    import LoginBanner from "@/components/LoginBanner";

    export default {
        name: 'login',
        components: {LoginBanner},
        data: () => ({
            snackbar: false,
            text: 'These login details are incorrect please try again',
            valid: true,
            name: '',
            nameRules: [
                v => !!v || 'Name is required',
                v => (v && v.length <= 25) || 'Name must be less than 25 characters'
            ],
            password: '',
            select: null,
        }),
        methods: {
            login() {
                let data = {
                    username: this.name,
                    password: this.password
                };
                this.$store.dispatch("login/checkUser", data).then((response) => {
                    if (response.data.status) {
                        sessionStorage.setItem('user', response.data.row.username);
                        sessionStorage.setItem('personID', response.data.row.id);
                        document.location.replace('/#/home');
                    } else {
                        // eslint-disable-next-line no-console
                        console.log("error");
                        // eslint-disable-next-line no-console
                        console.log(response);
                        this.snackbar = true;
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .login {
        border: 1px solid black;
        padding: 1.5rem;
        width: 300px;
        margin-left: auto;
        margin-right: auto;
        position: center;
        overflow: hidden;
    }

    .login-body {
        padding: 70px 0;
        text-align: center;
    }
</style>
