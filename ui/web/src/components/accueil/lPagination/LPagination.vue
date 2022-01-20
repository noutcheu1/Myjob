<template>
    <div class ="lPagination">
            <div @click="changeRange(-1)" class="lPtSLider" :style="{display:cPrevious}" ><Slider tsRotate='rotate(180deg)' /></div>
            <div @click="changeIndex(0)" :style="{backgroundColor:colors[0].bg, color: colors[0].color, display:cFirst}">{{ index +1 }}</div>
            <div @click="changeIndex(1)" :style="{backgroundColor:colors[1].bg, color: colors[1].color, display:cSecond}">{{ index +2 }}</div>
            <div @click="changeIndex(2)" :style="{backgroundColor:colors[2].bg, color: colors[2].color, display:cThird}">{{ index +3 }}</div>
            <div @click="changeRange(1)" class="lPtSLider" :style="{display:cNext }"><Slider /></div>
    </div>
</template>
<style src="./lPagination.css">
</style>
<script src="./lPagination.js">
</script>
