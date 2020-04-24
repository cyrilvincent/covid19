<h1>Etude du Covid19 en France par Machine Learning</h1>
<p>Par Cyril Vincent</p>
<p>Etant expert en IA et Machine Learning, j'ai mené une étude sur les données COVID disponible sur le site santepubliquefrance.fr</p>
<p>Evidement <b>je ne suis pas médecin</b> donc cette étude ne vaut rien!!</p>
<p>J'ai téléchargé et nettoyé les données sur https://coronavirus.politologue.com/coronavirus-france.FR </p>
<p>J'ai utilisé le framework Scikit-Learn pour analyser les données. Il était impossible d'utiliser Keras car le nombre de données est trop faible</p>
<p>J'ai également programmé le modèle SCIRE d'après https://interstices.info/modeliser-la-propagation-dune-epidemie
<p>Le tout a été programmé en 4h</p>
<img src="data/scir.png">
<p>J'ai créé 4 modèles en incluant les données :
    <ul>
        <li>à partir de J0 : le premier cas est diagnostiqué le 24/01, le modèle est peu fiable car les données de départ sont constantes</li>
        <li>à partir de 10 cas (J15) : le modèle est encore trop peu fiable car le stade 1 de l'épidémie en France était trop différent du stade 2</li>
        <li>à partir du J41, la veille du jour où l'épidémie commence à décollée, passage de 92 à 276 cas</li>
        <li>à partir du 1er jour du confinement, J56</li>
    </ul>
<p>J'ai ensuite créé les modèles SCIRE et de Machine Learning (ML) avec un polynôme de degré 4.</p>
<img src="data/figure.png"/>
<p>En date du 24/04</p>
<p>Sans confinement, ni mesure de distanciation, les chiffres sont catastrophiques
<p>Ci dessous l'état des lieux à la date du confinement J45 qui permet d'établire SCIRE.Beta = 0.22
<img src="data/figure45.png">
<p>Sans mesure de protection, le scénario suivant se serait alors produit
<img src="data/figure250.png">
<ul>
    <li>1.3 millions d'infection</li>
    <li>0.5 millions de décès en 250 jours avec le nombre de lit en réanimation adéquat</li>
    <li>0.75 millions de décès en 250 jours pour 5000 lits de réanimation</li>
    <li>Une pointe à 13000 morts en une journée avec le nombre de lit en réanimation nécessaire</li>
    <li>Une pointe à 19000 morts en une journée pour 5000 lits de réanimation</li>
</ul>

<p>A la date du déconfinement le 11 mai (J128), le modèle ML nous donne des chiffres assez optimistes mais avec <b>une RValue (score) trop faible pour que ces chiffres soient fiables</b>
<ul>
    <li>Nombre de nouveaux cas sera quasi nul!</li>
    <li>150000 cas confirmés</li>
    <li>23000 décès</li>
    <li>4.4 millions de personnes ayant été infectées</li>
    <li>Taux d'infection de 7%</li>
</ul>
<p>En Auvergne Rhône-Alpes à la date du déconfinement le 11 mai (Jour 128)
<ul>
    <li>Nombre de nouveaux cas sera quasi nul!</li>
    <li>1200 décès</li>
    <li>0.3 millions de personnes ayant été infectées</li>
    <li>Taux d'infection sera de 3%</li>
</ul>
<p>Au déconfinement, le modèle SCIRE nous propose 4 scénarios
<p>Scénario optimiste: Comme le SRAS, le virus quasi disparait, SCIRE.Beta = 0.01
    <ul>
        <li>D'après le modèle SCIRE, un pic d'infection très bref à j+5, puis le virus disparait assez rapidement à J+60</li>
        <li>D'après le modèle ML, le virus quasi disparait immédiatement</li>
        <li>&lt;25000 décès</li>
    </ul>
    <img src="data/figured1.png">
<p>Scénario pessimiste: le confinement est un échèc, SCIRE.Beta inchangé
    <ul>
        <li>Reconfinement à J+23</li>
        <li>Un énorme pic d'infection à J+50 si aucun reconfinement</li>
        <li>40000 décès avec reconfinement, 500000 sans</li>
    </ul>
    <img src="data/figured2.png">
<p>Scénario médian: les mesures de protection fonctionnent, SCIRE.Beta est divisé par 4
    <ul>
        <li>Un second pic à J+8 puis un 3ème en Octobre - Novembre</li>
        <li>D'après le modèle SCIRE, 70000 décès sur 250 jours</li>
        <li>D'après le modèle ML, 27000 décès sur 250 jours</li>
        <li>Entre 1.2 et 3 fois plus de personnes contaminées mais sur 7 mois</li>
        <li>Un taux d'immunisation de 9% à 21% en fin d'année</li>
    </ul>
<p>Scénario médian-pessimiste: les mesures de protection fonctionnent moyennement, SCIRE.Beta est divisé par 2
    <ul>
        <li>Grande divergence entre les modèles</li>
        <li>Un second pic à J+70 ou J+180 aussi important que le précédent mais plus étalé, soit en été soit à l'automne</li>
        <li>Le nombre de décès sur 250 jours varie de 27000 à 300000!</li>
    </ul>
<p>La moindre variation d'un paramètre peut complètement modifier l'évolution de l'épidémie, ma conclusion est donc de rester modeste</p>

Il faudra attendre 2.5 à 3 ans pour atteindre l'immunité collective situé autour de 60% de la population ayant été infectée par le virus

    


