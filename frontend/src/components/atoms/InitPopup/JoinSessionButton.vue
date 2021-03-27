<template>
    <Button
        icon="pi pi-link"
        label="Join activity checking session"
        class="w-full p-button-secondary m-1"
        @click="$emit('click')"
    />
</template>

<script>
    import Button from "primevue/button";
    export default {
        name: "JoinSessionButton",
        components: {
            Button
        }
    }
</script>

<style scoped>

</style>
