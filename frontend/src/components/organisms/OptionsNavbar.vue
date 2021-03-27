<template>
    <Menubar :model="items" />
</template>

<script>
    import Menubar from 'primevue/menubar';
    export default {
        name: "OptionsNavbar",
        components : {
            Menubar
        },
        data(){
            return {
                items: [
                    {
                        label: 'Ask question',
                        icon: 'pi pi-question-circle',
                        command: () => {
                            this.$emit("asking-question", prompt("Zadaj pytanie uczniom:"));
                        }
                    },
                    {
                        label: 'Activity log',
                        icon: 'pi pi-list',
                        command: () => {
                            this.requestSceneChange("ActivityLog");
                        }
                    },
                    {
                        label: 'Questions log',
                        icon: 'pi pi-comments',
                        command: () => {
                            this.requestSceneChange("QuestionsLog");
                        }
                    },
                    {
                        label: 'Members list',
                        icon: 'pi pi-users',
                        command: () => {
                            this.requestSceneChange("MembersList");
                        }
                    },
                    {
                        label: 'Terminate session',
                        icon: 'pi pi-fw pi-power-off',
                        command: () => {
                            this.requestSceneChange("TerminatedView");
                        }
                    }
                ]
            }
        },
        methods: {
            requestSceneChange(name){
                this.$emit("selected", name);
            }
        }
    }
</script>

<style scoped>

</style>
