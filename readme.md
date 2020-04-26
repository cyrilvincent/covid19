<h1>Etudes du Covid19 en France par Machine Learning</h1>
<p>Par Cyril Vincent</p>
<p>Etant expert en IA et Machine Learning, j'ai mené une étude sur les données COVID disponible sur le site santepubliquefrance.fr</p>
<p>Evidement <b>je ne suis pas médecin</b> donc cette étude ne vaut rien!!</p>
<img src="data/giphy.gif"/>
<p>J'ai téléchargé et nettoyé les données sur https://coronavirus.politologue.com/coronavirus-france.FR </p>
<p>J'ai utilisé le framework Scikit-Learn en Python 3.8 pour analyser les données avec du Machine Learning (ML) et une régression polynômiale ridge de degré 4. Un réseau neuronal a été tenté sans succès par manque de données</p>
<p>J'ai également programmé en Python le modèle SCIRE+ (Sain-Contaminé-Infecté-Rétablie-Etendue) avec des améliorations en modulant le facteur beta d'après https://interstices.info/modeliser-la-propagation-dune-epidemie
<img src="data/scir.png"><img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png"><img src="https://www.python.org/static/img/python-logo@2x.png">
<h2>Etude 3: Le déconfinement</h2>
<p>Au déconfinement, le 11 mai (J128), je propose 4 scénarios, pour cela j'ai modifié SCIRE pour ajouter un taux de détection des individus infectés et une fonction d'atténuation sinusoidale dû à l'été R = R * DetectionRate * sin(2xpi/365)
<p>Scénario Marseillais optimiste: Comme le SRAS et comme le propose le professeur Raoult, le virus disparait, R = R0 * 0.5 * 0.1 - fsin(t) ~= [0..0.4]
    <ul>
        <li>Le modèle SCIRE prévoit une extinction du virus début Juin avec une baisse par vaguelette</li>
        <li>Le modèle ML prévoit un extinction en Mai</li>
        <li>24000 décès au total</li>
    </ul>
    <img src="data/figured1.png">
<p>Scénario Start & Go pessimiste: le confinement est un échec, R=R0
    <ul>
        <li>Un énorme pic d'infection à J+50</li>
        <li>Reconfinement</li>
    </ul>
    <img src="data/figured2.png"><img src="data/figureml.png">
<p>Scénario Grenoblois médian: les mesures de protection fonctionnent avec 50% de détection, isolement des patients infectés, protections, un été protecteur, R = R0 * 0.5 * 0.5 - fsin(t) / 2 ~= [0.4:0.8]
    <ul>
        <li>Une baisse rapide du virus sur 1 mois</li>
        <li>Un petit rebond fin Juin</li>
        <li>27000 décès</li>
    </ul>
    <img src="data/figured3.png">
<p>Scénario Parisien médian-pessimiste : les mesures de détection fonctionnent moyennement à 50% des symptomatiques soit 10% de détection totale, le reste fonctionne bien et l'été fait son travail, baisse du R de 0.05 tous les 15 jours, R = R0 * 0.5 * 0.9 - fsin(t) / 4 ~= [1.6:2.2]
    <ul>
        <li>Très incertain en fonction du paramètre de saisonnalité</li>
        <li>Un gros pric à J+15 à la limite du confinement et une baisse sur 75 à 100 jours</li>
        <li>50000 décès</li>
        <li>Présence d'un pic à l'automne si l'été n'est pas chaud</li>
    </ul>
Ci dessous les 3 modélisation où l'amortissement de l'été est d'un facteur de 1/2, 1/3, 1/4
<img src="data/figured4.png"><img src="data/figured42.png"><img src="data/figured43.png">
<p>La moindre variation du paramètre R peut complètement modifier l'évolution de l'épidémie, le ML ne possède pas assez données pour être fiable, il faut donc rester modeste</p>
<p>Conclusion générale : les modèles sont très incertains, une boule de cristal ferait aussi bien, le paramètre R reflète l'interaction entre les personnes, le confinement l'a diminué d'un facteur 7, d'autres mesures comme les protections et les détections massives arrivent à un résultat proche, en mai un petit pic va avoir lieu mais avec un peu de chance l'épidémie va vite refluée si les moyens de détection fonctionnent et sont massifs, le risque de 2ème vague à l'automne est très fort mais peu quantifiable pour le moment.</p>
<p>Comme le montre le sud de la France et l'Afrique, les temps ensoleillés, secs et chauds semblent diminuer fortement R, donc soyons optimiste</p>

<h2>Etude 2 : Le confinement</h2>
<p>En date du 24/4 nous savons que le R0=3.3 est plus optimiste que mon étude 1 et le R a atteint 0.5 soit une baisse d'un facteur 7</p>
<p>Tout d'abord un modèle SCIRE a été mis en place avec un Rmoyen=0.8</p>
<img src="data/figurec.png">
<p>Ensuite un modèle ML a été mis en place à partir du 24/4</p>
<img src="data/figure.png">
<p>A la date du déconfinement le 11 mai (J128), le modèle ML nous donne un score trop faible (30%) pour être fiable et le modèle SCIRE est difficile à étudier quand R varie, le taux d'erreur est donc énorme</p>
<ul>
    <li>Le modèle SCIRE prévoit 360000 cas réels par jour, contre 10 pour ML</li>
    <li>150000 cas confirmés</li>
    <li>23000 décès</li>
    <li>4.5 millions de personnes ayant été infectées</li>
    <li>Taux d'infection de 7%</li>
</ul>
<p>En Auvergne Rhône-Alpes à la date du déconfinement le 11 mai (J128)
<ul>
    <li>Le modèle SCIRE prévoit 18000 cas réels par jour, contre 0 pour ML</li>
    <li>1200 décès</li>
    <li>0.3 millions de personnes ayant été infectées</li>
    <li>Taux d'infection de 3%</li>
</ul>


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

<H2>Mini étude: Analyse ADN</h2>
En 2011 et 2013 j'avais publié sur Google Code un programme en C# reproduisant le mécanisme génétique de l'ADN vers les protéines en passant par l'ARN et le Ribosome, pour différents types de cellule.

Le génôme complet du SARS-CoV-2 est disponible <a href="https://www.kaggle.com/paultimothymooney/coronavirus-genome-sequence#MN908947.txt">ici</a>
Il s'agit d'un virus à ARN qui pirate les ARNt des cellules humaines, le génôme fait un peu moins de 30000 bases

J'ai d'abord convertis le génôme en ARN <a href="data/covid19.rna">Covid19.rna</a>, j'ai ensuite créé par retro-transcription son ADN <a href="data/covid19.dna">Covid19.dna</a>.
La transcription d'un ARN de virus est plus complexe que celui d'un ARN celullaire car il peut être lu dans les 2 sens et avec 3 décalages différents en fonction de son insertion dans l'ARN hôte, il y a donc 6 transcriptions possibles : les frames 0,1,2,-0,-1 et -2. Le virus génère 41 proteines, dont voici la représentation <a href="data/covid19.aa">covid19.aa</a>

Similarité HIV

Il est vrai qu'une séquence de 38 bases ressemble au HIV
<img src="data/hiv1.png">
Il s'agit d'une ressemblance 33/38 soit 87%. Nous pouvons nous dire que 38 bases sur 30000 représente seulement 0.1% du virus, cependant cette séquence est utilisée pour transcrire un protéine, ce qui représente 2.5% des proteïnes générée ce qui n'est pas rien

Une autre séquence plus courte ressemble au HIV
<img src="data/hiv2.png">
Il s'agit d'une ressemblance 28/30 soit 93%
La probabilité d'avoir 30 bases identiques sur 30000 d'après la loi binomiale est n! / k!(n-k)! = 30000! / 28!(29972)! = 1/28!*PI(29973..30000) < 1e-64 = 0

Contre arguments: Un virus de chauve souris possède une séquence similaire
<img src="data/hiv2.png">
Ces séquences n'appartiennent pas à la proteine spike utilisée pour les vaccins.
Ces séquences sont très courtes car elles ne peuvent transcrire que 10 acides aminées ce qui est insufisant pour copier une proteine.

Conclusion: Avoir 2 protèines identiques au HIV ne peut pas être dûe au hasard, il y a une forte probabilité pour que ces séquences provinnent d'un autre virus, cependant pour la séquence de 30 bases un léger doute peut persister

  


