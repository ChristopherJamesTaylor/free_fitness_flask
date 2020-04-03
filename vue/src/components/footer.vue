<template>
    <v-container fluid>
        <v-footer>
            <div>A Taylor's Tales Production</div>
            <v-spacer></v-spacer>
            <div>Version 1.1.0</div>
            <v-spacer></v-spacer>
            <div>&copy; {{ new Date().getFullYear() }}</div>
        </v-footer>
    </v-container>
</template>

<script>
    export default {
        name: "footer"
    }
</script>

<style scoped>

</style>