<h1>Etudes du Covid19 en France par Machine Learning</h1>
<p>Par <a href="http://www.cyrilvincent.com">Cyril Vincent</a></p>
<img src="data/giphy.gif"/>
<p>Etant expert en IA et Machine Learning, j'ai mené une étude sur les données COVID disponible sur le site santepubliquefrance.fr</p>
<p>C'est juste un exercice de style, <b>je ne suis pas médecin</b> donc cette étude ne vaut rien!!</p>
<img src="https://i.ytimg.com/vi/8Dicw41hHlk/maxresdefault.jpg"/>
<p>J'ai téléchargé et nettoyé les données sur <a href="https://coronavirus.politologue.com/coronavirus-france.FR">politologue.com</a> </p>
<p>J'ai utilisé le framework Scikit-Learn en Python 3.8 pour analyser les données avec du Machine Learning (ML) et une régression polynômiale ridge de degré 4. Un réseau neuronal a été tenté sans succès par manque de données</p>
<p>J'ai également programmé en Python le modèle SCIRE+ à l'aide du framework NumPy (Sain-Contaminé-Infecté-Rétablie-Etendue) avec des améliorations en modulant le facteur beta d'après https://interstices.info/modeliser-la-propagation-dune-epidemie
<img src="data/scir.png"><img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png"><img src="https://numpy.org/_static/numpy_logo.png"><img src="https://www.python.org/static/img/python-logo@2x.png">
<h2>Etude 3: Le déconfinement</h2>
<p>Etude démarrée au 24/4. MAJ le 28/4 avec plan de déconfinement et les données inquiétantes de l'Allemagne où le R en déconfinement est passé de 0.7 à 1 en 10 jours. En France le R est à 0.5.</p>
<p>Au déconfinement, le 11 mai (J128), je propose 4 scénarios, pour cela j'ai modifié SCIRE pour avoir un R variable linéairement ou sinusoîdalement pour la saisonalité
<p>Scénario Marseillais optimiste: Comme le SRAS et comme le propose le professeur Raoult, le virus disparait, R = 0.5 - fsin(t) ~= [0..2.1]
    <ul>
        <li>Les modèles prédisent une disparition du virus fin Mai</li>
        <li>+1000 décès</li>
    </ul>
    <img src="data/figured1.png">
<p>Scénario Start & Go pessimiste: le déconfinement est un échec, R=R0
    <ul>
        <li>Un 2ème pic et reconfinement à J+50 pour le modèle SCIRE, J+20 pour ML</li>
        <li>Doublement des décès</li>
    </ul>
    <img src="data/figured2.png"><img src="data/figureml.png">
<p>Scénario Allemand médian: les mesures de protection fonctionnent. Le R remonte linéairement, un été protecteur, R = 0.5 + 0.3 + 0.1t - fsin(t) / 2 ~= [0:3.3]
    <ul>
        <li>Le virus disparait début Juin</li>
        <li>Pas de seconde vague</li>
        <li>+1000 décès</li>
    </ul>
    <img src="data/figured3.png">
<p>Scénario Grenoblois médian : les mesures de détection fonctionnent moyennement. Le R remonte linéairement, l'été n'est pas aussi protecteur qu'espéré, R = 0.5 + 0.5 + 0.2t * fsin(t) / 4 ~= [0.2:3.3]
    <ul>
        <li>L'été se passe à l'identique du confinement</li>
        <li>Reconfinement à la rentrée</li>
        <li>+ 20000 décès avant reconfinement </li>
    </ul>
<img src="data/figured4.png">
<p>Conclusion: Si R repasse au dessus de 1, un second pic sera inévitable</p>
<p>Comme le montre le sud de la France et l'Afrique, les temps ensoleillés, secs et chauds semblent diminuer fortement R, donc il faut être optimiste</p>

<h2>Etude 2 : Le confinement</h2>
<p>En date du 24/4 (MAJ le 27/04) nous savons que le R0=3.3 est plus optimiste que mon étude 1 et le R a atteint 0.5 soit une baisse d'un facteur 7</p>
<p>Tout d'abord un modèle SCIRE a été mis en place avec un Rmoyen=1 variant de 3.3 à 0.5</p>
<img src="data/figurec.png">
<p>Ensuite un modèle ML a été mis en place à partir du 24/4</p>
<img src="data/figure.png">
<p>A la date du déconfinement le 11 mai (J128), le modèle ML nous donne un score trop faible (30%) pour être fiable et le modèle SCIRE est difficile à étudier quand R varie, le taux d'erreur est donc énorme</p>
<ul>
    <li>Le modèle SCIRE prévoit 800000 personnes contaminantes</li>
    <li>Le modèle ML prévoit 160000 cas détectés et 3000 cas/jour détectés</li>
    <li>Le modèle SCIRE prévoit 32000 décès</li>
    <li>Le modèle ML prévoir 24000 décès hopitaux et EPHAD</li>
    <li>4.7 millions de personnes ayant été infectées</li>
    <li>Taux d'infection de 7%</li>
</ul>
<p>En Auvergne Rhône-Alpes à la date du déconfinement le 11 mai (J128)
<ul>
    <li>Le modèle SCIRE prévoit 18000 personnes contaminantes</li>
    <li>Le modèle ML prévoit 8500 cas détectés et 160 cas/jour détectés</li>
    <li>Le modèle ML prévoir 1300 décès hopitaux et EPHAD</li>
    <li>250000 personnes ayant été infectées</li>
    <li>Taux d'infection de 3%</li>
    <li>Sur le plateau des 4 montagnes dans le Vercors on peut extrapoler au déconfinement 30 contaminants, 15 cas détectés, 0 cas/jour, 2 décès et 400 personnes infectées</li>
</ul>
Conclusion: le paramètre R reflète l'interaction entre les personnes, le confinement l'a diminué d'un facteur 7, de 3.3 à 0.5 avec une moyenne à 1

<h2>Etude 1: Sans confinement</h2>
<p>Seul le modèle SCIRE a pu être utilisé car les données étaient insuffisantes pour le Machine Learning</p>
<p>Ci-dessous l'état des lieux à la date du confinement J45 qui permet de trouver R0 = 4.2
<img src="data/figure45.png">
<p>Sans confinement, ni protection, ni mesure de distanciation, les chiffres sont catastrophiques, en prenant comme hypothèse R0 = 4.2, en date de J45 la veille du confinement
<ul>
    <li>3 millions d'infection</li>
    <li>250000 décès en 250 jours avec le nombre de lit en réanimation adéquat</li>
    <li>Au moins 50000 décès supplémentaire par manque de lit</li>
    <li>Une pointe à 15000 morts par jour avec le nombre de lit en réanimation nécessaire</li>
    <li>Une pointe à 20000 morts par jour pour 5000 lits de réanimation</li>
</ul>
<img src="data/figure250.png">
Il faudra attendre 2 à 3 ans pour atteindre l'immunité collective situé autour de 60% de la population ayant été infectée par le virus, sauf si un vaccin efficace et disponible arrive avant

Voici un boulot de malade fait en <a href="https://www.kaggle.com/vanshjatana/machine-learning-and-time-series">Corée du Sud</a>

<H2>Etude 0: Analyse ADN</h2>
En 2011 et 2013 j'avais publié sur Google Code un programme en C# reproduisant le mécanisme génétique de la transcription de l'ADN vers les protéines, pour différents types de cellule dont les eucaryotes.

Le génôme complet du SARS-CoV-2 est disponible sur <a href="https://www.kaggle.com/paultimothymooney/coronavirus-genome-sequence#MN908947.txt">Kaggle</a>.
Il s'agit d'un virus à ARN qui pirate les ARNt des cellules humaines, le génôme contient 29903 bases

La transcription d'un ARN de virus est plus complexe que celui d'un ARN celullaire car il peut être lu dans les 2 sens et avec 3 décalages différents en fonction de son insertion dans l'ARN hôte qui est aléatoire, il y a donc 6 transcriptions: les frames 1,2,3,4,5,6. Le virus génère 141 proteines, dont voici la représentation <a href="data/covid19.aa">covid19.aa</a>

Similarité HIV

Il est vrai qu'une séquence de 38 bases ressemble à une séquence du HIV qui est beaucoup plus gros avec 4.5 millions de bases
<img src="data/hiv1.png">
Il s'agit d'une ressemblance 33/38 soit 87%. Nous pouvons nous dire que 38 bases sur 30000 représente seulement 0.1% du virus, cependant cette séquence est utilisée pour transcrire un protéine, ce qui représente 0.7% des proteïnes générées ce qui n'est pas rien

Une autre séquence plus courte ressemble au HIV
<img src="data/hiv2.png">
Il s'agit d'une ressemblance 28/30 soit 93%.
La probabilité d'avoir 30 bases identiques sur 30000 d'après la loi binomiale est n! / k!(n-k)! = 30000! / 28!(29972)! = 1/28!*PI(29973..30000) < 1e-64 = 0.
Ces 2 séquences sont actives dans la transcription

Contre arguments: Un virus de chauve souris possède une séquence similaire
<img src="data/bat1.png">Cette séquence code une enzyme indispensable à tous les virus ARN comme le HIV.
Ces séquences n'appartiennent pas à la proteine spike utilisée pour les vaccins, sauf accident il n'y aurait aucun intérêt à les injecter.
Ces séquences sont très courtes car elles ne peuvent transcrire que 10 acides aminées ce qui est insufisant pour copier une proteine entière.
Le HIV est un retrovirus qui fonctionne différement d'un virus coronavirus

La séquence TTCCTATGGACAGTACAGTTAAAAACTATT se retrouve dans une séquence plus grande à la position <a href="covid19.aa">20401</a> qui code la protéine commencant par SPFELEDFIP<b>MDSTVKNYFI</b>... de 80 acides aminées.

Une transcription détaillée du virus est disponible à la <a href="https://www.ncbi.nlm.nih.gov/nuccore/1798174254">NCBI</a>. Le virus produit 11 gênes.
Sur cette transcription nous retrouvons bien la séquence à la position 20401 mais elle ne semble pas produire de gêne. Elle semble être dans la plus grande zone de la séquence sans transcription comprise 13542 et 21543. La fameuse proteine Spike se trouve 1100 bases plus loin.

Conclusion: Ces séquences sont naturelles, il existe une infime possibilité que la séquence de 30 bases soit le résultat d'une manipulation humaine qui a échouée. J'encourage néanmoins à lire la page <a href="https://fr.wikipedia.org/wiki/Institut_de_virologie_de_Wuhan">Wikipedia du laboratoire P4 de Wuhan</a>.


