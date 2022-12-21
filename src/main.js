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
      songlist: [
        {
          title: "666",
          singer: "2020111601",
          album: "英语专业",
          class: "1班级",
          tableOption: [
            { score: "86" },
            { score: "91" },
            { score: "92" },
            { score: "89" },
            { score: "80" },
            { score: "94" },
          ],
          schoolYear: "2020~20121学年第一学期",
          currentsong_ID: 0,
        },
        {
          title: "88",
          singer: "2020111602",
          album: "英语专业",
          class: "1班级",
          tableOption: [
            { score: "91" },
            { score: "92" },
            { score: "86" },
            { score: "93" },
            { score: "89" },
            { score: "92" },
          ],
          schoolYear: "2020~20121学年第一学期",
          currentsong_ID: 2,
        },
      ],
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
  },
});
const app = createApp(App)
  .use(Vuex)
  .use(ElementPlus)
  .use(router)
  .use(store);
app.config.globalProperties.$axios = axios;
app.mount("#app");
