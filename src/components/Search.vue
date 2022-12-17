<script>
import { update } from 'lodash'
import { store } from '../store.js'

export default {
  data() {
    return {
      msg: 'Music',
      store,
      mysong:''

    }
  },
  methods:{
    send_search(){
      w
      this.$router.push('/B')
      
      this.$store.commit('changesong',this.mysong)
    
  
}}}
</script>

<template>
<div class="bottom"> 
  <input v-model="mysong" >
  <p>{{this.$store.state.song_to_check}}</p>
  <button @click="send_search "  >搜索</button>



</div>

  
</template>
<style lang="less" scoped>



</style>
