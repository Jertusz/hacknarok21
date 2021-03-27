<template>
    <header>
        <h1>Insightful</h1>
        <hr />
    </header>
</template>

<script>
    export default {
        name: "PopupHeader"
    }
</script>

<style scoped>
header {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
h1 {
    font-size: 16px;
}
hr {
    width: 80%;
}
</style>
