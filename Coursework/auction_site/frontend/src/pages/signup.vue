
<script lang="ts">

import  { router } from '../router'
import { defineComponent } from 'vue';
import { URL } from "../context/context"

  export type RegData = {
    email: string,
    first_name: string,
    last_name: string,
    password: string,
    confirm_password: string,
    dob : Date | null,
    username: string,
  };

  export default defineComponent({
    name: 'signup',
    data(){
      return{
        user_signup: {
          email: "",
          first_name: "",
          last_name: "",
          password: "",
          confirm_password: "",
          dob: null,
          username: "",
        } as RegData
      }
    },
    methods: {
      async signup() : Promise<void>{
        const response: Response = await fetch(`${URL}/api/sign_up/`, {method: "POST", body: JSON.stringify(this.user_signup)})
        
        if (response.ok){
          console.log("Sign up : " + response.ok)
          router.push({ path: '/' })
        }
        else{
          alert("Register unsuccessful, please try again")
          console.log("Sign up : " + response.ok)
        }
      },
    }
  })
</script>

<template>
    <div class="w-100  p-5 d-flex justify-content-center text-black align-items-center" style="background-color:#191970">
      <form class="w-50 vh-100 text-center text-black p-4" style="background-color:#191970; ">
        <div class = "form-signup bg-primary p-4 w-99 rounded vh-100">
          <h1 class=" header-register p-2 text-center bold  p-2">Register</h1>

        <div class="form-group form-outline form-dark  m-1.5">
            <label for="exampleInputEmail1">Email address</label>
            <input required type="email" class="form-control mx-auto w-50 border border-dark " id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email"  v-model="user_signup.email">

        </div>
        <br>
        <div class="form-group  m-1.5">
            <label for="exampleInputEmail1">First Name</label>
            <input required type="char" class="form-control mx-auto w-50 border border-dark" id="exampleInputEmail2" aria-describedby="emailHelp" placeholder="Enter first name" v-model="user_signup.first_name">
        </div>
        <br>
        <div class="form-group m-1.5">
            <label for="exampleInputEmail1">Last Name</label>
            <input required type="char" class="form-control mx-auto w-50 border border-dark" id="exampleInputEmail3" aria-describedby="emailHelp" placeholder="Enter last name" v-model="user_signup.last_name">
        </div>
        <br>
        <div class="form-group m-1.5">
            <label for="username" class="">Username</label>
            <input required type="char" class="form-control mx-auto w-50 border border-dark" id="username" aria-describedby="emailHelp" placeholder="Enter username" v-model="user_signup.username">
        </div>
        <br>
        <div class="form-group m-1.5">
            <label for="exampleInputPassword1">Password</label>
            <input required type="password" class="form-control mx-auto w-50 border border-dark" id="exampleInputPassword1" placeholder="Password" v-model="user_signup.password" >
        </div>
        <br>
        <div class="form-group m-1.5">
            <label for="exampleInputPassword1">Retype Password</label>
            <input required type="password" class="form-control mx-auto w-50 border border-dark" id="exampleInputPassword2" placeholder="Password" v-model="user_signup.confirm_password" >
        </div>
        <br>
        <div class="form-group m-1.5">
            <label for="dob">Date of birth</label>
            <input required type="date" class="form-control mx-auto w-50 border border-dark" v-model="user_signup.dob">
        </div>
        <br>
        <button class="register btn border border-dark w-25 mx-auto rounded btn btn-dark pb-2" style="color:#7DF9FF;" type = "button" @click = "signup">Register</button>
        <p>Please check your email after sign up for register confirmation!</p>  
      </div>
      </form>
    </div>
</template>

<style>
  .login {
      margin-top: 15px !important;
      margin-bottom:  15px !important;
  }
  .header-register {
    font-family: "monaco"
  }
</style>