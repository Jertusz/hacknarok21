<template>
    <div>
        <Button label="connect" @click="connect" />
        <Button label="send" @click="send" />
        <Button label="Register" @click="register" />
        <Button label="disconnect" @click="disconnect" />
    </div>
</template>

<script>
import Button from 'primevue/button';
import Communicator from '../background/Communicator.ts';
import { ALL_EVENTS, GENERIC_EVENTS } from '@/background/EventTypes';

export default {
    methods: {
        connect() {
            Communicator.connect('ws://127.0.0.1:8000/ws/sessions/sessionID/USERNAME/True/');
        },
        send() {
            Communicator.sendEvent(ALL_EVENTS.GENERIC_EVENT, {
                action: GENERIC_EVENTS.TAB_SWITCHED,
                text: 'Zmieniona karta',
            });
        },
        register() {
            Communicator.registerListener(ALL_EVENTS.RANDOM_QUESTION_APPEARS, (data) => {
                console.log(data);
            });
            Communicator.registerListener(ALL_EVENTS.GENERIC_EVENT, (data) => {
                this.generic_events.push(data);
            });
        },
        disconnect() {
            Communicator.disconnect();
        },
    },
    data() {
        return {
            generic_events: [],
        };
    },
    components: {
        Button,
    },
};
</script>

<style></style>
