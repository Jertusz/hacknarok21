<template>
    <aside class="w-full flex items-center justify-between p-2">
        <div class="w-2/3 flex items-center p-4">
            <p class="font-bold text-lg">{{ question }}</p>
        </div>
        <div class="w-1/3 flex items-center justify-center">
            <Button label="No" @click="answerWith(false)" class="m-1 p-button-danger" />
            <Button label="Yes" @click="answerWith(true)" class="m-1 p-button-success" />
        </div>
    </aside>
</template>

<script>
import Button from 'primevue/button';

export default {
    name: 'ActivityPrompt',
    props: {
        question: {
            type: String,
            default: '',
        },
    },
    components: {
        Button,
    },
    methods: {
        answerWith(confirmation) {
            // this.$emit("answered", confirmation);
        },
    },
    mounted() {
        // register to push event for random / teacher question
    },
};
</script>

<style></style>
