export default {
  name: 'Profile',
  props: {
    message: String,
  },
  methods: {
    rightMove() {
      if (this.position > -200) {
        this.position -= 100
      }
    },
    leftMove() {
      if (this.position < 0) {
        this.position += 100
      }
    },
  },
  data() {
    return {
      position: 0,
    }
  },
  computed: {
    Position() {
      return `${this.position}%`
    },
  },
}
