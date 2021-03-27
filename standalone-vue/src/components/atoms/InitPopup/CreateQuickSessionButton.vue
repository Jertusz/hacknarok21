<template>
    <div class="w-full px-4 flex">
        <div class="w-2/5">
            <Button label="QUICK SESSION" class="p-button-success m-1 w-full" />
        </div>
        <div class="w-3/5 px-4">
            <p class="text-justify text-sm">This option is best for lessons and lecturers to track students attention.</p>
        </div>
    </div>
</template>

<script>
import Button from "primevue/button";
export default {
    name: "CreateQuickSessionButton",
    components: {
        Button
    }
}
</script>

<style scoped>

</style>
