<template>
    <footer class = "FooterI" >
        <div class="FooterI_enterprise">
            <span>Bixterprise</span>
        </div>
        <div>
            <a>Templates</a>
            <a>Pricing</a>
            <a>Apps</a>
            <a>Jobs</a>
            <a>Blog</a>
            <a>Devellopers</a>
            <a>About</a>
            <a>Help</a>
            <a>Cookie Settings</a>
        </div>
    </footer>
</template>
<style>
    .FooterI {
        box-sizing: border-box;
        padding-bottom:19px;
        padding-top:19px;
    }
    .FooterI .FooterI_enterprise {
        margin-bottom: 10px;
        font-weight: bold;
        font-size: 22px;
        color:  #0052cc
    }
    .FooterI .FooterI_enterprise + div {
        color: #5E6C84;
        font-size: 15px;
        margin: 0px;
    }
    .FooterI a {
        margin-left: 5px;
        margin-right: 5px;
    }
    .FooterI a:hover {
        text-decoration: underline;
        cursor: pointer;
    }
</style>
