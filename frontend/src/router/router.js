import Vue from 'vue'
import Router from 'vue-router'
import MyHeader from '../components/common/MyHeader'
import Home from '../components/views/home'
import Goods from '../components/views/Goods'
import Login from '../components/views/Login'
import Register from '../components/views/Register'
import Publish from '../components/views/Publish'
import Personal from '../components/views/Personal'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/home',
      name: 'home',
      components: {
        default: Home,
        header: MyHeader},
      meta: {
        isLogin: false
      }
    },
    {
      path: '/goods',
      name: 'goods',
      components: {
        default: Goods,
        header: MyHeader},
      meta: {
        isLogin: true
      }
    },
    {
      path: '/login',
      name: 'login',
      components: {
        default: Login,
        header: MyHeader},
      meta: {
        isLogin: false
      }
    },
    {
      path: '/register',
      name: 'register',
      components: {
        default: Register,
        header: MyHeader},
      meta: {
        isLogin: false
      }
    },
    {
      path: '/personal',
      name: 'personal',
      components: {
        default: Personal,
        header: MyHeader
      },
      meta: {
        isLogin: true
      }
    },
    {
      path: '/publish',
      name: 'publish',
      components: {
        default: Publish,
        header: MyHeader},
      meta: {
        isLogin: true
      }
    }
  ]
})
