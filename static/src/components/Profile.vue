<template>
    <div>
        <Menu></Menu>


        <v-data-table
            :headers="headers"
            :items="user"
            class="elevation-0 userManagementDatatable"
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

    export default {
        name: 'Profile',
        components: {Menu},
        props:{

        },
        data: () => ({
            dialog: false,
            headers: [
                {
                    text: "Id",
                    align: "centre",
                    value: 'id'

                },

                {
                    text: "Username",
                    align: "centre",
                    value: "username"

                },

                {
                    text: "First name",
                    align: "centre",
                    value: "first_name"

                },

                {
                    text: "Last name",
                    align: "centre",
                    value: "last_name"

                },

                {
                    text: "Email",
                    align: "centre",
                    value: "email"

                },

                {
                    text: "Permissions",
                    align: "centre",
                    value: "permissions"

                },

                {
                    text: "Action",
                    align: "centre",
                    value: "action",
                    class: "hidden-xs-only",
                    sortable: false
                },

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
            deleteUser(){
                // eslint-disable-next-line no-console
                console.log("success");
            }
    },
    }
</script>

<style scoped>

</style>
