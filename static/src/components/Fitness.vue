<template>
    <div>
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
                <v-btn>Save</v-btn>
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
                                        <v-radio label="Outdoors" value="Outdoors"/>
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
                            </v-row>
                        </v-form>
                    </v-card>
                    <v-card v-else class="mb-12" color="grey lighten-1">
                        <v-form
                                ref="form"
                                lazy-validation
                        >
                            <v-col>
                                <h3>Goals</h3>
                                <v-radio-group v-model="goal" :mandatory="false">
                                    <v-radio label="Lose Weight" value="Lose Weight"/>
                                    <v-radio label="Gain Muscle" value="Gain Muscle"/>
                                    <v-radio label="Stay Healthy" value="Stay Healthy"/>
                                    <v-radio label="Get shredded" value="Get shredded"/>
                                </v-radio-group>
                            </v-col>
                        </v-form>
                    </v-card>
                </v-stepper-content>
            </v-stepper-items>
        </v-stepper>
    </div>
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
                    title: 'Body and Mind'
                }
            ],
            days: null,
            type: null,
            intensityLevel: null,
            goal: null,
            split: null,
            daysOfTheWeek: [],
            ability: null,
            training: null
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
        }
    }
</script>

<style scoped>

</style>
