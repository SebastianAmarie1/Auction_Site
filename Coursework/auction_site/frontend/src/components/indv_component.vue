

<script lang="ts">
//This component will display each component on the listing page.
import { URL } from "../context/context"

    export default {
        props: {
            item: Object,
        },
        data() {
            return{
                bid: 0 as number,
                url: URL as string,
            }
        },
        mounted() {
            fetch(`${URL}/api/bids/${this.item?.id}`, {method: "GET"})
                .then((res) => res.json())
                .then((data) => {
                    if (data.amount == 0){
                        this.bid = data.amount as number
                    }
                    else{
                        this.bid = data.bids[0].amount as number
                    }
                })
        },
    }
</script>

<template>
    <div class="indv border border-dark   rounded m-45 bg-primary " style =  "width=100%; background-color: ; min-height: 490px; margin:0 auto">
        <h3 class="text-white bg-dark p-1 ps-2"><router-link :to="'/home/'+item?.id" class="text-white text-decoration-none">{{ item?.name }}</router-link></h3>
        <img :src="url + item?.picture" class="img-fluid image" style= "min-height:300px;"/> 
        <h5 class="text-white bg-dark p-2">{{item?.owner.username}}</h5>
        <div class="text-wrap overflow:hidden ps-2">
            <h6>Description: {{item?.description}}</h6>
        </div>
        <div class="d-flex">
            <div class="float-left ps-2">
                <h5>Current Bid: £{{bid}}</h5>
                <router-link :to="'/home/'+item?.id" class=""> <button class="rounded btn btn-dark btn-md ps-2" style="color:#7DF9FF;  ">Details</button></router-link>  
            </div>
            <div class="p-3  ms-auto float-right">
                <h6>Start: {{item?.start_date}}</h6>
                <h6>End: {{item?.finish_date}}</h6>
            </div>
        </div>
    </div>
</template>

<style>
    .image{
        width: 100%;
        max-height: 300px;
        object-fit: cover;
        object-position: center;
    }

    .btn:hover{
        background-color: #00FFFF!important;
        color: black !important;
    }
</style>
