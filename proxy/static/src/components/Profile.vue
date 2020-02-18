<template>
    <div>
        <Menu/>
        <image-uploader v-model="avatar" align="center" color="black">
            <div slot="activator">
                <v-avatar size="150px" v-ripple v-if="!avatar" class="grey lighten-3 mb-3">
                    <span>Click to add a profile picture!</span>
                </v-avatar>
                <v-avatar size="150px" v-ripple v-else class="mb-3">
                    <img :src="avatar.imageURL" alt="avatar">
                </v-avatar>
            </div>
        </image-uploader>
        <CustomFileUploader
                    ref="custom"
                    @change="uploadFiles"
                    postURL="/airhub/imageUpload"
                    v-on:event_notify="setFiles"
                    successMessagePath="msg"
                    errorMessagePath="msg"
                    uploadButtonMessage="Save"
                    cancelButtonMessage="Clear"
                    :maxItems="5"
                    v-model="selImage"
              >
              </CustomFileUploader>
        <div align="center">
            <v-btn class="save-profile" @click="savePic">Save Profile picture</v-btn>
        </div>

        <v-data-table
                :headers="headers"
                :items="user"
                class="elevation-1"
        >

            <template v-slot:item.action="{ item }">
                <div style="white-space: nowrap;">

                    <v-tooltip bottom>
                        <template v-slot:activator="{ on }">
                            <v-icon
                                    @click="editUser(item)"
                                    medium
                                    class="mr-2"
                                    v-on="on">mdi-pencil
                            </v-icon>
                        </template>
                        <span>Edit User Details</span>
                    </v-tooltip>
                    <v-tooltip bottom>
                        <template v-slot:activator="{ on }">
                            <v-icon
                                    @click="deleteUser(item)"
                                    medium
                                    class="mr-2"
                                    v-on="on">mdi-delete
                            </v-icon>
                        </template>
                        <span>Delete User Details</span>
                    </v-tooltip>
                </div>
            </template>
        </v-data-table>
    </div>
</template>
<script>
    import Menu from './Menu'
    import ImageUploader from "./imageUploader";

    export default({
        name: 'Profile',
        components: {ImageUploader, Menu,},
        props: {},
        data: () => ({
            dialog: false,
            avatar: null,
            saving: false,
            saved: false,
            headers: [
                {text: "Id", value: 'id'},
                {text: "Username", value: "username"},
                {text: "First name", value: "first_name"},
                {text: "Last name", value: "last_name"},
                {text: "Email", value: "email", align: 'center'},
                {text: "Permissions", value: "permissions",},
                {text: "Action", value: "action", class: "hidden-xs-only", sortable: false},
            ]
        }),
        computed: {
            user() {
                let user = [];
                if (this.$store.getters["user/listUser"] !== '') {
                    user.push(this.$store.getters["user/listUser"]);
                }
                // eslint-disable-next-line no-console
                console.log(user);
                return user;
            }
        },
        methods: {
            editUser() {
                // eslint-disable-next-line no-console
                console.log("success");
            },
            deleteUser() {
                // eslint-disable-next-line no-console
                console.log("success");
            },
            savePic(avatar){
                // eslint-disable-next-line no-console
                console.log('The avatar is: ', avatar)
            },
            uploadImage() {
                this.saving = true;
                setTimeout(() => this.savedAvatar(), 1000)
            },
            uploadFiles(e) {
                var items = [];
                var formData = new FormData();
                let files = e.target.files;
                for (let x in files) {
                    if (!isNaN(x)) {
                        items = e.target.files[x];
                        formData.append('files[]', items);
                    }
                }
                // eslint-disable-next-line no-console
                console.log('About to hit the route');
                this.$store.dispatch('user/imageUpload', formData).then((response) => {
                    if (response) {
                        // eslint-disable-next-line no-console
                        console.log(response);
                    }
                    else {
                        // eslint-disable-next-line no-console
                        console.log('Error');
                    }
                });
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
    })
</script>

<style scoped>
    td.text-center {
        text-align: center;
    }
    .save-profile{
        align-items: center;
    }
</style>
