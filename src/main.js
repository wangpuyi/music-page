import { createApp } from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import Vuex from "vuex";
import { createStore } from "vuex";
import axios from "axios";

//icon
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

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

      //12-25 Sou-suojiemian的SongsData改为全局变量
      SongsData: [
        {
          listid: "2626492658",
          name: "粤语情歌世界最深情的歌V",
          image: "",
        },
      ],
      show1: 1,
      show2: 0,
      show3: 0,
      pt: 0,

      gedanneibu_label: "",
      gedanneibu_name: "",
      gedanneibu_author: "",
      //const payload = {'ids':res.data.ids}
      gedanneibu_SongsData: [],
      gedanneibu_views: "",
      gedanneibu_des: "",
      gedanneibu_url: "https://tupian.qqw21.com/article/UploadPic/2020-4/20204717444472684.jpg",

      Same_gedan: false,
    };
  },
  mutations: {
    Leave_gedan(state) {
      state.Same_gedan = false;

      state.gedanneibu_label = "";
      state.gedanneibu_name = "";
      state.gedanneibu_author = "";

      state.gedanneibu_SongsData = [];
      state.gedanneibu_views = "";
      state.gedanneibu_des = "";
      state.gedanneibu_url = "";
      state.gedanneibu_id = "";
    },
    Same_gedan(state) {
      state.Same_gedan = true;
    },
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
    Ge_danneibu_cache(state, data) {
      state.gedanneibu_label = data.label;
      state.gedanneibu_name = data.name;
      state.gedanneibu_author = data.author;
      state.gedanneibu_SongsData = data.SongsData;
      state.gedanneibu_views = data.views;
      state.gedanneibu_des = data.des;
      state.gedanneibu_url = data.url;
      state.gedanneibu_id = data.id;
    },
  },
});
const app = createApp(App).use(Vuex).use(ElementPlus).use(router).use(store);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
app.config.globalProperties.$axios = axios;
app.mount("#app");
