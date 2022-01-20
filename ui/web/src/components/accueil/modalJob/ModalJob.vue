<template>
<section id="modalJob">
    <h1>Community manager</h1>
    <form class = "insMainSection" @submit="submiting" action="#">
        <p>Avez vous un cv? <span class="red">*</span></p>
        <input type="radio" id="yes" value="oui">
        <label for="oui">OUI</label>
        <input type="radio" id="no" value="non">
        <label for="non">NON</label>
        <input type="file" id="upload" placeholder="Telecharger votre cv depuis votre appareil" value="telecharger">
        <input type="text" placeholder="Entrez votre texte ici" id="text" value="attentes">
        <label for="attentes">Quels sont vos attentes par rapport a cet offrre d’emploie ?  <span class="red">*</span></label>
        <input type="text" placeholder="Entrez le montant en Fcfa qui vous correspond!" id="salary" value="salaire">
        <label for="salaire">Quel offre de salaire pourra vous satisfaire? </label>
        <input type="button" value="Subscribe">
    </form>
</section>
</template>
<style src="./modalJob.css">
</style>
<script src="./modalJob.js">
</script>
