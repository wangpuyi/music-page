<template>


  <div id="header1">

  </div>
  <!-- 走马灯 放在helloworld中-->
  <!-- <el-carousel :interval="4000" type="card" height="200px">
    <el-carousel-item v-for="(img,index)  in images" :key="img.id">
        <el-image style="width: 100px; height: 100px" :src="img.goodsImage" :fit="fit"></el-image>
       
      
    </el-carousel-item>
  </el-carousel> -->
  <!-- 走马灯 end -->

  <el-row :gutter="10" style="background-color:white">
    <el-col :span="6">
      <div class="grid-content bg-purple" style="text-align:middle"><router-link to='/A' style="text-align:middle">
          个性化推荐 </router-link></div>
    </el-col>
    <el-col :span="6">
      <div class="grid-content bg-purple" @click="this.$store.commit('Leave_gedan')"><router-link to='/Ge-dan'> 歌单
        </router-link></div>
    </el-col>
    <el-col :span="6">
      <div class="grid-content bg-purple" @click="this.$store.commit('Leave_gedan')"><router-link to='/geshou'> 歌手
        </router-link></div>
    </el-col>
    <el-col :span="6">
      <div class="grid-content bg-purple" @click="this.$store.commit('Leave_gedan')"><router-link to='/C'> 可视化部分
        </router-link></div>
    </el-col>
  </el-row>







</template>

<script>
import HelloWorldVue from '@/components/HelloWorld.vue';
import { store } from '../store.js'
export default {

  components: {
    HelloWorldVue,

  }
  , data() {
    return {
      updata: store.update,

      //             images: [{id: 1, goodsImage: 'http://p1.music.126.net/3lrUXI96dmlEi2UgeIhOHg==/109951163076301483.jpg', goodsCategoryName: '家政服务'},
      // {id: 2, goodsImage: 'http://p1.music.126.net/3lrUXI96dmlEi2UgeIhOHg==/109951163076301483.jpg', goodsCategoryName: '家政服务'}, {id: 3, goodsImage: 'http://p1.music.126.net/3lrUXI96dmlEi2UgeIhOHg==/109951163076301483.jpg', goodsCategoryName: '家政服务'},
      //  {id: 4, goodsImage: 'http://p1.music.126.net/3lrUXI96dmlEi2UgeIhOHg==/109951163076301483.jpg', goodsCategoryName: '家政服务'},
      // {id: 5, goodsImage: 'http://p1.music.126.net/3lrUXI96dmlEi2UgeIhOHg==/109951163076301483.jpg', goodsCategoryName: '家政服务'},
      //  {id: 6, goodsImage: 'http://p1.music.126.net/3lrUXI96dmlEi2UgeIhOHg==/109951163076301483.jpg', goodsCategoryName: '家政服务'}]
      //        ,

    }

  },
  methods: {
  },
  watch: {
    update() {

    }
  }
}
</script>



<style lang="less" scoped>
#header1 {

  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
  height: 100px;
  background-color: rgb(255, 255, 255);
  z-index: 09;
  margin-bottom: 10px;
}

#app {
  @import "assets/css/base.css";
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  background-color: rgb(216, 240, 240);
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
  text-decoration-line: none;
  padding: 15px 0 0 0;
  margin: 0px;
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

// wpy
.router-link-active {
  text-decoration: none;
  color: #fff;
  display: inline-block;
}

a {
  text-decoration: none;
  color: #fff;
  display: inline-block;
}

* {
  margin: 0;
  padding: 0;
  border: 0;
}

// wpy end
</style>

