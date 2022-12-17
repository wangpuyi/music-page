<template>
  <div>
        <div class="album-list">
          <div v-for="(item,index) in tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" :key="index" >
            <img :src="item.image" >
            <p>{{ item.listname }}</p>
          </div>
        </div>
        <!-- 分页器 -->
        <div class="block" style="margin-top:15px;">
            <el-pagination align='center' @size-change="handleSizeChange" @current-change="handleCurrentChange" 
            :current-page="currentPage" 
            :page-sizes="[1,5,10,20]" 
            :page-size="pageSize" 
            layout="total, sizes, prev, pager, next, jumper" 
            :total="tableData.length">
            </el-pagination>
        </div>
    </div>
</template>


<script>
        export default {
            data() {
                return {
                    tableData: [
                        {
                            image: "http://p3.music.126.net/xMW_jFfcm1fRx3m8aegPrQ==/64871186051051.jpg?param=200y200",
                            listname: "黄凯芹 首张发烧和留念30首",
                            address: "上海市普陀区金沙江路 1518 弄"
                        },
                        {
                          image: "http://p3.music.126.net/zV1Yp7xPgQXYBdSaAmPqxA==/18939087788774646.jpg?param=200y200",
                          listname: "轻柔日系 | 平静的像天空中划过的流星",
                            address: "上海市普陀区金沙江路 1517 弄"
                        },
                        {
                          image: "http://p4.music.126.net/fu49FK1B1y6Zl2tyrYz-ow==/54975581401873.jpg?param=200y200",
                          listname: "发烧男声王闻 《男人40》 系列",
                            address: "上海市普陀区金沙江路 1519 弄"
                        },
                        {
                          image: "http://p4.music.126.net/XoEsVD2xjjiCMS9Rpex3Dg==/3261151496135632.jpg?param=200y200",
                          listname: "单曲循环，百听不厌，精选日系女声。",
                            address: "上海市普陀区金沙江路 1516 弄"
                        },
                        {
                          image: "http://p4.music.126.net/9sX-bEG-qi1EtlwqlqtEng==/3446968953135662.jpg?param=200y200",
                          listname: "那些过耳不忘的粤语歌曲",
                            address: "上海市普陀区金沙江路 1519 弄"
                        },
                        {
                          image: "http://p3.music.126.net/vfaAPF_6Mr_nYbcoEupUxg==/3353510465613659.jpg?param=200y200",
                          listname: "【华语】婚礼暖场，循环幸福。",
                            address: "上海市普陀区金沙江路 1516 弄"
                        },
                        {
                            image: "http://p3.music.126.net/xMW_jFfcm1fRx3m8aegPrQ==/64871186051051.jpg?param=200y200",
                            listname: "黄凯芹 首张发烧和留念30首",
                            address: "上海市普陀区金沙江路 1518 弄"
                        },
                        {
                          image: "http://p3.music.126.net/zV1Yp7xPgQXYBdSaAmPqxA==/18939087788774646.jpg?param=200y200",
                          listname: "轻柔日系 | 平静的像天空中划过的流星",
                            address: "上海市普陀区金沙江路 1517 弄"
                        },
                        {
                          image: "http://p4.music.126.net/fu49FK1B1y6Zl2tyrYz-ow==/54975581401873.jpg?param=200y200",
                          listname: "发烧男声王闻 《男人40》 系列",
                            address: "上海市普陀区金沙江路 1519 弄"
                        },
                        {
                          image: "http://p4.music.126.net/XoEsVD2xjjiCMS9Rpex3Dg==/3261151496135632.jpg?param=200y200",
                          listname: "单曲循环，百听不厌，精选日系女声。",
                            address: "上海市普陀区金沙江路 1516 弄"
                        },
                        {
                          image: "http://p4.music.126.net/9sX-bEG-qi1EtlwqlqtEng==/3446968953135662.jpg?param=200y200",
                          listname: "那些过耳不忘的粤语歌曲",
                            address: "上海市普陀区金沙江路 1519 弄"
                        },
                        {
                          image: "http://p3.music.126.net/vfaAPF_6Mr_nYbcoEupUxg==/3353510465613659.jpg?param=200y200",
                          listname: "【华语】婚礼暖场，循环幸福。",
                            address: "上海市普陀区金沙江路 1516 弄"
                        },
                        {
                            image: "http://p3.music.126.net/xMW_jFfcm1fRx3m8aegPrQ==/64871186051051.jpg?param=200y200",
                            listname: "黄凯芹 首张发烧和留念30首",
                            address: "上海市普陀区金沙江路 1518 弄"
                        },
                        {
                          image: "http://p3.music.126.net/zV1Yp7xPgQXYBdSaAmPqxA==/18939087788774646.jpg?param=200y200",
                          listname: "轻柔日系 | 平静的像天空中划过的流星",
                            address: "上海市普陀区金沙江路 1517 弄"
                        },
                        {
                          image: "http://p4.music.126.net/fu49FK1B1y6Zl2tyrYz-ow==/54975581401873.jpg?param=200y200",
                          listname: "发烧男声王闻 《男人40》 系列",
                            address: "上海市普陀区金沙江路 1519 弄"
                        },
                        {
                          image: "http://p4.music.126.net/XoEsVD2xjjiCMS9Rpex3Dg==/3261151496135632.jpg?param=200y200",
                          listname: "单曲循环，百听不厌，精选日系女声。",
                            address: "上海市普陀区金沙江路 1516 弄"
                        },
                        {
                          image: "http://p4.music.126.net/9sX-bEG-qi1EtlwqlqtEng==/3446968953135662.jpg?param=200y200",
                          listname: "那些过耳不忘的粤语歌曲",
                            address: "上海市普陀区金沙江路 1519 弄"
                        },
                        {
                          image: "http://p3.music.126.net/vfaAPF_6Mr_nYbcoEupUxg==/3353510465613659.jpg?param=200y200",
                          listname: "【华语】婚礼暖场，循环幸福。",
                            address: "上海市普陀区金沙江路 1516 弄"
                        },
                        {
                            image: "http://p3.music.126.net/xMW_jFfcm1fRx3m8aegPrQ==/64871186051051.jpg?param=200y200",
                            listname: "黄凯芹 首张发烧和留念30首",
                            address: "上海市普陀区金沙江路 1518 弄"
                        },
                        {
                          image: "http://p3.music.126.net/zV1Yp7xPgQXYBdSaAmPqxA==/18939087788774646.jpg?param=200y200",
                          listname: "轻柔日系 | 平静的像天空中划过的流星",
                            address: "上海市普陀区金沙江路 1517 弄"
                        },
                        {
                          image: "http://p4.music.126.net/fu49FK1B1y6Zl2tyrYz-ow==/54975581401873.jpg?param=200y200",
                          listname: "发烧男声王闻 《男人40》 系列",
                            address: "上海市普陀区金沙江路 1519 弄"
                        },
                        {
                          image: "http://p4.music.126.net/XoEsVD2xjjiCMS9Rpex3Dg==/3261151496135632.jpg?param=200y200",
                          listname: "单曲循环，百听不厌，精选日系女声。",
                            address: "上海市普陀区金沙江路 1516 弄"
                        },
                        {
                          image: "http://p4.music.126.net/9sX-bEG-qi1EtlwqlqtEng==/3446968953135662.jpg?param=200y200",
                          listname: "那些过耳不忘的粤语歌曲",
                            address: "上海市普陀区金沙江路 1519 弄"
                        },
                        {
                          image: "http://p3.music.126.net/vfaAPF_6Mr_nYbcoEupUxg==/3353510465613659.jpg?param=200y200",
                          listname: "【华语】婚礼暖场，循环幸福。",
                            address: "上海市普陀区金沙江路 1516 弄"
                        },
                    ],
                    currentPage: 1, // 当前页码
                    total: 20, // 总条数
                    pageSize: 8 // 每页的数据条数
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
                }
            }
        };
</script>
<style scoped>
.album-list {
	display: grid;
	justify-content: space-evenly;
	align-content: space-between;
	grid-template-rows: repeat(8, auto-fill);
	grid-template-columns: repeat(4, 25%);
}
</style>