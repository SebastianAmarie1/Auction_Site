
<script lang="ts">
// This page is for when clicking a item, it will show all the details about the specific item
import review from "../components/review.vue"
import { User, Product, Review, Reply, URL} from "../context/context"
import { router } from "../router"

    export default {
        data() {
                let user: any
                let product: any
                let reviews: any
                let replies: any
            return {
                id: this.$router.currentRoute.value.params.id as string,
                user,
                product,
                reviews,
                replies,
                message: "" as string,
                bid: {} as Object,
                currentBid: 0 as number,
                url: URL as string,
            }
        },
        mounted() {
            this.check_login()
            try {
                fetch(`${URL}/api/products/${this.id}`, {method: "GET"})
                    .then((res) => res.json())
                    .then((data) => this.product = data.product[0] as Product)
                //GET REVIEWS AND REPLIES
                fetch(`${URL}/api/reviews/${this.id}`, {method: "GET"})
                    .then((res) => res.json())
                    .then((data) => this.reviews = data.reviews as Review[])
                
                fetch(`${URL}/api/replies/${this.id}`, {method: "GET"})
                    .then((res) => res.json())
                    .then((data) => this.replies = data.replies as Reply[])
                
                fetch(`${URL}/api/bids/${this.id}`, {method: "GET"})
                    .then((res) => res.json())
                    .then((data) => {
                        if (data.amount == 0){
                            this.currentBid = data.amount as number
                        }
                        else{
                            this.currentBid = data.bids[0].amount as number
                        }
                    })
            } catch (error) {
                console.log(error)
            }
        },
        methods: {
            async handleReview(): Promise<void>{
                try {
                    await fetch(`${URL}/api/reviews/${this.id}/`, {
                    method: "POST",
                    body: JSON.stringify({
                        message: this.message,
                        sender_id: this.user.id,
                    })})
                    .then((res) => res.json())
                    .then(data => this.reviews = data.reviews as Review[])
                } catch (error) {
                    console.log(error)
                }
            },
            updateReplies(value: any): void {
                console.log("ran update replies")
                this.replies = value.replies as Reply
            },
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
                else{
                    this.user = check_user as User
                }
            },
            async handleBid(): Promise<void>{
                if (this.currentBid < this.bid){
                    try {
                        await fetch(`${URL}/api/bids/`, {
                            method: "POST",
                            body: JSON.stringify({
                                amount: this.bid,
                                sender_id: this.user.id,
                                product_id: this.product.id,
                            }) 
                            })
                        .then((res) => res.json())
                        .then(data => this.currentBid = data.bid.amount as number)
                        } catch (error) {
                        console.log(error)
                        }
                } else {
                    alert("Enter a bid larger than the current bid!")
                }
            },
        },
        components: {
            review,
        }
    }
</script>

<template>
<div className="mainBody">
    <div className="main fcc border border-dark rounded container-fluid" style="max-width: 1210px">
        <div class="text-black bg-primary" >
            <h1 class="bg-black text-white">{{product?.name}}</h1>
            <div className="img-desc">
                <div className="image" class="bg-primary"> 
                    <img className="pic" :src="url + product?.picture" />
                    <div className=" price" class=""><h5 class="p-2 bg-black text-white"><strong> Current Highest Bid: £{{currentBid}}</strong></h5></div>
                    <div className=" price" class="p-4  bg-primary"> 
                        <strong>
                            <label for="quantity" class="pe-2">Place Bid: £ </label>
                            <input v-model="bid" type="number" id="quantity" name="quantity" min= {{product?.starting_price}} class="border border-dark mx-auto w-25 rounded pe-2"> 
                            <button @click="handleBid" class=" margin-button btn btn-success border border-dark mx-auto w-25 col-xs-2 " >Bid</button>
                        </strong>
                    </div>
                </div>

                <div className="ProductInfo" class="bg-primary">
                    <div className="Description" class="p-2">
                        <h3><u>Description</u></h3>
                        <h6><em>{{product?.description}}</em></h6>
                    </div>
                    <div className="StartDate" class="p-2">
                        <h3><u>Bidding Start Time</u></h3>
                        <h6><em>{{product?.start_date}}</em></h6>
                    </div>
                    <div className="End Date" class="p-2">
                        <h3><u>Bidding End Time</u></h3>
                        <h6><em>{{product?.finish_date}}</em></h6>
                    </div>
                    <div className="User" class="p-2">
                        <h3><u>Sold By</u></h3>
                        <h6>{{product?.owner?.username}}</h6>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div className="messages-container bg-primary border border-dark rounded">
        <div class="text-center">
            <h1 class="p-4 bg-black text-white"><u><em>Questions and Reviews</em></u></h1>
            <textarea v-model="message" placeHolder="Enter review here..." class=" review d-block border border-dark mx-auto w-50 rounded p-3 h-100"></textarea>
            <button @click="handleReview" class="btn border border-dark w-25 mx-auto rounded btn btn-dark" style="color:#7DF9FF;">Add Review/Question</button>
            <div v-for="review in reviews" >
                <review :key="review.id" :review="review" :replies="replies" :userId="user?.id" @updateReplies="updateReplies($event)"/>
            </div>
        </div>
    </div>
</div>
</template>

<style scoped>
    .pic {
        width: 400px;
    }
    .mainBody {
        padding: 2em;

        background-color: #191970;
    }
    .main {
        height: calc(100vh - 100px);
        width: 100%;
        margin: 0 auto;
        margin-top: 5em;;
    }
    .img-desc{
        display: flex;
    }
    .ProductInfo{
        margin-left: 2em;
        width: 900px;
        background-color: #cecece;
    }
    .image {
        background-color: blue;
        height: 400px;
        width: 400px;
    }
    .price {
        margin-top: 1em;
        background-color: #cecece;
        width: 300px;
    }
    .messages-container{
        min-height: 500px;
        width: 80%;
        margin: 0 auto;
        margin-top: 3em;
        margin-bottom: 10em;
        padding: 2em;
    }
    .margin-button{
        margin-left: 15px !important;
    }
    .review {
        margin-top: 15px !important;
        margin-bottom:  15px !important;
    }
</style>