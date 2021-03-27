<template>
<div>
  <one/>
  <two/>
</div>
</template>

<script lang="ts">
import Vue from "vue";
import one from "@/components/one.vue";
import two from "@/components/two.vue";

export default Vue.extend({
  name: "App",
  components: { one, two },
});
</script>

<style>
html {
  width: 400px;
  height: 400px;
}
</style>
