<template>
    <div>
        <heading />
        <main>
            <CreateSessionButton />
            <JoinSessionButton />
        </main>
        <PopupFooter />
        <hr/>
        <popup-footer />
    </div>
</template>

<script>
import Heading from "./Heading.vue";
import CreateSessionButton from "./CreateSessionButton.vue";
import JoinSessionButton from "./JoinSessionButton.vue";
import PopupFooter from "./PopupFooter.vue";

export default {
    name: 'PopupInterior',
    components: {
        PopupFooter,
        JoinSessionButton,
        CreateSessionButton,
        Heading
    }
};
</script>
