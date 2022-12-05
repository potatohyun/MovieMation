<template>
  <div>
    <PopularityList
    :popularitymovies="popularitymovies"
    /> <!--  자식한테 내려주는거 추가-->
  </div>
</template>

<script>
import axios from 'axios'
import PopularityList from '@/components/PopularityList'

const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'PopularityView',
    components:{
      PopularityList,
    },
    data(){
      return{
        popularitymovies : null,
      }
    },
    created(){
      this.popularityMovies()
    },
    methods: {
      popularityMovies() {
        axios({
          method: 'get',
          url: `${API_URL}/main/recommend/popularity/`,
        })
        .then((res)=>{
          this.popularitymovies=res.data
        })
        .catch(err=>console.log(err))
      }
    }

}
</script>

<style>

</style>