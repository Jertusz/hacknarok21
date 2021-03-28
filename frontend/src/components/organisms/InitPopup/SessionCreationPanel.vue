<template>
    <div class="col w-full">
        <create-session-button @click="startCreation" v-if="!mode.isCreating && !mode.isJoining" />
        <div class="col w-full">
            <create-quick-session-button @clicked="createQuickSession" v-if="mode.isCreating" />
            <create-supervision-session-button @clicked="createSupervisionSession" v-if="mode.isCreating" />
        </div>
        <footer v-if="mode.isCreating">
            <hr class="my-1" />
            <back-home-button @click="stopCreation" />
        </footer>
    </div>
</template>

<script>
    import CreateQuickSessionButton from "../../atoms/InitPopup/CreateQuickSessionButton";
    import CreateSupervisionSessionButton from "../../atoms/InitPopup/CreateSupervisionSessionButton";
    import CreateSessionButton from "../../atoms/InitPopup/CreateSessionButton";
    import BackHomeButton from "../../atoms/InitPopup/BackHomeButton";
    import Connector from '@/background/Communicator'

    const generateCode = () => {
        const availableCharacters = "ABCDEFGHIJKLMNOPQRSTVUWXYZabcdefghijklmnopqrstuvxyz123456789";
        let result = "";
        function getRandomInt(min, max) {
            min = Math.ceil(min);
            max = Math.floor(max);
            return Math.floor(Math.random() * (max - min)) + min;
        }
        for(let i = 0; i < 12; i++){
            result += availableCharacters[getRandomInt(0, availableCharacters.length)];
        }
        return result;
    }

    export default {
        name: "SessionCreationPanel",
        components: {
            BackHomeButton,
            CreateSessionButton,
            CreateSupervisionSessionButton,
            CreateQuickSessionButton
        },
        props: {
            mode: {
                type: Object,
                required: true
            }
        },
        methods: {
            startCreation(){
                this.$emit("start-creation");
            },
            stopCreation(){
                this.$emit("back");
            },
            createQuickSession(){
                const newCode = generateCode();
                Connector.connect(`ws://127.0.0.1:8000/ws/sessions/${newCode}/ADMIN/True/`)
                browser.storage.local.set({
                    isCreator: true,
                    sessionCode: newCode
                }).then(_ => {
                    window.open("options.html");
                });
            },
            createSupervisionSession(){
                const newCode = generateCode();
                Connector.connect(`ws://127.0.0.1:8000/ws/sessions/${newCode}/ADMIN/True/`)
                browser.storage.local.set({
                    isCreator: true,
                    sessionCode: newCode
                }).then(_ => {
                    window.open("options.html");
                });
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
