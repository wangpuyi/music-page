
<template>

<h2 font-family="楷体">
        搜索：{{ this.$store.state.search_res }}
        
    </h2>

    <h3>
        共找到{{ this.$store.state.SongsData.length}}条相关内容
    </h3>
            

    <div class="btn">
               <el-button  :type='type1' @click="con0" style="width:10%; height:10%;">歌单<i class="icon-sprite"></i></el-button>
                <el-button :type='type2' @click="con1" style="width:10%; height:10%;back">歌曲<i class="icon-sprite"></i></el-button>
                <el-button :type='type3' @click="con2" style="width:10%; height:10%;back">歌手<i class="icon-sprite"></i></el-button>
      </div>

    <div v-show="this.$store.state.show1 == 1">
        <!-- 表格 -->
        <el-table :data="this.$store.state.SongsData.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%" @row-click="openDialog">
           
   
           
            <el-table-column prop="name" label="歌单名称" width="300" >
            </el-table-column>
            <el-table-column prop="author" label="创建者" width="300" >
            </el-table-column>
            <el-table-column prop="views" label="播放量" width="300" >
            </el-table-column>
            <el-table-column prop="label" label="标签" width="300" >
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
        <!---->
        <el-table :data="this.$store.state.SongsData.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%" @row-click="openDialog1">
           
           <el-table-column prop="title" label="歌曲名称" width="300" >
           </el-table-column>
           <el-table-column prop="singer" label="歌手" width="300" >
           </el-table-column>
           <el-table-column prop="album" label="专辑" width="300" >
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

        <el-table :data="this.$store.state.SongsData.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%" @row-click="openDialog2">
           
           <el-table-column prop="name" label="歌手名称" width="300" >
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
                    type1: 'primary',
                    type2: '',
                    type3: '',
   
                  SongsData:[
                   
                  ],
                    currentPage: 1, // 当前页码
                    total: 20, // 总条数
                    pageSize: 10, // 每页的数据条数
                    name:'',
            author:'',
            songids:'',
            views:'',
            des:'',
            label:''
                };
            },

            mounted(){
               console.log('mounted')
                
                this.initData()
              
            },
            
            watch: {
		'$route' (to, from) {
      this.$store.state.pt=1
     this.initData()
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
            if (this.$store.state.pt == 1)
            {this.$store.state.SongsData = res.data
              this.$store.state.pt = 0
            }
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
        this.$router.push({path: '/Ge-shoujiemian',query: {name:row.name}})
        console.log(row.name)
        //this.$router.push({path: '/Ge-qujiemian'}),
        //this.$store.commit('changesong_ID',row.currentsong_ID)
        console.log( (this.$store.state.currentsong_ID))
  },
  con1(){
    this.type1 = ''
    this.type2 = 'primary'
    this.type3 = ''
    const payload = {
          'search' :this.$store.state.search_res
          }
      this.$axios.get('http://127.0.0.1:5000/searchsong',{params:payload}).then(res => {    
            console.log(res.data)
            this.SongsData = res.data
            this.$store.state.SongsData=this.SongsData
            this.$store.state.show1=0
            this.$store.state.show2=1
            this.$store.state.show3=0
    })
    
    
  },
  con2(){
    this.type1 = ''
    this.type2 = ''
    this.type3 = 'primary'
    const payload = {
          'search' :this.$store.state.search_res
          }
      this.$axios.get('http://127.0.0.1:5000/searchsinger',{params:payload}).then(res => {    
            console.log(res.data)
            this.SongsData = res.data
            this.$store.state.SongsData=this.SongsData
            this.$store.state.show1=0
            this.$store.state.show2=0
            this.$store.state.show3=1
    })
    
    
  },con0(){
    this.type1 = 'primary'
    this.type2 = ''
    this.type3 = ''
    const payload = {
          'search' :this.$store.state.search_res
          }
      this.$axios.get('http://127.0.0.1:5000/search',{params:payload}).then(res => {    
            console.log(res.data)
            this.SongsData = res.data
            this.$store.state.SongsData=this.SongsData
            this.$store.state.show1=1
            this.$store.state.show2=0
        this.$store.state.show3=0
    })
    
    
  }}}
</script>



<style>
.button{
  background-color: azure;
}
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