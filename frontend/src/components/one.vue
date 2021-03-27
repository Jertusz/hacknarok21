<template>
    <div><Button label="LOL DZIAŁA" @click="sendToBg" /></div>
</template>

<script>
import Button from 'primevue/button';
import Communicator from '../background/Communicator.ts';

export default {
    methods: {
        sendToBg() {
            let sending = browser.runtime.sendMessage({ greet: 'message-From_popup' });
            sending.then((res) => {
                console.log(res);
            });
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
