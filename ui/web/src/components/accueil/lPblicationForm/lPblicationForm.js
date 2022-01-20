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
      publiTitle: '000FCFA',
      publiContent: 'vos attentes',
      titleWork: '',
      displayOui: 'none',
      displayNon: 'none',
      cvFileName: '',
      jobId: 1
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
      const axios = require('axios')
      axios.defaults.xsrfCookieName = 'csrftoken'
      axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
      axios.post(this.$store.state.baseUrl + 'postuler_job/', {
        user_id: this.$store.state.login.id,
        job_id: this.jobId,
        motivation_letter: this.publiContent
      })
        .then((response) => {
          alert('vous avez postuler')
          this.displaying()
        })
        .catch((error) => {
          // error.response.status Check status code
          alert(error)
          console.log(error)
        }).finally(() => {
          // Perform action in always
        })
    }
  },
  mounted () {
    this.$root.$on('displayForm', data => {
      this.displaying()
      this.titleWork = data.title
      this.jobId = data.id
    })
  }
}
