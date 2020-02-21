<template>
    <v-app class="app">
        <div class="login-body">
            <LoginBanner/>
            <div class="login">
                <h1>Registration</h1>

                <v-text-field
                        v-model="firstName"
                        :rules="nameRules"
                        label="First Name"
                        required
                />

                <v-text-field
                        v-model="lastName"
                        :rules="nameRules"
                        label="Last Name"
                        required
                />

                <v-text-field
                        v-model="username"
                        :counter="25"
                        :rules="nameRules"
                        label="Username"
                        required
                />

                <v-text-field
                        v-model="email"
                        label="Email"
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
                        v-on:click="register"
                >
                    Register
                </v-btn>
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
            <v-snackbar
                    v-model="snackbar_success"
            >
                {{ success_text }}
                <v-btn
                        color="pink"
                        text
                        @click="redirect"
                >
                    Close
                </v-btn>
            </v-snackbar>
        </div>
    </v-app>
</template>

<script>
    import LoginBanner from "@/components/LoginBanner";

    export default {
        name: 'login',
        components: {LoginBanner},
        data: () => ({
            snackbar: false,
            name: '',
            password: '',
            email: '',
            username: '',
            firstName: '',
            lastName: '',
            success_text: 'You have successfully registered to FreeFitness! ' +
                'Please close snack bar to be redirected',
            text: 'These details are already taken please try again',
            valid: true,
            snackbar_success: false,
            nameRules: [
                v => !!v || 'Name is required',
                v => (v && v.length <= 25) || 'Name must be less than 25 characters'
            ],
            select: null,
        }),
        methods: {
            redirect(){
                    this.snackbar_success = false;
                    document.location.replace('/');
            },
            register() {
                let data = {
                    firstName: this.firstName,
                    lastName: this.lastName,
                    email: this.email,
                    username: this.username,
                    password: this.password,
                };

                this.$store.dispatch("login/registerUser", data).then((response) => {
                    if (response['status']) {
                        this.snackbar_success = true;
                        setTimeout(() => {
                            // eslint-disable-next-line no-console
                             console.log("World!"); }, 8000);
                        document.location.replace('/');
                    } else {
                        // eslint-disable-next-line no-console
                        console.log("error");
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