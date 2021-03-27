<template>
    <aside>
        <popup-header />
        <main class="w-11/12">
            <session-creation-panel :mode="mode" @start-creation="enterCreationMode" @back="resetMode" />
            <session-joining-panel :mode="mode" @start-joining="enterJoiningMode" @back="resetMode" />
        </main>
        <popup-footer v-if="!isCreating && !isJoining" />
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
    },
    data(){
        return {
            isCreating: false,
            isJoining: false
        }
    },
    computed: {
        mode(){
            return {
                isJoining: this.isJoining,
                isCreating: this.isCreating
            }
        }
    },
    methods: {
        enterCreationMode(){
            this.isJoining = false;
            this.isCreating = true;
        },
        enterJoiningMode(){
            this.isCreating = false;
            this.isJoining = true;
        },
        resetMode(){
            this.isCreating = false;
            this.isJoining = false;
        }
    }
}
</script>

<style scoped>

    aside {
        max-width: 400px;
        min-height: 400px;
        max-height: 650px;
        border: 4px solid #323232;
        border-radius: 4px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

</style>
