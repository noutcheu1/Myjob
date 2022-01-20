export default {
  name: 'lDropDown',
  props: {
    bdColor: {
      type: String,
      default: 'solid 1px silver'
    },
    maxHeight: {
      type: String,
      default: '300%'
    },
    maxWidth: {
      type: String,
      default: '120px'
    },
    datas: Array
  },
  data () {
    return {
      currentImage: this.datas[0].image,
      currentType: this.datas[0].name,
      vheight: '0%',
      vpaddingTop: '0px',
      vpaddingBottom: '0px',
      isCollapsed: false
    }
  },
  methods: {
    heightCollapse () {
      this.vheight = this.isCollapsed ? '0%' : this.maxHeight
      this.vpaddingTop = this.isCollapsed ? '0px' : '5px'
      this.vpaddingBottom = this.vpaddingTop
      this.isCollapsed = !this.isCollapsed
    },
    selecting (index) {
      this.currentImage = this.datas[index].image
      this.currentType = this.datas[index].name
      this.heightCollapse()
    }
  }
}
