<template>
    <div id="app">
        <Popup />
    </div>
</template>

<script>
import Popup from '../components/pages/Popup.vue';

export default {
    components: {
        Popup,
    }
};
</script>

<style>
#app {
    min-width: 400px;
}
</style>
