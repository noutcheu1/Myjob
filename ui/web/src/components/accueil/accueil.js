import TNavBar from './tNavBar/TNavBar.vue'
import MyProfile from './myProfile/MyProfile.vue'
import CardBid from './cardBid/CardBid.vue'
import CardBid1 from './cardBid1/CardBid1.vue'
import modalJob from './modalJob/ModalJob.vue'
import LPblicationForm from './lPblicationForm/LPblicationForm.vue'
import CardProfil from './cardProfil/CardProfil.vue'
import LPagination from './lPagination/LPagination.vue'
export default {
  name: 'accueil',
  components: {
    TNavBar,
    MyProfile,
    CardBid,
    CardBid1,
    modalJob,
    LPblicationForm,
    CardProfil,
    LPagination
  },
  data () {
    return {
      publicationIndexes: []
    }
  },
  methods: {
    exist (a) {
      let result
      if (typeof a === 'undefined') {
        result = 'lll'
      } else result = a
      return result
    }
  },
  mounted () {
    this.$root.$on('pageChanged', data => {
      this.publicationIndexes = data
      let i, max
      max = this.publicationIndexes.length
     /* for (i = 0; i < max; i++) {
        this.publicationIndexes[i] = this.exist(this.publicationIndexes[i])
      } */
      window.scrollTo(0, 700)
    })
  }
}
