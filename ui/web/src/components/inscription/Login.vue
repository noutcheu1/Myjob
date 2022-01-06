<template>
<section class="inscription">
    <header>
        <img src="@/assets/bix_logo.jpg"/>
    </header>
    <div class="insMain">
        <form class = "insMainSection" @submit="submiting" action="#">
            <div class = "insTitle">
                <span>Log in</span>
            </div>
            <div class ="insInput">
                <InputI0 ref="name" placeholder="Enter name" type = "text" />
            </div>
            <div class ="insInput">
                <InputI0 ref="password" placeholder="Enter your password" type = "password"  pattern="^[a-zA-Z ]{4,22}$"/>
            </div>
            <div class="insLaw">
                <span class ="insPolicy">By loging in, you confirm that you are aware of our <span>Terms of Service</span> and <span>Privacy Policy</span>. </span>
            </div>
            <div @click="login"><ButtonI0 message = "Login" /></div>
            <div class = "insOR">
                <span class ="insPolicy">OR</span>
            </div>
            <div class="insLast">
                <a href="/inscription">You don't have an account? Sing Up</a>
            </div>
        </form>
        <section class = "insSiteLang">
            <DropDownList/>
        </section>
    </div>
    <FooterI/>
</section>
</template>
<script src = "./login.js">
</script>
<style src="./inscription.css">
</style>
