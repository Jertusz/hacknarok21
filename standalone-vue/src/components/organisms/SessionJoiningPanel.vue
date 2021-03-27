<template>
    <div class="col">
        <join-session-button @click="startJoining" v-if="!mode.isCreating && !mode.isJoining" />
        <form class="row" v-if="mode.isJoining">
            <InputText v-model="name" />
            <InputText v-model="token" />
        </form>
        <footer v-if="mode.isJoining">
            <hr />
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
    .row {
        justify-content: space-between;
    }
    .col {
        flex-direction: column;
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
