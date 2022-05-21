import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: function() {
            return import ( /* webpackChunkName: "about" */ '../views/AboutView.vue')
        }
    },

    {
        path: '/Catalogo_juegos',
        name: 'juegos',
        component: function() {
            return import ('../views/Catalogo_juegos.vue')
        }
    },

    {
        path: '/Catalogo_accesorios',
        name: 'accesorios',
        component: function() {
            return import ('../views/Catalogo_accesorios.vue')
        }
    }

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router