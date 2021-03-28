<template>
<div class="flex flex-col justify-center items-center">
    <h1 class="text-xl">Questions asked by teacher in this session:</h1>
    <hr class="w-80 my-2" />
    <Accordion :multiple="true" class="w-1/2">
        <AccordionTab v-for="q of questions" :header="q.title">
            <p v-if="q.answers.length === 0" class="text-opacity-25 text-xl">Brak odpowiedzi</p>
            <ul class="list-disc" v-if="q.answers.length > 0">
                <li class="my-1 py-1 flex justify-between items-center" v-for="a of q.answers">
                    <div>
                        <b>{{ a.person }}</b>: "{{ a.answer}}"
                    </div>
                    <div class="text-opacity-25">
                        {{ a.time }}
                    </div>
                </li>
            </ul>
        </AccordionTab>
    </Accordion>
</div>
</template>

<script>
    import Accordion from 'primevue/accordion';
    import AccordionTab from 'primevue/accordiontab';

    export default {
        name: "QuestionsLog",
        props: [ "questions" ],
        components: {
            Accordion,
            AccordionTab
        }
    }
</script>

<style scoped>

</style>
