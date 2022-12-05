<template>
  <div class="col">
    <div class="card h-100" @click="goMovieDetail">
      <img class="movieimg mb-3" :src="getImgUrl" alt="">
      <div class="title">
        <b>{{ movie.title }}</b>
      </div>

      <!-- <div class="link">
        <router-link 
          :to="{ 
            name : 'MovieDetailView',
            params: {id:movie.id}
          }"
        >
        <button type="button" class="btn btn-outline-danger btn-sm">영화정보보기</button>
        [영화정보보기] 
        </router-link>
      </div> -->

    </div>
  </div>
</template>

<script>

export default {
  name: 'MovieListItem',
  props: {
    movie:Object,
  },
  data() {
    return{
      getImgUrl: `${this.movie?.poster_path}`,
    }
  },
  methods:{
    goMovieDetail(){
      this.$router.push({name : 'MovieDetailView', params: {id:this.movie.id}})
    }
  }
}
</script>

<style>
.movieimg{
  height: 23vw;
  object-fit:cover
}
</style>