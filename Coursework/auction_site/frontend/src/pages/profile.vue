
<script lang=ts>
//This page is the home page, where users can see all the listings and messages
import  { router } from '../router'
import { defineComponent } from 'vue'
import { User,URL } from "../context/context"

    export type RegData = {
        email: string,
        dob : Date,
        city: string,
        profile_picture: File,
    };

    export default defineComponent({
        name: "profile",
        data(){
            let user: any
            let pic: any
            return {
                user,
                pic,
                formData : {
                    email: "",
                    city: "",
                    dob: new Date(),
                    profile_picture:{},
                } as RegData,
                url: URL as string,
            }
        },
        mounted() {
            this.check_login()
        },
        methods: {
            imageChange(e: Event): void {
                const target= e.target as HTMLInputElement;
                this.formData.profile_picture = (target.files as FileList)[0];
            },
            
            async check_login(): Promise<void>{
                let response: Response = await fetch(`${URL}/api/check_logged_in/`, {
                    method: "GET",
                    credentials: 'include',
                    mode: 'cors',
                    referrerPolicy:'no-referrer',
                })

                let check_user: User = await response.json()

                console.log(typeof(check_user.profile_picture))

                if (check_user.Message == "Not Logged In"){
                    console.log("Not logged in")
                    router.push({ path: '/' })
                }
                
                else{
                    this.formData.email = check_user.email
                    this.formData.city = check_user.city
                    this.formData.dob = check_user.dob
                    this.pic = check_user.profile_picture
                    this.user = check_user as User
                }
            },
            async handleEdit(): Promise<void>{
                
                const formData : FormData = new FormData();

                let date
                if (typeof(this.formData.dob) == "string"){
                    date = this.formData.dob
                }else {
                    date = this.formData.dob.toISOString()
                }

                formData.append('email', this.formData.email);
                formData.append('city', this.formData.city);
                formData.append('dob', date);
                formData.append('picture', this.formData.profile_picture);
                formData.append('userId', this.user.id);

                fetch(`${URL}/api/usersup/`, {method: 'POST',body: formData})
                    .then((res) => res.json())
                    .then((data) => {
                        this.user = data.user as User
                        this.pic = data.user.profile_picture as number
                    })
            }
        },
    })
</script>

<template>
    <div class="w-100 vh-100 d-flex justify-content-center align-items-center" style="background-color:#191970">
        <div class = "form-newitem w-50 bg-primary rounded" style="min-width: 1000px;">
            <h1 class="p-4 text-center bold text-white ">Profile</h1>
            <div class="container">
                <div class="row">
                    <div class="col-md-4">
                        <img :src=" url + pic" class="img-thumbnail rounded float-left img-responsive p-2"/>
                        <div class="form-group font-weight-bold">
                            <input type="file" @change="imageChange" ref="imageInput" class="p-2" />
                        </div>
                    </div>
                    <div class="d-flex vstack gap-3 col-md-8">
                        <div class="form-group text-center d-block text-white">
                            <h3><label for="exampleFormControlEmail">Email</label></h3>
                            <input v-model="formData.email" type="email " class="form-control d-block mx-auto w-50" placeholder="johndoe@example.com" id="Email" >
                        </div>
                        <div class="form-group text-center d-block text-white">
                            <h3><label for="City">City</label></h3>
                            <input v-model="formData.city" type="text" class="form-control mx-auto d-block w-50" id="City" aria-describedby="City" placeholder="City...">
                        </div>
                        <div class="form-group text-center d-block text-white"> 
                            <h3><label class="control-label" for="Birthday">Date of Birth</label></h3>
                            <input v-model="formData.dob" type ='date' class="form-control w-50 mx-auto"/>
                        </div>
                        <button @click="handleEdit" type="button" class=" btn border border-dark w-25 mx-auto rounded btn btn-dark" style="color:#7DF9FF;">Edit Profile</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style >
    .form-newitem{
        padding: 2em;
        margin-top: 3em;
    }
</style>