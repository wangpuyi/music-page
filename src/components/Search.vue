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
      
      this.$router.push({path:'/So-suo',query:{search:this.mysonglist}})
      
      //this.$store.commit('changesong',this.mysonglist)
    
  
}}}
</script>

<template>
<div class="bottom"> 
  <input v-model="mysonglist" >
  <router-link :to="{path:'/So-suo',query:{search:this.mysonglist}}">
  <button >搜索</button>
</router-link>
</div>

  
</template>
<style lang="less" scoped>



</style>
