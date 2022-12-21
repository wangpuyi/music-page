<template>
<div class="SortBoxContainer" style="height:50px;">
  <div class="pop" v-if="showModal">
        <button @click="showModal=false" class="btn">{{ this.$store.state.picked_tag }}</button>
        <br>
        <br>
        <br>
        <br>
        <div class="tb">
          <div v-if="this.$store.state.picked_tag === '全部歌单' ">
            <p class="txt1" @click="modify_tag('全部歌单' )"  >全部歌单</p>
          </div>
          <div v-else>
            <p class="txt2" @click="modify_tag('全部歌单' )"  >全部歌单</p>
          </div>
        </div>
        
        <div class="tb">
          <div class="un">
            <p style="float:left">语种</p>
          </div>
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '华语' ">
              <p class="txt1" @click="modify_tag('华语' )"  >华语</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('华语' )"  >华语</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '欧美' ">
              <p class="txt1" @click="modify_tag('欧美' )"  >欧美</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('欧美' )"  >欧美</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '日语' ">
              <p class="txt1" @click="modify_tag('日语' )"  >日语</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('日语' )"  >日语</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '韩语' ">
              <p class="txt1" @click="modify_tag('韩语' )"  >韩语</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('韩语' )"  >韩语</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '粤语' ">
              <p class="txt1" @click="modify_tag('粤语' )"  >粤语</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('粤语' )"  >粤语</p>
            </div>
          </div>
        </div>

        <div class="tb">
          <div class="un">
            <p style="float:left">风格</p>
          </div>
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '流行' ">
              <p class="txt1" @click="modify_tag('流行' )"  >流行</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('流行' )"  >流行</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '摇滚' ">
              <p class="txt1" @click="modify_tag('摇滚' )"  >摇滚</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('摇滚' )"  >摇滚</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '民谣' ">
              <p class="txt1" @click="modify_tag('民谣' )"  >民谣</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('民谣' )"  >民谣</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '电子' ">
              <p class="txt1" @click="modify_tag('电子' )"  >电子</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('电子' )"  >电子</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '舞曲' ">
              <p class="txt1" @click="modify_tag('舞曲' )"  >舞曲</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('舞曲' )"  >舞曲</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '说唱' ">
              <p class="txt1" @click="modify_tag('说唱' )"  >说唱</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('说唱' )"  >说唱</p>
            </div>
          </div>
        </div>

        <div class="tb">
          <div class="un">
            <p style="float:left"></p>
          </div>
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '轻音乐' ">
              <p class="txt1" @click="modify_tag('轻音乐' )"  >轻音乐</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('轻音乐' )"  >轻音乐</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '爵士' ">
              <p class="txt1" @click="modify_tag('爵士' )"  >爵士</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('爵士' )"  >爵士</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '乡村' ">
              <p class="txt1" @click="modify_tag('乡村' )"  >乡村</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('乡村' )"  >乡村</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === 'R&B/Soul' ">
              <p class="txt1" @click="modify_tag('R&B/Soul' )"  >R&B/Soul</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('R&B/Soul' )"  >R&B/Soul</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '古典' ">
              <p class="txt1" @click="modify_tag('古典' )"  >古典</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('古典' )"  >古典</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '民族' ">
              <p class="txt1" @click="modify_tag('民族' )"  >民族</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('民族' )"  >民族</p>
            </div>
          </div>
        </div>

        <div class="tb">
          <div class="un">
            <p style="float:left"></p>
          </div>
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '英伦' ">
              <p class="txt1" @click="modify_tag('英伦' )"  >英伦</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('英伦' )"  >英伦</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '金属' ">
              <p class="txt1" @click="modify_tag('金属' )"  >金属</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('金属' )"  >金属</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '朋克' ">
              <p class="txt1" @click="modify_tag('朋克' )"  >朋克</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('朋克' )"  >朋克</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '蓝调' ">
              <p class="txt1" @click="modify_tag('蓝调' )"  >蓝调</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('蓝调' )"  >蓝调</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '雷鬼' ">
              <p class="txt1" @click="modify_tag('雷鬼' )"  >雷鬼</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('雷鬼' )"  >雷鬼</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '世界音乐' ">
              <p class="txt1" @click="modify_tag('世界音乐' )"  >世界音乐</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('世界音乐' )"  >世界音乐</p>
            </div>
          </div>
        </div>

        <div class="tb">
          <div class="un">
            <p style="float:left"></p>
          </div>
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '拉丁' ">
              <p class="txt1" @click="modify_tag('拉丁' )"  >拉丁</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('拉丁' )"  >拉丁</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === 'New Age' ">
              <p class="txt1" @click="modify_tag('New Age' )"  >New Age</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('New Age' )"  >New Age</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '古风' ">
              <p class="txt1" @click="modify_tag('古风' )"  >古风</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('古风' )"  >古风</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '后摇' ">
              <p class="txt1" @click="modify_tag('后摇' )"  >后摇</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('后摇' )"  >后摇</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === 'Bossa Nova' ">
              <p class="txt1" @click="modify_tag('Bossa Nova' )"  >Bossa Nova</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('Bossa Nova' )"  >Bossa Nova</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '' ">
              <p class="txt1" @click="modify_tag('' )"  ></p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('' )"  ></p>
            </div>
          </div>
        </div>

        <div class="tb">
          <div class="un">
            <p style="float:left">场景</p>
          </div>
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '清晨' ">
              <p class="txt1" @click="modify_tag('清晨' )"  >清晨</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('清晨' )"  >清晨</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '夜晚' ">
              <p class="txt1" @click="modify_tag('夜晚' )"  >夜晚</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('夜晚' )"  >夜晚</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '学习' ">
              <p class="txt1" @click="modify_tag('学习' )"  >学习</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('学习' )"  >学习</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '工作' ">
              <p class="txt1" @click="modify_tag('工作' )"  >工作</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('工作' )"  >工作</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '午休' ">
              <p class="txt1" @click="modify_tag('午休' )"  >午休</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('午休' )"  >午休</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '下午茶' ">
              <p class="txt1" @click="modify_tag('下午茶' )"  >下午茶</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('下午茶' )"  >下午茶</p>
            </div>
          </div>
        </div>

        <div class="tb">
          <div class="un">
            <p style="float:left"></p>
          </div>
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '地铁' ">
              <p class="txt1" @click="modify_tag('地铁' )"  >地铁</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('地铁' )"  >地铁</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '驾车' ">
              <p class="txt1" @click="modify_tag('驾车' )"  >驾车</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('驾车' )"  >驾车</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '运动' ">
              <p class="txt1" @click="modify_tag('运动' )"  >运动</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('运动' )"  >运动</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '旅行' ">
              <p class="txt1" @click="modify_tag('旅行' )"  >旅行</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('旅行' )"  >旅行</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '散步' ">
              <p class="txt1" @click="modify_tag('散步' )"  >散步</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('散步' )"  >散步</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '酒吧' ">
              <p class="txt1" @click="modify_tag('酒吧' )"  >酒吧</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('酒吧' )"  >酒吧</p>
            </div>
          </div>
        </div>

        <div class="tb">
          <div class="un">
            <p style="float:left">情感</p>
          </div>
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '怀旧' ">
              <p class="txt1" @click="modify_tag('怀旧' )"  >怀旧</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('怀旧' )"  >怀旧</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '清新' ">
              <p class="txt1" @click="modify_tag('清新' )"  >清新</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('清新' )"  >清新</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '浪漫' ">
              <p class="txt1" @click="modify_tag('浪漫' )"  >浪漫</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('浪漫' )"  >浪漫</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '伤感' ">
              <p class="txt1" @click="modify_tag('伤感' )"  >伤感</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('伤感' )"  >伤感</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '治愈' ">
              <p class="txt1" @click="modify_tag('治愈' )"  >治愈</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('治愈' )"  >治愈</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '放松' ">
              <p class="txt1" @click="modify_tag('放松' )"  >放松</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('放松' )"  >放松</p>
            </div>
          </div>
        </div>

        <div class="tb">
          <div class="un">
            <p style="float:left"></p>
          </div>
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '孤独' ">
              <p class="txt1" @click="modify_tag('孤独' )"  >孤独</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('孤独' )"  >孤独</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '感动' ">
              <p class="txt1" @click="modify_tag('感动' )"  >感动</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('感动' )"  >感动</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '兴奋' ">
              <p class="txt1" @click="modify_tag('兴奋' )"  >兴奋</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('兴奋' )"  >兴奋</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '快乐' ">
              <p class="txt1" @click="modify_tag('快乐' )"  >快乐</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('快乐' )"  >快乐</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '安静' ">
              <p class="txt1" @click="modify_tag('安静' )"  >安静</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('安静' )"  >安静</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '放松' ">
              <p class="txt1" @click="modify_tag('放松' )"  >放松</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('放松' )"  >放松</p>
            </div>
          </div>
        </div>

        <div class="tb">
          <div class="un">
            <p style="float:left">主题</p>
          </div>
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '综艺' ">
              <p class="txt1" @click="modify_tag('综艺' )"  >综艺</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('综艺' )"  >综艺</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '影视原声' ">
              <p class="txt1" @click="modify_tag('影视原声' )"  >影视原声</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('影视原声' )"  >影视原声</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === 'ACG' ">
              <p class="txt1" @click="modify_tag('ACG' )"  >ACG</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('ACG' )"  >ACG</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '儿童' ">
              <p class="txt1" @click="modify_tag('儿童' )"  >儿童</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('儿童' )"  >儿童</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '校园' ">
              <p class="txt1" @click="modify_tag('校园' )"  >校园</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('校园' )"  >校园</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '游戏' ">
              <p class="txt1" @click="modify_tag('游戏' )"  >游戏</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('游戏' )"  >游戏</p>
            </div>
          </div>
        </div>

        <div class="tb">
          <div class="un">
            <p style="float:left"></p>
          </div>
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '70后' ">
              <p class="txt1" @click="modify_tag('70后' )"  >70后</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('70后' )"  >70后</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '80后' ">
              <p class="txt1" @click="modify_tag('80后' )"  >80后</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('80后' )"  >80后</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '90后' ">
              <p class="txt1" @click="modify_tag('90后' )"  >90后</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('90后' )"  >90后</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '网络歌曲' ">
              <p class="txt1" @click="modify_tag('网络歌曲' )"  >网络歌曲</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('网络歌曲' )"  >网络歌曲</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === 'KTV' ">
              <p class="txt1" @click="modify_tag('KTV' )"  >KTV</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('KTV' )"  >KTV</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '经典' ">
              <p class="txt1" @click="modify_tag('经典' )"  >经典</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('经典' )"  >经典</p>
            </div>
          </div>
        </div>

        <div class="tb">
          <div class="un">
            <p style="float:left"></p>
          </div>
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '翻唱' ">
              <p class="txt1" @click="modify_tag('翻唱' )"  >翻唱</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('翻唱' )"  >翻唱</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '吉他' ">
              <p class="txt1" @click="modify_tag('吉他' )"  >吉他</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('吉他' )"  >吉他</p>
            </div>
          </div>
          
          <div class="un">
            <div v-if="this.$store.state.picked_tag === '钢琴' ">
              <p class="txt1" @click="modify_tag('钢琴' )"  >钢琴</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('钢琴' )"  >钢琴</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '器乐' ">
              <p class="txt1" @click="modify_tag('器乐' )"  >器乐</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('器乐' )"  >器乐</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '榜单' ">
              <p class="txt1" @click="modify_tag('榜单' )"  >榜单</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('榜单' )"  >榜单</p>
            </div>
          </div>

          <div class="un">
            <div v-if="this.$store.state.picked_tag === '00后' ">
              <p class="txt1" @click="modify_tag('00后' )"  >00后</p>
            </div>
            <div v-else>
              <p class="txt2" @click="modify_tag('00后' )"  >00后</p>
            </div>
          </div>
        </div>
</div>
      <button @click="showModal=true" class="btn">{{ this.$store.state.picked_tag }}</button>

</div>


<!-- 歌单列表 -->
<div class = 'listCard' style="width:980px;" infinite-scroll-disabled="true" infinite-scroll-distance="300">
      <div v-for="o in 25" :key='o' class = 'listCardItem'>
        <router-link :to="{path: '/B', query: {listid: ids[o-1]}}">

        <div class="image">
          <img class="img" :src='ListImage[o-1]' />
        </div>
        <div class="title">{{name[o-1]}}</div>
      </router-link>

      </div>

    </div>

<!-- 歌单列表 end -->
      <!-- 分页器 -->
      <el-pagination 
      background="true"
      @size-change="handleSizeChange" 
      @current-change="handleCurrentChange" 
      :current-page="currentPage" 
      :total='total'
      :page-size=35
      layout=" prev, pager, next" 
      >
      </el-pagination>
        
 
</template>
 
<script>
  export default {
    data() {
        return {
          showModal : false,
          currentPage: 1, // 当前页码
          total: 1200, // 总条数
          // pageSize: 2, // 每页的数据条数
          ListImage: [],
          name : [],
          ids : []
        };
    },
    methods: {
        //每页条数改变时触发 选择一页显示多少行
      handleSizeChange(val) {
          console.log(`每页 ${val} 条`);
          this.currentPage = 1;
          this.pageSize = val;
      },
      //当前页改变时触发 跳转其他页
      handleCurrentChange(val) {
          console.log(`当前页: ${val}`);
          this.currentPage = val;
          this.initData()
      },
      modify_tag(para1) {
                  console.log(para1)
                  this.$store.commit('changetag',para1)
                  this.showModal = false
                  this.initData()
                },
      initData () {
        const payload = {
          'label' : this.$store.state.picked_tag,
          'page': this.currentPage
        }
        this.$axios.get('http://127.0.0.1:5000/gedans',{params:payload}).then(res => {
        // this.datetime = res.data.listid
        console.log(res.data)
        this.total = 35*res.data[0].pages
        let i = 1;
        this.name = []
        this.ids = []
        this.ListImage = []
        for(; i <= 35; i++){
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
/* .SortBoxContainer{
  position: ;
} */
.listCard {
  display: flex;
  flex-wrap: wrap;
  margin: 10px 0;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  /* display: block; */

  height: 1740px;
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

/*按钮*/
.pop {
  background-color: #fff;
 
  position: fixed;
  top: 300px;
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
.tb {
  width:1000px; 
  display: table;
}
.txt1 {
  color:rgb(227, 47, 47);
  float: left;
}
.txt2 {
  color:#000;
  float: left;
}
.un {
  display : table-cell;
  width: 100px;
}
/* 按钮 end */

</style>

<style>
.el-pagination {
  width: 1000px;
  padding-bottom: 20px;
  /* margin-top:15px; */
  /* float: left; */
  position: absolute;
  display: flex;
  justify-content: center;
}

.el-pagination.is-background .btn-prev, .el-pagination.is-background .btn-next, .el-pagination.is-background .el-pager li{
  border-radius: 10%;
  background-color: #fff;
}
</style>
