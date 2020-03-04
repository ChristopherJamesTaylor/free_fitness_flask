<template>
    <div>
        <Menu></Menu>
        <v-card>
            <h1 align="center">Macronutrient calculator</h1>
            <br/>
            <div align="center">
                <h3>Age</h3>
                <v-text-field filled></v-text-field>
                <h3>Sex</h3>
                <v-radio-group>
                    <v-radio label="Male" value="Male"/>
                    <v-radio label="Female" value="Male"/>
                </v-radio-group>
            </div>
            <br/>
            <div align="center">
                <h3>Height</h3>
                <v-radio-group v-model="height">
                    <v-radio label="Feet" value="feet"/>
                    <v-radio label="Metres" value="height"/>
                </v-radio-group>
                <v-text-field filled placeholder="{{height}}"></v-text-field>
            </div>
            <br/>
            <div align="center">
                <h3>Weight</h3>
                <v-radio-group v-model="weight">
                    <v-radio label="Pounds" value="Pounds"/>
                    <v-radio label="Kilograms" value="Kilograms"/>
                </v-radio-group>
                <v-text-field filled placeholder="{{weight}}"></v-text-field>
            </div>
            <br/>
            <div align="center">
                <h3>Goal</h3>
                <v-radio-group>
                    <v-radio label="Fat loss" value="fatLoss"/>
                    <v-radio label="Maintenance" value="maintain"/>
                    <v-radio label="Muscle gain" value="muscleGain"/>
                </v-radio-group>
            </div>
            <br/>
            <div align="center">
                <h3>Activity Level</h3>
                <v-radio-group>
                    <v-radio label="sedentary" value="sedentary"/>
                    <v-radio label="Active" value="active"/>
                    <v-radio label="Vigorously active" value="vActive"/>
                </v-radio-group>
            </div>
            <v-btn align="center">Calculate</v-btn>
        </v-card>
    </div>
</template>

<script>
    import Menu from './Menu'

    export default {
        name: 'Macros',
        components: {Menu},
        data() {
            return {
                weight: null,
                height: null,
            }
        }
    }
</script>

<style scoped>

</style>
