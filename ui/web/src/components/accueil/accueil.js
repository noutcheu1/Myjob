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
  mounted () {
    this.$root.$on('pageChanged', data => {
      this.publicationIndexes = data
      window.scrollTo(0, 700)
    })
  }
}
