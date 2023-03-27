
<script lang="ts">

import  { router } from '../router'
import { defineComponent } from 'vue';
import { User, URL } from "../context/context"

  export type LogData = {
    password: string,
    username: string,
  };

  export default defineComponent({
    name:"signin",
    data(){
      return{
        user_login: {
          username: "",
          password: "",
        } as LogData,
      }
    },
    methods: {
      async login(): Promise<void>{
        let response: Response = await fetch(`${URL}/api/sign_in/`, {
          method: "POST",
          credentials: "include",
          mode: "cors",
          referrerPolicy: "no-referrer",
          body: JSON.stringify(this.user_login)
        })

        let check_user: User = await response.json()

        if (check_user.username != null){
          console.log("Login Successfull")
          router.push({ path: '/Home' })
        }
        else{
          alert("Username/password incorrect")
          console.log("Login Unsuccessfull")
        }
      },
    }
  })
</script>

<template>
  <div class="vh-100" style="background-color:#0096FF">
    <div class="vh-100 d-flex justify-content-center " style= "background-color:#191970">
      <form class="w-50 m-5 rounded text-black" style="background-color: #191970;">
          <div class = "form-signup justify-content-center text-center bg-primary rounded ">
            <h1 class="header-login p-4 text-center bold  bg-primary">Login Form</h1>

          <div class="form-group form-outline form-dark  m-4">
              <label for="exampleInputEmail1">Username</label>
              <input type="email" class="form-control mx-auto w-50 border border-dark" aria-describedby="Username" placeholder="Enter Username" v-model="user_login.username" required>
          </div>

          <div class="form-group form-outline form-dark  m-4">
              <label for="exampleInputPassword1">Password</label>
              <input type="password" class="form-control mx-auto w-50 border border-dark" placeholder="Password" v-model="user_login.password" required>
          </div>
          <button type="button" class="login btn border border-dark w-25 mx-auto rounded btn btn-dark pb-2" style="color:#7DF9FF;" @click = "login">Login</button> 
        </div>
      </form>
    </div>
  </div>
</template>

<style>
  .login {
      margin-top: 15px !important;
      margin-bottom:  15px !important;
  }

  .header-login {
    font-family: "monaco";
  }
</style>