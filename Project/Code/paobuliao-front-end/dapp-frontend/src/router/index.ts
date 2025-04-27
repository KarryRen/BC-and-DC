import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Dashboard from '../views/Dashboard.vue'
import SellerPanel from '../views/SellerPanel.vue'
import BuyerPanel from '../views/BuyerPanel.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/dashboard', component: Dashboard },
  { path: '/seller', component: SellerPanel },
  { path: '/buyer', component: BuyerPanel }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
