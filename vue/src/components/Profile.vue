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
        <!--        <CustomFileUploader-->
        <!--                    ref="custom"-->
        <!--                    @change="uploadFiles"-->
        <!--                    postURL="/airhub/imageUpload"-->
        <!--                    v-on:event_notify="setFiles"-->
        <!--                    successMessagePath="msg"-->
        <!--                    errorMessagePath="msg"-->
        <!--                    uploadButtonMessage="Save"-->
        <!--                    cancelButtonMessage="Clear"-->
        <!--                    :maxItems="5"-->
        <!--                    v-model="selImage"-->
        <!--              >-->
        <!--              </CustomFileUploader>-->
        <div align="right">
            <v-btn class="save-profile" @click="saveDetails" color="#2196F3">Save Details</v-btn>
        </div>
        <v-data-table
                :headers="headers"
                :items="profile"
        >
            <template v-slot:item.id="{ item }">
                <v-text-field
                    v-model="user_id"
                    :items="item"
                    :item-text="item.id"
                    :placeholder="item.id"
                    place
                    outlined
                    disabled
                    type="text"
            ></v-text-field>
            </template>
            <template v-slot:item.username="{ item }">
                <v-text-field
                    v-model="username"
                    :items="item"
                    :item-text="item.username"
                    :placeholder="item.username"
                    place
                    outlined
                    clearable
                    type="text"
            ></v-text-field>
            </template>
            <template v-slot:item.first_name="{ item }">
                <v-text-field
                    v-model="first_name"
                    :items="item"
                    :item-text="item.first_name"
                    :placeholder="item.first_name"
                    place
                    outlined
                    clearable
                    type="text"
            ></v-text-field>
            </template>
            <template v-slot:item.last_name="{ item }">
                <v-text-field
                    v-model="last_name"
                    :items="item"
                    :item-text="item.last_name"
                    :placeholder="item.last_name"
                    place
                    outlined
                    clearable
                    type="text"
            ></v-text-field>
            </template>
            <template v-slot:item.email="{ item }">
                <v-text-field
                    v-model="email"
                    :items="item"
                    :item-text="item.email"
                    :placeholder="item.email"
                    place
                    outlined
                    clearable
                    type="text"
            ></v-text-field>
            </template>
            <template v-slot:item.permissions="{ item }">
                <v-text-field
                    v-model="permissions"
                    :items="item"
                    :item-text="item.permissions"
                    :placeholder="item.permissions"
                    place
                    outlined
                    disabled
                    type="text"
            ></v-text-field>
            </template>

        </v-data-table>
    </div>
</template>
<script>
    import Menu from './Menu'
    import ImageUploader from "./imageUploader";
    export default {
        name: 'Profile',
        components: {ImageUploader, Menu},
        props: {},
        data: () => ({
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
            permissions:null,
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
            profile() {
                let userDetails = [];
                // eslint-disable-next-line no-console
                console.log(this.$store.getters['user/listUser']);
                let profile = this.$store.getters['user/listUser'];
                // eslint-disable-next-line no-console
                console.log(profile);
                userDetails.push(profile);
                return userDetails
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
            savePic(avatar) {
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
                    } else {
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
