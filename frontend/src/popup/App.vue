<template>
    <div>
        <one />
    </div>
</template>

<script lang="ts">
import Vue from 'vue';
import one from '@/components/one.vue';

export default Vue.extend({
    name: 'App',
    components: { one },
});
</script>

<style>
html {
    width: 400px;
    height: 400px;
}
</style>
