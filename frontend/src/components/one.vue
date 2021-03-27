<template>
    <div>
        <Button label="connect" @click="connect" />
        <Button label="send" @click="send" />
        <Button label="disconnect" @click="disconnect" />
    </div>
</template>

<script>
import Button from 'primevue/button';
import Communicator from '../background/Communicator.ts';

export default {
    methods: {
        connect() {
            Communicator.connect('ws://127.0.0.1:8000/ws/sessions/gowno/zygi/False/');
        },
        send() {
            Communicator.send(JSON.stringify({ type: 'custom_question_asked', question: 'Jakies pytania?' }));
        },
        disconnect() {
            Communicator.disconnect();
        },
    },
    data() {
        return { comms: Communicator.getInstance() };
    },
    components: {
        Button,
    },
};
</script>

<style></style>
