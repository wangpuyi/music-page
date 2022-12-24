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
      
      this.$router.push('/So-suo')
      
      this.$store.commit('changesong',this.mysonglist)
    
  
}}}
</script>

<template>
<div class="bottom"> 
  <input v-model="mysonglist" >
  <button @click="send_search ">搜索</button>
</div>

  
</template>
<style lang="less" scoped>



</style>
