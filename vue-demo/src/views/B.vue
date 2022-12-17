
   
    

<template>

  
<div>
<div class="wrapper">
    <div class="f1"><el-card class="box-card">
  <div v-for="o in 4" :key="o" class="text item">
    {{'列表内容 ' + o }}
  </div>

</el-card></div>
    <div class="f2"><el-card class="box-card1">
  <div v-for="o in 4" :key="o" class="text item">
    {{'列表内容 ' + o }}
  </div>
</el-card></div>
</div></div>

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
                            date: this.$store.state.song_to_check,
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
                    pageSize: 5 // 每页的数据条数
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



<style>
  .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .box-card {
    width: 600px;
  }
  
  .box-card1 {
    width: 1200px;
  }
  
.div1{
    float: left;
}

.div2{
    float: left;
}

.f1 {
    width: 600px;
    border: 1px solid #F00;
    float: left;
}

.f2 {
    width: 600px;
    border: 1px solid #F00;
    float: left;
}
</style>