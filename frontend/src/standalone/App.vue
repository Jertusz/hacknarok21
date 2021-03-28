<template>
    <activityPopup />
</template>

<script lang="ts">
import Vue from 'vue';
import activityPopup from '@/components/atoms/InitPopup/activityPopup.vue';

export default Vue.extend({
    name: 'App',
    components: { activityPopup },
});
</script>
