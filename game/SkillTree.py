import pygame
from Type import Type
import random

QUESTIONS = {
    "SOCIAL": [
        ("Les réseaux sociaux peuvent avoir un impact négatif sur la santé mentale des employés", True),
        ("Le travail d'équipe est souvent plus productif que le travail individuel", True),
        ("Les stéréotypes de genre n'ont aucune influence sur les choix de carrière", False),
        ("La communication non verbale est moins importante que la communication verbale", False),
        ("L'éducation joue un rôle crucial dans la réduction des inégalités sociales", True),
        ("La discrimination au travail est illégale dans de nombreux pays", True),
        ("Le multiculturalisme enrichit la société", True),
        ("La pauvreté n'a aucun impact sur le développement des enfants", False),
        ("Les loisirs et les hobbies peuvent améliorer le bien-être mental", True),
        ("La politique n'influence pas la vie sociale des individus", False),
        ("Le bénévolat peut augmenter le sentiment de satisfaction personnelle", True),
        ("Les compétences interpersonnelles sont essentielles dans de nombreux emplois", True),
        ("L'isolement social peut conduire à des problèmes de santé mentale", True),
        ("L'âge n'a pas d'impact sur les perspectives d'emploi", False),
        ("La culture influence les comportements et les valeurs des individus", True),
        ("Le salaire est le seul facteur de motivation au travail", False),
        ("La démocratie permet une participation égale de tous les citoyens", True),
        ("Le harcèlement en ligne n'a pas de conséquences graves", False),
        ("L'accès à l'éducation est un droit humain fondamental", True),
        ("Les normes sociales évoluent avec le temps", True),
        ("Les employés qui se sentent valorisés sont plus productifs", True),
        ("La diversité dans les équipes peut stimuler l'innovation", True),
        ("La transparence de la gestion améliore la confiance des employés", True),
        ("Les conflits interpersonnels doivent être évités à tout prix", False),
        ("Les formations régulières augmentent l'efficacité des employés", True),
        ("La reconnaissance des performances améliore la motivation", True),
        ("Les horaires flexibles peuvent augmenter la satisfaction au travail", True),
        ("La gestion du stress est essentielle pour le bien-être des employés", True),
        ("Les réunions fréquentes sont toujours bénéfiques pour la productivité", False),
        ("La rotation des postes peut prévenir la monotonie au travail", True),
        ("Le leadership participatif implique les employés dans la prise de décision", True),
        ("Les managers doivent éviter tout feedback négatif", False),
        ("La communication claire réduit les malentendus au travail", True),
        ("Les employés doivent être encouragés à proposer des idées", True),
        ("Les pauses régulières augmentent la productivité", True),
        ("Le télétravail ne présente que des avantages", False),
        ("La gestion des talents est cruciale pour la réussite de l'entreprise", True),
        ("Les employés ayant un bon équilibre travail-vie sont plus performants", True),
        ("Les objectifs SMART sont spécifiques, mesurables, atteignables, réalistes et temporels", True),
        ("Le mentorat peut accélérer le développement des compétences", True),
        ("Le développement personnel n'a pas sa place en entreprise", False),
        ("La culture d'entreprise influence la satisfaction des employés", True),
        ("Les entretiens de performance doivent être annuels", False),
        ("L'intelligence émotionnelle est importante pour un manager", True),
        ("La délégation des tâches améliore l'efficacité des équipes", True),
        ("Les programmes de bien-être augmentent la rétention des employés", True),
        ("La gestion de projet Agile favorise la flexibilité", True),
        ("Les évaluations 360 degrés donnent une vue complète de la performance", True),
        ("Les feedbacks doivent toujours être positifs", False),
        ("Le turnover élevé des employés indique une bonne gestion", False),
        ("Les équipes diversifiées résolvent mieux les problèmes complexes", True),
        ("Les managers doivent être accessibles et à l'écoute", True),
        ("La formation continue est inutile pour les employés expérimentés", False),
        ("Le réseautage est crucial pour les opportunités de carrière", True),
        ("Les employés doivent être encouragés à prendre des initiatives", True),
        ("La microgestion réduit l'autonomie des employés", True),
        ("Les objectifs doivent être alignés avec la vision de l'entreprise", True),
        ("Le stress au travail peut entraîner des absences fréquentes", True),
        ("Les programmes de reconnaissance augmentent l'engagement des employés", True),
        ("La gestion du changement est essentielle pour l'adaptation de l'entreprise", True),
        ("Le développement des compétences soft est aussi important que les compétences techniques", True),
        ("La satisfaction des clients est directement liée à la satisfaction des employés", True),
        ("Les leaders doivent inspirer et motiver leurs équipes", True),
        ("La flexibilité au travail est une tendance en croissance", True),
        ("Les employés doivent toujours suivre les processus établis", False),
        ("La diversité des points de vue améliore la prise de décision", True),
        ("La communication descendante est la plus efficace", False),
        ("Le télétravail nécessite des compétences de gestion spécifiques", True),
        ("Les employés doivent être responsabilisés dans leurs rôles", True),
        ("La planification stratégique est essentielle pour la croissance", True),
        ("Les conflits au travail doivent être résolus rapidement", True),
        ("La culture du feedback améliore la performance continue", True),
        ("Les employés doivent être encouragés à se perfectionner", True),
        ("Les décisions doivent toujours être prises en groupe", False),
        ("La formation en leadership doit être continue", True),
        ("Les programmes de mentorat sont bénéfiques pour tous les employés", True),
        ("Le bien-être au travail est une responsabilité partagée", True),
        ("Les managers doivent modéliser les comportements souhaités", True),
        ("Les employés satisfaits sont plus fidèles à l'entreprise", True),
        ("La gestion du temps est cruciale pour la productivité", True),
        ("La transparence financière augmente la confiance des employés", True),
        ("Les objectifs individuels doivent être alignés avec ceux de l'équipe", True),
        ("Le télétravail peut augmenter la productivité", True),
        ("La gestion des performances doit être proactive", True),
        ("Les employés doivent comprendre la vision de l'entreprise", True),
        ("Les horaires de travail flexibles sont toujours bénéfiques", False),
        ("Les récompenses doivent être équitables et basées sur la performance", True),
        ("Les outils de collaboration en ligne améliorent la communication", True),
        ("Le feedback constructif favorise le développement des employés", True),
        ("Les compétences techniques sont plus importantes que les compétences interpersonnelles", False),
        ("Les employés doivent avoir des objectifs clairs", True),
        ("La satisfaction au travail est liée à l'autonomie des employés", True),
        ("Les programmes de bien-être réduisent le stress au travail", True),
        ("Les managers doivent encourager la prise de risques calculés", True),
        ("Les équipes virtuelles nécessitent des stratégies de gestion spécifiques", True),
        ("Les employés doivent être impliqués dans les décisions qui les concernent", True)
    ],
    "TECHNO": [
        ("L'intelligence artificielle peut remplacer tous les emplois humains", False),
        ("Le cloud computing permet de stocker des données sur des serveurs distants", True),
        ("HTML est un langage de programmation", False),
        ("Les mises à jour logicielles peuvent améliorer la sécurité d'un système", True),
        ("La blockchain est une technologie utilisée principalement pour les cryptomonnaies", True),
        ("Les algorithmes de machine learning nécessitent de grandes quantités de données", True),
        ("Le Big Data se réfère à des ensembles de données extrêmement volumineux", True),
        ("JavaScript est utilisé principalement pour le développement web", True),
        ("Les réseaux 5G sont plus rapides que les réseaux 4G", True),
        ("L'open source signifie que le code source est disponible publiquement", True),
        ("La réalité augmentée superpose des informations numériques au monde réel", True),
        ("Un VPN (Virtual Private Network) améliore la confidentialité en ligne", True),
        ("Les drones ne sont utilisés que pour les loisirs", False),
        ("L'impression 3D permet de créer des objets physiques à partir de modèles numériques", True),
        ("Les smartphones modernes ont souvent des processeurs multicœurs", True),
        ("Les cryptomonnaies sont stockées dans des portefeuilles numériques", True),
        ("La cybersécurité concerne la protection des systèmes informatiques", True),
        ("Les bases de données relationnelles utilisent le langage SQL", True),
        ("L'IoT (Internet of Things) connecte des appareils physiques à Internet", True),
        ("Les logiciels antivirus sont inutiles sur les ordinateurs modernes", False),
        ("Python est un langage de programmation interprété", True),
        ("Les tests unitaires sont essentiels pour assurer la qualité du code", True),
        ("Git est un système de contrôle de version distribué", True),
        ("Le refactoring de code consiste à modifier le code sans changer son comportement externe", True),
        ("Les microservices sont des services autonomes qui communiquent entre eux", True),
        ("REST est un style d'architecture pour les services web", True),
        ("Les conteneurs Docker permettent l'isolation des applications", True),
        ("Java et JavaScript sont le même langage", False),
        ("Une API (Application Programming Interface) permet à différentes applications de communiquer entre elles", True),
        ("Le développement agile favorise des itérations courtes et flexibles", True),
        ("Les frameworks comme Django et Flask sont utilisés avec Python", True),
        ("Les data lakes sont utilisés pour stocker de grandes quantités de données brutes", True),
        ("Le DevOps vise à améliorer la collaboration entre les équipes de développement et d'exploitation", True),
        ("Le CSS (Cascading Style Sheets) est utilisé pour le style des pages web", True),
        ("Les bases de données NoSQL sont adaptées pour les données non structurées", True),
        ("Les algorithmes de tri comme QuickSort et MergeSort sont fondamentaux", True),
        ("L'authentification à deux facteurs améliore la sécurité des comptes en ligne", True),
        ("Les réseaux de neurones artificiels sont utilisés dans le machine learning", True),
        ("Le front-end et le back-end sont des termes utilisés pour décrire les différentes parties d'une application web", True),
        ("Un IDE (Integrated Development Environment) est un logiciel qui aide à la programmation", True),
        ("L'optimisation des performances est cruciale dans le développement logiciel", True),
        ("Les hooks de React sont des fonctions qui permettent d'utiliser l'état et d'autres fonctionnalités de React dans les composants fonctionnels", True),
        ("L'injection de dépendances est un concept clé dans de nombreux frameworks", True),
        ("Les tests d'intégration vérifient que différents modules fonctionnent bien ensemble", True),
        ("Le caching permet de réduire le temps de réponse des applications", True),
        ("Les PWA (Progressive Web Apps) offrent une expérience utilisateur similaire aux applications natives", True),
        ("L'ORM (Object-Relational Mapping) permet de manipuler une base de données en utilisant des objets", True),
        ("Les API RESTful utilisent les verbes HTTP comme GET, POST, PUT, DELETE", True),
        ("Les tests de charge mesurent les performances d'un système sous forte demande", True),
        ("Les expressions régulières sont utilisées pour la recherche de motifs dans les chaînes de caractères", True),
        ("La virtualisation permet d'exécuter plusieurs systèmes d'exploitation sur une seule machine physique", True),
        ("Le machine learning est une branche de l'intelligence artificielle", True),
        ("Les services sans serveur (serverless) permettent d'exécuter du code sans gérer de serveurs", True),
        ("Les pipelines CI/CD automatisent les processus de développement et de déploiement", True),
        ("Les algorithmes de compression réduisent la taille des données pour économiser de l'espace", True),
        ("Le paradigme fonctionnel est un style de programmation où les fonctions sont des citoyens de première classe", True),
        ("Les événements asynchrones permettent de gérer les opérations d'E/S sans bloquer le flux du programme", True),
        ("L'automatisation des tests améliore la qualité et la vitesse de développement", True),
        ("Les conteneurs permettent de déployer des applications de manière portable et cohérente", True),
        ("Le cloud computing offre des ressources informatiques à la demande", True),
        ("Les services de cloud comme AWS, Azure et Google Cloud sont populaires", True),
        ("Les applications web progressives (PWA) fonctionnent hors ligne et offrent des notifications push", True),
        ("Les frameworks CSS comme Bootstrap facilitent la création de sites web réactifs", True),
        ("Les webhooks permettent de recevoir des notifications en temps réel d'autres applications", True),
        ("Les tests de pénétration (pentests) sont utilisés pour évaluer la sécurité des systèmes", True),
        ("Les bases de données graphes sont utilisées pour représenter des relations complexes", True),
        ("L'indexation améliore les performances des requêtes de bases de données", True),
        ("Les principes SOLID sont des bonnes pratiques pour la conception orientée objet", True),
        ("Le développement piloté par les tests (TDD) commence par écrire les tests avant le code", True),
        ("Les architectures hexagonales permettent une meilleure séparation des préoccupations", True),
        ("Les CDN (Content Delivery Networks) améliorent les performances de distribution de contenu", True),
        ("Les microfrontends permettent de développer des parties indépendantes d'une application front-end", True),
        ("Les paradigmes de programmation incluent procédural, orienté objet et fonctionnel", True),
        ("Les algorithmes de chiffrement sécurisent les données sensibles", True),
        ("Le versionnage sémantique utilise des numéros de version pour indiquer les changements", True),
        ("Le pair programming consiste à deux développeurs travaillant ensemble sur le même code", True),
        ("Les applications serverless peuvent évoluer automatiquement selon la demande", True),
        ("Les pipelines de données traitent les données en plusieurs étapes séquentielles", True),
        ("Les moteurs de recherche utilisent des algorithmes complexes pour classer les pages web", True),
        ("Les plateformes de conteneurs comme Kubernetes facilitent la gestion des déploiements à grande échelle", True),
        ("Le paradigme MVC (Model-View-Controller) est une architecture couramment utilisée pour les applications web", True),
        ("Le codage de paires permet de détecter les erreurs plus rapidement", True),
        ("Les systèmes de gestion de bases de données relationnelles (SGBDR) utilisent le SQL", True),
        ("Les algorithmes de tri sont importants pour l'efficacité des recherches", True),
        ("Les API GraphQL permettent de récupérer précisément les données nécessaires", True),
        ("Les microservices permettent une architecture modulaire et évolutive", True),
        ("Le pattern observer permet de notifier les changements d'état à plusieurs observateurs", True),
        ("Les environnements de développement intégrés (IDE) comme VSCode augmentent la productivité des développeurs", True)
    ],
    "PHYSIC": [
        ("Pour soulever une charge lourde, il est préférable de plier les genoux que de courber le dos", True),
        ("L'hydratation est essentielle pour le bon fonctionnement du corps", True),
        ("Une alimentation équilibrée n'a pas d'impact sur la santé", False),
        ("Faire de l'exercice régulièrement peut réduire le risque de maladies cardiaques", True),
        ("Le sommeil n'affecte pas la performance physique", False),
        ("L'étirement avant l'exercice aide à prévenir les blessures", True),
        ("Les protéines sont nécessaires à la construction musculaire", True),
        ("La vitamine D est principalement obtenue par l'exposition au soleil", True),
        ("Le tabagisme n'a aucun effet sur les capacités physiques", False),
        ("Le stress chronique peut affecter la santé physique", True),
        ("Les glucides sont une source importante d'énergie pour le corps", True),
        ("Le surentraînement peut entraîner des blessures et de la fatigue", True),
        ("L'IMC (Indice de Masse Corporelle) est une mesure précise de la santé", False),
        ("Le yoga peut améliorer la flexibilité et la force", True),
        ("Boire de l'alcool en excès peut endommager le foie", True),
        ("Les graisses saturées sont meilleures pour la santé que les graisses insaturées", False),
        ("Les abdominaux seuls ne suffisent pas pour perdre de la graisse abdominale", True),
        ("La déshydratation peut entraîner des crampes musculaires", True),
        ("Les fibres alimentaires aident à la digestion", True),
        ("Une mauvaise posture peut causer des douleurs dorsales", True),
        ("Les muscles ont besoin de repos pour se reconstruire après l'exercice", True),
        ("Le cardio-training améliore l'endurance cardiovasculaire", True),
        ("Les vitamines et les minéraux sont essentiels à une bonne santé", True),
        ("L'exercice régulier peut améliorer l'humeur et réduire le stress", True),
        ("Les boissons énergétiques sont une source saine d'hydratation", False),
        ("L'exercice physique aide à maintenir un poids santé", True),
        ("Les graisses trans sont bonnes pour la santé", False),
        ("La consommation excessive de sucre peut conduire à l'obésité", True),
        ("L'exercice physique régulier peut améliorer la qualité du sommeil", True),
        ("Le stretching post-exercice aide à réduire les courbatures", True),
        ("Les protéines végétales peuvent être aussi bénéfiques que les protéines animales", True),
        ("Le saut à la corde est un exercice cardiovasculaire efficace", True),
        ("Le calcium est important pour la santé des os", True),
        ("L'exercice à haute intensité brûle plus de calories en moins de temps", True),
        ("La pratique du sport améliore la coordination et l'équilibre", True),
        ("Les exercices de résistance renforcent les muscles et les os", True),
        ("La consommation de fruits et légumes est bénéfique pour la santé", True),
        ("Le surpoids peut augmenter le risque de maladies chroniques", True),
        ("La natation est un exercice complet pour le corps", True),
        ("L'exercice physique peut réduire les risques de dépression", True),
        ("Les boissons sucrées sont une bonne source d'énergie rapide", False),
        ("Le surentraînement peut mener à l'épuisement et aux blessures", True),
        ("La marche rapide est bénéfique pour la santé cardiovasculaire", True),
        ("Les oméga-3 sont importants pour la santé du cœur", True),
        ("L'exercice physique peut renforcer le système immunitaire", True),
        ("Les entraînements de HIIT (High-Intensity Interval Training) sont efficaces pour brûler des calories", True),
        ("Les régimes yo-yo peuvent nuire à la santé", True),
        ("L'activité physique aide à réguler le métabolisme", True),
        ("Le vélo est une activité physique à faible impact", True),
        ("Les exercices de relaxation peuvent réduire le stress et l'anxiété", True),
        ("Les aliments riches en fibres peuvent aider à contrôler le poids", True),
        ("Le yoga améliore la flexibilité et la gestion du stress", True),
        ("Une hydratation adéquate est essentielle pour la performance physique", True),
        ("La musculation aide à prévenir la perte de masse musculaire avec l'âge", True),
        ("Les séances d'exercice courtes mais fréquentes sont bénéfiques", True),
        ("Le sommeil réparateur est crucial pour la récupération physique", True),
        ("La course à pied améliore l'endurance et la santé cardiovasculaire", True),
        ("Le stretching avant le sport diminue le risque de blessure", True),
        ("Les noix et les graines sont de bonnes sources de graisses saines", True),
        ("La danse est une activité physique qui améliore la condition physique générale", True),
        ("La pratique régulière d'exercices de relaxation peut améliorer la santé mentale", True),
        ("Les abdominaux seuls ne permettent pas de réduire la graisse abdominale", True),
        ("Une alimentation équilibrée et variée est cruciale pour la santé physique", True),
        ("La consommation d'alcool en excès peut nuire à la performance physique", True),
        ("L'exercice physique améliore la circulation sanguine", True),
        ("L'hydratation avant, pendant et après l'exercice est essentielle", True),
        ("La respiration profonde peut aider à réduire le stress et améliorer la santé", True),
        ("Les exercices de musculation augmentent la force et la masse musculaire", True),
        ("Les sports d'équipe peuvent améliorer les compétences sociales", True),
        ("Les aliments riches en protéines sont importants pour la réparation musculaire", True),
        ("L'exercice physique aide à réduire les niveaux de cholestérol", True),
        ("Le fitness améliore l'équilibre et la coordination", True),
        ("Les entraînements cardio augmentent la fréquence cardiaque et brûlent des calories", True),
        ("Les pauses régulières pendant l'exercice sont nécessaires pour éviter les blessures", True),
        ("Les régimes déséquilibrés peuvent mener à des carences nutritionnelles", True),
        ("L'exercice physique améliore la souplesse et la mobilité", True),
        ("Les exercices de renforcement musculaire aident à maintenir la densité osseuse", True),
        ("La pratique régulière de la méditation peut améliorer le bien-être général", True),
        ("Les exercices cardiovasculaires sont essentiels pour une bonne santé cardiaque", True),
        ("Une alimentation riche en fruits et légumes réduit le risque de maladies chroniques", True),
        ("La pratique régulière d'un sport améliore la condition physique", True),
        ("Les techniques de relaxation peuvent aider à gérer le stress quotidien", True),
        ("La natation est un excellent exercice pour les personnes souffrant de douleurs articulaires", True),
        ("L'entraînement par intervalles peut améliorer la capacité aérobie", True),
        ("Les exercices de respiration peuvent réduire le stress et améliorer la concentration", True),
        ("Les protéines sont essentielles pour la réparation et la croissance des tissus", True),
        ("L'exercice physique aide à réguler les hormones", True),
        ("Le tai-chi améliore l'équilibre et réduit le stress", True)
    ]
}



class Tree:
    def __init__(self,player,size=(1920,1080)):
        self.social = player.social_points
        self.techno = player.technologic_points
        self.physic = player.physical_points

        self.player = player
        self.player_remain_pos = (size[0]//3,size[1]//6)

        self.ask = False
        self.question = ""
        self.question_index = 0
        self.question_pos = (size[0]//5,size[1]//2)
        self.question_thema = ""

        self.buttons_ask_pos = [(0,0),
                                (size[0]//4,size[1]//5*4),
                                (size[0]//4*3,size[1]//5*4)]
        
        self.buttons_ask_texts = ["back",
                                  "Vrai",
                                  "Faux"]


        self.button_pos = [(0,0),
                           (size[0]//3,size[1]//5*2),
                           (size[0]//3,size[1]//5*3),
                           (size[0]//3,size[1]//5*4),
                           (size[0]//2,size[1]//5*2),
                           (size[0]//2,size[1]//5*3),
                           (size[0]//2,size[1]//5*4),
                           (size[0]//4*3,size[1]//5*2),
                           (size[0]//4*3,size[1]//5*3),
                           (size[0]//4*3,size[1]//5*4),]
        


        self.button_texts = ["back",
                             "-",
                             "-",
                             "-",
                             "Social : "+str(self.social),
                             "Tech : "+str(self.techno),
                             "Physic : "+str(self.physic),
                             "+",
                             "+",
                             "+"]

    def draw(self,display):
        if self.ask:
            smallfont = pygame.font.SysFont('Corbel',35) 
            mouse = pygame.mouse.get_pos()

            text = smallfont.render(self.question, True , (255,255,255)) 
            display.blit(text,(self.question_pos))


            for x,pos in enumerate(self.buttons_ask_pos) :
                if pos[0] <= mouse[0] <= pos[0]+50 and pos[1] <= mouse[1] <= pos[1]+50: 
                    pygame.draw.rect(display,(150,150,150),[pos[0],pos[1],50,50])
                text = smallfont.render(self.buttons_ask_texts[x], True , (255,255,255)) 
                display.blit(text,(pos[0],pos[1]))

        else:
            smallfont = pygame.font.SysFont('Corbel',35) 
            mouse = pygame.mouse.get_pos()

            text = smallfont.render("Points restants : " +str(self.player.remain_points), True , (255,255,255)) 
            display.blit(text,(self.player_remain_pos))
                    
            for x,pos in enumerate(self.button_pos) :
                if self.button_texts[x] == "+" or self.button_texts[x] == "-" or self.button_texts[x] == "back":
                    if pos[0]-55 <= mouse[0] <= pos[0]+73 and pos[1] <= mouse[1] <= pos[1]+35: 
                        pygame.draw.rect(display,(150,150,150),[pos[0]-55,pos[1],128,35])
                text = smallfont.render(self.button_texts[x], True , (255,255,255)) 
                display.blit(text,(pos[0],pos[1]))
                

    def check_click(self,x,y):
        if self.ask:
            for index,pos in enumerate(self.buttons_ask_pos):
                if pos[0] <= x <= pos[0] + 50 and  pos[1] <= y <= pos[1]+50:
                    
                    if self.question_thema == "SOCIAL":
                        if self.buttons_ask_texts[index] == "Vrai" and QUESTIONS["SOCIAL"][self.question_index][1]:
                            self.player.add_point(Type.MANAGE,5)
                        elif self.buttons_ask_texts[index] == "Faux" and not QUESTIONS["SOCIAL"][self.question_index][1]:
                            self.player.add_point(Type.MANAGE,5)
                        elif self.buttons_ask_texts[index] == "back":
                            pass
                        else : 
                            self.player.remain_points = self.player.remain_points -5
                    elif self.question_thema == "TECHNO":
                        if self.buttons_ask_texts[index] == "Vrai" and QUESTIONS["TECHNO"][self.question_index][1]:
                            self.player.add_point(Type.TECHNO,5)
                        elif self.buttons_ask_texts[index] == "Faux" and not QUESTIONS["TECHNO"][self.question_index][1]:
                            self.player.add_point(Type.TECHNO,5)
                        elif self.buttons_ask_texts[index] == "back":
                            pass
                        else : 
                            self.player.remain_points = self.player.remain_points -5
                    elif self.question_thema == "PHYSIC":
                        if self.buttons_ask_texts[index] == "Vrai" and QUESTIONS["PHYSIC"][self.question_index][1]:
                            self.player.add_point(Type.PHYSIQUE,5)
                        elif self.buttons_ask_texts[index] == "Faux" and not QUESTIONS["PHYSIC"][self.question_index][1]:
                            self.player.add_point(Type.PHYSIQUE,5)
                        elif self.buttons_ask_texts[index] == "back":
                            pass
                        else : 
                            self.player.remain_points = self.player.remain_points -5
                    

                    self.update_player()
                    self.ask = False
                    break
        else:
            
            for index,pos in enumerate(self.button_pos):
                
                if pos[0] <= x <= pos[0] + 50 and  pos[1] <= y <= pos[1] +50:
                    
                    if self.button_texts[index] == "-":
                        if (index %3 == 1 and self.social == 0) or (index %3 == 2 and self.techno == 0) or (index %3 == 0 and self.physic == 0):
                            continue   
                        else :
                            self.player.delete_point( (Type.MANAGE if index %3 == 1 
                                                    else Type.TECHNO if index %3 == 2 
                                                    else Type.PHYSIQUE) ,1)
                            

                    elif self.button_texts[index] == "+":
                        if self.player.remain_points >= 5 :
                            self.ask = True
                            if index % 3 == 1:
                                self.question_thema = "SOCIAL"
                                ques = QUESTIONS["SOCIAL"]
                                self.question_index = random.randint(0,len(ques)-1)

                                self.question = QUESTIONS["SOCIAL"][self.question_index][0]
                            elif index % 3 == 2:
                                self.question_thema = "TECHNO"
                                ques = QUESTIONS["TECHNO"]
                                self.question_index = random.randint(0,len(ques)-1)

                                self.question = QUESTIONS["TECHNO"][self.question_index][0]
                            else:
                                self.question_thema = "PHYSIC"
                                ques = QUESTIONS["PHYSIC"]
                                self.question_index = random.randint(0,len(ques)-1)

                                self.question = QUESTIONS["PHYSIC"][self.question_index][0]


    def update_player(self):
        self.social = self.player.social_points
        self.techno = self.player.technologic_points
        self.physic = self.player.physical_points

        self.button_texts[4] = "Social : "+str(self.social)
        self.button_texts[5] = "Tech : "+str(self.techno)
        self.button_texts[6] = "Physic : "+str(self.physic)