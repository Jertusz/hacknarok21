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
import Communicator from '@/background/Communicator';
import { ALL_EVENTS } from '@/background/EventTypes';

console.log(window.location.href);

export default {
    name: 'ActivityPrompt',
    components: {
        Button,
    },
    methods: {
        answerWith(confirmation) {
            Communicator.sendEvent(ALL_EVENTS.ANSWER_RANDOM_QUESTION, {
                answer: String(confirmation),
                question_id: this.id,
            });
            window.close();
        },
    },

    computed: {
        id() {
            return window.location.href.split('?')[1].split('&')[1].split('=')[1];
        },
        question() {
            return window.location.href.split('?')[1].split('&')[0].split('=')[1];
        },
    },
    mounted() {
        // register to push event for random / teacher question
    },
};
</script>

<style></style>
