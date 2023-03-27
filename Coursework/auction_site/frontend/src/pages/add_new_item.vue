
<script lang="ts">
//This page is for adding new items to auction.
import  { router } from '../router'
import { User, URL } from "../context/context"

    export type frmData = {
        name: string,
        description: string, 
        start_date: Date,
        finish_date: Date,
        image: File,
    }

    export default {
        data() {
            let user: any
            return {
                user,
                formData: {
                    name: "",
                    description: "", 
                    start_date: new Date(),
                    finish_date: new Date(),
                    image: {},
                } as frmData,
                url: URL as string,
            }
        },
        methods : {
            imageChange(e: Event) : void{
                const target= e.target as HTMLInputElement;
                this.formData.image = (target.files as FileList)[0];
            },
            handleSubmit(): void {
                const formData = new FormData();

                let sDate
                if (typeof(this.formData.start_date) == "string"){
                    sDate = this.formData.start_date
                }else {
                    sDate = this.formData.start_date.toISOString().slice(0, -6)
                }

                let fDate
                if (typeof(this.formData.finish_date) == "string"){
                    fDate = this.formData.finish_date
                }else {
                    fDate = this.formData.finish_date.toISOString().slice(0, -6)
                }

                formData.append('image', this.formData.image);
                formData.append('name', this.formData.name);
                formData.append('description', this.formData.description);
                formData.append('start_date', sDate);
                formData.append('finish_date', fDate);
                formData.append('sender_id', this.user.id);

                fetch(`${URL}/api/products/`, {method: 'POST',body: formData})
                    .then(response => response.json())
                    .then(data => console.log(data))
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
        },

        mounted() {
            this.check_login()
        },
    }
</script>

<template>
    <div class="vh-100 d-flex justify-content-center align-items-center fixed" style="background-color:#191970">
        <form @submit.prevent="handleSubmit">
            <div class = "form-newitem bg-primary rounded m-0" style="min-width: 1000px;">
                <h1 class="text-center bold text-white m-4">Sell Product</h1>
                <div class="container rounded">
                    <div class="row">
                        <div class="col-md-4">
                            <img :src="url + '/images/ItemNoImage.jpg'" class="img-thumbnail rounded float-left img-responsive p-2"/>
                            <div class="form-group font-weight-bold text-white">
                                <h4><label for="Image">Add Image</label></h4>
                                <input required  type="file" @change="imageChange" ref="imageInput" class="p-2" />
                            </div>
                        </div>
                        <div class="d-flex vstack gap-3 col-md-8">
                            <div class="form-group text-center text-white d-block">
                                <h3><label for="Product Name">Product Name</label></h3>
                                <input required  v-model="formData.name" type="text" class="form-control mx-auto d-block w-50" id="ProductName" aria-describedby="Product" placeholder="Product Name...">
                            </div>
                            <div class="form-group text-center text-white d-block">
                                <h3><label for="exampleFormControlTextarea1">Product Description</label></h3>
                                <textarea v-model="formData.description" class="form-control d-block mx-auto w-50" id="ProuctDescription" rows="3"></textarea>
                            </div>
                            <div class="form-group text-center text-white d-block"> 
                                <h3><label class="control-label" for="start">Start</label></h3>
                                <input required  v-model="formData.start_date" type ='datetime-local' class="form-control w-50 mx-auto"/>
                            </div>
                            <div class="form-group text-center text-white d-block"> 
                                <h3><label class="control-label" for="end">End</label></h3>
                                <input required  v-model="formData.finish_date" type ='datetime-local' class="form-control w-50 mx-auto"/>
                            </div>
                            <button type="submit" class=" btn border border-dark w-25 mx-auto rounded btn btn-dark" style="color:#7DF9FF;">Add Item</button>
                            <p>After submitting go back to home page</p>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

