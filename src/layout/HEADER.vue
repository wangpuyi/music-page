<template>
	<!-- <div id = "header1">
	</div> -->
	<div id="header" >
    	<div style="margin-left: 180px;">	
			<img alt="Vue logo" src="../assets/logo2.jpg" width="70" height="70" style=" text-align: center;">
		</div>
		
    	<div class="title">
			<div class="icon"><span class="iconfont icon-yinleyanzou"></span></div>
			<div class="text" style="margin-left: 180px;"><span>交你听</span></div>
		</div>
		
		<!-- <div class="search" style="float:left" >
			<SearchVue />
		</div> -->
		<div class="header-search">
              <input v-model="mysonglist" id="search_song" type="text" class="text" placeholder="请输入内容">
              <div class="btn">
                <button @click="con" style="width:100%; height:100%;back"><i class="icon-sprite"></i></button>
              </div>
              <!-- <div class="result">
                <a href="#" class="result-item">
                  <span class="rank">1</span>
                  <span class="title">默</span>
                  <span class="num">3.4万</span>
                </a>
                <a href="#" class="result-item">
                  <span class="rank">2</span>
                  <span class="title">侧田</span>
                  <span class="num">3.4万</span>
                </a>
                <a href="#" class="result-item">
                  <span class="rank">3</span>
                  <span class="title">让我留在你身边</span>
                  <span class="num">3.4万</span>
                </a>
                <a href="#" class="result-item">
                  <span class="rank">4</span>
                  <span class="title">皮皮虾我们走</span>
                  <span class="num">3.4万</span>
                </a>
                <a href="#" class="result-item">
                  <span class="rank">5</span>
                  <span class="title">欢乐好声音</span>
                  <span class="num">3.4万</span>
                </a> -->
                <!-- <div class="history">
                  <span>搜索历史</span>
                  <i class="icon-sprite"></i>
                </div> -->
              <!-- </div> -->
        </div>
	</div>
	
</template>


<script>
import { update } from 'lodash'
import { store } from '../store.js'

import SearchVue from '@/components/Search.vue';
export default {
    name: "Header",
    components: { SearchVue },
	data() {
		return {
      msg: 'Music',
      store,
      mysong:''
		};
	},
	methods: {
    con(){
      var res = document.getElementById('search_song').value
      this.$store.commit('search',res)
      //this.$router.push({path:'/So-suo'})
      this.$router.push({path:'/So-suo',query:{search:this.mysonglist}})
      this.$store.state.show1=1
            this.$store.state.show2=0
            this.$store.state.show3=0
      this.$store.state.pt=1
    }
}}
</script>

<style lang="less" scoped>

#header {

	position: fixed;
	display: flex;
	align-items: center;
	width: 100%;
	height: 100px;
	background-color:rgb(230, 167, 167) ;
	z-index: 99;
	margin:0 0 10px 0;
	padding: 0;
	.search{
		// position: relative;
		flex: 2;
		display: flex;
		align-items: center;
		
		height: 60px;
		margin-left: 60px;

	// 	position: relative;
    // float: left;
    // width: 248px;
    // height: 36px;
    // // margin-top: 26px;
    // margin-left: 300px;
    // border: 1px solid #c9c9c9;
    // border-radius: 3px;
    // font-size: 0;
	
	}
	.title {
		
		display: flex;
		
		height: 60px;
		
		margin-left: 10px;
	
		.text {
			font-size: 22px;
			color: rgb(60, 39, 39);
			font-family: Arial, Helvetica, sans-serif;
			line-height: 60px;

		}
}}

// wpy
.icon-sprite {
    background: url(../assets/icon_sprite.png) no-repeat;
}
.header-search {
  position: relative;
  float: left;
  width: 248px;
  height: 36px;
  align-items: center;
  margin-left: 180px;
  border: 1px solid #c9c9c9;
  border-radius: 3px;
  font-size: 0;
}
.header-search .text {
  display: inline-block;
  width: 212px;
  height: 36px;
  padding-left: 14px;
  box-sizing: border-box;
  font-family: "Microsoft Yahei";
  font-size: 1px;
  vertical-align: top;
}
.header-search .btn {
  display: inline-block;
  width: 36px;
  height: 36px;
  // line-height: 52px;
  text-align: center;
  cursor: pointer;
  color: #000;
}
.header-search .btn i {
  display: inline-block;
  width: 16px;
  height: 16px;
  background-position: 0 -40px;
}
.header-search .btn:hover i {
  background-position: 0 -60px;
}
.header-search .result {
  display: none;
  position: absolute;
  z-index: 999;
  top: 36px;
  left: -1px;
  width: 248px;
  padding: 6px 0 14px;
  border: 1px solid #c9c9c9;
  font-size: 14px;
  background-color: #fff;
}
.header-search .result-item {
  position: relative;
  padding: 0 15px;
  height: 36px;
  line-height: 36px;
  font-size: 12px;
}
.header-search .result-item:hover {
  background-color: #31c27c;
}
.header-search .result-item .rank {
  margin-right: 12px;
  color: #ff594b;
}
.header-search .result-item .title {
  font-size: 14px;
}
.header-search .result-item .num {
  position: absolute;
  right: 15px;
  color: #999;
}
.header-search .result-item:hover .rank,
.header-search .result-item:hover .title,
.header-search .result-item:hover .num {
  color: #fff;
}
.header-search .history {
  position: relative;
  padding: 0 15px;
  margin-top: 15px;
  height: 24px;
  line-height: 24px;
}
.header-search .history span {
  color: #999;
}
.header-search .history i {
  position: absolute;
  top: 5px;
  right: 15px;
  width: 16px;
  height: 16px;
  background-position: -100px 0;
  cursor: pointer;
}
.header-search .history i:hover {
  background-position: -20px -60px;
}

*{
  margin:0;
  padding:0;
  border:0;
}
// wpy end
</style>