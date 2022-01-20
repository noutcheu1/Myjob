// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuex from 'vuex'
import VueCountryCode from 'vue-country-code-select'

Vue.use(VueCountryCode)

Vue.use(Vuex)

Vue.config.productionTip = false

/* creating the store ----- */

const store = new Vuex.Store({
  state: {
    count: 0,
    // datas are saved in src/asset
    langDatas: [
      {image: 'flags/Flag_of_UK.svg', name: 'English'},
      {image: 'flags/Flag_of_Cameroon.svg', name: 'Cameroonian'},
      {image: 'flags/Flag_of_France.svg', name: 'French'}
    ],
    publiTypeDatas: [
      {image: 'publiType/football1.svg', name: 'Football'},
      {image: 'publiType/philo.svg', name: 'Philosophy'},
      {image: 'publiType/socialProblem.svg', name: 'Social problems'},
      {image: 'publiType/politic.svg', name: 'Politic'},
      {image: 'publiType/beauty.svg', name: 'Beauty'},
      {image: 'publiType/physics.svg', name: 'Physics'},
      {image: 'publiType/other.svg', name: 'Other'}
    ],
    login: {
      connected: false,
      id: 12
    },
    inscription: {
      surname: '',
      name: '',
      password: ''
    },
    baseUrl: 'http://127.0.0.1:8000/api/v1/',
    // --- pop ups this variable is boolean which decides if when publication component is created should or not display message
    publicationMessage: false
  },
  mutations: {
    increment (state) {
      state.count++
    },
    updateLogin (state, playload) {
      state.login.connected = playload.connected
      state.login.id = playload.id
    },
    mutPubliMessage (state, playload) {
      state.publicationMessage = playload
    },
    mutInscription (state, playload) {
      state.inscription.surname = playload.surname
      state.inscription.name = playload.name
      state.inscription.password = playload.password
    }
  }
})
/* eslint-disable no-new */

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  store: store
})
