export default {
  name: 'cardProfil',
  data () {
    return {
      Display: 'block',
      isDisplayed: true,
      name: 'name',
      email: 'email'
    }
  },
  methods: {
    displaying () {
      this.Display = this.isDisplayed ? 'none' : 'block'
      this.isDisplayed = !this.isDisplayed
    },
    updateProfile () {
      this.name = this.$store.state.login.name
      this.email = this.$store.state.login.email
    }
  },
  mounted () {
    this.$root.$on('displayProfile', data => {
      this.displaying()
    })
    this.updateProfile()
    if (this.$store.state.login.connected) {
      this.Display = 'block'
    } else this.Display = 'none'
  }
}
