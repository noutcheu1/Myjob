<template>
  <div class="Myprofile">
    <div class="profileMain">
        <div
          class="profileContent"
          :style="{ left:Position }"
        >
          <div class="profileCont">
            <img src="./Arsenal-1280x640.jpg" />
          </div>
          <div class="profileCont">
            22222222222222222222222222222222222
          </div>
          <div class="profileCont">
            3333333333333333333333333333333333333333333333
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
