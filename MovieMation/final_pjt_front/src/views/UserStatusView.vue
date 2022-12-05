<template>
    <div class="border border-dark m-3 me-5 me-5 rounded-2 pt-5 pb-3">
      <h1>{{username}}님 안녕하세요?</h1>
      
      <div class="re-btn">
        <button type="button" class="btn btn-outline-dark"  @click="logOut">로그아웃</button>
      </div><hr>
      <div>
      <MyReviewList
      :myreviews="myreviews"
      />
      
      <!-- <b-container class= "center-block" style="width: 300px;padding:15px;">
      <b-col>
        <b-form @submit.prevent="changePassword">
          <b-form-group id="new_password1" label="새로운 비밀번호:" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="new_password1"
              type="password"
              placeholder="비밀번호를 입력하세요"
              required
            ></b-form-input>
          </b-form-group>
          <br>
          <b-form-group id="new_password2" label="비밀번호 재확인:" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="new_password2"
              type="password"
              placeholder="비밀번호를 다시 입력하세요"
              required
            ></b-form-input>
          </b-form-group>
          <br>
          <b-button type="submit" variant="primary">비밀번호수정</b-button>
        </b-form>
      </b-col>
    </b-container> -->
      </div>
    </div>
  </template>
  
  <script>
  const API_URL = "http://127.0.0.1:8000"
  import axios from 'axios'
  import MyReviewList from '@/components/MyReviewList'

  export default {
    name: 'UserStatusView',
    components:{
      MyReviewList,
    },
    data(){
      return{
        username : null,
        myreviews : null,
        // new_password1: null,
        // new_password2: null,
      }
    },
    created(){
      this.getUsername()
      this.getMyReviews()
    },
    // 싸피에서 알려준 방법
    
    methods: {
      getToken: function (){
        const key = this.$store.state.token

        const config = {
          headers:{
              Authorization: `Token ${ key }`
          }
        }
      return config
      },
      logOut() {
        this.$store.dispatch('logOut')
      },
      getUsername(){
        const config = this.getToken()
        axios.get(`${API_URL}/accounts/user/`, config)
        .then((res) => {
          console.log(res.data)
          this.username = res.data.username
        }
      )},
      getMyReviews(){
        const config = this.getToken()
        axios.get(`${API_URL}/main/mypage`, config)
        .then((res)=>{
          console.log(res.data)
          this.myreviews = res.data
        })
        .catch(err=>console.log(err))
      }
      // changePassword(){
      //   const new_password1 = this.new_password1
      //   const new_password2 = this.new_password2

      //   const payload = {
      //     new_password1: new_password1,
      //     new_password2: new_password2
      //   }
      //   this.$store.dispatch('changePassword', payload)
      // }
    }
  }
  </script>