import LDropDown from '@/components/accueil/lDropDown/LDropDown.vue'
export default {
  name: 'lPblicationForm',
  components: {
    LDropDown
  },
  data () {
    return {
      cv: '',
      Display: 'none',
      isDisplayed: false,
      publiTitle: '',
      publiContent: '',
      titleWork: '',
      displayOui: 'none',
      displayNon: 'none',
      cvFileName: ''
    }
  },
  methods: {
    displaying () {
      this.Display = this.isDisplayed ? 'none' : 'block'
      this.isDisplayed = !this.isDisplayed
    },
    fillCv (cv) {
      // alert(this.cv)
      if (cv === 'oui') {
        this.displayOui = 'block'
        this.displayNon = 'none'
      }
      if (cv === 'non') {
        this.displayNon = 'block'
        this.displayOui = 'none'
      }
    },
    preview () {
      const [file] = this.$refs.cvInput.files
      if (file) {
        // document.getElementById('lPbblah').src = URL.createObjectURL(file)
        this.cvFileName = file.name
      }
    },
    sendImage () {
      const axios = require('axios')
      var formData = new FormData()
      const [file] = this.$refs.cvFile.files
      if (file) {
        formData.append('image', file)
        axios.post(this.$store.state.baseUrl + 'saveImage.php', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
          .then((response) => {
            alert(response.data)
            this.publishing() // on publi après avoir enregistré l'image
          })
          .catch((error) => {
            alert(error)
          })
      } else { this.publishing() } // s'il n(y a pas de fichier on publi quand meme le reste)
    },
    validation () {
      return true
    },
    publishing () {
      if (!this.validation()) alert('echec de validation')
      else {
        const axios = require('axios')
        axios.post(this.$store.state.baseUrl + 'savePublication.php', {
          publiTitle: this.publiTitle,
          publiContent: this.publiContent,
          type: this.$refs.types.currentType,
          userId: this.$store.state.login.id
        })
          .then((response) => {
            alert('success' + response.data)
          })
          .catch((error) => {
            alert(error)
          })
      }
    }
  },
  mounted () {
    this.$root.$on('displayForm', data => {
      this.displaying()
      this.titleWork = data.title
    })
  }
}
