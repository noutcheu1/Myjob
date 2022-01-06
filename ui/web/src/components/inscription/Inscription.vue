<template>
<section class="inscription">
    <header>
        <img src="@/assets/bix_logo.jpg"/>
    </header>
    <div class="insMain">
        <form class = "insMainSection" @submit="submiting" action="#">
            <div class = "insTitle">
                <span>Sign up for your account</span>
            </div>
            <div class ="insInput">
                <InputI0 placeholder="Enter your Surname" ref="surname" type = "text" pattern="^[a-zA-Z ]{4,22}$"/>
            </div>
            <div class ="insInput">
                <InputI0 placeholder="Enter name" ref="name" type = "text" pattern="^[a-zA-Z ]{4,22}$"/>
            </div>
            <div class ="insInput">
                <InputI0 placeholder="Enter your password" ref="password" type = "password" pattern="^.{4,22}$" />
            </div>
            <div class ="insInput">
                <InputI0 placeholder="Confirm password" ref="confirmpw" type = "password" pattern="^.{4,22}$" />
            </div>
            <div class="insLaw">
                <span class ="insPolicy">By signing up, you confirm that you've read and accepted our <span>Terms of Service</span> and <span>Privacy Policy</span>. </span>
            </div>
            <div @click='toNext' ><ButtonI0 message = "continue" /></div>
            <div class = "insOR">
                <span class ="insPolicy">OR</span>
            </div>
            <div class="insLast">
                <a href='/login'>Already have an account? Log In</a>
            </div>
        </form>
        <section class = "insSiteLang">
            <DropDownList/>
        </section>
    </div>
    <FooterI/>
</section>
</template>
<style src="./inscription.css">
</style>
<script src = "./inscription.js">
</script>
