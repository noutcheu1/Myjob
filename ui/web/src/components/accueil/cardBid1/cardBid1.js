export default {
  name: 'cardBid1',
  data () {
    return {
      reference: '1',
      title: 'Community manager'

    }
  },
  methods: {

    displayForm () {
      this.$root.$emit('displayForm', {id: this.reference, title: this.title})
    }
  }
}
