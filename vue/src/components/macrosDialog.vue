<template>
    <v-dialog v-model="dialog">
        <v-card>
            <v-form>
                <v-text-field label="TDEE" :placeholder="tdee"/>
            </v-form>
        </v-card>
        <v-card>
            <v-data-table :headers="headers" :items="macros"/>
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        name: "macrosDialog",
        data() {
            return {
                headers: [
                    {text: "Calories", value: "Calories"},
                    {text: "Protein", value: "name"},
                    {text: "Carbohydrates", value: "body_part"},
                    {text: "Fat", value: "sets"},
                ]
            }
        },
        props: {
            tdee: Object,
            macros: Object,
            dialog: Boolean
        },
        methods: {

        }
    }
</script>

<style scoped>

</style>