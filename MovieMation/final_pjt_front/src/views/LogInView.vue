<template>
  <div class="border border-dark m-3 me-5 p-5 rounded-2">
    <h1>로그인</h1>
    <hr>
    <!-- <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username">
      <hr>
      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password">
      <hr>
      <input 
        type="submit" 
        value="logIn"
      />
    </form> -->
    <b-container class= "center-block" style="width: 300px;padding:15px;">
      <b-col>
        <b-form @submit.prevent="logIn">
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
          <b-form-group id="password" label="비밀번호:" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="password"
              type="password"
              placeholder="비밀번호를 입력하세요"
              required
            ></b-form-input>
          </b-form-group>
          <br>
          <b-button type="submit" variant="primary">로그인</b-button>
        </b-form>
      </b-col>
    </b-container>

  </div>
</template>

<script>
// import {mapState, mapActions} from "vuex"

export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },

  // computed:{
  //   ...mapState(["isLogin"], "isLoginError")
  // },
  // methods: {
  //   ...mapActions(["login"])
  // }
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>