<template>
    <Menubar :model="items">
        <template #end>
            <div class="flex items-center">
                <p class="heartbeat inline-flex justify-center items-center font-bold text-red-800 mr-4" v-show="showTip">COPY and SHARE token with your students<i class="ml-2 pi pi-angle-double-right"></i> </p>
                <p class="text-xl mr-2">Session token: <b @click="copyCode" v-tooltip.bottom="'Copy to clipboard'" class="cursor-pointer hover:text-blue-600">{{ sessionCode }}</b></p>
            </div>
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
                showTip: true,
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
                            this.$emit("show-users-list");
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
            },
            copyCode(){
                let dummy = document.createElement("textarea");
                document.body.appendChild(dummy);
                dummy.value = this.sessionCode;
                dummy.select();
                document.execCommand("copy");
                document.body.removeChild(dummy);
            }
        },
        mounted() {
            setTimeout(()=>{
                this.showTip = false;
            }, 12000);
        }
    }
</script>

<style scoped>
    /* ----------------------------------------------
     * Generated by Animista on 2021-3-28 3:32:43
     * Licensed under FreeBSD License.
     * See http://animista.net/license for more info.
     * w: http://animista.net, t: @cssanimista
     * ---------------------------------------------- */

    /**
     * ----------------------------------------
     * animation heartbeat
     * ----------------------------------------
     */
    @-webkit-keyframes heartbeat {
        from {
            -webkit-transform: scale(1);
            transform: scale(1);
            -webkit-transform-origin: center center;
            transform-origin: center center;
            -webkit-animation-timing-function: ease-out;
            animation-timing-function: ease-out;
        }
        10% {
            -webkit-transform: scale(0.91);
            transform: scale(0.91);
            -webkit-animation-timing-function: ease-in;
            animation-timing-function: ease-in;
        }
        17% {
            -webkit-transform: scale(0.98);
            transform: scale(0.98);
            -webkit-animation-timing-function: ease-out;
            animation-timing-function: ease-out;
        }
        33% {
            -webkit-transform: scale(0.87);
            transform: scale(0.87);
            -webkit-animation-timing-function: ease-in;
            animation-timing-function: ease-in;
        }
        45% {
            -webkit-transform: scale(1);
            transform: scale(1);
            -webkit-animation-timing-function: ease-out;
            animation-timing-function: ease-out;
        }
    }
    @keyframes heartbeat {
        from {
            -webkit-transform: scale(1);
            transform: scale(1);
            -webkit-transform-origin: center center;
            transform-origin: center center;
            -webkit-animation-timing-function: ease-out;
            animation-timing-function: ease-out;
        }
        10% {
            -webkit-transform: scale(0.91);
            transform: scale(0.91);
            -webkit-animation-timing-function: ease-in;
            animation-timing-function: ease-in;
        }
        17% {
            -webkit-transform: scale(0.98);
            transform: scale(0.98);
            -webkit-animation-timing-function: ease-out;
            animation-timing-function: ease-out;
        }
        33% {
            -webkit-transform: scale(0.87);
            transform: scale(0.87);
            -webkit-animation-timing-function: ease-in;
            animation-timing-function: ease-in;
        }
        45% {
            -webkit-transform: scale(1);
            transform: scale(1);
            -webkit-animation-timing-function: ease-out;
            animation-timing-function: ease-out;
        }
    }
    .heartbeat {
        -webkit-animation: heartbeat 1s ease-in-out infinite both;
        animation: heartbeat 1s ease-in-out infinite both;
    }

/deep/ .green-option a .p-menuitem-text{
color: #065F46 !important;
}
/deep/ .red-option a .p-menuitem-text{
    color: #7F1D1D !important;
}
</style>
