<template>

<div class="playing-song-detail" ref="playingSongDetail">

    <button  class="icon-down-arrow" @click="closeSongDetail">返回歌单</button>
    
    <div  @click="playmusic" :class="{'rotate360':showAnimate}"  
 class="icon-iconfontshuaxin"  >
    
    </div>
    
    <div class="play-tab">
        <audio  src="https://music.163.com/song/media/outer/url?id=562598065.mp3"
            @timeupdate="getCurr"
        
            
             
            ref="audio"
            controls="controls"
            @canplay="showLong"
            ></audio>
    </div>
    
    
    
   
 
</div>
 
<div class="play-tab">
        <audio src="tianxie-url" controls="controls"></audio>

    </div>
</template>


<script>
export default{

    
    data() {
    return {
      showAnimate: false,
      is_stop:true
    }
  },

  methods: {
  
    play() {
      this.showAnimate = false
    },
   
    closeSongDetail() {
			this.$router.push('/B');
		},
        
        playmusic() {
			this.showAnimate=!this.showAnimate
          

            if (this.showAnimate) {
            this.$refs.audio.play()
        } else {
            this.$refs.audio.pause()
        }
		},

  }
}
</script>

<style lang="less" scoped>
.play-tab {
    position: absolute;
    left: 170px;
    top :550px;
}


.playing-song-detail {
	position: absolute;
	bottom: 0;
	left: 0;
	right: 0;
	width: 100%;
	height: calc(100vh);
	background: rgb(144, 57, 57);
	z-index: 99;
	overflow-y: scroll;
	// 关闭页面按钮
	.icon-down-arrow {
		position: fixed;
		top: 10px;
		left: 20px;
		font-size: 32px;
		font-weight: 700;
	
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
  
}

</style>
