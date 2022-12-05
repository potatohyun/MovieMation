<template>
  <div class="border border-dark m-3 me-5 me-5 rounded-2"  >
    <h1 >계정 생성</h1>
    <hr>
    <!-- <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username">
      <hr>
      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1">
      <hr>
      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      <hr>
      <input 
        type="submit"
        value="Signup"
      >
    </form> -->
    <b-container class= "center-block" style="width: 300px;padding:15px;">
      <b-col>
        <b-form @submit.prevent="signUp">
          <b-form-group id="username" label="아이디:" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="username"
              type="text"
              placeholder="아이디를 입력하세요"
              required
            ></b-form-input>
          </b-form-group>
          <br>
          <b-form-group id="password1" label="비밀번호:" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="password1"
              type="password"
              placeholder="비밀번호를 입력하세요"
              :state="validation_length"
              required
            ></b-form-input>
            <b-form-invalid-feedback :state="validation_length">
              비밀번호 길이는 8자 이상이어야 합니다.
            </b-form-invalid-feedback>
            <b-form-valid-feedback :state="validation_length">
              <!-- 적당한 길이입니다. 이 비밀버호는 안전합니다! -->
            </b-form-valid-feedback>
          </b-form-group>
          <br>
          <b-form-group id="password2" label="비밀번호 확인:" label-for="input-3">
            <b-form-input
              id="input-3"
              v-model="password2"
              type="password"
              placeholder="비밀번호를 다시 입력하세요"
              :state="validation_same"
              required
            ></b-form-input>
            <b-form-invalid-feedback :state="validation_same">
              비밀번호가 일치하지 않습니다.
            </b-form-invalid-feedback>
            <b-form-valid-feedback :state="validation_same">
              비밀번호가 일치합니다.
            </b-form-valid-feedback>
          </b-form-group>
          <br>
          <b-button type="submit" variant="primary">회원가입</b-button>
        </b-form>
      </b-col>
    </b-container>
    

    </div>

</template>

<script>
// import { mapActions} from "vuex";

export default {
  name: 'SignUpView',
  // data(){
  //   return{
  //     username: null,
  //     password1: null,
  //     password2: null,
  //   }
  // },
  // methods:{
  //   ...mapActions(["signup"])
  // }

  // 싸피에서 알려준 방법
  data() {
    return {
      username: "",
      password1: "",
      password2: "",
    }
  },
  computed:{
    validation_length(){
      return this.password1.length > 7
    },
    
    validation_same(){
      return this.password2.length>7 && this.password2 === this.password1
    },
    
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        // username,
        // password1,
        // password2,
        username: username,
        password1: password1,
        password2: password2,
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>
<style>

</style>