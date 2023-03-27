import { createApp } from 'vue'
import App from './App.vue'
import {createRouter,createWebHistory} from 'vue-router'
import Individual_item from '../pages/individual_item.vue';
import Signin from '../pages/signin.vue';
import Signup from '../pages/signup.vue';
import New_item from '../pages/add_new_item.vue';
import Home from '../pages/home.vue';
import Profile from '../pages/profile.vue';

const routes = [
    {
        path: '/',
        name:'Signin',
        component: Signin,
    },
    {
        path: '/signup',
        name:'Signup',
        component: Signup,
    },
    {
        path: '/home',
        name:'Home',
        component: Home,
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile
    },
    {
        path: '/new_item',
        name:'New Item',
        component: New_item,
    },
    {
        path: '/home/:id',
        name:'Individaul_Item',
        component: Individual_item,
    },
]

const router = createRouter ({
    history: createWebHistory(),
    routes
})

export {router}

