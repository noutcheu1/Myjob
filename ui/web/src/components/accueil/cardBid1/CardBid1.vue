<template>
  <div class="cardBid1" :style="{display:Display}">
      <div class="cb1Title  ">{{title}}</div>
      <div class="cb1Info">
        <div><img src='./hand-bag.svg'/><span>{{ employer }}</span></div>
        <div><img src='./notepad-note.svg'/><span>{{ type_contrat }}</span></div>
        <div><img src='./location.svg'/><span>{{ location }}</span></div>
      </div>
      <div>
          <span class="cb1Post">post: {{ post }}</span>
          <span>Exp: {{ exp }}</span>
      </div>
      <div>
        <button @click="displayForm">subscribe</button>
        <div :style="{display:displayNumbCandidate}">6/15 candidats</div>
      </div>
      <div :style="{display:displayNew}" class="cb1New"><img src="./new.svg"></div>
  </div>
</template>
<style src="./cardBid1.css">
</style>
<script src="./cardBid1.js">
</script>
