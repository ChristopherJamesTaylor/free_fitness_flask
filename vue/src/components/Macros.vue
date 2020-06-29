<template>
    <div>
        <Menu></Menu>
        <v-container fluid>
            <v-form ref="macrosForm" lazy-validation class="text-xs-center">
                <v-layout row wrap>
                    <v-flex xs3>
                        <h3>Age</h3>
                        <v-text-field outlined v-model="age" required
                                      :rules="[v => !!v || 'Item is required']"></v-text-field>
                    </v-flex>
                    <v-flex xs3>
                        <v-spacer></v-spacer>
                    </v-flex>
                    <v-flex xs3>
                        <h3>Sex</h3>
                        <v-radio-group justify="justify" v-model="sex" required
                                       :rules="[v => !!v || 'Item is required']">
                            <v-radio label="Male" value="male"/>
                            <v-radio label="Female" value="female"/>
                        </v-radio-group>
                    </v-flex>
                    <v-flex xs3>
                        <h3>Weight and Height</h3>
                        <v-radio-group justify="justify" v-model="unit" required
                                       :rules="[v => !!v || 'Item is required']">
                            <v-radio label="Imperial" value="imperial"/>
                            <v-radio label="Metric" value="metric"/>
                        </v-radio-group>
                        <v-btn @click="setType">Confirm Unit</v-btn>
                    </v-flex>
                    <v-flex xs12>
                        <h3>Weight</h3>
                        <v-text-field outlined :placeholder="unitTypeWeight" v-model="weight" required
                                      :rules="[v => !!v || 'Item is required']"></v-text-field>
                        <h3>Height</h3>
                        <v-text-field outlined :placeholder="unitTypeHeight" v-model="height" required
                                      :rules="[v => !!v || 'Item is required']"></v-text-field>
                    </v-flex>
                    <v-flex xs6>
                        <h3>Goal</h3>
                        <v-radio-group class="center" v-model="goal" required :rules="[v => !!v || 'Item is required']">
                            <v-radio label="Fat loss" value="fatLoss"/>
                            <v-radio label="Maintenance" value="maintain"/>
                            <v-radio label="Muscle gain" value="muscleGain"/>
                        </v-radio-group>
                    </v-flex>
                    <v-flex xs6>
                        <h3>Activity Level</h3>
                        <v-radio-group v-model="activity" required :rules="[v => !!v || 'Item is required']">
                            <v-radio label="Sedentary" value="Sedentary"/>
                            <v-radio label="Slightly active" value="Slightly active"/>
                            <v-radio label="Lightly Active" value="Lightly Active"/>
                            <v-radio label="Moderately Active" value="Moderately Active"/>
                            <v-radio label="Very Active" value="Very Active"/>
                            <v-radio label="Extremely Active" value="Extremely Active"/>
                        </v-radio-group>
                        <v-btn class="center" rounded color="#64FFDA" @click="getMacros">Calculate</v-btn>
                    </v-flex>
                </v-layout>
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
            <MacrosDialog :macrosDialog.sync="macrosDialog" :macros="macros"/>
        </v-container>
        <Footer></Footer>
    </div>
</template>

<script>
    import Menu from './Menu'
    import MacrosDialog from './MacrosDialog'
    import Footer from "./footer";

    export default {
        name: 'Macros',
        components: {Footer, MacrosDialog, Menu},
        data() {
            return {
                macrosDialog: false,
                unitTypeWeight: '',
                unitTypeHeight: '',
                weight: null,
                height: null,
                unit: null,
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
            test() {
                this.macrosDialog = true;
            },
            setType() {
                if (this.unit != null) {
                    if (this.unit == "imperial") {
                        this.unitTypeHeight = 'ft';
                        this.unitTypeWeight = 'st';
                    } else {
                        this.unitTypeHeight = 'cm';
                        this.unitTypeWeight = 'kg';
                    }
                } else {
                    this.snackbar = true;
                }
            },
            getMacros() {
                if (this.$refs.macrosForm.validate()) {
                    let data = {
                        'weight': this.weight,
                        'height': this.height,
                        'unit': this.unit,
                        'age': this.age,
                        'sex': this.sex,
                        'goal': this.goal,
                        'activity': this.activity,
                    };
                    this.$store.dispatch("macros/getMacros", data).then((response) => {
                        if (response) {
                            // eslint-disable-next-line no-console
                            console.log("Success");
                            if (this.macros.length == 0) {
                                this.macros.push(response['Macros']);
                            }
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

</style>
