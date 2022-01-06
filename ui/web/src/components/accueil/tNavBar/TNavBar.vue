<template>
    <div class ="tNavBar">
        <div class ="tNavLogo"><div>My Job</div></div>
        <div>
            <div class="tNavButton">Find Job<div><img src='./down_arrow.svg'/></div></div>
            <div class="tNavButton">Find Talent<div><img src='./down_arrow.svg'/></div></div>
            <div class="tNavButton">Why MyJob ?<div><img src='./down_arrow.svg'/></div></div>
            <div><InputSearch/></div>
        </div>
        <div>
            <div class="navLang" for="aaa" ><img src="./world.svg"/>
                <select id="aaa">
                <option>Fr</option> <option>Eng</option>
                </select>
            </div>
            <div class="tNavLogin"><Button1 message="Log In"/></div>
            <div><Button message="Sign Up" /></div>
        </div>
    </div>
</template>
<style src="./tNavBar.css">
</style>
<script src="./tNavBar.js">
</script>
