<template>
<div>
    <OptionsNavbar @selected="changeScene" @asking-question="pushQuestion" :session-code="code"/>

    <div class="mt-12">
        <component :is="scene" :questions="questions" :events="events"/>
    </div>

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
    import {ALL_EVENTS, GENERIC_EVENTS} from "@/background/EventTypes";

    const events = [
        {
            type: GENERIC_EVENTS.WINDOW_SWITCHED,
            person: "Benedykt K.",
            text: 'zmienił(a) okno.',
            date: '15/10/2020 10:30',
            icon: 'pi pi-window-minimize',
            color: '#FF9800'
        },
        {
            type: GENERIC_EVENTS.LEFT_SESSION,
            person: "Jędrzej S.",
            text: 'opuścił(a) sesję.',
            date: '15/10/2020 14:00',
            icon: 'pi pi-user-minus',
            color: '#ae1818'
        },
        {
            type: GENERIC_EVENTS.TAB_SWITCHED,
            person: "Paweł P.",
            text: 'zmienił(a) kartę.',
            date: '15/10/2020 16:15',
            icon: 'pi pi-external-link',
            color: '#FF9800'
        },
        {
            type: ALL_EVENTS.TEACHER_QUESTION_APPEARS,
            person: "",
            text: 'Zadano pytanie',
            date: '16/10/2020 10:00',
            icon: 'pi pi-question-circle',
            color: '#2d62b8'
        },
        {
            type: ALL_EVENTS.QUESTION_TIMEOUT,
            person: "Benedykt K.",
            text: 'nie wykazał aktywności.',
            date: '15/10/2020 10:30',
            icon: 'pi pi-clock',
            color: '#ae1818'
        },
        {
            type: GENERIC_EVENTS.JOINED_SESSION,
            person: "Jędrzej S.",
            text: 'dołączył(a) do sesji.',
            date: '15/10/2020 14:00',
            icon: 'pi pi-user-plus',
            color: '#289417'
        },
        {
            type: GENERIC_EVENTS.MOUSE_INACTIVE,
            person: "Filip D.",
            text: 'nie rusza myszką.',
            date: '16/10/2020 10:00',
            icon: 'pi pi-pause',
            color: '#FF9800'
        },
        {
            type: "du",
            person: "Filip D.",
            text: 'nie rusza myszką. 2',
            date: '16/10/2020 10:00',
            icon: 'pi pi-pause',
            color: '#FF9800'
        }
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
