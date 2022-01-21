<template>
    <div class ="tNavBar">
        <div class ="tNavLogo"><div><br><img src='../../../assets/myjob.png'/></div></div>
        <div>
            <div class="tNavButton"> <select class = "tNavDropDownList">
                <option> Find Job </option>
                <option> Creer un CV </option>
                <option> Postuler a un Job </option>
                <option>  Rechercher un Job </option>
                </select>
            </div>
            <div class="tNavButton"> <select class = "tNavDropDownList">
                <option> Find Talent </option>
                <option> Selectionner un candidat </option>
                <option> Passer un entretien </option>
                <option>  Poster un Job </option>
                <option>  Voir les CV </option>
                </select>
            </div>
            <div class="tNavButton">Why MyJob ?</div>
            <div><InputSearch/></div>
        </div>
        <div>
            <div class="navLang" for="aaa" ><img src="./world.svg"/>
                <select id="aaa">
                <option>Fr</option> <option>Eng</option>
                </select>
            </div>
            <div class="tNavLogin"><a :style ="{display:connectDisplay}"> <Button1 message="Log In" link='login' /> </a></div>
            <div :style ="{display:connectDisplay}"><Button message="Sign Up" link='inscription' /></div>
            <div :style ="{display:nonConnectDisplay}" @click="displayProfile"><Button message='profile'/></div>
        </div>
    </div>
</template>
<style src="./tNavBar.css">
</style>
<script src="./tNavBar.js">
</script>
