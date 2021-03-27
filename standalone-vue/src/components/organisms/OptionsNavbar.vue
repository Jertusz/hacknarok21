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
                        label:'Ask question',
                        icon:'pi pi-question-circle',
                        command: () => {
                            this.emitEvent("asking-question");
                        }
                    },
                    {
                        label:'Activity log',
                        icon:'pi pi-list',
                        command: () => {
                            this.emitEvent("activity-log");
                        }
                    },
                    {
                        label:'Questions log',
                        icon:'pi pi-comments',
                        command: () => {
                            this.emitEvent("questions-log");
                        }
                    },
                    {
                        label:'Members list',
                        icon:'pi pi-users',
                        command: () => {
                            this.emitEvent("members-list");
                        }
                    },
                    {
                        label:'Terminate session',
                        icon:'pi pi-fw pi-power-off',
                        command: () => {
                            this.emitEvent("terminated");
                        }
                    }
                ]
            }
        },
        methods: {
            emitEvent(name){
                this.$emit("selected", name);
            }
        }
    }
</script>

<style scoped>

</style>
