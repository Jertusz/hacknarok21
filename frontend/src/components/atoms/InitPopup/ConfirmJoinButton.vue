<template>
    <Button label="Confirm" class="p-button-secondary p-button-sm mb-1 w-40" @click="$emit('click')"/>
</template>

<script>
    import Button from "primevue/button";
    export default {
        name: "ConfirmJoinButton",
        components: {
            Button
        }
    }
</script>

<style scoped>

</style>
