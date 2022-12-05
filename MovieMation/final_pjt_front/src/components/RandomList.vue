<template>
  <div class="box mx-5" style="margin-bottom:100px; padding-left:17vw;"><!-- 마진바텀 다른데에도 페이지 넘김 그런거로 하면 해야함 -->
    <br><h2>고르기 어려우시다구요?<br>그럼 이건 어떤가요?</h2>
    <div class="re-btn">
      <button type="button" class="btn btn-outline-danger" id="retry" @click="randomMovies">다시뽑기</button>
    </div><div class="row row-cols-3 row-cols-md-5 g-4">
    <RandomListItem
      v-for="r_movie in randommovies"
      :key="r_movie.id"
      :r_movie="r_movie"
    />
    </div>
    
    
  </div>
</template>

<script>
import axios from 'axios'
import RandomListItem from '@/components/RandomListItem'

const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'RandomList',
  components:{
    RandomListItem,
  }, 
  data(){
    return{
      randommovies : null,
    }
  },
  created(){
    this.randomMovies()
  },
  methods: {
    randomMovies() {
      axios({
        method: 'get',
        url: `${API_URL}/main/recommend/random/`,
      })
      .then((res)=>{
        this.randommovies=res.data
      })
      .catch(err=>console.log(err))
    }
  }
}
</script>

<style>
/* .re-btn{
  margin-top: 30px;
} */
.re-btn{
  margin-top: 20px;
  margin-bottom:25px;
}
#retry{
  width:11vw;
  margin:auto;
  font-size: 1.3vw;
  /* display:block; */
  /* style="display: flex; justify-content: center;" */
}
</style>