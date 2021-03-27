<template>
  <div class="main_app">
    <h1>Hello popup</h1>
    <baton />
    <two />
  </div>
</template>

<script lang="ts">
import baton from "./baton.vue";
import Two from "./two.vue";

export default {
  name: "app",
  components: { baton, Two },
};
</script>

<style>
.main_app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
