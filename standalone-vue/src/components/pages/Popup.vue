<template>
    <aside>
        <popup-header />
        <session-creation-panel />
        <session-joining-panel />
        <popup-footer />
    </aside>
</template>

<script>
import PopupFooter from "../atoms/PopupFooter";
import PopupHeader from "../atoms/PopupHeader";
import SessionCreationPanel from "../organisms/SessionCreationPanel";
import SessionJoiningPanel from "../organisms/SessionJoiningPanel";

export default {
    name: "Popup",
    components: {
        SessionJoiningPanel,
        SessionCreationPanel,
        PopupHeader,
        PopupFooter
    }
}
</script>

<style scoped>

</style>
