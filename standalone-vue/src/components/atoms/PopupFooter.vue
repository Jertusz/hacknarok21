<template>
    <footer>
        <hr />
        <p>Napotkałeś problem? <a href="mailto:s17839@pjwstk.edu.pl">Skontaktuj się</a> z nami!</p>
    </footer>
</template>

<script>
    export default {
        name: "PopupFooter"
    }
</script>

<style scoped>
footer {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 100%;
}
hr {
    width: 80%;
}
p {
    font-size: 18px;
}
a {
    text-decoration: none;
    color: cornflowerblue;
}
</style>
