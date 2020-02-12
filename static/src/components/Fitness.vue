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
                                    <h3>Training level</h3>
                                    <v-radio-group v-model="training" :mandatory="false">
                                        <v-radio label="Beginner" value="Beginner"/>
                                        <v-radio label="Intermediate" value="Intermediate"/>
                                        <v-radio label="Advanced" value="Advanced"/>
                                        <v-radio label="Savage" value="Savage"/>
                                    </v-radio-group>
                                </v-col>
                                <v-col><h3>Type of workouts</h3>
                                    <v-radio-group v-model="type" :mandatory="false">
                                        <v-radio label="Gym" value="Gym"/>
                                        <v-radio label="Home" value="Home"/>
                                        <v-radio label="Mixed" value="Mixed"/>
                                        <v-radio label="I hate exercise" value="I hate exercise"/>
                                    </v-radio-group>
                                </v-col>
                                <v-col>
                                    <h3>Days of the week to workout</h3>
                                    <v-checkbox v-model="daysOfTheWeek" label="Monday" value="Monday"/>
                                    <v-checkbox v-model="daysOfTheWeek" label="Tuesday" value="Tuesday"/>
                                    <v-checkbox v-model="daysOfTheWeek" label="Wednesday" value="Wednesday"/>
                                    <v-checkbox v-model="daysOfTheWeek" label="Thursday" value="Thursday"/>
                                    <v-checkbox v-model="daysOfTheWeek" label="Friday" value="Friday"/>
                                    <v-checkbox v-model="daysOfTheWeek" label="Saturday" value="Saturday"/>
                                    <v-checkbox v-model="daysOfTheWeek" label="Sunday" value="Sunday"/>
                                </v-col>
                                <v-col>
                                    <h3>Goals</h3>
                                    <v-radio-group v-model="goal" :mandatory="false">
                                        <v-radio label="Lose Weight" value="Lose Weight"/>
                                        <v-radio label="Gain Muscle" value="Gain Muscle"/>
                                        <v-radio label="Stay Healthy" value="Stay Healthy"/>
                                        <v-radio label="Get shredded" value="Get shredded"/>
                                    </v-radio-group>
                                </v-col>
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
        name: 'Fitness',
        components: {Menu},
        data: () => ({
            e1: 1,
            steps: [
                {
                    number: 1,
                    title: 'Basic Information',
                },
                {
                    number: 2,
                    title: 'Generated Plan'
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
            headers: [
                {text: "Monday", value: ""},
                {text: "Tuesday", value: ""},
                {text: "Wednesday", value: ""},
                {text: "Thursday", value: ""},
                {text: "Friday", value: ""},
                {text: "Saturday", value: ""},
                {text: "Sunday", value: ""},
                {text: "Action", value: "action", class: "hidden-xs-only", sortable: false},
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
                let basicInformation = {
                    'trainingLevel': this.trainingLevel,
                    'type': this.type,
                    'days': this.daysOfTheWeek,
                    'goals': this.goals,
                };
                if (this.training != null && this.type != null && this.daysOfTheWeek !== [] && this.goal != null) {
                    this.$store.dispatch("fitness/getExercises", basicInformation).then((response) => {
                        if (response) {
                            // eslint-disable-next-line no-console
                            console.log("success");
                            // eslint-disable-next-line no-console
                            console.log(response);
                            this.exercises = response.data;
                        } else {
                            // eslint-disable-next-line no-console
                            console.log("error");
                        }
                    })
                } else {
                    this.snackbar = true
                }

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

<style lang="stylus" scoped>

</style>
