<template>

  <!-- 按钮 -->
  <!-- <div style="width:2000px; display: table;">
    <div class="pop" v-if="showModal">
        <button @click="showModal=false" class="btn">{{ pick_tag }}</button>
        <br>
        <br>
        <br>
        <br>
        <a style="float:left" href="">全部歌单</a>
        <br>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left">语种</p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">华语</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">欧美</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">日语</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">韩语</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">粤语</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href=""></a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left">风格</p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">流行</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">摇滚</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">民谣</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">电子</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">舞曲</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">说唱</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">轻音乐</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">爵士</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">乡村</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">R&B/Soul</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">古典</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">民族</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">英伦</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">金属</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">朋克</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">蓝调</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">雷鬼</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">世界音乐</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">拉丁</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">New Age</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">古风</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">后摇</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">Bossa Nova</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">说唱</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left">场景</p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">清晨</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">夜晚</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">学习</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">工作</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">午休</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">下午茶</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">地铁</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">驾车</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">运动</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">旅行</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">散步</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">酒吧</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left">情感</p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">怀旧</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">清新</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">浪漫</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">伤感</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">治愈</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">放松</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">孤独</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">感动</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">兴奋</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">快乐</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">安静</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">思念</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left">主题</p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">综艺</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">影视原声</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">ACG</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">儿童</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">校园</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">游戏</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">70后</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">80后</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">90后</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">网络歌曲</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">KTV</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">经典</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">翻唱</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">吉他</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">钢琴</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">器乐</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">榜单</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">00后</a>
          </div>
        </div>
      </div>
      <button @click="showModal=true" class="btn">{{ pick_tag }}</button>
  </div> -->
  <!-- 按钮 end -->
<!-- 图片走马灯 -->
<div class="center" style="margin: 0 260px 0">
<div class="carousel" style="width:1000px;" auto>
  <el-carousel :interval="4000" type="card" height="200px">
    <el-carousel-item v-for="img in images" :key="img.id">
      <div class="rowing_image"><el-image style="width: 100%; height: 200px" :src="img.Image" ></el-image></div>
    </el-carousel-item>
  </el-carousel>
</div>
<!-- 图片走马灯 end -->

<!-- 歌单列表 -->
    <div class = 'listCard' style="width:1000px;"  infinite-scroll-disabled="true" infinite-scroll-distance="300">
      <div v-for="o in 10" :key='o' class = 'listCardItem'>
        <router-link :to="{path: '/B',  query: {listid: ids[o-1]}}">
        <div class="image">
          <img class="img" :src='ListImage[o-1]' />
        </div>
        <div class="title">{{name[o-1]}}</div>
      </router-link>
      </div>
    </div>
</div>
<!-- 歌单列表 end-->
</template>

<script>

export default {
  data() {
    return {
      // showModal: false,
      // pick_tag: "华语",
      images: [{id: 1, Image: 'http://p1.music.126.net/es5iS_FTfgKBngEGpswzUw==/109951168153707267.jpg '},
        {id: 2, Image: 'http://p1.music.126.net/XkhUtVDdGLcg5KpXa_Vw-w==/109951168153726125.jpg'}, 
        {id: 3, Image: 'http://p1.music.126.net/e1eNRZLZEgMzG0GxPFtTiA==/109951168153738247.jpg'},
        {id: 4, Image: 'http://p1.music.126.net/Qp-6Lgrkg8KkaBeaSjgq4g==/109951168153713033.jpg'},
        {id: 5, Image: 'http://p1.music.126.net/JVeTK-MnkeLj3b3F8u49Pw==/109951168153726257.jpg'},
        {id: 6, Image: 'http://p1.music.126.net/jLT0ETZuxg17L1NnVbwnJA==/109951168153727929.jpg'}],
      ListImage: [],
      name : [],
      ids : []
    };
  },
  methods: {
    initData () {
      //const payload = {'label' : '华语'}
      this.$axios.get('http://127.0.0.1:5000/zhuye').then(res => {
        // this.datetime = res.data.listid
        console.log(res.data)
        let i = 0;
        for(; i < 10; i++){
          console.log(res.data[i])
          this.name.push(res.data[i].name)
          this.ListImage.push(res.data[i].listimage)
          this.ids.push(res.data[i].listid)
        }
          
      })
    }
  },
  mounted () {
    this.initData()
  }
};
</script>

<style scoped>

/* wpy */
.listCard {
  display: flex;
  flex-wrap: wrap;
  margin: 10px 0;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  /* display: block; */

  height: 500px  !important;
  position: relative;
}
.listCardItem {
  width: 18.4%;
  margin: 0 2% 20px 0;
  overflow: hidden;
  cursor: pointer;
  /* display: table-cell; */
  float: left;
}
/* .listCard {
  display: flex;
  flex-wrap: wrap;
  margin: 10px 0;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  display: block;
}
.listCardItem {
  width: 18.4%;
  margin: 0 2% 20px 0;
  overflow: hidden;
  cursor: pointer;
  float: left;
} */
.listCardItem:nth-child(5n) {
  margin-right: 0;
}
.image {
  width: 100%;
  padding-bottom: 100%;
  height: 0;
  position: relative;
}
.image::after {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background: url(data:image/png;base64,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) no-repeat center;
  background-size: contain;
  border-radius: 10px;
  z-index: -1;
}
.image img {
  width: 100%;
  border-radius: 10px;
}
.title {
  margin-top: 8px;
  padding: 0 2px;
  font-size: 14px;
  color: black;
  line-height: 17px;
  /* 两行溢出 */
  text-overflow: -o-ellipsis-lastline;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
}
/* wpy end */

/* wpy */
.rowing_image>el-image{
    /* overflow-clip-margin: content-box;
    overflow: clip; */
    /* height: 100%; */
    display: block;
    height: 100%;
    border-radius: 10px;
    
  background-size: contain;
  /* 图片比例不变，将元素铺满 */
  background-size: cover;
  /* 背景图片大小，第二个属性默认auto */
  background-size: 100% 100%;

}
/* wpy end */

.mask {
  background-color: #000;
  opacity: 0.3;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1
}
.pop {
  background-color: #fff;
 
  position: fixed;
  top: 200px;
  left: 50px;
  width: 1000px;
  height:1000px;
  z-index: 9999
}
.btn {
  background-color: #fff;
  border-radius: 4px;
  border: 1px solid rgb(0, 0, 0);
  padding: 20px 24px;
  position: fixed;
  top: 300px;
  left:50px;
  z-index: 999;
}
.router-link-active {
  text-decoration: none;
  color: #fff;
  text-align: center;
}
a {
  text-decoration: none;
  color: #fff;
  
}
</style>