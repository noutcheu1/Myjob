<template>
  <div class="profile">
    <div class="profileTitle">
      Our client say
    </div>
    <div>
      <div
        class="profileBack"
        @click="leftMove"
      />
      <div>
        <div
          class="profileContent"
          :style="{ left:Position }"
        >
          <div class="profileCont">
            <div class="profileImage">
              <div /></div>
            <div class="profileName">
              Magne Kamdem <br>Teacher
            </div>
            <div class="profileSay">Something that she says and that could be you to show that our project is good or the we are
              doig good stuff out here and i just want to to get this text longer so i could see the result, will look certainly greaat!</div>
          </div>
          <div class="profileCont">
            <div class="profileImage">
              <div /></div>
            <div class="profileName">
              Magne Kamdem <br>Teacher
            </div>
            <div class="profileSay">
              Something that se says and that could be you to show that our project is good or the we are doig good stuff out here
            </div>
          </div>
          <div class="profileCont">
            <div class="profileImage">
              <div /></div>
            <div class="profileName">
              Magne Kamdem <br>Teacher
            </div>
            <div class="profileSay">
              Something that se says and that could be you to show that our project is good or the we are doig good stuff out here
            </div>
          </div>
        </div>
      </div>
      <div
        class="profileNext"
        @click="rightMove"
      />
    </div>
  </div>
</template>
<style src="./profile.css">
</style>
<script src="./profile.js">
</script>
