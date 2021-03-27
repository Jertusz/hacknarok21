<template>
<div>
    <OptionsNavbar @selected="changeScene" @asking-question="pushQuestion" :session-code="code"/>
    <component :is="scene" :questions="questions" :events="events"/>
    <Dialog header="Header" :visible.sync="currentlyAsking" :style="{width: '35vw'}" :modal="true">
        <InputText v-model="question" placeholder="Enter your question..." class="m-1 w-80"/>
        <template #footer>
            <Button label="Cancel" icon="pi pi-times"  @click="cancelQuestion" class="p-button-text"/>
            <Button label="Confirm" icon="pi pi-check" @click="submitQuestion" autofocus />
        </template>
    </Dialog>
</div>
</template>
<script lang="js">
    import OptionsNavbar from "@/components/organisms/OptionsNavbar";
    import TerminatedView from "@/components/organisms/OptionsScenes/TerminatedView";
    import QuestionsLog from "@/components/organisms/OptionsScenes/QuestionsLog";
    import ActivityLog from "@/components/organisms/OptionsScenes/ActivityLog";
    import MembersList from "@/components/organisms/OptionsScenes/MembersList";
    import Dialog from 'primevue/dialog';
    import InputText from "primevue/inputtext";
    import Button from "primevue/button";

    const events = [
        {
            type: true,
            person: "Benedykt K.",
            text: 'zmienił(a) okno.',
            date: '15/10/2020 10:30',
            icon: 'pi pi-shopping-cart',
            color: '#9C27B0'
        },
        {
            person: "Jędrzej S.",
            text: 'opuścił(a) sesję.',
            date: '15/10/2020 14:00',
            icon: 'pi pi-cog',
            color: '#673AB7'
        },
        { person: "Paweł P.", text: 'zmienił(a) kartę.', date: '15/10/2020 16:15', icon: 'pi pi-shopping-cart', color: '#FF9800'},
        { person: "", text: 'Zadano pytanie', date: '16/10/2020 10:00', icon: 'pi pi-check', color: '#607D8B'},
        { person: "Benedykt K.", text: 'nie wykazał aktywności.', date: '15/10/2020 10:30', icon: 'pi pi-shopping-cart', color: '#9C27B0'
        },
        { person: "Jędrzej S.", text: 'dołączył(a) do sesji.', date: '15/10/2020 14:00', icon: 'pi pi-cog', color: '#673AB7'},
        { person: "Filip D.", text: 'nie rusza myszką.', date: '16/10/2020 10:00', icon: 'pi pi-check', color: '#607D8B'}
    ];

    export default {
        name: "Options",
        components: {
            OptionsNavbar,
            TerminatedView,
            QuestionsLog,
            ActivityLog,
            MembersList,
            Dialog,
            InputText,
            Button
        },
        data(){
            return {
                scene: "activity-log",
                currentlyAsking: false,
                question: "",
                code: "",
                questions: [],
                events
            }
        },
        methods: {
            pushQuestion(){
                this.currentlyAsking = true;
            },
            changeScene(scene){
                // Possible values:
                // - "activity-log"
                // - "questions-log"
                // - "members-list"
                // - "terminated-view"
                this.scene = scene;
            },
            submitQuestion(){
                this.questions.push(this.question);
                this.currentlyAsking = false;
                this.question = "";
            },
            cancelQuestion(){
                this.currentlyAsking = false;
                this.question = "";
            }
        },
        async mounted() {
            const browserStorage = await browser.storage.local.get('sessionCode');
            this.code = browserStorage.sessionCode;
        }
    }
</script>

<style scoped>

</style>
