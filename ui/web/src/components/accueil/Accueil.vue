<template>
    <div>
        <TNavBar/>
        <div>
            <MyProfile/>
        </div>
        <div class="flex_acceuil">
            <div>
            <CardBid title='Déposer votre CV' text="Des miliers de cv sont déposé chaque jour sur MyJob. Déposé votre cv pour avoir la chance d'etre contacté direstement par un recruteur"/>
        </div>
         <div>
            <CardBid link='postJob'/>
        </div>
        </div>
        <div class="div_offres_recentes">
            <div class="lign_offres">
            </div>
            <div class="img_offres_recentes">
                <img src='../../assets/offresRecentes.png'/>
            </div>
            <div class="lign_offres">
            </div>
        </div>
         <div class="flex_acceuil">
            <div>
                <CardBid1 displayNumbCandidate='none'/>
            </div>
            <div>
                <CardBid1 displayNumbCandidate='none'/>
            </div>
            <div>
                <CardBid1 displayNumbCandidate='none'/>
            </div>
        </div>
        <div class="div_offres_recentes">
            <div class="lign_offres">
            </div>
            <div class="img_offres_recentes">
                <img src='../../assets/offresCandidates.png'/>
            </div>
            <div class="lign_offres">
            </div>
        </div>
          <div class="flex_acceuil">
            <div>
                <CardBid1 :datas='publicationIndexes[0]' displayNew='none' />
            </div>
            <div>
                <CardBid1 :datas='publicationIndexes[1]' displayNew='none'/>
            </div>
            <div>
                <CardBid1 :datas='exist(publicationIndexes[2])' displayNew='none'/>
            </div>
        </div>
        <div class="flex_acceuil">
            <div>
                <CardBid1 :datas='exist(publicationIndexes[3])' displayNew='none'/>
            </div>
            <div>
                <CardBid1 :datas='publicationIndexes[4]' displayNew='none'/>
            </div>
            <div>
                <CardBid1 :datas='publicationIndexes[5]' displayNew='none'/>
            </div>
        </div>
        <div style="display:flex; justify-content:center; align-items:center;"><LPagination/></div>

        <div>
            <L-pblication-form/>
        </div>
         <footer>
            <div class="flex_acceuil">
            <div class="text_left">
                  <div class="description_myjob">
                    <h2>Why My Job ?</h2>
                    <p>    My Job  est un site web qui vient résoudre dans une certaines mesure se probleme en donnant entre autres la <br> possibilitée a un utilisateur de rechercher des offres d’emplois en fonction de son curriculum vitae, a un administrateur de <br> filtrer les annoces poster et a des recruteurs de pouvoir  rechercher des profils pour des eventuels recrutements.  </p>
                    </div>
                    <div class="flex_acceuil">
                        <div class="find_job card">
                            <h2>Find Job?</h2>
                        </div>
                        <div class="find_talent card">
                            <h2>Find Talent?</h2>
                        </div>
                        <div class="pages card">
                            <h2>Pages</h2>
                        </div>
                    </div>
              </div>
              <div class="social_network">
                    <h2>Plan du Site</h2>
                   <ul>
                       <li>
                            <a href="#services">
                               <br>
                                <p>Services</p>
                            </a>
                        </li>
                        <li>
                            <a href="#realisation">
                                <P>-----------------------</P>
                                <p>Réalisations</p>
                            </a>
                        </li>
                        <li>
                            <a href="#team">
                                <P>-----------------------</P>
                                <p>Equipe</p>
                            </a>
                        </li>
                        <li>
                            <a href="#partenaires">
                                <P>-----------------------</P>
                                <p>partenaires</p>
                            </a>
                        </li>
                        <li>
                            <a href="#contact">
                                <P>-----------------------</P>
                                <p>Contacts</p>
                                <P>-----------------------</P>
                            </a>
                        </li>
                   </ul>
              </div>
            </div>
            <div class="lign_offres_footer"></div>
            <div class="copyright">
                <p>Copyrigth 2022. All rigth reserved </p>
            </div>
        </footer>
    </div>
</template>
<style src="./accueil.css">
</style>
<script src="./accueil.js">
</script>
