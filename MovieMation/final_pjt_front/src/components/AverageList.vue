<template>
  <div class="box mx-5" style="margin-bottom:100px; padding-left:17vw;">
    <br><h2><b style="color: blue;">평점</b>순으로 보여드립니당</h2><br>
    <div class="row row-cols-3 row-cols-md-5 g-4">
      <AverageListItem
        v-for="a_movie in averagemovies"
        :key="a_movie.id"
        :a_movie="a_movie"
      />
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import AverageListItem from '@/components/AverageListItem'

// const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'AverageList',
    components:{
      AverageListItem,
    }, 
    props:{
      averagemovies:Array
    },
    // data(){
    //   return{
    //     averagemovies : null,
    //   }
    // },
    // created(){
    //   this.averageMovies()
    // },
    // methods: {
    //   averageMovies() {
    //     axios({
    //       method: 'get',
    //       url: `${API_URL}/main/recommend/average/`,
    //     })
    //     .then((res)=>{
    //       console.log('평점으로 넘어오긴해')
    //       this.averagemovies=res.data
    //     })
    //     .catch(err=>console.log(err))
    //   }
    // }
}
</script>

<style>

</style>