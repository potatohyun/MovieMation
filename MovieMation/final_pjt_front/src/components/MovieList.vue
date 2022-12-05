<template><!-- -->
  <div class="box mx-5"> <!-- 양쪽에 마진넣은거-->
    <!-- <br>
    <h1>MOVIE LIST</h1> 
    <br> --> 
    <!-- 아래 꺼에서 각각ㄱ이 뭔지 명확히좀 알아야할듯 -->
    <div class="row row-cols-3 row-cols-md-5 g-4">  <!-- row-cols-1 row-cols-md-3 두개 뭔차이야(뒤에껀 대충알겠는데 앞에껀 뭐야)-->
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem';

export default {
    name: 'MovieList',
    components:{
        MovieListItem
    },
    computed: {
      movies() {
        return this.$store.state.movies
      }
    }

}
</script>

<style>

</style>