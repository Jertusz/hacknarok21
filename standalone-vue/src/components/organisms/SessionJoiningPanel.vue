<template>
    <div class="flex-col w-full">
        <join-session-button @click="startJoining" v-if="!mode.isCreating && !mode.isJoining" />
        <form class="flex flex-col w-full" v-if="mode.isJoining">
            <InputText v-model="name" placeholder="Your name..." class="m-1 w-full"/>
            <InputText v-model="token" placeholder="Session token..." class="m-1 w-full"/>
        </form>
        <footer v-if="mode.isJoining">
            <hr class="my-1" />
            <back-home-button @click="stopJoining" />
        </footer>
    </div>
</template>

<script>
    import BackHomeButton from "../atoms/BackHomeButton";
    import InputText from "primevue/inputtext";
    import JoinSessionButton from "@/components/atoms/JoinSessionButton";

    export default {
        name: "SessionJoiningPanel",
        components: {
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
            }
        }
    }
</script>

<style scoped>
    div {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    hr {
        width: 80%;
    }
    footer {
        display: flex;
        width: 75%;
        justify-content: center;
        flex-direction: column;
        align-items: center;
    }
</style>
