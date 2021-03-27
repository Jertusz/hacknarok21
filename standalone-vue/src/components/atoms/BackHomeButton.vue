<template>
    <Button label="Back" class="p-button-secondary p-button-text p-button-sm" @click="$emit('click')"/>
</template>

<script>
    import Button from "primevue/button";
    export default {
        name: "BackHomeButton",
        components: {
            Button
        }
    }
</script>

<style scoped>

</style>
