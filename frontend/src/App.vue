<template>
  <div class="container mt-5">

    <navigation />

    <hr/>

    <main>
      <router-view />
    </main>

  </div>
</template>
<script>
import Navigation from "@/components/molecules/common/Navigation";

export default {
    name: "AppRoot",
    components: { Navigation }
}
</script>
