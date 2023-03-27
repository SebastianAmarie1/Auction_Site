
<script lang="ts">
//This component is the reviews for each product
import replies from "./replies.vue"
import { URL } from "../context/context"
    export default {
        props: {
            review: Object ,
            replies: Object,
            userId: Number,
        },
        data() {
            return {
                message: "" as string,
                url: URL as string,
            }
        },
        methods: {
            async handleReply(): Promise<void> {
                try {
                    await fetch(`${URL}/api/replies/${this.review?.item.id}/`, {
                    method: "POST",
                    body: JSON.stringify({
                        message: this.message,
                        sender_id: this.userId, 
                        replying: this.review?.id,
                    })})
                        .then((res) => res.json())
                        .then(data => {this.$emit('updateReplies',data)})
                } catch (error) {
                    console.log(error)
                }
            }
        },
        components: {
            replies
        },
    }
</script>

<template>
    <div class="msg border border-dark rounded" style="background-color:#0096FF">
        <div className="reviews">
            <img className="pfp" :src="url + review?.sender?.profile_picture"/>
            <h5><u>{{review?.sender.username}}</u></h5>
            <h5>{{review?.message}}</h5>
            <h5>{{review?.date_posted}}</h5>
        </div>

        <div className="replies">
            <div  v-for="reply in replies">
                <div v-if="reply.replying.id == review?.id"  >
                    <replies :key="reply.id" :reply="reply" style="background-color: #ADD8E6;"/>
                </div>
            </div>
        </div>
        <textarea v-model="message" placeholder="Enter a reply" class=" reply-enter d-block mx-auto w-50 border border-dark rounded"></textarea>
        <button @click="handleReply" class=" reply-button btn border border-dark w-25 mx-auto rounded btn btn-dark" style="color:#7DF9FF;">Reply</button>
    </div>
</template>

<style scoped>
.pfp{
    width: 50px;
}
.msg{
    min-height: 100px;
    width: 80%;
    margin: 0 auto;
    margin-top: 2em;
    border-radius: 10px;
    padding: 0.5em;
    background-color: var(--clr-secondary);
}

.reply-button {
    margin-top: 15px !important;
    margin-bottom:  15px !important;
}

.reply-enter {
    margin-top: 15px !important;
    margin-bottom:  15px !important;
}
</style>