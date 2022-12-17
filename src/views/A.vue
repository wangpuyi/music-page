<template>

    
    <RouterLink to ="/A/4"></RouterLink><br/>
    
    <HelloWorldVue />
   

</template>

<script>
import HelloWorldVue from '@/components/HelloWorld.vue';
export default
{
  components:{
    HelloWorldVue 
  },
  data() {
    return {
      left: 300,
      top:0
    }
  },
  methods:{
    
  }
}
</script>