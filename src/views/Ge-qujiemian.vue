<template>

  <div class="playing-song-detail" ref="playingSongDetail">
    <button class="icon-down-arrow" @click="closeSongDetail"> 返回歌单</button>
    <!-- <br><br><br><br> -->
    <!-- {{ this.image }} -->
  
    <el-container style="height: 1000px; border: 1px solid #eee">
          
      <div @click="playmusic" :class="{ 'rotate360': showAnimate }" class="icon-iconfontshuaxin">
        <img  class="tupian" :src="image" >
      </div>
        <div class="songxinxi">
          <h2>{{this.title}}</h2>
          <h3>{{this.singer}}</h3>
        </div>
          <ul class="lyric" ref="lyric">
            <li :class="{each:true, choose: (index==lyricIndex)}" v-for="(item, i) in lyricsObjArr"  :key="item.uid"
              :data-index='i' >{{ item.lyric }}</li>
          </ul>

    <!-- <ul class="lyric" v-show="isShowMusicList" ref="lyric">
        <li :class="{each:true, choose: (index==lyricIndex)}" v-for="(item, key, index) in currentMUsicLyric" :key="key">{{item}}</li>
    </ul> -->

    
    <div class="bottom">
      <div class="play-tab">
        <audio @timeupdate="updateTime" ref="audio" controls="controls" ontimeupdate>
          <source :src='mscurl' />
        </audio>
      </div>
    </div>

    </el-container>>

  </div>
</template>


<script>
export default {


data() {
  return {
    singer:'',
    album:"",
    lyric:'',
    tilte:'',
    image:'',
    mscurl : 'https://music.163.com/song/media/outer/url?id='+(this.$route.query.id)+'.mp3',
    showAnimate: false,
    is_stop: true,
    current_time_instore: 0,
    lyricsObjArr: []


  }
},

watch: {
  // 匹配歌词
  // 匹配歌词
  current_time_instore() {
    for (let i = 0; i < this.lyricsObjArr.length; i++) {
      if (this.current_time_instore > (parseInt(this.lyricsObjArr[i].time))) {
        const index = this.$refs.lyric[i].dataset.index
        if (i === parseInt(index)) {
          this.lyricIndex = i
          this.$refs.lyricUL.style.transform = `translateY(${20 - (5 * (i + 1))}px)`
        }
      }
    }
    // let i = 0
    //         // 循环歌词对象
    //         for (let key in this.lyricsObjArr) {
    //         // key表示歌词对象中的时间，如果key等于歌曲进度value，改变当前歌词进度		lyricIndex
    //             if (+key == this.value) {
    //                 this.lyricIndex = i;
    //                 // 当歌词进度大于5，即播放到了第5句歌词，开始滚动
    //                 if (i > 5) {
    //                     this.$refs.lyric.scrollTop = 30 * (i - 5);
    //                 }
    //             }
    //             i++;
    //         }
  }

},
mounted() {
  this.initData()
  //this.$refs.audio.src = this.$store.state.currentsong_url
  

},


methods: {
  initData () {
    //id=(this.$route.query.listid)
    this.$axios.get('http://127.0.0.1:5000/querysong/'+this.$route.query.id).then(res => {
      // this.datetime = res.data.listid
      //console.log(res.data)
      //let i = 0;
        console.log(res.data)
        //this.label = res.data.label
        this.title=(res.data.title)
        this.singer=(res.data.singer)
        this.album=res.data.album
        this.image=res.data.image
        this.lyric=res.data.lyric
  })
  this.$axios.get('http://127.0.0.1:5000/geci/'+this.$route.query.id).then(res => {
      // this.datetime = res.data.listid
      //console.log(res.data)
      //let i = 0;
        console.log(res.data)
        let lyric = res.data
        const regNewLine = /\n/
        const lineArr = lyric.split(regNewLine) // 每行歌词的数组
        const regTime = /\[\d{2}:\d{2}.\d{2,3}\]/
        lineArr.forEach(item => {
        if (item === '') return
          const obj = {}
          const time = item.match(regTime)

          obj.lyric = item.split(']')[1].trim() === '' ? '' : item.split(']')[1].trim()
          obj.time = time ? this.formatLyricTime(time[0].slice(1, time[0].length - 1)) : 0
          obj.uid = Math.random().toString().slice(-6)
          if (obj.lyric === '') {
            console.log('这一行没有歌词')
          } else {
            this.lyricsObjArr.push(obj)
          }
        })
    })
  },
  formatLyricTime (time) { // 格式化歌词的时间 转换成 sss:ms
     const regMin = /.*:/
     const regSec = /:.*\./
     const regMs = /\./

     const min = parseInt(time.match(regMin)[0].slice(0, 2))
     let sec = parseInt(time.match(regSec)[0].slice(1, 3))
     const ms = time.slice(time.match(regMs).index + 1, time.match(regMs).index + 3)
     if (min !== 0) {
       sec += min * 60
     }
     return Number(sec + '.' + ms)
   },

  updateTime() {
    let s = this.$refs.audio.currentTime;//获取当前播放时间
    console.log(s + '=======获取当前播放时间')
    this.current_time_instore = parseFloat(s)

  },
  play() {
    this.showAnimate = false
  },

  closeSongDetail() {
    //this.$router.push('/B');
    window.history.go(-1)
    /*
          if (window.history.length <= 0) {
              this.$router.push({path:'/Ge-dan'})
              return false
          } else {
            this.$router.back()
          }
      */
  },

  playmusic() {
    this.showAnimate = !this.showAnimate


    if (this.showAnimate) {
      this.$refs.audio.play()
    } else {
      this.$refs.audio.pause()
    }
  },
  updata() {
    console.log("播放");
    var audio = document.querySelector("audio");
    audio.duration;//获取总播放时间
    audio.currentTime;//获取播放进度
    console.log(audio.currentTime);//控制台显示


  }
}
}
</script>

<style lang="less" scoped>
// wpy
.lyric {
        width: 600px;
        height: 450px;
        position: absolute;
        margin-top: 13%;
        margin-left: 40%;
        background-color: rgb(255, 255, 255);
        // 滚动条
        overflow: auto;
        color: rgb(0, 0, 0);
        font-size: 10px;
        font-weight: normal;
        padding: 5px 10px;
        border: 1px solid rgb(255, 255, 255);
        border-left: none;
        .each {
        height: 30px;
        // border: 1px solid #000;
        line-height: 30px;
        text-align: center;
        color: #000;
        }
        .choose {
            height: 30px;
            line-height: 30px;
            font-size: 20px;
            color: rgb(62, 39, 39);
        }
        // 修改滚动条样式
        &::-webkit-scrollbar {
            width: 10px;
            height: 1px;
        }
        // 滑块部分
        &::-webkit-scrollbar-thumb {
            background-color: rgb(218, 218, 218);
        }
        // 轨道部分
        &::-webkit-scrollbar-track {
            background-color: rgb(255, 255, 255);
        }
    }

// wpy end
.play-tab {
position: relative;
left: 45%;
}


.playing-song-detail {
position: absolute;
bottom: 0;
left: 0;
right: 0;
width: 100%;
height: calc(100vh);
background: rgb(251, 251, 251);
z-index: 99;
overflow-y: scroll;

// 关闭页面按钮
.icon-down-arrow {
  position: fixed;
  top: 10px;
  left: 20px;
  font-size: 16px;
  font-weight: 700;
  background-color: rgb(237, 240, 27);
  color: rgb(0, 0, 0);
}

.disc {
  position: relative;
  margin-top: 10%;
  margin-left: 10%;

  width: 300px;
  height: 300px;
  border-radius: 300px;
  transform: rotate(45deg);
  background-image: radial-gradient(5em 30em ellipse, #fff, #000);
  border: 2px solid #131313;
  box-shadow: 0 0 0 10px #343935;
  opacity: 0.7;
}

.rotate360 {
  animation: rotate360 17s linear 0.1s infinite;
}

@keyframes rotate360 {

  100% {
    transform: rotate(360deg);
  }
}

.icon-iconfontshuaxin {
  position: relative;
  margin-top: 10%;
  margin-left: 10%;
  width: 300px;
  height: 300px;
  border-radius: 300px;
  // transform: rotate(0deg);
  // background-image: radial-gradient(5em 30em ellipse, #fff, #000);
  // border: 2px solid #131313;
  // box-shadow: 0 0 0 10px #343935;


}
.tupian{
  position: relative;
  // margin-top: 10%;
  // margin-left: 10%;
  width: 300px;
  height: 300px;
  border-radius: 300px;
  transform: rotate(0deg);
  // background-image: radial-gradient(5em 30em ellipse, #fff, rgb(0, 0, 0));
  border: 4px solid #b00808;
  box-shadow: 0 0 0 50px #000000;
}

.songxinxi{
  position: relative;
  margin-top: 5%;
  margin-left: 20%;
  width: 500px;
  height: 800px;
}
.bottom {
  position: fixed;
  background-color: #fff;
  width: 100%;
  bottom: 0px;
}
}
</style>
