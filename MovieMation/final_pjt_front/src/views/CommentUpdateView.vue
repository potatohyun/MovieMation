<template>
    <div class="border border-dark m-3 me-5 me-5 rounded-2 py-4">
      <h1>댓글 수정</h1><hr>
      <!-- <form @submit.prevent="updateComment">
        <label for="title">제목: </label>
        <input type="text" id="title" v-model="comment.title"><br>
        <label for="content">내용: </label>
        <textarea 
          id="content" cols="30" rows="10"
          v-model="comment.content">
        </textarea><br>
        <label for="grade">평점: </label>
        <input type="int" id="grade" v-model="comment.grade">
        <input type="submit" id="submit">
      </form> -->
      <b-form @submit.prevent="updateComment">
      <b-container class= "center-block" style="width: 500px;padding:15px;">
        <b-col>
          <b-form-group id="title" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="comment.title"
              type="text"
              placeholder="제목을 입력하세요"
              required
            ></b-form-input>
          </b-form-group>
          <br>
          <b-form-group>
            <b-form-textarea
              id="content"
              v-model="comment.content"
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
          <b-form-rating v-model="comment.grade" color="#ff8800"></b-form-rating>
        <b-input-group-append>
          <b-button @click="grade = null">Clear</b-button>
        </b-input-group-append>
        </b-input-group>
      </b-container>
      <b-button type="submit" id="submit" variant="primary">제출</b-button>
    </b-form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import router from '@/router'
  const API_URL = "http://127.0.0.1:8000"
  // const ID = ""
  
  export default {
      name: 'CommentUpdateView',
      props: {
        pk:Number
      },
      data(){
        return{
          comment : null,
          // title : null,
          // content : null,
          // grade : null,
        }
      },
      created(){
        this.getCommentDetail()
      },
      methods:{
        getCommentDetail(){
            axios({
                method: 'get',
                url: `${API_URL}/main/comment/${this.$route.params.pk}`,
                headers:{
                    Authorization: `Token ${ this.$store.state.token }`
                }
            })
            .then((res)=>{
                console.log(res)
                this.comment=res.data
            })
            .catch(err=>console.log(err))
        },
        updateComment(){
          const title = this.comment.title
          const content = this.comment.content
          const grade = this.comment.grade
          // if(!title){
          //   alert('제목이 없어요')
          //   return
          // } else if(!content){
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
            method: 'put',
            url:`${API_URL}/main/comment/${this.$route.params.pk}/`,
            headers:{
                    Authorization: `Token ${ this.$store.state.token }`
                },
            data: {title, content, grade},
  
          })
            .then((res)=>{
              console.log(res)
              alert("리뷰가 수정되었습니다.")
              router.push({ name: "MovieDetailView" })
            })
            .catch(err=>console.log(err))
        }
      }
  }
  </script>
  
  <style>
  
  </style>