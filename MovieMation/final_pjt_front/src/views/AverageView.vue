<template>
  <div>
    <!-- <h1>AverageView</h1> -->
    <AverageList
    :averagemovies="averagemovies"
    />
  </div>
</template>

<script>
import axios from 'axios'
import AverageList from '@/components/AverageList'

const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'AverageView',
    components:{
      AverageList,
    },
    data(){
      return{
        averagemovies : null,
      }
    },
    created(){
      this.averageMovies()
    },
    methods: {
      averageMovies() {
        axios({
          method: 'get',
          url: `${API_URL}/main/recommend/average/`,
        })
        .then((res)=>{
          // console.log('평점으로 넘어오긴해')
          this.averagemovies=res.data
        })
        .catch(err=>console.log(err))
      }
    }
}
</script>

<style>

</style>