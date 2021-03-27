<template>
<ul>
    <li v-for="q of questions">
        "{{ q }}"
        <ul>
            <li>BenK: "Ksiadz gąsiennica"</li>
            <li>JanekKowalski: "HelloWorld"</li>
        </ul>
    </li>
</ul>
</template>

<script>
    export default {
        name: "QuestionsLog",
        props: [ "questions" ]
    }
</script>

<style scoped>

</style>
