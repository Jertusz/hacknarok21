<template>
    <Button icon="pi pi-plus-circle" label="Create activity checking session" class="p-button-success m-1" @click="$emit('click')" />
</template>

<script>
    import Button from "primevue/button";
    export default {
        name: "CreateSessionButton",
        components: {
            Button
        }
    }
</script>

<style scoped>

</style>
