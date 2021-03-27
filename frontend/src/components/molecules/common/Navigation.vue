<template>
    <nav>
        <router-link to="/">Index</router-link> |
        <router-link to="/plugins">Plugins</router-link>
    </nav>
</template>

<script>
export default {
    name: "Navigation"
}
</script>

<style scoped>
    a {
        text-decoration: none;
        text-transform: uppercase;
        font-weight: bold;
    }
</style>
