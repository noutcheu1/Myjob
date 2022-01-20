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
      cdd: 'CDD',
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
        this.Display = 'block'
        this.title = this.datas.titre
      }
    }
  },
  watch: {
    datas: function (newVal, oldVal) { // watch it
      this.updateDatas()
    }
  }
}
