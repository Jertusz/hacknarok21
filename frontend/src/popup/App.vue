<template>
    <aside>

        <popup-header />

        <main class="w-11/12" v-if="isCreator">
            <session-creation-panel :mode="mode" @start-creation="enterCreationMode" @back="resetMode" />
            <session-joining-panel :mode="mode" @start-joining="enterJoiningMode" @back="resetMode" />
        </main>

        <main class="w-11/12" v-if="isJustUser">
            Dobra robota! Twoja obecność jest aktualnie mierzona poprawnie.
        </main>

        <main v-if="isPrompted">
            <ActivityPopup question="Czy jesteś obecny duchem?" />
        </main>

        <popup-footer v-if="!isCreating && !isJoining" />

        <hr />


    </aside>
</template>

<script>
import PopupFooter from '../components/atoms/InitPopup/PopupFooter';
import PopupHeader from '../components/atoms/InitPopup/PopupHeader';
import SessionCreationPanel from '../components/organisms/InitPopup/SessionCreationPanel';
import SessionJoiningPanel from '../components/organisms/InitPopup/SessionJoiningPanel';
import One from '@/components/one';
import ActivityPopup from '@/components/atoms/InitPopup/activityPopup.vue';

export default {
    name: 'Popup',
    components: {
        One,
        SessionJoiningPanel,
        SessionCreationPanel,
        PopupHeader,
        PopupFooter,
        ActivityPopup,
    },
    data() {
        return {
            isCreating: false,
            isJoining: false,
        };
    },
    computed: {
        mode() {
            return {
                isJoining: this.isJoining,
                isCreating: this.isCreating,
            };
        },
        async isCreator() {
            const browserStorage = await browser.storage.local.get('isCreator');
            return browserStorage.isCreator;
        },
        async sessionCode() {
            const browserStorage = await browser.storage.local.get('sessionCode');
            return browserStorage.sessionCode;
        },
        isJustUser(){
            if(this.sessionCode === undefined) return false
            if(this.isCreator === undefined) return false
            return !this.isCreator && this.sessionCode.length > 0;
        },
        isPrompted() {
            return false;
            // console.log(window.location.href);
            // return true;
            // let result = window.location.href.split('?')[1];
            // return result.length > 0;
        },
    },
    methods: {
        enterCreationMode() {
            this.isJoining = false;
            this.isCreating = true;
        },
        enterJoiningMode() {
            this.isCreating = false;
            this.isJoining = true;
        },
        resetMode() {
            this.isCreating = false;
            this.isJoining = false;
        },
    },
};
</script>

<style scoped>
aside {
    min-width: 400px;
    max-width: 500px;
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
