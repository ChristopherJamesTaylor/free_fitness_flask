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
            </v-stepper-header>

            <v-stepper-items>
                <v-stepper-content
                        v-for="step in steps"
                        :key="`${step.number}-content`"
                        :step="step.number"
                >
                    <v-card v-if="step.number == 1" class="mb-12" color="grey lighten-1" height="200px">
                        <v-form
                                ref="form"
                                lazy-validation
                        >
                            <v-text-field
                                    v-model="name"
                                    :counter="10"
                                    :rules="nameRules"
                                    label="Name"
                                    required
                            />

                            <v-text-field
                                    v-model="email"
                                    :rules="emailRules"
                                    label="E-mail"
                                    required
                            />

                            <v-select
                                    v-model="select"
                                    :items="items"
                                    :rules="[v => !!v || 'Item is required']"
                                    label="Item"
                                    required
                            />

                            <v-checkbox
                                    v-model="checkbox"
                                    :rules="[v => !!v || 'You must agree to continue!']"
                                    label="Do you agree?"
                                    required
                            />

                            <v-btn
                                    :disabled="!valid"
                                    color="success"
                                    class="mr-4"
                            >
                                Validate
                            </v-btn>

                            <v-btn
                                    color="error"
                                    class="mr-4"
                            >
                                Reset Form
                            </v-btn>

                            <v-btn
                                    color="warning"
                            >
                                Reset Validation
                            </v-btn>
                        </v-form>
                    </v-card>
                    <v-card v-else class="mb-12" color="grey lighten-1" height="200px">
                        <v-form
                                ref="form"
                                lazy-validation
                        >
                            <v-text-field
                                    v-model="name"
                                    :counter="10"
                                    :rules="nameRules"
                                    label="Name"
                                    required
                            />

                            <v-text-field
                                    v-model="email"
                                    :rules="emailRules"
                                    label="E-mail"
                                    required
                            />

                            <v-select
                                    v-model="select"
                                    :items="items"
                                    :rules="[v => !!v || 'Item is required']"
                                    label="Item"
                                    required
                            />

                            <v-checkbox
                                    v-model="checkbox"
                                    :rules="[v => !!v || 'You must agree to continue!']"
                                    label="Do you agree?"
                                    required
                            />

                            <v-btn
                                    :disabled="!valid"
                                    color="success"
                                    class="mr-4"
                            >
                                Validate
                            </v-btn>

                            <v-btn
                                    color="error"
                                    class="mr-4"
                            >
                                Reset Form
                            </v-btn>

                            <v-btn
                                    color="warning"
                            >
                                Reset Validation
                            </v-btn>
                        </v-form>
                    </v-card>

<!--                    <v-btn-->
<!--                            color="primary"-->
<!--                            @click="nextStep(n)"-->
<!--                    >-->
<!--                        Continue-->
<!--                    </v-btn>-->

<!--                    <v-btn text>Cancel</v-btn>-->
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
                    title:'One',
                },
                {
                    number: 2,
                    title:'Two'
                }
            ],
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
