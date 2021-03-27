import Vue from "vue";
import AppComponent from "./App/App.vue";
import PrimeVue from 'primevue/config';


Vue.use(PrimeVue);

import "primevue/resources/themes/saga-blue/theme.css";       //theme
import "primevue/resources/primevue.min.css";                 //core css
import "primeicons/primeicons.css"; 

new Vue({
  el: "#app",
  render: (createElement) => {
    return createElement(AppComponent);
  },
});
