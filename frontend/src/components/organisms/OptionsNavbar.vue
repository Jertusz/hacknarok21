<template>
    <Menubar :model="items">
        <template #end>
            <p class="text-xl">Session token: <b>{{ sessionCode }}</b></p>
        </template>
    </Menubar>
</template>

<script>
    import Menubar from 'primevue/menubar';
    export default {
        name: "OptionsNavbar",
        props: ["sessionCode"],
        components : {
            Menubar
        },
        data(){
            return {
                code: "",
                items: [
                    {
                        label: 'Ask question',
                        icon: 'pi pi-question-circle',
                        command: () => {
                            // const promptEvent = prompt("Zadaj pytanie uczniom:");
                            this.$emit("asking-question");
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
