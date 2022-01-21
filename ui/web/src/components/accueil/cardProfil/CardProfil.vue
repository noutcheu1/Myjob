<template>
<section :style="{display:Display}" id="cardProfil">
  <div class="cardProfil">
    <div class="carProlPBFCCross" @click="displaying()"><img src="./more.svg"/></div>
    <br><div class="avatarMyjob" >
          <img src="./avatar.png">
     </div> <br>
     <div class="idUser space">
         <div class="nameUser space">{{ name }}</div>
         <div class="emailUser"> <span class="">{{ email }}</span></div> <br>
     </div>
     <div class="account space x">
         <div class="img"><img src="./person.png"></div>
         <div class="txt"><a href="#">Account</a></div>
     </div>
     <div class="settings space x">
          <div class="img"><img src="./setting.png"></div>
         <div class="txt"><a href="UpdatProfil">Settings</a></div>
     </div>
     <div class="messages space x">
          <div class="img"><img src="./message.png"></div>
         <div class="txt"><a href="#">Messages</a></div>
     </div>
     <div class="notifications space x">
          <div class="img"><img src="./notification.png"></div>
         <div class="txt"><a href="#">Notifications</a></div>
     </div>
     <div class="languages space x">
          <div class="img"><img src="./navigation.png"></div>
         <div class="txt"><a href="#">Languages</a></div>
     </div>
     <div class="logOut space x">
          <div class="img"><img src="./logout.png"></div>
         <div class="txt"><a href="#">Log Out</a></div>
     </div>
     <div class="logoMyjob">
          <img src="./My Job.png">
     </div> <br>
     <div class="description space">
         MyJob is a software develop by student in Info l3 <br> to propose solution for a job
     </div>
     <div class="socialNetwork">
        <ul>
            <li><a href="#">Facebook</a></li>
            <li><a href="#">Twitter</a></li>
            <li><a href="#">Linkedin</a></li>
        </ul>
     </div>
  </div>
</section>
</template>
<style src="./cardProfil.css">
</style>
<script src="./cardProfil.js">
</script>
