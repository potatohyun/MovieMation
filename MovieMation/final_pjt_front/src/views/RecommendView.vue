<template>
  <div>
    <nav class="recommend-nav" >
      <ul class="menu">
        <li @click="onclick"><router-link id="link" :to="{ name:'PopularityView' }" style="font-size:1.7vw;">인기순</router-link></li>
        <li @click="onclick"><router-link id="link" :to="{ name:'AverageView' }" style="font-size:1.7vw;">평점순</router-link></li>
        <li @click="onclick"><router-link id="link" :to="{ name:'RandomView' }" style="font-size:1.7vw;">랜덤!</router-link></li>
      </ul>
    </nav>
    <router-view />
    <div v-if="!clicked" class="box mx-5" style="margin-bottom:100px; padding-left:17vw;">
    <br><h2>←&nbsp;&nbsp;추천항목을 클릭해주세요</h2>
    </div>
  </div>
</template>

<script>

export default {
  name: 'RecommendView',
  data(){
    return{
      clicked:false
    }
  },
  methods:{
    onclick(){
      this.clicked = true
    }
  }
}
</script>

<style>
li{
  list-style: none;
}
.recommend-nav{
  /* width: 200px; */
  width: 18vw;
  /* background-color: rgb(184, 184, 184); */
  background-color: rgb(226, 226, 226);
  /* border-right: 3px solid rgb(184, 184, 184); */
  
  position: fixed;
  height: 100%;
  padding: 0%;
  /* padding-top: 20px; */
}
.menu li #link{
  height: 70px;
  line-height: 25px;
  display:block;
  /* padding: 0px 20px; */
  font-size: 16px;
  color: black;
  text-decoration-line: none;
}
.menu li #link:hover {
  background-color: rgb(65, 64, 64); /* 마우스 올렸을때 배경색*/
  color: rgb(255, 47, 47) /* 마우스 올렸을때 글자색*/
}
.menu{
  padding: 0%;
}
a{
  padding-top: 25px;
}
/* #link{ */
  /* border-bottom: 1px solid rgb(255, 255, 255); /*이게 제일 무난한거같기도.. 근데 위에 네브바랑 같이 적용됨*/
  /* border-bottom: 1px solid rgb(181, 181, 181); */
/* } */
</style>