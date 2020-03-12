<template>
    <div>
        <Menu></Menu>
        <v-card>
            <v-row align="center">
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
                <v-col>
                    <h3>Age</h3>
                    <v-text-field filled v-model="age"></v-text-field>
                </v-col>
                <v-col>
                    <h3>Sex</h3>
                    <v-radio-group class="content" justify="justify" v-model="sex">
                        <v-radio label="Male" value="male"/>
                        <v-radio label="Female" value="female"/>
                    </v-radio-group>
                </v-col>

                <v-col>
                    <h3>Height</h3>
                    <v-radio-group align-content="center" v-model="heightUnit">
                        <v-radio label="Feet" value="feet"/>
                        <v-radio label="Metres" value="metres"/>
                    </v-radio-group>
                    <v-text-field filled :placeholder="heightUnit" v-model="height"></v-text-field>
                </v-col>

                <v-col>
                    <h3>Weight</h3>
                    <v-radio-group v-model="weightUnit">
                        <v-radio label="Pounds" value="pounds"/>
                        <v-radio label="Kilograms" value="kilograms"/>
                    </v-radio-group>
                    <v-text-field filled :placeholder="weightUnit" v-model="weight"></v-text-field>
                </v-col>
                <v-col>
                    <h3>Goal</h3>
                    <v-radio-group class="center" v-model="goal">
                        <v-radio label="Fat loss" value="fatLoss"/>
                        <v-radio label="Maintenance" value="maintain"/>
                        <v-radio label="Muscle gain" value="muscleGain"/>
                    </v-radio-group>
                </v-col>
                <v-col>
                    <h3>Activity Level</h3>
                    <v-radio-group align="center" justify="center" v-model="activity">
                        <v-radio label="Sedentary" value="sedentary"/>
                        <v-radio label="Active" value="active"/>
                        <v-radio label="Vigorously active" value="vActive"/>
                    </v-radio-group>
                </v-col>
                <v-col>
                    <v-btn class="center" rounded color="#64FFDA" @click="getMacros">Calculate</v-btn>
                </v-col>
            </v-row>
        </v-card>
        <MacrosDialog :macrosDialog.sync="macrosDialog" :macros="macros"/>
    </div>
</template>

<script>
    import Menu from './Menu'
    import MacrosDialog from './MacrosDialog'

    export default {
        name: 'Macros',
        components: {MacrosDialog, Menu},
        data() {
            return {
                macrosDialog: false,
                weight: null,
                height: null,
                heightUnit: null,
                weightUnit: null,
                age: null,
                sex: null,
                goal: null,
                activity: null,
                snackbar: false,
                tdee: [],
                macros: [],
                text: 'Please fill out the form correctly',
            }
        },
        methods: {
            test(){
                this.macrosDialog = true;
            },
            getMacros() {
                if (this.weight && this.height && this.heightUnit && this.weightUnit && this.age && this.sex && this.goal && this.activity) {
                    let data = {
                        'weight': this.weight,
                        'height': this.height,
                        'heightUnit': this.heightUnit,
                        'weightUnit': this.weightUnit,
                        'age': this.age,
                        'sex': this.sex,
                        'goal': this.goal,
                        'activity': this.activity,
                    };
                    this.$store.dispatch("macros/getMacros", data).then((response) => {
                        if (response) {
                            // eslint-disable-next-line no-console
                            console.log("Success");
                            this.macros.push(response['Macros']);
                            this.macrosDialog = true;
                        } else {
                            // eslint-disable-next-line no-console
                            console.log("error");
                        }
                    })
                } else {
                    // eslint-disable-next-line no-console
                    console.log("Not all the information has been filled out");
                    let data = {
                        'weight': this.weight,
                        'height': this.height,
                        'heightUnit': this.heightUnit,
                        'weightUnit': this.weightUnit,
                        'age': this.age,
                        'sex': this.sex,
                        'goal': this.goal,
                        'activity': this.activity,
                    };
                    // eslint-disable-next-line no-console
                    console.log(data);
                    this.snackbar = true;
                }
            }
        }
    }
</script>

<style scoped>
    .content {
        align-content: center;
    }

</style>
