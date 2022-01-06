import InputI0 from '@/components/inscription/InputI0.vue'
import ButtonI0 from '@/components/inscription/ButtonI0.vue'
import ButtonI1 from '@/components/inscription/ButtonI1.vue'
import DropDownList from '@/components/inscription/DropDownList.vue'
import FooterI from '@/components/inscription/FooterI.vue'
export default {
  name: 'inscription',
  components: {
    InputI0,
    ButtonI0,
    ButtonI1,
    DropDownList,
    FooterI
  },
  methods: {
    submiting (e) {
      e.preventDefault()
      return false
    },
    toNext () {
      if (!this.validation()) alert('echec de validation')
      else {
        const axios = require('axios')
        axios.post(this.$store.state.baseUrl + 'inscription.php', {
          surname: this.$refs.surname.message,
          name: this.$refs.name.message,
          password: this.$refs.password.message,
          confirmpw: this.$refs.confirmpw.message
        })
          .then((response) => {
            this.$router.push('inscription1')
          })
          .catch((error) => {
            // error.response.status Check status code
            alert(error)
          }).finally(() => {
            // Perform action in always
          })
      }
    },
    validation () {
      let regex1 = /^[a-zA-Z ]{4,22}$/
      let regex2 = /^.{4,22}$/
      if (!regex1.test(this.$refs.surname.message) ||
          !regex1.test(this.$refs.name.message) ||
          !regex2.test(this.$refs.password.message) ||
          !regex2.test(this.$refs.confirmpw.message) ||
        this.$refs.password.message !== this.$refs.confirmpw.message) return false
      return true
    }
  },
  created () {
    if (this.$store.state.publicationMessage) {
      this.$store.commit('mutPubliMessage', false)
      alert('Compte existant\n veuillez réesayer')
    }
  }
}
