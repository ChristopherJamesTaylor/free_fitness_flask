<template>
    <v-container fluid>
        <Menu></Menu>
        <v-stepper v-model="e1">
            <v-stepper-header>
                <template v-for="step in steps">
                    <v-stepper-step
                            :key="`${step.number}-step`"
                            :complete="e1 > step.number"
                            :step="step.number"
                            editable
                    >
                        Step {{ step.title }}
                    </v-stepper-step>

                    <v-divider
                            v-if="step.number !== steps"
                            :key="step.number"
                    />
                </template>
                <v-btn id="edit" class="ma-2" color="#64FFDA" @click.native="generate()">Generate plan</v-btn>
            </v-stepper-header>

            <v-stepper-items>
                <v-stepper-content
                        v-for="step in steps"
                        :key="`${step.number}-content`"
                        :step="step.number"
                >
                    <v-card v-if="step.number == 1">
                        <v-form>
                            <v-container>
                                <v-layout>
                                    <v-flex>
                                        <v-row>
                                            <v-col>
                                                <v-flex xs12>
                                                    <h3>Daily Calorie intake</h3>
                                                    <v-text-field v-model="calories"/>
                                                </v-flex>
                                            </v-col>
                                            <v-col>
                                                <v-flex xs12>
                                                    <h3>Dietary requirements </h3>
                                                    <v-radio-group v-model="diet" :mandatory="false">
                                                        <v-radio label="Vegan" value="vegan"/>
                                                        <v-radio label="Vegetarian" value="vegetarian"/>
                                                        <v-radio label="Keto" value="keto"/>
                                                        <v-radio label="Paleo" value="paleo"/>
                                                        <v-radio label="Standard" value="standard"/>
                                                    </v-radio-group>
                                                </v-flex>
                                            </v-col>
                                            <v-col>
                                                <h3>Allergies</h3>
                                                <v-radio-group v-model="allergies" :mandatory="false">
                                                    <v-radio label="None" value="none"/>
                                                    <v-radio label="Dairy" value="dairy"/>
                                                    <v-radio label="Egg" value="egg"/>
                                                    <v-radio label="Gluten" value="gluten"/>
                                                    <v-radio label="Grain" value="grain"/>
                                                    <v-radio label="Peanut" value="peanut"/>
                                                    <v-radio label="Seafood" value="seafood"/>
                                                    <v-radio label="Sesame" value="sesame"/>
                                                    <v-radio label="ShellFish" value="shellfish"/>
                                                    <v-radio label="Soy" value="soy"/>
                                                    <v-radio label="Sulfite" value="sulfite"/>
                                                    <v-radio label="Tree nut" value="tree nut"/>
                                                    <v-radio label="Wheat" value="wheat"/>
                                                </v-radio-group>
                                            </v-col>
                                            <v-btn color="#00897B" class="ma-2" @click.native="clear()">Clear</v-btn>
                                        </v-row>
                                        <v-snackbar
                                                v-model="snackbar"
                                        >
                                            {{ text }}
                                            <v-btn
                                                    color="#D50000"
                                                    text
                                                    @click="snackbar = false"
                                            >
                                                Close
                                            </v-btn>
                                        </v-snackbar>
                                    </v-flex>
                                </v-layout>
                            </v-container>
                        </v-form>
                    </v-card>


                    <v-card v-else class="mb-12">
                        <v-btn class="ma-2" color="#64FFDA" @click="savePlan">Save Plan</v-btn>
                        <v-spacer></v-spacer>
                        <v-text-field label="Search" v-model="search" ></v-text-field>
                        <v-data-table
                                :search="search"
                                :headers="headers"
                                :items="plan"
                                class="elevation-1"
                        >
                        </v-data-table>
                    </v-card>
                </v-stepper-content>
            </v-stepper-items>
        </v-stepper>
        <Footer></Footer>
    </v-container>
</template>

<script>
    import Menu from './Menu'
    import Footer from "./footer";

    export default {
        name: 'Nutrition',
        components: {Footer, Menu},
        data: () => ({
            search: '',
            e1: 1,
            steps: [
                {
                    number: 1,
                    title: 'Nutrition requirements',
                },
                {
                    number: 2,
                    title: 'Food Plan'
                }
            ],
            diet: null,
            allergies: null,
            calories: null,
            headers: [
                {text: "Breakfast", value: "breakfast"},
                {text: "Lunch", value: "lunch"},
                {text: "Dinner", value: "dinner"},
                {text: "Protein", value: "protein"},
                {text: "Carbohydrates", value: "carbohydrates"},
                {text: "Fat", value: "fat"},
                {text: "Days", value: "day"},
                {text: "Cooking time", value: "cookInMinutes"},
            ],
            plan: [],
            snackbar: false,
            text: 'Please fill out basic information',
        }),
        watch: {
            steps(val) {
                if (this.e1 > val) {
                    this.e1 = val
                }
            },
        },

        methods: {
            nextStep(n) {
                if (n === this.steps) {
                    this.e1 = 1
                } else {
                    this.e1 = n + 1
                }
            },
            generate() {

                let data = {
                    "calories": this.calories,
                    "diet": this.diet,
                    "allergies": this.allergies
                };
                this.$store.dispatch("nutrition/getMealPlan", data).then((response) => {
                    if (response) {
                        this.plan = response;
                        this.e1 = 2;
                    } else {
                        // eslint-disable-next-line no-console
                        console.log("error");
                        alert("A plan couldn't be generate");
                    }
                })
            },
            savePlan() {
                let data = {
                    "calories": this.calories,
                    "diet": this.diet,
                    "allergies": this.allergies,
                    "plan": this.plan,
                    "personID": sessionStorage.getItem('personID')
                };
                this.$store.dispatch("nutrition/savePlan", data).then((response) => {
                    if (response.data !== {}) {
                        // eslint-disable-next-line no-console
                        console.log("save plan");
                    } else {
                        // eslint-disable-next-line no-console
                        console.log("error");
                        alert("A plan couldn't be saved");
                    }
                })
            },
            clear() {
                this.training = null;
                this.type = null;
                this.daysOfTheWeek = [];
                this.goal = null;
            }
        }
    }
</script>

<style scoped>

</style>
