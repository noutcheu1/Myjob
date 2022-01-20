<template>
  <div class="Myprofile">
    <div class="profileMain">
        <div
          class="profileContent"
          :style="{ left:Position }"
        >
          <div class="profileCont">
            <img src="./caroussel myjob/slide1.png" />
          </div>
          <div class="profileCont">
            <img src="./caroussel myjob/slide2.png" />
          </div>
          <div class="profileCont">
            <img src="./caroussel myjob/slide3.png" />
          </div>
        </div>
      </div>
      <div class=myPUpground>
              <div class="profileBack" @click="move(1)"></div>
              <div>
                  <div class="myPostuler">Postuler a des offres d'emploi<br> et déposer votre cv</div>
                  <div><Button message="Find job"/><Button message="Find talent"/></div>
              </div>
              <div class="profileNext" @click="move(-1)"></div>
      </div>
  </div>
</template>
<style src="./myProfile.css">
</style>
<script src="./myProfile.js">
</script>
