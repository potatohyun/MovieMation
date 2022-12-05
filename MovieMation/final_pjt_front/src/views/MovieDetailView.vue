<template>
  <div class="contatiner">
    <div class="row">
      <div class="box col-4">
        <img id="imggg" :src="movie?.poster_path" alt="이미지가 없습니다." >
      </div>

      <div class="box col-8">

        <div class="row">

          <div class="layout ">
            <div class="col mt-5 mb-4 ms-2" style="text-align:left">
              <h1 >{{movie?.title}}</h1> 
            </div >

            <div class="col d-flex flex-wrap p-3 rounded-2 " id="overview-scroll" >
              <h5 class="col">
                {{movie?.overview}} {{getSummary()}}
              </h5>
            </div>

            <div class="border border-dark m-3 me-5" id="testest">
              <div class="d-flex justify-content-between mx-3 mt-3 me-5" >
                <h3>RE:VIEW</h3>
                <div style="font-size:1.4vw;" @click="createComment">[리뷰쓰기]</div>
              </div>
              <div id="overview-scroll2">
                <div class="col ms-3" style="text-align:left">
                  <!-- <router-link style="text-align:right" :to="{ name : 'CommentCreateView' }">[댓글쓰기]</router-link> -->
                  <CommentList :comments="movie?.comments"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'
import CommentList from '@/components/CommentList'

const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'MovieDetailView',
    components:{
      CommentList,
    }, 
    data(){
      return{
        movie : null,
        summary : null,
      }
    },
    created(){
      this.getMovieDetail()
    },
    methods:{
      getMovieDetail(){
        axios({
          method: 'get',
          url: `${API_URL}/main/movies/${this.$route.params.id}`,
        })
        .then((res)=>{
          console.log(res.data.overview)
          this.movie=res.data
        })
        .catch((err)=>{
          console.log(err)
          alert("잘못된 접근입니다! 홈으로 이동합니다.")
          router.push({ name: "MovieView" })
        })

      },
      createComment(){
        if(this.$store.state.token === null){
          alert("로그인이 필요합니다.")
          this.$router.push({name : 'LogInView'})
        }else{
          router.push ({ name : 'CommentCreateView' })
        }
        
      },
      getSummary(){
        if(this.movie?.overview===""){
          return this.summary = "줄거리가 없습니다."
        }
      }
    },
    
}
</script>

<style>
#imggg {
  width: 100%;
  object-fit: cover;
}
/* #overview-scroll{
  overflow:auto; 
  width:1350px;
  height:200px;
  background-color: cornsilk;
} */
/* style="overflow:auto; width:63vw; height:13vw; text-align:left" */
#overview-scroll{
  overflow:auto; 
  width:62vw; 
  height:13vw; 
  text-align:left;
  background-color: rgb(255, 239, 177);
  margin-left: 15px;
}
#testest{
  height: 26vw
}
#overview-scroll2{
  overflow:auto; 
  width: 100%;
  height:22.5vw;
  text-align:left;
  background-color: cornsilk;
}
</style>