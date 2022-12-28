<template>
    <div id="myChart3" :style="{width: '1500px', height: '1000px'}"></div>
    <br>
    <br>
    <div id="myChart1" :style="{width: '1500px', height: '800px'}"></div>
    <br>
    <br>
    <div id="myChart2" :style="{width: '1500px', height: '800px'}"></div>
</template> 
<script>
// 引入基本模板
let echarts = require('echarts/lib/echarts')
              require('echarts-wordcloud');
import 'echarts/theme/macarons.js'
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
            text: '歌曲库中歌曲最多的前10名歌手排名',
            x: '20%',
            textStyle:{
                fontStyle:'normal',//'italic'(倾斜) | 'oblique'(倾斜体) ，字体风格
                fontWeight:'bold',//'bold'(粗体) | 'bolder'(粗体) | 'lighter'(正常粗细) ，字体粗细
                fontFamily:'Microsoft YaHei',//'sans-serif' | 'serif' | 'monospace' | 'Arial' | 'Courier New' 
                // 'Microsoft YaHei'(微软雅黑) ，文字字体
                fontSize:40,//字体大小
                lineHeight:40//字体行高
            }
        },
        grid: {
            left: '20%',
            right: '20%',
            bottom: '20%',
            top: "15%"
        },
        tooltip: {
        },
        legend: {
            x: '70%',
            textStyle:{
                fontWeight:'bold',//'bold'(粗体) | 'bolder'(粗体) | 'lighter'(正常粗细) ，字体粗细
                fontSize:25,//字体大小
                lineHeight:25//字体行高
            }
        },
        xAxis: {
            data: ['群星','Various Artists','陈奕迅','Beyond','张学友','张国荣','V.A.','HOYO-MiX','邓丽君','The Beatles'],
            axisLabel: {
                interval:0,
                rotate:40,
                textStyle:{
                    fontWeight:'bold',
                    fontSize:20,
                    lineHeight:40
                },   
                boundaryGap: false     
            },
            
        },
        yAxis: [
            {
                type: 'value',
                name: '歌曲数',
                min: 0,
                max: 1400,
                interval: 100,
                splitnumber: 100
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
                color: '#8dc1a9',
                data: [1368,532,418,392,377,300,286,278,263,259],
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
            text: '点击量最高的10大歌单排名',
            x: '20%',
            textStyle:{
                fontStyle:'normal',//'italic'(倾斜) | 'oblique'(倾斜体) ，字体风格
                fontWeight:'bold',//'bold'(粗体) | 'bolder'(粗体) | 'lighter'(正常粗细) ，字体粗细
                fontFamily:'Microsoft YaHei',//'sans-serif' | 'serif' | 'monospace' | 'Arial' | 'Courier New' 
                // 'Microsoft YaHei'(微软雅黑) ，文字字体
                fontSize:40,//字体大小
                lineHeight:40//字体行高
            }
        },
        tooltip: {
        },
        grid: {
            left: '20%',
            right: '20%',
            bottom: '20%',
            top: "15%"
        },
        legend: {
            x: '70%',
            textStyle:{
                fontWeight:'bold',//'bold'(粗体) | 'bolder'(粗体) | 'lighter'(正常粗细) ，字体粗细
                fontSize:25,//字体大小
                lineHeight:25//字体行高
            }
        },
                xAxis: {
                    data: ['老歌越听越经典，旧人越看越无情。','人这一辈子，最怕突然听懂了一首歌','歌词唱透了心声，回忆模糊了眼眸','痛彻心扉地哭，然后刻骨铭心地记住','单曲循环丨绝对不能错过的欧美歌曲','如果你想听民谣，可以从这些歌曲开始。','一个比较走心的民谣歌单','百首老歌：再续当年情','华语‖一听就忍不住想哭的歌','徐良＋汪苏泷＋许嵩＝青春'],
                    axisLabel: {
                        interval:0,
                        rotate:30,
                        textStyle:{
                            fontWeight:'bold',
                            fontSize:15,
                            lineHeight:20
                        }
                    },   
                    boundaryGap: false          
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
      let myChart3 = echarts.init(document.getElementById('myChart3'));
 
            myChart3.setOption ({
                series: [{
                    type: 'wordCloud',
                   //maskImage: maskImage,
                    sizeRange: [50, 150],
                    rotationRange: [0, 90],
                    rotationStep: 45,
                    gridSize: 8,
                    shape: 'rectangle',
                    width: '100%',
                    height: '100%',
                     textStyle: {
                        normal: {
                            color: function () {
                                return 'rgb(' + [
                                    Math.round(Math.random() * 160),
                                    Math.round(Math.random() * 160),
                                    Math.round(Math.random() * 160)
                                ].join(',') + ')';
                            },
                            fontFamily: 'sans-serif',
                            fontWeight: 'normal'
                        },
                        emphasis: {
                            shadowBlur: 10,
                            shadowColor: '#333'
                        }
                    },
                    data: [ {"name":"华语","value":1749},
                            {"name":"流行","value":1489},
                            {"name":"伤感","value":286},
                            {"name":"治愈","value":259},
                            {"name":"民谣","value":218},
                            {"name":"浪漫","value":165},
                            {"name":"说唱","value":165},
                            {"name":"欧美","value":152},
                            {"name":"古风","value":144},
                            {"name":"翻唱","value":135},
                            {"name":"怀旧","value":127},
                            {"name":"夜晚","value":110},
                            {"name":"经典","value":109},
                            {"name":"粤语","value":99},
                            {"name":"放松","value":98},
                            {"name":"摇滚","value":76},
                            {"name":"思念","value":72},
                            {"name":"孤独","value":71},
                            {"name":"清新","value":59},
                            {"name":"网络歌曲","value":57},
                            {"name":"感动","value":56},
                            {"name":"快乐","value":54},
                            {"name":"日语","value":52},
                            {"name":"安静","value":46},
                            {"name":"韩语","value":40},
                            {"name":"榜单","value":39},
                            {"name":"90后","value":38},
                            {"name":"影视原声","value":34},
                            {"name":"R&B/Soul","value":30},
                            {"name":"兴奋","value":28},
                            {"name":"学习","value":25},
                            {"name":"小语种","value":23},
                            {"name":"旅行","value":23},
                            {"name":"驾车","value":22},
                            {"name":"散步","value":19},
                            {"name":"电子","value":19},
                            {"name":"00后","value":19},
                            {"name":"民族","value":18},
                            {"name":"清晨","value":17},
                            {"name":"综艺","value":16},
                            {"name":"另类/独立","value":15},
                            {"name":"运动","value":12},
                            {"name":"KTV","value":10},
                            {"name":"80后","value":10},
                            {"name":"吉他","value":9},
                            {"name":"校园","value":8},
                            {"name":"乡村","value":8},
                            {"name":"酒吧","value":8},
                            {"name":"爵士","value":7},
                            {"name":"地铁","value":7},
                            {"name":"轻音乐","value":7},
                            {"name":"ACG","value":7},
                            {"name":"下午茶","value":6},
                            {"name":"舞曲","value":6},
                            {"name":"工作","value":6},
                            {"name":"世界音乐","value":6},
                            {"name":"性感","value":5},
                            {"name":"古典","value":4},
                            {"name":"英伦","value":3},
                            {"name":"钢琴","value":3},
                            {"name":"游戏","value":2},
                            {"name":"雷鬼","value":2},
                            {"name":"Bossa Nova","value":2},
                            {"name":"器乐","value":2},
                            {"name":"午休","value":1},
                            {"name":"后摇","value":1},
                            {"name":"蓝调","value":1}]
                }]
            });
    }
  }
}
</script>
