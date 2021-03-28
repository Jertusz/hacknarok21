<template>
    <div class="flex flex-col w-full justify-center items-center">
        <join-session-button @click="startJoining" v-if="!mode.isCreating && !mode.isJoining" />
        <form v-if="mode.isJoining" @submit.prevent>
            <InputText v-model="name" placeholder="Your name..." class="m-1 w-full"/>
            <InputText v-model="token" placeholder="Session token..." class="m-1 w-full"/>
        </form>
        <footer class="w-3/4" v-if="mode.isJoining">
            <hr class="w-full my-1" />
            <div class="w-full flex items-between justify-between">
                <back-home-button @click="stopJoining" />
                <confirm-join-button @click="handleSubmition" />
            </div>
        </footer>
    </div>
</template>

<script>
    import BackHomeButton from "../../atoms/InitPopup/BackHomeButton";
    import InputText from "primevue/inputtext";
    import JoinSessionButton from "@/components/atoms/InitPopup/JoinSessionButton";
    import ConfirmJoinButton from "@/components/atoms/InitPopup/ConfirmJoinButton";
import Communicator from '@/background/Communicator';
import { ALL_EVENTS } from '@/background/EventTypes';

    export default {
        name: "SessionJoiningPanel",
        components: {
            ConfirmJoinButton,
            JoinSessionButton,
            BackHomeButton,
            InputText
        },
        props: {
            mode: {
                type: Object,
                required: true
            }
        },
        data(){
            return {
                name: "",
                token: ""
            }
        },
        methods: {
            startJoining(){
                this.$emit("start-joining");
            },
            stopJoining(){
                this.$emit("back");
            },
            handleSubmition(){
                Communicator.connect(`ws://127.0.0.1:8000/ws/sessions/${this.token}/${this.name}/False/`)
                browser.storage.local.set({
                    isCreator: false,
                    sessionCode: this.token
                }).then(_ => {
                    // alert("Subscribed!");
                });
            }
        }
    }
</script>

<style scoped>
    form {
        @apply w-11/12 flex flex-col justify-center items-center;
    }
</style>
