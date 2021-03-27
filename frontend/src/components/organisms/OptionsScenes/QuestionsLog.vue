<template>
<div class="flex justify-center">
    <Accordion :multiple="true">
        <AccordionTab v-for="q of questions" :header="q.title">
            <p></p>
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
