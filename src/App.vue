<template>
  <!--这里是第一层div，用来放网格-->

  <div id="app">
    <HEADERVue />

    <MAIN />

  </div>



  <router-view></router-view>









</template>





<script>
import HelloWorld from './components/HelloWorld.vue'
import Search from './components/Search.vue'
import { store } from './store'
import axios from "axios"
import HEADERVue from './layout/HEADER.vue'
import MAIN from './layout/MAIN.vue'
export default {
  name: 'App',
  components: {
    HelloWorld,
    Search,
    HEADERVue,
    MAIN
  }
  ,
  data() {
    return {
      name1: "hi"
    }
  }
  ,


  methods: {
    search(data) {
      console.log(data);
      store.song_to_check = data;
      var appData = require('./data.json');
      console.log(appData)
      name1 = appData
    }
  }

}
</script>

<style lang="less" scoped>
#app {

  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  background-color: rgb(216, 240, 240);
}



body {
  margin: 0;
}


.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #eb4527;
}

.bg-purple {
  background: #eb4527;
}

.bg-purple-light {
  background: #e7a094;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #eb4527;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}
</style>
