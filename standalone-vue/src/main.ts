import Vue from "vue";
import App from "./App.vue";
import store from "./store";

import PrimeVue from 'primevue/config';

Vue.use(PrimeVue);

import "primevue/resources/themes/saga-blue/theme.css";       //theme
import "primevue/resources/primevue.min.css";                 //core css
import "primeicons/primeicons.css";                           //icons

new Vue({
  store,
  render: (h) => h(App),
}).$mount("#app");
