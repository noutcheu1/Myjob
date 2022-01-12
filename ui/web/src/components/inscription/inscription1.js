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
        axios.post(this.$store.state.baseUrl + 'inscription1.php', {
          age: this.$refs.age.message,
          country: this.country,
          sex: this.sex,
          pseudo: this.$refs.pseudo.message
        })
          .then((response) => {
            if (response.data === 'account existing') {
              this.$store.commit('mutPubliMessage', true)
              this.$router.push('inscription')
            } else {
              this.$store.commit('updateLogin', {connected: true, id: response.data})
              this.$router.push('loveProject')
              alert('compte créé avec success')
            }
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
      let regex1 = /^[1-9]{1,3}$/
      let regex2 = /^[a-zA-Z ]{0,22}$/
      if (!regex1.test(this.$refs.age.message)) return false
      if (this.$refs.age.message < 12 || this.$refs.age.message > 130) return false
      if (!regex2.test(this.$refs.pseudo.message)) return false
      return true
    }
  }
}
