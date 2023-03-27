
<script lang="ts">
//This component will contain the navigation links to the webpage
import  { router } from '../router'
import { User, URL } from '../context/context'

  export default {
    data(){
      let user: any
      return{
        user,
      }
    },
    methods: {
      async signout(){
        await fetch(`${URL}/api/sign_out/`, {
          method: "POST",
          credentials: 'include',
          mode: 'cors',
          referrerPolicy:'no-referrer',
          body: JSON.stringify('Signing out')
        })
        router.push({ path: '/' })
      },

      async check_login(){
        let response: Response = await fetch(`${URL}/api/check_logged_in/`, {
          method: "GET",
          credentials: 'include',
          mode: 'cors',
          referrerPolicy:'no-referrer',
        })

        let check_user = await response.json() as User
        if (this.user != check_user){
          this.user = check_user as User
        }
      },
    },
    mounted() {
      this.check_login()
    },
    watch: {
      $route(newRoute, oldRoute) {
        if (newRoute != oldRoute){
          this.check_login()
        }
      }
    },
  }
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-primary " style=" background-color: #FF5F1F ">
      <a><router-link to="/home" class="navbar-brand m-2" style="color:azure"  ><strong>YouBid</strong></router-link></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse ms-auto " id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto " style="margin-left: 20em">
            <li v-if="(user?.Message == null)" class="nav-item active" style="margin-left: 2em">
              <router-link to="/home" class="btn btn-primary" >Home</router-link>
            </li>
            <li v-if="(user?.Message == null)" class="nav-item active" style="margin-left: 2em">
              <router-link to="/new_item" class="btn btn-primary" >Sell</router-link>
            </li>
            <li v-if="(user?.Message != null)" class="nav-item active" style="margin-left: 2em">
              <router-link to="/signup" class="btn btn-primary">Register</router-link>
            </li>
            <li v-if="(user?.Message != null)" class="nav-item active" style="margin-left: 2em">
              <router-link to="/" class="btn btn-primary">Sign In</router-link>
            </li>
            <li v-if="(user?.Message == null)" class="nav-item dropdown" style="margin-left: 2em">
              <router-link to="/profile" class="btn btn-primary"> Profile </router-link>
            </li>
        </ul>
      </div>

    <div class="col-md-1">
      <li v-if="(user?.Message == null)" class="nav-item active float-right list-unstyled p-1" style="margin-left: 2em">
        <button onclick @click="signout" class="btn btn-primary">Sign out</button>
      </li>
    </div>

    <div class=" mx-auto float-right col-md-1 font-weight-bold ">
      <li v-if="(user?.Message == null)" class="nav-item dropdown text-dark list-unstyled" ><strong> Logged in as {{user?.username}} </strong></li>
    </div>
  </nav>
<router-view />
</template>



