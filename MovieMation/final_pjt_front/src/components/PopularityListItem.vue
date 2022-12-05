<template>
  <div class="col">
    <div class="card h-100" @click="goMovieDetail">
      <img class="movieimg mb-3" :src="getImgUrl" alt="">
        <div>
          <b>{{ p_movie.title }}</b>
        <!-- <p>{{ p_movie.overview }}</p>
        <p>인기도 : {{ p_movie.popularity }}</p>
        <p>개봉일 : {{ p_movie.release_date }}</p> -->

        <!-- <router-link 
          :to="{ 
            name : 'MovieDetailView',
            params: {id:p_movie.id}
          }"
        >
          [영화정보보기]
        </router-link>  -->
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PopularityListItem',
  props: {
    p_movie:Object,
  },
  data() {
    return{
      getImgUrl: `${this.p_movie?.poster_path}`
    }
  },
  methods:{
    goMovieDetail(){
      this.$router.push({name : 'MovieDetailView', params: {id:this.p_movie.id}})
    }
  }
}
</script>

<style>
.movieimg{
  height: 23vw;
  width: auto;
  object-fit:cover
}
</style>