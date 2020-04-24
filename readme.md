<h1>Etude du Covid19 en France par Machine Learning</h1>
<p>Par Cyril Vincent</p>
<p>Etant expert en IA et Machine Learning, j'ai mené une étude sur les données COVID disponible sur le site santepubliquefrance.fr</p>
<p>Evidement <b>je ne suis pas médecin</b> donc cette étude ne vaut rien!!</p>
<p>J'ai téléchargé et nettoyé les données sur https://coronavirus.politologue.com/coronavirus-france.FR </p>
<p>J'ai utilisé le framework Scikit-Learn pour analyser les données. Il était impossible d'utiliser Keras car le nombre de données est trop faible</p>
<p>J'ai également programmé le modèle SCIRE (Sain-Contaminé-Infecté-Rétablie-Etendue) avec mofdification d'après https://interstices.info/modeliser-la-propagation-dune-epidemie
<img src="data/scir.png">
<p>Le tout a été programmé en 4h, le code est disponible ci-dessus, le modèle SCIRE fait moins de 50 lignes</p>
<p>Ces modèles existent depuis + de 10 ans et toutes les données du SCIRE étaient déjà disponible avant la mi-février, pourquoi ne pas les avoir montrées avant ?</p>
<p>J'ai créé 4 modèles en incluant les données :
    <ul>
        <li>à partir de J0 : le premier cas est diagnostiqué le 24/01, le modèle est peu fiable car les données de départ sont constantes</li>
        <li>à partir de 10 cas (J15) : le modèle est encore trop peu fiable car le stade 1 de l'épidémie en France était trop différent du stade 2</li>
        <li>à partir du J41, la veille du jour où l'épidémie commence à décollée, passage de 92 à 276 cas</li>
        <li>à partir du 1er jour du confinement, J56</li>
    </ul>
<p>J'ai ensuite créé les modèles SCIRE et Machine Learning (ML) avec une regréssion polynômiale ridge de degré 4. Ci dessous un extrait du modèle ML</p>
<img src="data/figure.png"/>
<p>En date du 24/04</p>
<p>Ci dessous l'état des lieux à la date du confinement J45 qui permet de trouver R0 = 4.2 au lieu de 3.3 admis aujourd'hui, le virus serait donc 25% plus virulent suivant mon modèle
<img src="data/figure45.png">
<p>Sans confinement, ni protection, ni mesure de distanciation, les chiffres sont catastrophiques
<img src="data/figure250.png">
<ul>
    <li>3 millions d'infection</li>
    <li>250000 décès en 250 jours avec le nombre de lit en réanimation adéquat</li>
    <li>Au moins 50000 décès supplémentaire par manque de lit</li>
    <li>Une pointe à 15000 morts par jour avec le nombre de lit en réanimation nécessaire</li>
    <li>Une pointe à 20000 morts par jour pour 5000 lits de réanimation</li>
</ul>

<p>A la date du déconfinement le 11 mai (J128), le modèle ML nous donne des chiffres assez optimistes mais avec <b>une RValue (score) trop faible pour que ces chiffres soient fiables</b>, de plus le modèle SCIRE ne fonctionne pas car R varie pendant cette période, le taux d'erreur est donc énorme</p>
<ul>
    <li>Nombre de nouveaux cas sera quasi nul!</li>
    <li>150000 cas confirmés</li>
    <li>23000 décès</li>
    <li>4.5 millions de personnes ayant été infectées</li>
    <li>Taux d'infection de 7%</li>
</ul>
<p>En Auvergne Rhône-Alpes à la date du déconfinement le 11 mai (J128)
<ul>
    <li>Nombre de nouveaux cas sera quasi nul!</li>
    <li>1200 décès</li>
    <li>0.3 millions de personnes ayant été infectées</li>
    <li>Taux d'infection de 3%</li>
</ul>
<p>Au déconfinement, je propose 4 scénarios
<p>Scénario optimiste: Comme le SRAS et comme le propose le professeur Raoult, le virus disparait, R=0.01
    <ul>
        <li>D'après le modèle SCIRE, un pic d'infection très bref, puis le virus disparait assez rapidement à J+50</li>
        <li>D'après le modèle ML, le virus disparait immédiatement</li>
        <li>Entre 23000 et 27000 décès au total</li>
    </ul>
    <img src="data/figured1.png">
<p>Scénario pessimiste: le confinement est un échèc, R=R0, peu probable car ne se produit pas ailleurs dans le monde
    <ul>
        <li>Un énorme pic d'infection à J+50</li>
        <li>40000 décès au total avec reconfinement, 500000 sans</li>
    </ul>
    <img src="data/figured2.png">
<p>Scénario médian: les mesures de protection fonctionnent avec 90% de détection, isolement des patients I, protections, un été protecteur, R=R0*0.1
    <ul>
        <li>Une petite reprise rapide, un été clément</li>
        <li>Un second pic modeste à l'automne, <40000 décès au total sur 250 jours</li>
    </ul>
    <img src="data/figured3.png">
<p>Scénario médian-pessimiste: les mesures de protection fonctionnent moyennement ou déconfinement trop rapide, R = 1
    <ul>
        <li>Divergence entre les modèles</li>
        <li>D'après le modèle SCIRE, un second pic entre Juillet et Novembre, reconfinement possible, 200000 décès possible</li>
        <li>D'après le modèle ML, un second pic à l'automne mais plus étalé qu'au printemps, 40000 à 50000 décès</li>
    </ul>
    <img src="data/figured4.png">
<p>La moindre variation du paramètre R peut complètement modifier l'évolution de l'épidémie, le ML ne possède pas assez données pour être fiable, ma conclusion est donc de rester modeste</p>
<p>Comme le montre le sud de la France et l'Afrique, les temps secs et chaud semble diminuer fortement R, donc soyons optimiste</p>

Il faudra attendre 2 à 3 ans pour atteindre l'immunité collective situé autour de 60% de la population ayant été infectée par le virus, sauf si un vaccin efficace et disponible arrive avant

    


