<template>
    <div><Button label="LOL DZIAŁA" @click="sendToBg" /></div>
</template>

<script>
import Button from 'primevue/button';

export default {
    methods: {
        sendToBg() {
            let sending = browser.runtime.sendMessage({ greet: 'message-From_popup' });
            sending.then((res) => {
                console.log(res)
            });
        },
    },
    data() {
        return {};
    },
    components: {
        Button,
    },
};
</script>

<style></style>
