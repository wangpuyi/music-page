<template>
    <div id="myChart1" :style="{width: '1200px', height: '800px'}"></div>
    <div id="myChart2" :style="{width: '1200px', height: '800px'}"></div>
</template> 
<script>
// 引入基本模板
let echarts = require('echarts')
export default {
  name: 'hello',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  mounted() {
    this.drawLine();
  },
  methods: {
    drawLine() {
      // 基于准备好的dom，初始化echarts实例
      let myChart1 = echarts.init(document.getElementById('myChart1'))
      // 绘制图表
      myChart1.setOption({
        title: {
            text: '歌曲库中歌曲最多的前10名歌手排名'
        },
        tooltip: {},
        legend: {},
        xAxis: {
            data: ['陈奕迅','G.E.M.邓紫棋','林俊杰','薛之谦','张学友','周深','孙燕姿','毛不易','王菲','许嵩']
        },
        yAxis: [
            {
                type: 'value',
                name: '歌曲数',
                min: 0,
                max: 110,
                interval: 10,
                splitnumber: 10
            }/*,
            {
                type: 'value',
                name: '播放量',
                min: 0,
                max: 10,
                interval: 2,
                splitnumber: 5
            }*/
        ],
        series: [
            {
                name: '歌曲数',
                type: 'bar',
                data: [107,59,59,53,51,42,39,38,36,36],
                yAxisIndex: 0
            },/*
            {
                name: '占品牌份额',
                type: 'bar',
                data: [8.47,8.01,6.90,6.34,5.60,5.26,5.25,3.77,3.74,3.47],
                yAxisIndex: 1
            }*/
        ]
      });
      let myChart2 = echarts.init(document.getElementById('myChart2'));
      myChart2.setOption({
        title: {
                    text: '点击量最高的10大歌单排名'
                },
                tooltip: {},
                legend: {},
                xAxis: {
                    data: ['老歌越听越经典，旧人越看越无情。','人这一辈子，最怕突然听懂了一首歌','歌词唱透了心声，回忆模糊了眼眸','痛彻心扉地哭，然后刻骨铭心地记住','单曲循环丨绝对不能错过的欧美歌曲','如果你想听民谣，可以从这些歌曲开始。','一个比较走心的民谣歌单','百首老歌：再续当年情','华语‖一听就忍不住想哭的歌','徐良＋汪苏泷＋许嵩＝青春']
                },
                yAxis: [
                    {
                        type: 'value',
                        name: '点击量',
                        min: 0,
                        max: 150000000,
                        interval: 10000000,
                        splitnumber: 15
                    },
                    {
                        type: 'value',
                        name: '歌曲数',
                        min: 0,
                        max: 600,
                        interval: 60,
                        splitnumber: 10
                    }
                ],
                series: [
                    {
                        name: '点击量',
                        type: 'line',
                        data: [116917928,85767184,68313688,67856960,65590844,58323880,48602492,44439860,40710532,28510744],
                        yAxisIndex: 0,
                        areaStyle: {}
                    },
                    {
                        name: '歌曲数',
                        type: 'line',
                        data: [295,263,512,305,227,109,42,100,120,39],
                        yAxisIndex: 1,
                        areaStyle:  {
                            color: "#ff0",
                            opacity: 0.5
                        }
                    }
                ]
      });
    }
  }
}
</script>
