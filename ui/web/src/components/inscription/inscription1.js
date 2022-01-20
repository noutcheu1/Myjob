import InputI0 from '@/components/inscription/InputI0.vue'
import ButtonI0 from '@/components/inscription/ButtonI0.vue'
import ButtonI1 from '@/components/inscription/ButtonI1.vue'
import DropDownList from '@/components/inscription/DropDownList.vue'
import FooterI from '@/components/inscription/FooterI.vue'
export default {
  name: 'inscription1',
  components: {
    InputI0,
    ButtonI0,
    ButtonI1,
    DropDownList,
    FooterI
  },
  data () {
    return {
      country: '',
      sex: 'male'
    }
  },
  methods: {
    submiting (e) {
      e.preventDefault()
      return false
    },
    countrySelect ({name, iso2, dialCode}) {
      this.country = name
    },
    previous () {
      this.$router.push('inscription')
    },
    toNext () {
      if (!this.validation()) alert('echec de validation')
      else {
        const axios = require('axios')
        /* axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN' */
        axios.post(this.$store.state.baseUrl + 'Users/', {
          username: this.$store.state.inscription.surname,
          password: this.$store.state.inscription.password,
          first_name: this.$store.state.inscription.name,
          email: this.$refs.email.message
        })
          .then((response) => {
            alert('inscription de' + response.data.username + ' ' + response.data.first_name + 'reuissi')
            console.log(response.data.id)
            let playload = {connected: true, id: response.data.id}
            this.$store.commit('updateLogin', playload)
            this.$router.push('accueil')
          })
          .catch((error) => {
            // error.response.status Check status code
            this.$router.push('inscription')
            alert(error.response.data.username)
            console.log(error.response.data)
          }).finally(() => {
            // Perform action in always
          })
      }
    },
    validation () {
      let regex1 = /^[1-9]{1,3}$/
      if (!regex1.test(this.$refs.age.message)) return false
      if (this.$refs.age.message < 12 || this.$refs.age.message > 130) return false
      return true
    }
  }
}
