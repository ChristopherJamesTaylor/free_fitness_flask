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
                        <v-form
                                ref="form"
                        >
                            <v-row justify="space-around">
                                <v-col>
                                    <h3>Calories</h3>
                                    <v-text-field/>
                                </v-col>
                                <v-col><h3>Dietary requirements </h3>
                                    <v-radio-group v-model="type" :mandatory="false">
                                        <v-radio label="Vegan" value="vegan"/>
                                        <v-radio label="Vegetarian" value="vegetarian"/>
                                        <v-radio label="Keto" value="keto"/>
                                        <v-radio label="Paleo" value="paleo"/>
                                        <v-radio label="Standard" value="standard"/>
                                    </v-radio-group>
                                </v-col>
                                <v-flex>
                                    <v-autocomplete
                                         label="Intolerance"
                                         v-model="intolerances"
                                         :items="allergies"
                                    >
                                    </v-autocomplete>
                                </v-flex>
                            </v-row>
                        </v-form>
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
                    </v-card>
                    <v-card v-else class="mb-12" color="grey lighten-1">
                        <v-form
                                ref="form"
                                lazy-validation
                        >
                            <v-data-table
                                    :headers="headers"
                                    :items="exercises"
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
            days: null,
            type: null,
            goal: null,
            split: null,
            daysOfTheWeek: [],
            ability: null,
            training: null,
            exercises: [],
            intolerances: null,
            allergies: ['Dairy','Egg','Gluten', 'Grain', 'Peanut', 'Seafood', 'Sesame', 'Shellfish', 'Soy', 'Sulfite', 'Tree Nut', 'Wheat'],
            headers: [
                {text: "Exercise", value: "name"},
                 {text: "Body Part", value: "body_part"},
                {text: "Sets", value: "sets"},
                {text: "Repetitions", value: "reps"},
                {text: "Day", value: "day"},
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
                let data = {};
                this.$store.dispatch("nutrition/getMealPlan", data).then((response) => {
                        if (response) {
                            // eslint-disable-next-line no-console
                            console.log("success");
                            // eslint-disable-next-line no-console
                            console.log(response);
                        } else {
                            // eslint-disable-next-line no-console
                            console.log("error");
                        }
                    })
            },
            clear(){
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
