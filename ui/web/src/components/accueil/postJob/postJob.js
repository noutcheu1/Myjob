import TNavBar from '../tNavBar/TNavBar'
export default {
  name: 'accueil',
  data () {
    return {
      titre: 'titre metier',
      type_contrat: 'CDD',
      salaire_min: '100',
      salaire_max: '300',
      metier: 'Computer Scientist',
      profil_recruteur: 1,
      date_fin: '2022-01-20',
      description: 'description',
      work_location: 'Cameroon',
      nombres_experiences: 0

    }
  },
  components: {
    TNavBar
  },
  methods: {
    toNext () {
      const axios = require('axios')
      axios.defaults.xsrfCookieName = 'csrftoken'
      axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
      axios.post(this.$store.state.baseUrl + 'Job/', {
        titre: this.titre,
        metier: this.metier,
        type_contrat: this.type_contrat,
        salaire_min: this.salaire_min,
        salaire_max: this.salaire_max,
        profilretruteur: 1,
        date_fin: this.date_fin,
        description: this.description,
        work_location: this.work_location,
        nombres_experiences: 0
      })
        .then((response) => {
          console.log(response.data)
          this.$router.push('accueil')
        })
        .catch((error) => {
          // error.response.status Check status code
          alert(error)
          console.log(error)
        }).finally(() => {
          // Perform action in always
        })
    }
  }
}
