<template>
<div>
    <OptionsNavbar
        @selected="changeScene"
        @asking-question="pushQuestion"
        @show-users-list="usersList = true"
        v-if="scene !== 'TerminatedView'"
        :session-code="code"
    />

    <div class="mt-12">
        <component :is="scene" :questions="questions" :events="events" :users="users" />
    </div>

    <Dialog :visible.sync="currentlyAsking" :style="{ width: '35vw' }" :modal="true" :closable="false">
        <InputText v-model="question" placeholder="Enter your question..." class="p-inputtext-lg m-1 w-4/5" />
        <template #footer>
            <Button label="Cancel" icon="pi pi-times"  @click="cancelQuestion" class="p-button-text"/>
            <Button label="Confirm" icon="pi pi-check" @click="submitQuestion" autofocus />
        </template>
    </Dialog>

    <Sidebar :visible.sync="usersList" position="right" :showCloseIcon="false" @hide="usersList = false">
        <ul v-for="user of users">
            <li class="flex items-center p-3">
                <Avatar :label="user.charAt(0).toUpperCase()" class="mr-2" />
                <p>{{ user }}</p>
            </li>
        </ul>
    </Sidebar>

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
    import Sidebar from 'primevue/sidebar';
    import Avatar from 'primevue/avatar';
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
            type: GENERIC_EVENTS.RETURNED_TAB,
            person: "Paweł P.",
            text: 'powrócił na kartę.',
            date: '15/10/2020 16:15',
            icon: 'pi pi-replay',
            color: '#289417'
        },
        {
            type: ALL_EVENTS.TEACHER_QUESTION_APPEARS,
            person: "Zadano pytanie",
            text: '',
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
            type: ALL_EVENTS.ANSWER_RANDOM_QUESTION,
            person: "Filip D.",
            text: 'wykazał aktywności.',
            date: '15/10/2020 10:30',
            icon: 'pi pi-check',
            color: '#289417'
        },
        {
            type: ALL_EVENTS.ANSWER_TEACHERS_QUESTION,
            person: "Filip D.",
            text: 'Odpowiedział na pytanie',
            date: '16/10/2020 10:00',
            icon: 'pi pi-check',
            color: '#289417'
        }
    ];
    const questions = [
        {
            title: "What is the purpose of life?",
            answers: [
                { person: "Benedykt K.", answer: "retro 1:1 czemu gify nie działają", time: "15/10/2020 10:30" },
                { person: "Jędrzej S.", answer: "python.serializers", time: "15/10/2020 10:30"  },
                { person: "Paweł P.", answer: "Big endian", time: "15/10/2020 10:30"  },
            ]
        },
        {
            title: "What is the purpose of life 2?",
            answers: [
                { person: "Jędrzej S.", answer: "python.models", time: "15/10/2020 10:30"  },
                { person: "Benedykt K.", answer: "retro 2:2 czemu gify nie działają", time: "15/10/2020 10:30"  },
                { person: "Paweł P.", answer: "Little endian", time: "15/10/2020 10:30"  },
            ]
        }
    ];
    const users = [
        "Benedykt K.",
        "Filip D.",
        "Paweł P.",
        "Jędrzej Sz.",
        "Paweł B."
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
            Sidebar,
            Avatar,
            Button
        },
        data(){
            return {
                scene: "activity-log",
                currentlyAsking: false,
                usersList: false,
                question: "",
                code: "",
                questions,
                events,
                users
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
                this.questions.push(
                    {
                        title: this.question,
                        answers: []
                    }
                );
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
/deep/ .p-dialog-content {
    display: flex;
    justify-content: center;
}
</style>
