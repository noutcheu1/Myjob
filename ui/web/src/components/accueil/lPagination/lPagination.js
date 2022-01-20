import Slider from './Slider'
export default {
  name: 'lPagination',
  data () {
    return {
      datas: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17], // i should delete that
      datas1: [],
      index: 0, // -- the first index amongs index pages visible
      dataIndex: 0, // the current page
      currentElement: [],
      colors: [
        { bg: '#2057AA', color: 'white' },
        { bg: 'transparent', color: 'inherit' },
        { bg: 'transparent', color: 'inherit' }
      ]
    }
  },
  components: {
    Slider
  },
  methods: {
    splitTable (table, slice) {
      let i
      let j = 0
      let k = 0
      let max = table.length
      let result = []
      let resultElement = []
      for (i = 0; i < max; i++) {
        j++
        resultElement.push(table[i])
        if (j === slice) {
          k = i
          result.push(resultElement)
          resultElement = []
          j = 0
        }
      }
      // --- ajoutons le reste des éléments
      resultElement = []
      if (max < slice) k = -1
      for (i = k + 1; i < max; i++) {
        resultElement.push(table[i])
      }
      if (resultElement.length > 0) result.push(resultElement)
      return result
    },
    changeIndex (newIndex) {
      this.datasIndex = this.index + newIndex
      this.$root.$emit('pageChanged', this.datas1[this.index + newIndex])
      this.initializeColor(newIndex)
    },
    changeRange (i) {
      this.index += i * 3
      this.changeIndex(0)
      this.$root.$emit('pageChanged', this.datas1[this.index])
      this.datasIndex = this.index
    },
    initializeColor (current) {
      let i
      for (i = 0; i < 3; i++) {
        this.colors[i].bg = 'transparent'
        this.colors[i].color = 'inherit'
      }
      this.colors[current].bg = '#2057AA'
      this.colors[current].color = 'white'
    },
    updateDatas () {
      const axios = require('axios')
      axios.get(this.$store.state.baseUrl + 'Job/?page=1')
        .then((response) => {
          this.datas1 = this.splitTable(response.data.results, 6)
          this.$root.$emit('pageChanged', this.datas1[0])
        })
        .catch((error) => {
          alert(error)
        })
    }
  },
  computed: {
    cPrevious () {
      if (this.index < 3 || this.datas1.length < 1) {
        return 'none'
      }
      return 'block'
    },
    cNext () {
      if (this.index >= this.datas1.length - 3 || this.datas1.length < 1) {
        return 'none'
      }
      return 'block'
    },
    cFirst () {
      if (this.datas1.length < 1 || this.index > this.datas1.length - 1) {
        return 'none'
      }
      return 'block'
    },
    cSecond () {
      if (this.datas1.length < 2 || this.index + 1 > this.datas1.length - 1) {
        return 'none'
      }
      return 'block'
    },
    cThird () {
      if (this.datas1.length < 3 || this.index + 2 > this.datas1.length - 1) {
        return 'none'
      }
      return 'block'
    }
  },
  created () {
    this.updateDatas()
    // this.datas1 = this.splitTable(this.datas, 4)
  }
}
