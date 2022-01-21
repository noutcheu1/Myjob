<template>
<section class="postJob"  >
    <div class="contentPostJob">
        <div class="dashboard">
                <div class="menu space"><img src="./menu.png"></div>
                <div class="menuEntretien space"><img src="./entretien.png"></div>
                <div class="menuPostJob space"><img src="./postjob.png"></div>
                <div class="menuLireCv space"><img src="./voir cv.png"></div>
                <div class="menuLogOut space"><img src="./logOut.png"></div>
        </div>
        <div class="postJobZone">
            <div><TNavBar/></div>
            <div class="wrapperPostJob">
                <div class="flex">
                    <div class="titlePostJob"><h3>Recruteur</h3></div>
                    <div class="title2PostJob"><h1>Poster Job</h1></div>
                </div>
                <div class="updNom"><span class="blue">Titre métier</span><span class="red"> *</span><textarea v-model="publiContent" placeholder="Entrer votre metier"></textarea></div><br>
                <div class="updTypeContrat">
                    <span class="blue">Type de contrat <span class="red"> *</span></span>
                    <select class = "DropDownList">
                        <option> CDI </option>
                        <option> CDD </option>
                        <option> occasionel </option>
                        <option> Stage </option>
                        <option> Freelancer </option>
                    </select>
                </div><br>
                <div class="updPrenom"><span class="blue">Salaire minimal</span><span class="red"> *</span><textarea v-model="publiTitle" placeholder="Editer le Salaire minimum"></textarea> </div><br>
                <div class="updUsername"><span class="blue">Salaire maximal</span><span class="red"> *</span><textarea v-model="publiContent" placeholder="Editer le Salaire maximum"></textarea></div><br>
                <div class="updEmail"><span class="blue">Profil Recherché</span><span class="red"> *</span><textarea v-model="publiTitle" placeholder="Editer votre profil"></textarea> </div><br>
                <div class="updConfirmEmail"><span class="blue">Date de fin</span><span class="red"> *</span><textarea v-model="publiContent" placeholder="Editer la date de fin du contrat"></textarea></div><br>
                <div class="updPassword"><span class="blue">Description</span><span class="red"> *</span><textarea v-model="publiTitle" placeholder="Editer la description"></textarea> </div><br>
                <div class="updConfirmPassword"><span class="blue">Localisation du travail</span><span class="red"> *</span><textarea v-model="publiContent" placeholder="Editer la localisation"></textarea></div><br>
                <div class="updConfirmPassword"><span class="blue">Nombre d'année requis</span><span class="red"> *</span><textarea v-model="publiContent" placeholder="Editer le nombre d'année requis"></textarea></div><br>
            </div>
            <button @click='sendImage' class="pushJob">Post Job</button>
        </div>
    </div>
</section>
</template>
<style src="./postJob.css">
</style>
<script src="./postJob.js">
</script>
