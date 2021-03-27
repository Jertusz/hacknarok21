<template>
    <header>
        <h1>
            Insightful
        </h1>
        <hr />
    </header>
</template>

<script>
    export default {
        name: "Heading"
    }
</script>

<style scoped>
    header {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    h1 {
        font-size: 14px;
        color: #434343;
    }
    hr {
        width: 80%;
    }
</style>
