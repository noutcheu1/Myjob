<template>
<section class="lPblicationForm" :style="{ display:Display }" >
    <div class="lPBFCTitle"><span class="blue">{{titleWork}}</span>
        <div class="lPBFCCross" @click="displaying()"><img src="./more.svg"/></div>
    </div>
    <div class="lPBFCBody">
        <span class="blue">Avez vous un CV? <span class="red"> *</span></span>
        <div class ="insInput insSex">
            <div>oui<input @click="fillCv('oui')" type = "radio" name="yes" value="oui"/></div>
            <div>non<input  @click="fillCv('non')" type = "radio" name="yes" value="non"/></div>
        </div>
        <div class="lPBoui" :style="{display:displayOui}">
            <div class="lPBuploadCV"><span class="blue">uploader votre CV </span><span class="red"> *</span>
            <label class="custom-file-upload"><input ref='cvInput' @change="preview" type="file"/><img src="./uploader.png"></label>
            <div>{{ cvFileName }}</div>
            </div>
        </div>
        <div class="lPBnon" :style="{display:displayNon}">
            <div @click='sendImage' class="lPBpublier">Parlez nous de vous</div>
                <div>
                    <h3>coordonées</h3>
                </div>
            <label class="custom-file-upload"><input ref='image' @change="preview" type="file"/><img src="./uploader.png"></label>
            <img id="lPbblah" />
        </div>
        <div class="lPBattenteOffre"><span class="blue">Quels sont vos attentes par rapport a cet offrre d’emploie ?</span><span class="red"> *</span><textarea v-model="publiContent" placeholder="Entrer votre texte ici"></textarea></div><br>
        <div class="lPBoffreSalaire"><span class="blue">Quel offre de salaire pourra vous arranger ?</span><span class="red"> *</span><textarea v-model="publiTitle" placeholder="Entrer votre montant ici en FCFA"></textarea> </div><br>
        <div @click='publishing' class="lPBpublier">Publier</div>
    </div>
</section>
</template>
<style src="./lPblicationForm.css">
</style>
<script src="./lPblicationForm.js">
</script>
