<template>
    <div class="flex flex-col items-center justify-center">
        <SelectButton v-model="filterType" :options="filterTypes" optionLabel="label" optionValue="value" />
        <Timeline :value="eventsIn" align="right" class="customized-timeline mt-6">
            <template #opposite="slotProps">
                <p class="text-opacity-25">{{ slotProps.item.date }}</p>
            </template>
            <template #marker="slotProps">
                <span class="custom-marker p-shadow-2" :style="{backgroundColor: slotProps.item.color}">
                    <i :class="slotProps.item.icon"></i>
                </span>
            </template>
            <template #content="slotProps">
                <p>
                    <span class="font-bold">{{ slotProps.item.person }}</span>
                    {{ slotProps.item.text }}
                </p>
            </template>
        </Timeline>
    </div>
</template>

<script>
    import Timeline from "primevue/timeline";
    import SelectButton from 'primevue/selectbutton';
    import {ALL_EVENTS, GENERIC_EVENTS} from "@/background/EventTypes";

    export default {
        name: "ActivityLog",
        props: [ "events" ],
        data(){
            return {
                filterType: "logDefault",
                filterTypes: [
                    {
                        value: "logDefault",
                        label: "Domyślne filtrowanie"
                    },
                    {
                        value: "logAll",
                        label: "Wszystkie akcje"
                    },
                    {
                        value: "logNegatives",
                        label: "Tylko akcje negatywne"
                    }
                ],
                eventsIn: []
            }
        },
        watch: {
            filterType(){
                this.filterFn();
            }
        },
        methods: {
            filterFn(){
                if(this.filterType === "logDefault") this.eventsIn = this.events.slice().filter((i)=>{
                    if(i.type === ALL_EVENTS.QUESTION_TIMEOUT) return true;
                    if(i.type === GENERIC_EVENTS.MOUSE_INACTIVE) return true;
                    if(i.type === GENERIC_EVENTS.TAB_SWITCHED) return true;
                    if(i.type === GENERIC_EVENTS.WINDOW_SWITCHED) return true;
                    if(i.type === GENERIC_EVENTS.LEFT_SESSION) return true;
                    if(i.type === GENERIC_EVENTS.JOINED_SESSION) return true;
                    if(i.type === ALL_EVENTS.TEACHER_QUESTION_APPEARS) return true;
                    return false;
                });
                if(this.filterType === "logAll") this.eventsIn = this.events.slice();
                if(this.filterType === "logNegatives") this.eventsIn = this.events.slice().filter((i)=>{
                    if(i.type === ALL_EVENTS.QUESTION_TIMEOUT) return true;
                    if(i.type === GENERIC_EVENTS.MOUSE_INACTIVE) return true;
                    if(i.type === GENERIC_EVENTS.TAB_SWITCHED) return true;
                    if(i.type === GENERIC_EVENTS.WINDOW_SWITCHED) return true;
                    if(i.type === GENERIC_EVENTS.LEFT_SESSION) return true;
                    return false;
                });
            }
        },
        components: {
            Timeline,
            SelectButton
        },
        mounted() {
            this.filterFn();
        }
    }
</script>

<style lang="scss" scoped>
    .custom-marker {
        display: flex;
        width: 2rem;
        height: 2rem;
        align-items: center;
        justify-content: center;
        color: #ffffff;
        border-radius: 50%;
        z-index: 1;
    }

    ::v-deep(.p-timeline-event-content) ::v-deep(.p-timeline-event-opposite) {
        line-height: 1;
    }

        @media screen and (max-width: 960px) {
            ::v-deep(.customized-timeline) {

            .p-timeline-event:nth-child(even) {
                flex-direction: row !important;

            .p-timeline-event-content {
                text-align: left !important;
                padding: 0 .3rem !important;
            }
        }

        .p-timeline-event-opposite {
            flex: 0;
        }

        .p-card {
            margin-top: 1rem;
        }

        }
    }
</style>
