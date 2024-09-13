import Vue from 'vue';
import Router from 'vue-router';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';
import Dashboard from '../components/Dashboard.vue';
import Index from "@/components/Index.vue";

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/login',
            name: 'Login',
            component: Login,
        },
        {
            path: '/register',
            name: 'Register',
            component: Register,
        },
        {
            path: '/dashboard',
            name: 'Dashboard',
            component: Dashboard,
        },
        {
            path: '/index',
            name: 'Index',
            component: Index,
        },
        {
            path: '*',
            redirect: '/login',
        },
    ],
});
