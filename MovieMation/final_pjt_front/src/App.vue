<template>
  <div id="app">
    <div>
      <img class= "logo" 
      src="./assets/moviemation_Agency_FB.png" 
      alt="logo"
      @click="goMovieHome"
    >
    </div>
    <b-navbar class="navbar navbar-expand-sm bg-dark navbar-dark" style="" :sticky=true>
      <div class="container-fluid">
        <div class="collapse navbar-collapse justify-content-center" id="collapsibleNavbar">
          <ul class="navbar-nav" v-if="this.$store.state.token">
            <li class="nav-item">
              <a class="nav-link">
                <router-link :to="{ name:'MovieView' }">
                  Home
                </router-link> 
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link :to="{ name:'RecommendView' }">
                  Recommend
                </router-link>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link :to="{ name:'UserStatusView'}">
                  UserInfo
                </router-link>
              </a>
            </li>
          </ul>
          <ul class="navbar-nav" v-if="!this.$store.state.token">
            <li class="nav-item">
              <a class="nav-link">
                <router-link :to="{ name:'MovieView' }">
                  Home
                </router-link>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link :to="{ name:'LogInView' }">
                  Login
                </router-link>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link :to="{ name:'SignUpView' }">
                  Signup
                </router-link>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </b-navbar>
    <router-view/>
  </div>
</template>

<script>
export default {
  methods:{
    goMovieHome(){
      if(this.$route.path!='/'){
        this.$router.push({ name:'MovieView' })
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color:silver;
  text-decoration-line: none;
}

nav a.router-link-exact-active {
  color: #b9333a;
}

.logo {
  width: 50vw;
  padding: 30px;
}
.nav-item{
  font-size: 25px;
}
.nav-link{
  margin: 0px 15px;
}

</style>
