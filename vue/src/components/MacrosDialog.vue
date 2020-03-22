<template>
    <v-container fluid>
                <v-dialog v-model="macrosDialog" fullscreen hide-overlay transition="dialog-bottom-transition" :macros="Macros">
                    <v-card>
                        <v-toolbar color="#64FFDA">
                            <v-btn icon dark @click="close">
                                <v-icon>mdi-close</v-icon>
                            </v-btn>
                        </v-toolbar>
                        <v-data-table :headers="headers" :items="Macros"/>
                    </v-card>
                </v-dialog>
    </v-container>
</template>

<script>
    export default {
        name: "MacrosDialog",
        computed: {
            // getMacros(){
            //     return [this.$store.getters['macros/listMacros']['Macros']];
            // },
        },
        data() {
            return {
                headers: [
                    {text: "Total Daily Energy Expenditure", value: "tdee"},
                    {text: "Protein (grams)", value: "protein"},
                    {text: "Carbohydrates (grams)", value: "carbohydrates"},
                    {text: "Fat (grams)", value: "fat"},
                ]
            }
        },
        props: {
            macrosDialog: {
                type: Boolean,
                required: true,
            },
            Macros: {
                type: Array,
                required: true,
            },
        },
        methods: {
            close() {
                this.$emit("update:macrosDialog", false);
            }
        }
    }
</script>

<style scoped>

</style>