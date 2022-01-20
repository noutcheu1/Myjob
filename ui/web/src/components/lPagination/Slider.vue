<template>
    <div class ="bsSlider">
<svg :style="{transform:tsRotate, opacity:vopacity}" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
viewBox="0 0 477.175 477.175" style="enable-background:new 0 0 477.175 477.175;fill:rgb(200,200,200);" xml:space="preserve">
<g>
<path d="M360.731,229.075l-225.1-225.1c-5.3-5.3-13.8-5.3-19.1,0s-5.3,13.8,0,19.1l215.5,215.5l-215.5,215.5
c-5.3,5.3-5.3,13.8,0,19.1c2.6,2.6,6.1,4,9.5,4c3.4,0,6.9-1.3,9.5-4l225.1-225.1C365.931,242.875,365.931,234.275,360.731,229.075z
" stroke="rgb(100,100,100)" stroke-width="25"/>
</g>
</svg>

</div>
</template>
<style>
.bsSlider {
    width:20px;
}
.bsSlider:hover {
    cursor: pointer;
}
</style>
<script>
export default {
  name: 'Slider',
  props: {
    tsRotate: {
      type: String,
      default: 'rotate(0deg)'
    },
    vopacity: {
      type: String,
      default: '1'
    }
  }
}
</script>
