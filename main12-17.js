import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import  ElementPlus from "element-plus"
import 'element-plus/dist/index.css'
import Vuex from 'vuex'
import { createStore } from 'vuex'
const store = createStore({
  
    namespaced: true,
    state () {
      return {
        count: 0,
        song_to_check:"sdsd",
        update : 0,
        picked_tag: "00",
        
      }
    },
    mutations: {
      increment (state) {
        state.count++
      },
      changesong(state,data1){
        state.song_to_check = data1
      },
      changetag(state,data1){
        state.picked_tag = data1
      }
    }
  })
const app=createApp(App).use(Vuex).use(ElementPlus).use(router).use(store).mount('#app')
app.config.globalProperties.$axios=axios
app.mount('#app')





