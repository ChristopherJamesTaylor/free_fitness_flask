<template>
    <v-card>
        <Menu></Menu>
        <v-card-title class="headline grey lighten-2">
        </v-card-title>
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
                <v-btn color="#00897B" class="ma-2" @click.native="clear()">Clear</v-btn>
                <v-btn id="edit" class="ma-2" color="#64FFDA" @click.native="generate()">Generate plan</v-btn>
            </v-stepper-header>

            <v-stepper-items>
                <v-stepper-content
                        v-for="step in steps"
                        :key="`${step.number}-content`"
                        :step="step.number"
                >
                    <v-card v-if="step.number == 1" class="mb-12" color="grey lighten-1">
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


                    <v-card v-else class="mb-12" color="grey lighten-1">
                        <v-form
                                ref="form"
                                lazy-validation
                        >
                            <v-data-table
                                    :headers="headers"
                                    :items="plan"
                                    class="elevation-1"
                            >
                            </v-data-table>
                        </v-form>
                    </v-card>
                </v-stepper-content>
            </v-stepper-items>
        </v-stepper>
    </v-card>
</template>

<script>
    import Menu from './Menu'

    export default {
        name: 'Nutrition',
        components: {Menu},
        data: () => ({
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
                {text: "Meal names", value: "meal_names"},
                {text: "Protein", value: "protein"},
                {text: "Carbohydrates", value: "carbohydrates"},
                {text: "Fat", value: "fat"},
                {text: "Days", value: "days"},
                {text: "Cooking time", value: "readyInMinutes"},
            ],
            meals: {
                "meal_names": [],
                "protein": null,
                "carbohydrates": null,
                "fat": null,
                "day": null,
                "cookInMinutes": []
            },
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
                        // eslint-disable-next-line no-console
                        console.log("success");
                        for(var i=0; i<=response.length; i++) {
                            // eslint-disable-next-line no-console
                            console.log("The key is",response[i].key);
                            this.meals["days"] = response[i].key;
                            this.meals['protein'] = response[i]['nutrients']['protein'];
                            this.meals['carbohydrates'] = response[i]['nutrients']['carbohydrates'];
                            this.meals['fat'] = response[i]['nutrients']['fat'];
                            this.meals['meal_names'].push(response[i]['meals']['cleanTitle']);
                            this.meals['cookInMinutes'].push(response[i]['meals']['readyInMinutes']);
                            this.plan.push(this.meals)
                        }
                    } else {
                        // eslint-disable-next-line no-console
                        console.log("error");
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
