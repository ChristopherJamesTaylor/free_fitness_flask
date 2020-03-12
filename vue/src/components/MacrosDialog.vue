<template>
    <div id="app">
        <v-app id="inspire">
                <v-dialog v-model="macrosDialog" fullscreen hide-overlay transition="dialog-bottom-transition">
                    <v-card>
                        <v-toolbar color="#64FFDA">
                            <v-btn icon dark @click="close">
                                <v-icon>mdi-close</v-icon>
                            </v-btn>
                        </v-toolbar>
                        <v-data-table :headers="headers" :items="getMacros"/>
                    </v-card>
                </v-dialog>
        </v-app>
    </div>
</template>

<script>
    export default {
        name: "MacrosDialog",
        computed: {
            getMacros(){
                // eslint-disable-next-line no-console
                console.log(this.$store.getters['macros/listMacros']['Macros']);
                return [this.$store.getters['macros/listMacros']['Macros']];
            },
        },
        data() {
            return {
                macros: [],
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