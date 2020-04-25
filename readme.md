<h1>Etudes du Covid19 en France par Machine Learning</h1>
<p>Par Cyril Vincent</p>
<p>Etant expert en IA et Machine Learning, j'ai mené une étude sur les données COVID disponible sur le site santepubliquefrance.fr</p>
<p>Evidement <b>je ne suis pas médecin</b> donc cette étude ne vaut rien!!</p>
<img src="giphy.gif"/>
<p>J'ai téléchargé et nettoyé les données sur https://coronavirus.politologue.com/coronavirus-france.FR </p>
<p>J'ai utilisé le framework Scikit-Learn en Python 3.8 pour analyser les données avec du Machine Learning (ML) et une régression polynômiale ridge de degré 4. Un réseau neuronal a été tenté sans succès par manque de données</p>
<p>J'ai également programmé en Python le modèle SCIRE+ (Sain-Contaminé-Infecté-Rétablie-Etendue) avec des améliorations en modulant le facteur beta d'après https://interstices.info/modeliser-la-propagation-dune-epidemie
<img src="data/scir.png"><img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png"><img src="https://www.python.org/static/img/python-logo@2x.png">
<h2>Etude 3: Le déconfinement</h2>
<p>Au déconfinement, le 11 mai (J128), je propose 4 scénarios, pour cela j'ai modifié SCIRE pour ajouter un taux de détection des individus infectés et une fonction d'atténuation sinusoidale dû à l'été R = R * DetectionRate * sin(2xpi/365)
<p>Scénario Marseillais optimiste: Comme le SRAS et comme le propose le professeur Raoult, le virus disparait, R = R0 * 0.5 * 0.1 - sin(t) * r ~= [0:0.2]
    <ul>
        <li>Le modèle SCIRE prévoit un petit pic à J+5 et une extinction du virus début Juin</li>
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
<p>Scénario Grenoblois médian: les mesures de protection fonctionnent avec 50% de détection, isolement des patients infectés, protections, un été protecteur, baisse du R de 0.1 tous les 15 jours, R = R0 * 0.5 * 0.5 - fsin(t) / 2 ~= [0.4:0.8]
    <ul>
        <li>Un petit pic à J+5, puis une disparition du virus en Juin</li>
        <li>Pas de seconde vague si R continue à baisser avec une grosse incertitude</li>
    </ul>
    <img src="data/figured3.png">
<p>Scénario Parisien médian-pessimiste : les mesures de détection fonctionnent moyennement à 50% des symptomatiques soit 10% de détection totale, le reste fonctionne bien et l'été fait son travail, baisse du R de 0.05 tous les 15 jours, R = R0 * 0.5 * 0.1 - fsin(t) / 4 ~= [1.6:2.2]
    <ul>
        <li>Un gros pric à J+15 à la limite du confinement et un été tranquille</li>
        <li>70000 décès</li>
        <li>D'après le modèle ML un pic à l'automne, d'après SCIRE pas de second pic, mais une petite variation de la fonction de saisonalité fait apparaitre un énorme pic au printemps 2021</li>
    </ul>
    <img src="data/figured4.png"><img src="data/figured42.png">
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

  


