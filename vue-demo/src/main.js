import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import  ElementPlus from "element-plus"
import 'element-plus/dist/index.css'
import Vuex from 'vuex'
import { createStore } from 'vuex'
import axios from 'axios'
// import VueAxios from 'vue-axios'

const store = createStore({
    state () {
      return {
        count: 0,
        song_to_check:"sdsd",
        update : 0,
       
        
      }
    },
    mutations: {
      increment (state) {
        state.count++
      },
      changesong(state,data1){
        state.song_to_check = data1
      }
    }
  })
const app=createApp(App).use(Vuex).use(ElementPlus).use(router).use(store)
// const app=createApp(App).use(VueAxios,axios).use(Vuex).use(ElementPlus).use(router).use(store).mount('#app')
app.config.globalProperties.$axios=axios
app.mount('#app')





