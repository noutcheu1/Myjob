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
      connectDisplay: 'block'
    }
  },
  methods: {
    connexionVisible () {
      if (this.$store.state.login.connected) {
        this.connectDisplay = 'none'
      } else this.connectDisplay = 'block'
    }
  },
  mounted () {
    this.connexionVisible()
  }
}
