
<script lang="ts">
//This page is the home page, where users can see all the listings 
import indvidual_item_component from "../components/indv_component.vue";
import  { router } from '../router'
import { Product, User, URL } from "../context/context";

    export default {
        data(){
            let products: any
            return {
                products,
            }
        },
        mounted() {
            this.check_login()
            try {
                fetch(`${URL}/api/products/`, {method: "GET"})
                    .then((res) => res.json())
                    .then((data) => this.products = data.products as Product[])
            } catch (error) {
                console.log(error)
            }
        },
        methods: {
            async check_login(): Promise<void>{
                let response = await fetch(`${URL}/api/check_logged_in/`, {
                    method: "GET",
                    credentials: 'include',
                    mode: 'cors',
                    referrerPolicy:'no-referrer',
                })
                
                let check_user = await response.json() as User
                if (check_user.Message == "Not Logged In"){
                    console.log("Not logged in")
                    router.push({ path: '/' })
                }
            },
        },
        components: {
            indvidual_item_component,
        }
    }
</script>

<template>
    <div class="main w-80 p-5 mvh-100 container-fluid text-break " style = "background-color: #191970" >
        <div class="row w-80 rounded" style="background-color:#191970">
            <p style="color: white">If there are no products on sale. please sell one yourself from the sell tab. this may be because the finish date for the auction has expired</p>
            <div class="col-md-4 h-100 p-2 m-0.5 rounded" style="background-color: #191970 "  v-for="product in products" >
                <indvidual_item_component :key="product.id" :item="product" />
            </div>
        </div>
    </div>

</template>



