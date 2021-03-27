import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Options from "../components/pages/Options.vue";
import Popup from "../components/pages/Popup.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    redirect: "/options"
  },
  {
    path: "/options",
    name: "Options",
    component: Options,
  },
  {
    path: "/popup",
    name: "Popup",
    component: Popup,
  }
];

const router = new VueRouter({
  routes,
});

export default router;
