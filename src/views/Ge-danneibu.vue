
   
    

<template>


  <div>
    <h1>{{ this.$store.state.gedanneibu_name }}</h1>
    <div class="wrapper">

      <div class="f1">
        <el-card class="box-card">
          <el-image style="width: 360px; height: 350px" :src="this.$store.state.gedanneibu_url" :fit="cover">


          </el-image>
        </el-card>
      </div>

      <div class="f2">
        <el-card class="box-card1">
          <div class="text item">
            创建者：{{ this.$store.state.gedanneibu_author }}
          </div>
          <div class="text item">
            播放量：{{ this.$store.state.gedanneibu_views }}
          </div>
          <div class="text item">
            标签：{{ this.$store.state.gedanneibu_label }}
          </div>

          <div class="text item">
            {{ this.$store.state.gedanneibu_des }}
          </div>

        </el-card>
      </div>
    </div>
  </div>

  <div>
    <!-- 表格 -->
    <el-table :data="this.$store.state.gedanneibu_SongsData.slice((currentPage - 1) * pageSize, currentPage * pageSize)"
      style="width: 100%" @row-click="openDialog">


      <el-table-column prop="title" label="标题" width="480" height="150">
      </el-table-column>
      <el-table-column prop="singer" label="歌手" width="480">
      </el-table-column>
      <el-table-column prop="album" label="专辑" width="480">
      </el-table-column>
    </el-table>


    <!-- 分页器 -->
    <div class="block" style="margin-top:15px;">
      <el-pagination align='center' @size-change="handleSizeChange" @current-change="handleCurrentChange"
        :current-page="currentPage" :page-sizes="[1, 5, 10, 20]" :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper" :total="SongsData.length">
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
      name: '',
      author: '',
      songids: '',
      views: '',
      des: '',
      url: '',
      label: '',
    };
  },

  mounted() {
    console.log(this.$route.query.listid)
    console.log(this.$store.state.gedanneibu_id)

    if (this.$store.state.gedanneibu_id != this.$route.query.listid) {
      this.$store.commit('Ge_danneibu_cache', { id: this.$route.query.listid, label: "loading", name: "loading", author: "loading", SongsData: [], views: "loading", des: "loading", url: "https://tupian.qqw21.com/article/UploadPic/2020-4/20204717444472684.jpg" })

      this.initData()
    }

  },

  methods: {
    initData() {
      //id=(this.$route.query.listid)
      this.$axios.get('http://127.0.0.1:5000/list1/' + this.$route.query.listid).then(res => {
        // this.datetime = res.data.listid
        //console.log(res.data)
        //let i = 0;

        console.log(res.data)
        this.label = res.data.label
        this.name = (res.data.name)
        this.author = (res.data.author)
        //const payload = {'ids':res.data.ids}
        this.SongsData = res.data.SongsData
        this.views = (res.data.views)
        this.des = (res.data.description)
        this.url = res.data.listimage
        this.$store.commit('Ge_danneibu_cache', { id: this.$route.query.listid, label: this.label, name: this.name, author: this.author, SongsData: res.data.SongsData, views: res.data.views, des: res.data.description, url: res.data.listimage })


      })

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
      this.$router.push({ path: '/Ge-qujiemian', query: { id: row.songid } })
      //this.$router.push({path: '/Ge-qujiemian'}),
      //this.$store.commit('changesong_ID',row.currentsong_ID)
      console.log((this.$store.state.currentsong_ID))
      this.$store.commit('Same_gedan')
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
  width: 395px;
}

.box-card1 {
  width: 1203px;
  height: 394px;
}

.div1 {
  float: left;
}

.div2 {
  float: left;
}

.f1 {
  width: 395px;
  border: 1px solid #F00;
  float: left;
}

.f2 {
  width: 1205px;
  height: 396px;
  border: 1px solid #F00;
  float: left;
}
</style>