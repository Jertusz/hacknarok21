<template>
    <div class="w-full px-4 flex">
        <div class="w-2/5">
            <Button label="SUPERVISION SESSION" class="p-button-help m-1 w-full" @click="createSupervisionSession" />
        </div>
        <div class="w-3/5 px-4">
            <p class="text-justify text-sm">This option is best for tests and exams to check if the students are cheating.</p>
        </div>
    </div>
</template>

<script>
import Button from "primevue/button";
export default {
    name: "CreateSupervisionSessionButton",
    components: {
        Button
    },
    methods: {
        createSupervisionSession(){
            this.$emit("clicked");
        }
    }
}
</script>

<style scoped>

</style>
