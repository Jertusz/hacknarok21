<template>
<div>
    <OptionsNavbar @selected="changeScene" @asking-question="pushQuestion"/>
    <component :is="scene" :questions="questions" />
</div>
</template>

<script>
    import OptionsNavbar from "@/components/organisms/OptionsNavbar";
    import TerminatedView from "@/components/organisms/OptionsScenes/TerminatedView";
    import QuestionsLog from "@/components/organisms/OptionsScenes/QuestionsLog";
    import ActivityLog from "@/components/organisms/OptionsScenes/ActivityLog";
    import MembersList from "@/components/organisms/OptionsScenes/MembersList";

    export default {
        name: "Options",
        components: {
            OptionsNavbar,
            TerminatedView,
            QuestionsLog,
            ActivityLog,
            MembersList
        },
        data(){
            return {
                scene: "activity-log",
                questions: []
            }
        },
        methods: {
            pushQuestion(question){
                this.questions.push(question);
            },
            changeScene(scene){
                // Possible values:
                // - "activity-log"
                // - "questions-log"
                // - "members-list"
                // - "terminated-view"
                this.scene = scene;
            }
        }
    }
</script>

<style scoped>

</style>
