import { createApp } from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import Vuex from "vuex";
import { createStore } from "vuex";
import axios from "axios";

const store = createStore({
  state() {
    return {
      count: 0,
      song_to_check: "sdsd",
      update: 0,
      picked_tag: "华语",
      currentsong_url:
        "https://music.163.com/song/media/outer/url?id=562598065.mp3",
      currentsong_ID: 0,
      songlist: [],
      search_res: "",
    };
  },
  mutations: {
    increment(state) {
      state.count++;
    },
    changesong(state, data1) {
      state.song_to_check = data1;
    },

    changetag(state, data1) {
      state.picked_tag = data1;
    },
    changesong_ID(state, data1) {
      state.currentsong_ID = data1;
    },
    search(state, data1) {
      state.search_res = data1;
      console.log(state.search_res);
    },
  },
});
const app = createApp(App)
  .use(Vuex)
  .use(ElementPlus)
  .use(router)
  .use(store);
app.config.globalProperties.$axios = axios;
app.mount("#app");
