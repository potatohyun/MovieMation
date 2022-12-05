<template>
  <div >
    <div class="border border-dark m-3 me-5 me-5 rounded-2 py-4" >
     <h1>댓글 작성</h1><hr>
    <!--<form @submit.prevent="createComment">
      <label for="title">제목: </label>
      <input type="text" id="title" v-model="title"><br>
      <label for="content">내용: </label>
      <textarea 
        id="content" cols="30" rows="10"
        v-model="content">
      </textarea><br>
      <label for="grade">평점: </label>
      <input type="int" id="grade" v-model="grade">
      <input type="submit" id="submit">
      유저
      <label for="user">user: </label>
      <input type="int" id="user" v-model="user">
      <input type="submit" id="submit">
    </form> -->
    <b-form @submit.prevent="createComment">
      <b-container class= "center-block" style="width: 500px;padding:15px;">
        <b-col>
          <b-form-group id="title" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="title"
              type="text"
              placeholder="제목을 입력하세요"
              required
            ></b-form-input>
          </b-form-group>
          <br>
          <b-form-group>
            <b-form-textarea
              id="content"
              v-model="content"
              type="text"
              placeholder="내용을 입력하세요"
              rows="3"
              required
            ></b-form-textarea>
          </b-form-group>          
        </b-col>
      </b-container>
      <b-container class= "center-block" style="width: 300px;padding:15px;">
        <b-input-group id="grade" label="평점:" label-for="input-3">
          <b-form-rating v-model="grade" color="#ff8800"></b-form-rating>
        <b-input-group-append>
          <b-button @click="grade = null">Clear</b-button>
        </b-input-group-append>
        </b-input-group>
      </b-container>
      <b-button type="submit" id="submit" variant="primary">제출</b-button>
    </b-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

const API_URL = "http://127.0.0.1:8000"
// const ID = ""

export default {
    name: 'CommentCreateView',
    props: {
      id:Number
    },
    data(){
      return{
        title : '',
        content : '',
        grade : 0,
        // userid : this.$store.state.username
        // user : null,
      }
    },
    methods:{
      // getToken: function () {
      //   const config = {
      //     headers:{
      //       Authorization: `Token ${ this.$store.state.token }`
      //     }
      //   }
      //   return config
      // },
      getToken: function(){
        const key = this.$store.state.token
        const config = {
          headers:{
            Authorization: `Token ${key}`
          }
        }
        return config
      },
      createComment: function(){
      //   const config = this.getToken()

      //   const reviewItem = {
      //   title: this.title,
      //   content: this.content,
      //   grade: this.grade,
      // }
      // console.log(reviewItem)
      // if (reviewItem.title) {
      //   axios.post(`${API_URL}/main/movies/${this.$route.params.id}/createcomments/`, reviewItem, config)
      //     .then((res)=>{
      //       console.log(res)
      //       alert("소중한 리뷰 고맙습니다!")
      //       router.push({ name: "MovieDetailView" })
            
      //     })
      //     .catch((err) => {
      //       console.log(err)
      //     })
      // } 

        const title = this.title
        const content = this.content
        const grade = this.grade
        // const userid = this.userid

        // if(!title){
        //   alert('제목이 없어요')
        //   return
        // } else if(!content){
        //   console.log(this.title)
        //   console.log(title)
        //   alert('내용이 없어요')
        //   return
        // } else if(!grade){
        //   alert('평점주세요!')
        //   return
        // }
        if(grade===0){
          alert('0점은 좀....ㅠㅠㅠ')
          return
        }

        axios({
          method: 'post',
          url: `${API_URL}/main/movies/${this.$route.params.id}/createcomments/`,
          headers:{
                    Authorization: `Token ${ this.$store.state.token }`
                },
          data : {title, content, grade}
          })
          .then((res)=>{
            console.log(res)
            console.log(res.data)
            console.log(res.data.username)
            alert("소중한 리뷰 고맙습니다!")
            router.push({ name: "MovieDetailView" })
            
          })
          .catch((err)=>{
            console.log(err)
          })
          
      }
    }
}
</script>

<style>

</style>
