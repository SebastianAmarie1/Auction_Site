
<script lang="ts">
//This component is the replies for the reviews/questions
import { URL } from "../context/context"
    export default {
        props: {
            reply: Object,
        },
        data(){
            return{
                url: URL as string,
            }
        }
    }

</script>

<template>
    <div className="msgrep border border-dark rounded">
        <img className="pfp" :src="url + reply?.sender?.profile_picture"/>
        <h5><u>{{reply?.sender.username}}</u></h5>
        <h5>{{reply?.message}}</h5>
        <h5>{{reply?.date_posted}}</h5>
    </div>
</template>

<style scoped>
    .pfp{
        width: 50px;
    }
    .msgrep{
        min-height: 100px;
        width: 80%;
        margin: 0 auto;
        margin-top: 2em;
        border-radius: 10px;
        padding: 0.5em;
        background-color: pink;
    }
</style>