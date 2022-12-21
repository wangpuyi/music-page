<template>

    <div class="playing-song-detail" ref="playingSongDetail">
      <button class="icon-down-arrow" @click="closeSongDetail"> 返回歌单</button>
      <el-container style="height: 1000px; border: 1px solid #eee">
            
        <div @click="playmusic" :class="{ 'rotate360': showAnimate }" class="icon-iconfontshuaxin">
        </div>
          <div class="lyric">
            <h2>歌名</h2>
            <h3>作者</h3>
            <ul ref="lyricUL">
              <li v-for="(item, i) in lyricsObjArr" :style="{ color: lyricIndex === i ? 'skyblue' : '#ded9d9' }" :key="item.uid"
                :data-index='i' ref="lyric">{{ item.lyric }}</li>
            </ul>
          </div>
      
      <div class="bottom">
        <div class="play-tab">
          <audio src='https://music.163.com/song/media/outer/url?id=562598065.mp3' @timeupdate="updateTime" ref="audio"
            controls="controls" ontimeupdate></audio>
        </div>
      </div>

      </el-container>>

    </div>
</template>


<script>
export default {


  data() {
    return {
      showAnimate: false,
      is_stop: true,
      current_time_instore: 0,
      lyricsObjArr: [
        {
          time: 2,
          lyric: '爱上你是我情非得已',
          uid: '234432'
        },
        {
          time: 4,
          lyric: 'WDNMD非得已',
          uid: '233332'
        },
        {
          time: 6,
          lyric: '爱上你是我情非得已',
          uid: '234432'
        },
        {
          time: 8,
          lyric: 'WDNMD非得已',
          uid: '233332'
        },
        {
          time: 10,
          lyric: '爱上你是我情非得已',
          uid: '234432'
        },
        {
          time: 12,
          lyric: 'WDNMD非得已',
          uid: '233332'
        },
        {
          time: 14,
          lyric: '爱上你是我情非得已',
          uid: '234432'
        },
        {
          time: 16,
          lyric: 'WDNMD非得已',
          uid: '233332'
        }
      ]


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
    }

  },
  mounted() {
    this.$refs.audio.src = this.$store.state.currentsong_url


  },


  methods: {
    updateTime() {
      let s = this.$refs.audio.currentTime;//获取当前播放时间
      console.log(s + '=======获取当前播放时间')
      this.current_time_instore = parseFloat(s)

    },
    play() {
      this.showAnimate = false
    },

    closeSongDetail() {
      this.$router.push('/B');
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
  background: rgb(133, 76, 72);
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
    transform: rotate(45deg);
    background-image: radial-gradient(5em 30em ellipse, #fff, #000);
    border: 2px solid #131313;
    box-shadow: 0 0 0 10px #343935;


  }
  
  .lyric {
    position: relative;
    margin-top: 10%;
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
