<template>
<section id="Profile">
    <div class="dashboard">
        <div class="menu space"><img src="./menu.png"></div>
        <div class="menuProfil space"><img src="./profil.png"></div>
        <div class="menuNotification space"><img src="./notification.png"></div>
        <div class="menuLanguage space"><img src="./navigation.png"></div>
        <div class="menuSetting space"><img src="./setting.png"></div>
        <div class="menuLogOut space"><img src="./logOut.png"></div>
    </div>
    <div class="proContent">
        <div><TNavBar/></div>
        <div class="titleUpdProfil"><h1>Profil</h1></div>
        <div class="wrapperUpdProfil">
            <div class="updAvatar">
                <div class="imgUser"> </div><br><br>
            </div>
        </div>
        <div class="profileFirstName"><span class="blue">{{title}}</span></div><br>
        <div class="profileLastName">{{title}}</div><br>
        <div class="profileUserName">{{title}}</div><br>
        <div class="profileEmail">{{title}}</div>
        <div class="profilePassword">{{title}}</div>
        <div class="profileLocation">{{title}}</div>
        <div class="profileDescription">{{title}}</div>
        <div class="profileAddress">{{title}}</div>
        <div class="profileNationalite">{{title}}</div>
        <div class="profileBirthday">{{title}}</div>
        <div class="profileMetier">{{title}}</div>
        <div class="profileCV">{{title}}</div>
        <div class="butt">
            <button @click='sendImage' class="butProfile">Next</button>
        </div>
    </div>
</section>
</template>
<style src="./profile.css">
</style>
<script src="./profile.js">
</script>
