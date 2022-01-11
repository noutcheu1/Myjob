<template>
<section class="inscription">
    <header>
        <img src="@/assets/myjob.png"/>
    </header>
    <div class="wrapper">
        <div class="insMain">
        <form class = "insMainSection" @submit="submiting" action="#">
            <div class = "insTitle">
                <span><h1>Welcome Back..</h1></span>
            </div>
            <div class ="insInput">
                <InputI0 ref="name" placeholder="Enter name" type = "text" />
            </div>
            <div class ="insInput">
                <InputI0 ref="password" placeholder="Enter your password" type = "password"  pattern="^[a-zA-Z ]{4,22}$"/>
            </div>
            <div class="insLaw">
                <span class ="insPolicy">By login in, you confirm that you are aware of our <span>Terms of Service</span> and <span>Privacy Policy</span>. </span>
            </div>
            <div @click="login"><ButtonI0 message = "Login" /></div>
            <div class = "insOR">
                <span class ="insPolicy">OR</span>
            </div>
            <div class="insLast">
                <a href="/inscription">You don't have an account? Sing Up</a>
            </div>
            <DropDownList/>
        </form>
    </div>
    <div class="img_login">
        <img src="@/assets/filleLogin.png"/>
    </div>
    </div>
</section>
</template>
<script src = "./login.js">
</script>
<style src="./inscription.css">
</style>
