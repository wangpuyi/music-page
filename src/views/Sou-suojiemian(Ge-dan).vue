
<template>

<h2 font-family="楷体">
        搜索：{{ this.$store.state.search_res }}
        
    </h2>

    <h3>
        共找到{{ SongsData.length}}条相关内容
    </h3>
            

    <div class="btn">
               <button @click="con0" style="width:10%; height:10%;back">歌单<i class="icon-sprite"></i></button>
                <button @click="con1" style="width:10%; height:10%;back">歌曲<i class="icon-sprite"></i></button>
                <button @click="con2" style="width:10%; height:10%;back">歌手<i class="icon-sprite"></i></button>
      </div>

    <div v-show="this.$store.state.show1 == 1">
        <!-- 表格 -->
        <el-table :data="SongsData.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%" @row-click="openDialog">
           
   
           
            <el-table-column prop="name" label="歌单名称" width="300" >
            </el-table-column>
            <el-table-column prop="listid" label="歌单编号" width="300" >
            </el-table-column>
        </el-table>
        <div class="block" style="margin-top:15px;">
            <el-pagination align='center' @size-change="handleSizeChange" @current-change="handleCurrentChange" 
            :current-page="currentPage" 
            :page-sizes="[1,5,10,20]" 
            :page-size="pageSize" 
            layout="total, sizes, prev, pager, next, jumper" 
            :total="SongsData.length">
            </el-pagination>
        </div>
        </div>
      <div v-show="this.$store.state.show2 == 1">
        <el-table :data="SongsData.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%" @row-click="openDialog1">
           
   
           
           <el-table-column prop="title" label="歌曲名称" width="300" >
           </el-table-column>
           <el-table-column prop="songid" label="歌曲编号" width="300" >
           </el-table-column>
          </el-table>
        <!-- 分页器 -->
        <div class="block" style="margin-top:15px;">
            <el-pagination align='center' @size-change="handleSizeChange" @current-change="handleCurrentChange" 
            :current-page="currentPage" 
            :page-sizes="[1,5,10,20]" 
            :page-size="pageSize" 
            layout="total, sizes, prev, pager, next, jumper" 
            :total="SongsData.length">
            </el-pagination>
        </div>

        </div>
      <div v-show="this.$store.state.show3 == 1">
        <el-table :data="SongsData.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%" @row-click="openDialog2">
           
   
           
           <el-table-column prop="name" label="歌手名称" width="300" >
           </el-table-column>
           <el-table-column prop="summary" label="歌手编号" width="300" >
           </el-table-column>
           
       </el-table>

       

        <!-- 分页器 -->
        <div class="block" style="margin-top:15px;">
            <el-pagination align='center' @size-change="handleSizeChange" @current-change="handleCurrentChange" 
            :current-page="currentPage" 
            :page-sizes="[1,5,10,20]" 
            :page-size="pageSize" 
            layout="total, sizes, prev, pager, next, jumper" 
            :total="SongsData.length">
            </el-pagination>
        </div>
    </div>
 
</template>
 
  <script>
        export default {
            data() {
                return {
                    
   
                  SongsData:[
                    {
                        "listid":"2626492658"
                        ,
                        "name":"粤语情歌世界最深情的歌V"
                    }
                  ],
                    currentPage: 1, // 当前页码
                    total: 20, // 总条数
                    pageSize: 5, // 每页的数据条数
                    name:'',
            author:'',
            songids:'',
            views:'',
            des:'',
            label:''
                };
            },

            mounted(){
                this.initData()

            },
            
            watch: {
		'$route' (to, from) {
			this.initData(); // 这是我ajax获取用户信息的方法
		}},


            methods: {
              initData () {
      //id=(this.$route.query.listid)
      const payload = {
          'search' :this.$store.state.search_res
          
        }
      this.$axios.get('http://127.0.0.1:5000/search',{params:payload}).then(res => {    
            console.log(res.data)
            this.SongsData = res.data

      })
      
    } ,
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
        this.$router.push({path: '/Ge-danneibu',query: {listid:row.listid}})
        console.log(row.listid)
        //this.$router.push({path: '/Ge-qujiemian'}),
        //this.$store.commit('changesong_ID',row.currentsong_ID)
        console.log( (this.$store.state.currentsong_ID))
  },openDialog1(row) {
        this.$router.push({path: '/Ge-qujiemian',query: {id:row.songid}})
        console.log(row.songid)
        //this.$router.push({path: '/Ge-qujiemian'}),
        //this.$store.commit('changesong_ID',row.currentsong_ID)
        console.log( (this.$store.state.currentsong_ID))
  },openDialog2(row) {
        this.$router.push({path: '/Ge-danneibu',query: {listid:row.listid}})
        console.log(row.listid)
        //this.$router.push({path: '/Ge-qujiemian'}),
        //this.$store.commit('changesong_ID',row.currentsong_ID)
        console.log( (this.$store.state.currentsong_ID))
  },
  con1(){
    const payload = {
          'search' :this.$store.state.search_res
          }
      this.$axios.get('http://127.0.0.1:5000/searchsong',{params:payload}).then(res => {    
            console.log(res.data)
            this.SongsData = res.data
            this.$store.state.show1=0
            this.$store.state.show2=1
            this.$store.state.show3=0
    })
    
    
  },
  con2(){
    const payload = {
          'search' :this.$store.state.search_res
          }
      this.$axios.get('http://127.0.0.1:5000/searchsinger',{params:payload}).then(res => {    
            console.log(res.data)
            this.SongsData = res.data
            this.$store.state.show1=0
            this.$store.state.show2=0
            this.$store.state.show3=1
    })
    
    
  },con0(){
    const payload = {
          'search' :this.$store.state.search_res
          }
      this.$axios.get('http://127.0.0.1:5000/search',{params:payload}).then(res => {    
            console.log(res.data)
            this.SongsData = res.data
            this.$store.state.show1=1
            this.$store.state.show2=0
        this.$store.state.show3=0
    })
    
    
  }}}
</script>



<style>
  .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .box-card {
    width: 100px;
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
    width: 100px;
    border: 1px solid #F00;
    float: left;
}

.f2 {
    width: 600px;
    border: 1px solid #F00;
    float: left;
}
</style>