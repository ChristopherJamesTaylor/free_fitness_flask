<template>
    <div>
        <Menu/>
        <v-data-table
                :headers="headers"
                :items="plan"
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
    export default {
        name: "CurrentFitnessPlan",
        components: {Menu},
        data: () => ({
            dialog: false,
            avatar: null,
            saving: false,
            saved: false,
            headers: [
                {text: "Monday", value: 'id'},
                {text: "Tuesday", value: "username"},
                {text: "Wednesday", value: "first_name"},
                {text: "Thursday", value: "last_name"},
                {text: "Friday", value: "email", align: 'center'},
                {text: "Saturday", value: "permissions",},
                {text: "Sunday", value: "permissions",},
                {text: "Action", value: "action", class: "hidden-xs-only", sortable: false},
            ]
        }),
    }
</script>

<style scoped>

</style>