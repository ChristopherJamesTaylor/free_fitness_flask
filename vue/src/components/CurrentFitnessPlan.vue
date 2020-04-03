<template>
    <v-container fluid>
        <Menu/>
        <v-data-table
                :headers="headers"
                :items="plan"
        >
        </v-data-table>
    </v-container>
</template>

<script>
    import Menu from './Menu'

    export default {
        name: "CurrentFitnessPlan",
        components: {Menu},
        computed: {
           plan() {
               // eslint-disable-next-line no-console
               console.log(this.$store.getters['fitness/listCurrentPlan']);
               return this.$store.getters['fitness/listCurrentPlan'];
           }
        },
        data: () => ({
            dialog: false,
            avatar: null,
            saving: false,
            saved: false,
            headers: [
                {text: "Exercise", value: "exerciseName"},
                {text: "Body Part", value: "bodyPart"},
                {text: "Sets", value: "sets"},
                {text: "Repetitions", value: "reps"},
                {text: "Day", value: "day"},
            ],
        }),
    }
</script>

<style scoped>

</style>