import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Industries from '../views/Industries.vue'
import Services from '../views/Services.vue'
import Products from '../views/Products.vue'
import Product from '../views/Product.vue'
import Login from '../views/Login.vue'
import MyAccount from '../views/MyAccount.vue'
import SignUp from '../views/Signup.vue'
import Trial from '../views/Trial.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/industries',
    name: 'Industries',
    component: Industries
  },
  {
    path: '/services',
    name: 'Services',
    component: Services
  },
  {
    path: '/products',
    name: 'Products',
    component: Products
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/trial',
    name: 'Trial',
    component: Trial
  },
  {
    path: '/:category_slug/:product_slug/',
    name: 'Product',
    component: Product
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
