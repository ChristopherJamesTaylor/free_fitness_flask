<template>
    <v-container fluid>
        <Menu/>
        <v-card>
            <v-toolbar>
                <v-toolbar-title>Fitness Plan</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-btn class="save-profile" @click="saveDetails" color="#64FFDA">Save Details</v-btn>
            </v-toolbar>
            <v-data-table
                    :headers="headers"
                    :items="plan"
            >
                <template v-slot:item.exerciseName="{ item }">
                    <v-text-field
                            v-model="item.exerciseName"
                            :items="item"
                            :item-text="item.exerciseName"
                            outlined
                            clearable
                            type="text"
                    ></v-text-field>
                </template>
                <template v-slot:item.bodyPart="{ item }">
                    <v-text-field
                            v-model="item.bodyPart"
                            :items="item"
                            :item-text="item.bodypart"
                            outlined
                            clearable
                            type="text"
                    ></v-text-field>
                </template>
                <template v-slot:item.sets="{ item }">
                    <v-text-field
                            v-model="item.sets"
                            :items="item"
                            :item-text="item.sets"
                            place
                            outlined
                            clearable
                            type="text"
                    ></v-text-field>
                </template>
                <template v-slot:item.reps="{ item }">
                    <v-text-field
                            v-model="item.reps"
                            :items="item"
                            :item-text="item.reps"
                            place
                            outlined
                            clearable
                            type="text"
                    ></v-text-field>
                </template>
                <template v-slot:item.day="{ item }">
                    <v-text-field
                            v-model="item.day"
                            :items="item"
                            item-text="day"
                            place
                            outlined
                            clearable
                            type="text"
                    ></v-text-field>
                </template>
            </v-data-table>
            <v-snackbar
                    v-model="snackbar"
            >
                {{ text }}
                <v-btn
                        color="pink"
                        text
                        @click="snackbar = false"
                >
                    Close
                </v-btn>
            </v-snackbar>
        </v-card>
    </v-container>
</template>

<script>
    import Menu from './Menu'

    export default {
        name: "CurrentFitnessPlan",
        components: {Menu},
        methods: {
            saveDetails() {
                let data = {
                    'plan': this.plan,
                    'personID': sessionStorage.getItem('personID')
                };
                this.$store.dispatch('fitness/saveEditedPlan', data).then((response) => {
                    if (response) {
                        // eslint-disable-next-line no-console
                        console.log('success');
                        this.snackbar = true;
                    } else {
                        // eslint-disable-next-line no-console
                        console.log("error");
                    }
                });
            }
        },
        computed: {
            cache: false,
            plan() {
                return this.$store.getters['fitness/listCurrentPlan'];
            }
        },
        data: () => ({
            dialog: false,
            avatar: null,
            saving: false,
            saved: false,
            snackbar: false,
            text: 'You have successfully updated your plan',
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