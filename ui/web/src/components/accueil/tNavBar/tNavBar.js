import Button from './Button.vue'
import Button1 from './Button1.vue'
import InputSearch from './inputSearch/InputSearch.vue'
export default {
  name: 'tNavBar',
  components: {
    Button,
    Button1,
    InputSearch
  },
  data () {
    return {
      connectDisplay: 'block',
      nonConnectDisplay: 'none'
    }
  },
  methods: {
    connexionVisible () {
      if (this.$store.state.login.connected) {
        this.connectDisplay = 'none'
        this.nonConnectDisplay = 'block'
      } else this.connectDisplay = 'block'
    },
    displayProfile () {
      this.$root.$emit('displayProfile', {id: this.reference, title: this.title})
    }
  },
  mounted () {
    this.connexionVisible()
  }
}
