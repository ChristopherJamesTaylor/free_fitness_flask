<template>
    <v-container fluid>
        <Menu/>
        <v-card>
            <v-toolbar>
                <v-toolbar-title>Profile Details</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-btn class="save-profile" @click="editDetails" color="#64FFDA">Save Details</v-btn>
            </v-toolbar>
            <v-data-table
                    :headers="headers"
                    :items="profile"
            >
                <template v-slot:item.id="{ item }">
                    <v-text-field
                            v-model="item.id"
                            :items="item"
                            :item-text="item.id"
                            outlined
                            disabled
                            type="text"
                    ></v-text-field>
                </template>
                <template v-slot:item.username="{ item }">
                    <v-text-field
                            v-model="item.username"
                            :items="item"
                            :item-text="item.username"
                            :rules="nameRules"
                            outlined
                            clearable
                            type="text"
                    ></v-text-field>
                </template>
                <template v-slot:item.first_name="{ item }">
                    <v-text-field
                            v-model="item.first_name"
                            :items="item"
                            :item-text="item.first_name"

                            outlined
                            clearable
                            type="text"
                    ></v-text-field>
                </template>
                <template v-slot:item.last_name="{ item }">
                    <v-text-field
                            v-model="item.last_name"
                            :items="item"
                            :item-text="item.last_name"
                            outlined
                            clearable
                            type="text"
                    ></v-text-field>
                </template>
                <template v-slot:item.email="{ item }">
                    <v-text-field
                            v-model="item.email"
                            :items="item"
                            :item-text="item.email"
                            :rules="emailRules"
                            outlined
                            clearable
                            type="text"
                    ></v-text-field>
                </template>
                <template v-slot:item.permissions="{ item }">
                    <v-text-field
                            v-model="item.permissions"
                            :items="item"
                            :item-text="item.permissions"
                            outlined
                            disabled
                            type="text"
                    ></v-text-field>
                </template>
            </v-data-table>
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
        </v-card>
        <Footer></Footer>
    </v-container>
</template>
<script>
    import Menu from './Menu'
    import Footer from "./footer";

    export default {
        name: 'Profile',
        components: {Footer, Menu},
        props: {
        },
        data: () => ({
            snackbar:null,
            text:'You have updated your profile!',
            username: null,
            user_id: null,
            dialog: false,
            avatar: null,
            saving: false,
            saved: false,
            message: null,
            email: null,
            first_name: null,
            last_name: null,
            permissions: null,
            nameRules: [
                v => !!v || 'Name is required',
                v => (v && v.length <= 25) || 'Name must be less than 25 characters'
            ],
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],
            headers: [
                {text: "Id", value: 'id'},
                {text: "Username", value: "username"},
                {text: "First name", value: "first_name"},
                {text: "Last name", value: "last_name"},
                {text: "Email", value: "email", align: 'center'},
                {text: "Permissions", value: "permissions",},
            ]
        }),
        computed: {
            cache: false,
            profile() {
                return this.$store.getters['user/listUser']
            }
        },
        methods: {
            editDetails() {
                let data = {
                    'profile': this.profile,
                    'id': sessionStorage.getItem('personID')
                };
                this.$store.dispatch('user/editProfile', data).then((response) => {
                    if (response) {
                        this.snackbar = true;
                    } else {
                        // eslint-disable-next-line no-console
                        console.log("error");
                    }
                });
            },
            deleteUser() {
                // eslint-disable-next-line no-console
                console.log("success");
            },
            savePic(avatar) {
                // eslint-disable-next-line no-console
                console.log('The avatar is: ', avatar)
            },
            uploadImage() {
                this.saving = true;
                setTimeout(() => this.savedAvatar(), 1000)
            },
            savedAvatar() {
                this.saving = false;
                this.saved = true
            }
        },
        watch: {
            avatar: {
                handler: function () {
                    this.saved = false
                },
                deep: true
            }
        },
    }
</script>

<style scoped>
    td.text-center {
        text-align: center;
    }

    .save-profile {
        align-items: center;
    }
</style>
