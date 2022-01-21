<template>
<section class="updatProfil"  >
    <div><TNavBar/></div>
    <div class="titleUpdProfil"><h1>Settings</h1></div>
    <div class="wrapperUpdProfil">
        <div class="updAvatar">
            <div class="test">
                <div class="imgUser"></div><br>
                <div class="editImg">
                    <div class="iconTxt"><a href="#">Edit image</a></div>
                <div class="iconImg"><img src="./edit.png"></div>
            </div><br><br>
        </div>
        </div>
        <div class="updNom"><span class="blue">Nom</span><span class="red"> *</span><textarea v-model="publiContent" placeholder="Editer votre nom"></textarea></div><br>
        <div class="updPrenom"><span class="blue">Prenom</span><span class="red"> *</span><textarea v-model="publiTitle" placeholder="Editer votre prenom"></textarea> </div><br>
        <div class="updUsername"><span class="blue">User name</span><span class="red"> *</span><textarea v-model="publiContent" placeholder="Editer votre username"></textarea></div><br>
        <br><span class="orange">Change E-mail</span><br><br>
        <div class="updEmail"><span class="blue">E-mail</span><span class="red"> *</span><textarea v-model="publiTitle" placeholder="Editer votre email"></textarea> </div><br>
        <div class="updConfirmEmail"><span class="blue">Confirm E-mail</span><span class="red"> *</span><textarea v-model="publiContent" placeholder="Editer votre email"></textarea></div><br>
        <br><span class="orange">Change Password</span><br><br>
        <div class="updPassword"><span class="blue">Password</span><span class="red"> *</span><textarea v-model="publiTitle" placeholder="Editer votre password"></textarea> </div><br>
        <div class="updConfirmPassword"><span class="blue">Confirm Password</span><span class="red"> *</span><textarea v-model="publiContent" placeholder="Editer votre password"></textarea></div><br>
    </div>
    <a href="accueil"><button @click='sendImage' class="nextupdUser">Next</button></a>
</section>
</template>
<style src="./updatProfil.css">
</style>
<script src="./updatProfil.js">
</script>
