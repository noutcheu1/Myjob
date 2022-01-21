import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import todolist from '@/components/todo'
import Inscription from '@/components/inscription/Inscription'
import Inscription1 from '@/components/inscription/Inscription1'
import Login from '@/components/inscription/Login'
import Accueil from '@/components/accueil/Accueil'
import UpdatProfil from '@/components/accueil/updatProfil/UpdatProfil'
import PostJob from '@/components/accueil/postJob/PostJob'
import Profile from '@/components/accueil/profile/Profile'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'todolist',
      component: todolist
    },
    {
      path: '/inscription',
      name: 'inscription',
      component: Inscription
    },
    {
      path: '/inscription1',
      name: 'inscription1',
      component: Inscription1
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/accueil',
      name: 'accueil',
      component: Accueil
    },
    {
      path: '/UpdatProfil',
      name: 'updatProfil',
      component: UpdatProfil
    },
    {
      path: '/PostJob',
      name: 'postJob',
      component: PostJob
    },
    {
      path: '/Profile',
      name: 'profile',
      component: Profile
    }

  ]
})
