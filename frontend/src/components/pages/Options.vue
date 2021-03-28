<template>
<div>
    <OptionsNavbar @selected="changeScene" />
<!--    <component :is="scene" />-->
</div>
</template>

<script>
    import OptionsNavbar from "@/components/organisms/OptionsNavbar";
    export default {
        name: "Options",
        components: {OptionsNavbar},
        data(){
            return {
                scene: "activity-log"
            }
        },
        methods: {
            changeScene(scene){
                // Possible values:
                // - "asking-question"
                // - "activity-log"
                // - "questions-log"
                // - "members-list"
                // - "terminated"
                this.scene = scene;
            }
        }
    }
</script>

<style scoped>

</style>
