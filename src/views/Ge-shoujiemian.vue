<template>

<div>
  <h1>{{ name }}</h1>
<div class="wrapper">
    <div class="f1"><el-card class="box-card">
      <el-image
      style="width: 350px; height: 350px"
      :src="url"
      :fit="fit">
 

 </el-image>
</el-card></div>
    <div class="f2"><el-card class="box-card1">
      <div  class="text item">
    歌手：{{ name }}
  </div>

  <div  class="text item">
    简介：{{ des }}
  </div>

</el-card></div>
</div></div>


  <div>
    <!-- 表格 -->
    <el-table
      :data="SongsData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
      style="width: 100%"
      @row-click="openDialog"
    >
      <el-table-column prop="title" label="标题" width="280"> </el-table-column>
      <el-table-column prop="singer" label="歌手" width="180">
      </el-table-column>
      <el-table-column prop="album" label="专辑" width="180"> </el-table-column>
    </el-table>

    <!-- 分页器 -->
    <div class="block" style="margin-top: 15px">
      <el-pagination
        align="center"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[1,5,10,20]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="SongsData.length"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        SongsData: [],
        currentPage: 1, // 当前页码
        total: 20, // 总条数
        pageSize: 5, // 每页的数据条数
        name: "bird",
        des:"很懒sddddddddddddddddddsssssssssssssssssss",
        url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
      };
    },

    mounted() {
      this.initData();
    },

    methods: {
      initData() {
        //id=(this.$route.query.listid)
        this.$axios
          .get("http://127.0.0.1:5000/list1/" + this.$route.query.listid)
          .then((res) => {
            // this.datetime = res.data.listid
            //console.log(res.data)
            //let i = 0;
            console.log(res.data);
            this.label = res.data.label;
            this.name = res.data.name;
            this.author = res.data.author;
            //const payload = {'ids':res.data.ids}
            this.SongsData = res.data.SongsData;
            this.views = res.data.views;
            this.des = res.data.description;
          });
      //把这里改成歌手的相关内容即可
        },

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
      },

      openDialog(row) {
        console.log(row.songid);
        this.$router.push({ path: "/Ge-qujiemian", query: { id: row.songid } });
        //this.$router.push({path: '/Ge-qujiemian'}),
        //this.$store.commit('changesong_ID',row.currentsong_ID)
        console.log(this.$store.state.currentsong_ID);
      },
    },
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
    width: 400px;
  }
  
  .box-card1 {
    
    width: 600px;
    height: 390px;
  }
  
.div1{
    float: left;
}

.div2{
    float: left;
}

.f1 {
    width: 400px;
    border: 1px solid #F00;
    float: left;
}

.f2 {
    width: 600px;
    height: 396px;
    border: 1px solid #F00;
    float: left;
}
</style>
