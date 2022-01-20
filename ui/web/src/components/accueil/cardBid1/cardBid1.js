export default {
  name: 'cardBid1',
  props: {
    displayNew: {
      type: String,
      default: 'block'
    },
    displayNumbCandidate: {
      type: String,
      default: 'block'
    },
    datas: []
  },
  data () {
    return {
      Display: 'block',
      reference: '1',
      title: 'Manager',
      employer: 'Mtn Cameroon',
      location: 'Douala',
      type_contrat: 'CDD',
      post: '01/01/2022',
      exp: '01/06/2022'
    }
  },
  methods: {
    displayForm () {
      this.$root.$emit('displayForm', {id: this.reference, title: this.title})
    },
    updateDatas () {
      if (typeof this.datas === 'undefined') this.Display = 'none'
      else {
        console.log(this.datas)
        this.Display = 'block'
        this.reference = this.datas.id
        this.title = this.datas.titre
        this.post = this.datas.date_debut
        this.exp = this.datas.date_fin
        this.type_contrat = this.datas.type_contrat
        this.location = this.datas.work_location
        this.recruteurId(this.datas.profilretruteur)
      }
    },
    recruteurId (id) {
      const axios = require('axios')
      axios.get(this.$store.state.baseUrl + 'Retruteur/' + id + '/')
        .then((response) => {
          this.userName(response.data.id)
        })
        .catch((error) => {
          alert(error)
        })
    },
    userName (id) {
      const axios = require('axios')
      axios.get(this.$store.state.baseUrl + 'Users/' + id + '/')
        .then((response) => {
          this.employer = response.data.username
        })
        .catch((error) => {
          alert(error)
        })
    }
  },
  watch: {
    datas: function (newVal, oldVal) { // watch it
      this.updateDatas()
    }
  }
}
