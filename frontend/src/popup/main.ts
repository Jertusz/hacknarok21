import Vue from "vue";
import App from "./App.vue";

import PrimeVue from 'primevue/config';

Vue.use(PrimeVue);

import "primevue/resources/themes/saga-blue/theme.css";       //theme
import "primevue/resources/primevue.min.css";                 //core css
import "primeicons/primeicons.css";          

/* eslint-disable no-new */
new Vue({
  el: "#app",
  render: (h) => h(App),
});
