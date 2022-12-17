<template>

<div class="pop" v-if="showModal">
        <button @click="showModal=false" class="btn">{{ pick_tag }}</button>
        <br>
        <br>
        <br>
        <br>
        <a style="float:left" href="">全部歌单</a>
        <br>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left">语种</p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">华语</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">欧美</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">日语</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">韩语</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">粤语</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href=""></a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left">风格</p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">流行</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">摇滚</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">民谣</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">电子</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">舞曲</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">说唱</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">轻音乐</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">爵士</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">乡村</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">R&B/Soul</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">古典</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">民族</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">英伦</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">金属</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">朋克</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">蓝调</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">雷鬼</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">世界音乐</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">拉丁</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">New Age</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">古风</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">后摇</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">Bossa Nova</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">说唱</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left">场景</p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">清晨</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">夜晚</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">学习</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">工作</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">午休</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">下午茶</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">地铁</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">驾车</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">运动</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">旅行</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">散步</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">酒吧</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left">情感</p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">怀旧</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">清新</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">浪漫</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">伤感</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">治愈</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">放松</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">孤独</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">感动</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">兴奋</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">快乐</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">安静</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">思念</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left">主题</p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">综艺</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">影视原声</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">ACG</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">儿童</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">校园</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">游戏</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">70后</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">80后</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">90后</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">网络歌曲</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">KTV</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">经典</a>
          </div>
        </div>
        <br>
        <div style="width:1000px; display: table;">
          <div style="display: table-cell;;width: 100px;;">
            <p style="float:left"></p>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">翻唱</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">吉他</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">钢琴</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">器乐</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">榜单</a>
          </div>
          <div style="display: table-cell;;width: 100px;;">
            <a style="float:left" href="">00后</a>
          </div>
        </div>
</div>
      <button @click="showModal=true" class="btn">{{ pick_tag }}</button>





    <div>
        <!-- 表格 -->
        <el-table :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%">
            <el-table-column prop="date" label="日期" width="180">
            </el-table-column>
            <el-table-column prop="name" label="姓名" width="180">
            </el-table-column>
            <el-table-column prop="address" label="地址">
            </el-table-column>
        </el-table>
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
                            date: "2016-05-02",
                            name: "第一页",
                            address: "上海市普陀区金沙江路 1518 弄"
                        },
                        {
                            date: "2016-05-04",
                            name: "第二页",
                            address: "上海市普陀区金沙江路 1517 弄"
                        },
                        {
                            date: "2016-05-01",
                            name: "第三页",
                            address: "上海市普陀区金沙江路 1519 弄"
                        },
                        {
                            date: "2016-05-03",
                            name: "第四页",
                            address: "上海市普陀区金沙江路 1516 弄"
                        },
                        {
                            date: "2016-05-01",
                            name: "第五页",
                            address: "上海市普陀区金沙江路 1519 弄"
                        },
                        {
                            date: "2016-05-03",
                            name: "第六页",
                            address: "上海市普陀区金沙江路 1516 弄"
                        },
                    ],
                    currentPage: 1, // 当前页码
                    total: 20, // 总条数
                    pageSize: 2 // 每页的数据条数
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

