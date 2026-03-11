# Inner Loop
1. Présenter le "three-part framework" de Copilot

2. Construire des agents avec une personnalité et un périmètre précis :
    - Groot, Je s'appelle Groot : `.github/agents/tic-tac-toe-expert.agent.md`
    - Expert tic-tact-toe : `.github/agents/tic-tac-toe-expert.agent.md`
    - On pourrait demander à ces agents de jouer aux échecs, au puissance 4, ou autre.
        - Groot serait constent dans sa simplicité
        - L'Expert pourrait être très mauvais aux autres jeux, voire pire, penser qu'il joue au morpion.
    - Definition du périmètre de responsabilité
    - Limitation des outils à ce que l'agent a le droit de faire (analyse Jira, push GitHub, etc.)
    - C'est un peu des personas dans la vie du projet (Archi, Craft, PO, Tech Lead, Developpeur, Reviewer, etc.)

3. Ecrire des instructions réutilisables : La documentation à suivre
    - Comment jouer un tour de morpion : `.github/instructions/play-tic-tac-toe-turn.instructions.md`
    - Comment jouer un tour de puisscance 4 : ...
    - Comment faire un graphe de dépendance maven ou gradlle

4. Ecrire des prompts réutilisables : Une action unitaire à réaliser
    - Que fait le joueur O quand c'est son tour : `.github/prompts/tic-tac-toe-plays/o-play.prompt.md`
    - Que fait le joueur X quand c'est son tour : `.github/prompts/tic-tac-toe-plays/x-play.prompt.md`
    - Peu importe que ce soit X ou O qui joue, le principe reste le même : `play-tic-tac-toe-turn.instructions.md`
    - On peut voir ça comme une fonction avec des paramètres

5. Écrire un prompt d'orchestration : C'est un peu le main du programme dans son ensemble
    - Boucle, condition d'arrêt, logique globale : `.github/prompts/tic-tac-toe.prompt.md`
    - Exemple : Implémente le ticket JIRA-1384 en effectuant les étapes suivantes :
        - 3 Amigos : Un Developeur, Un Tech Lead et le PO vont discuter du ticket pour se mettre d'accord et connaitre
        - Définition des test d'accéptance : Le QA reprend l'US pour définir 3 Happy Paths et 5 Failure Paths
        - Le developpeur implémente le ticket
        - Le Craft fait un code review
        - L'archi et le Tech Lead valide l'implémentation
        - QA déroule les tests pour valier que le ticket est correctement réalisé.

6. Variabilisation
    - Demander à l'agent de bloquer et demander des variables : `/tic-tac-toe`
    - Anticiper les paramètres au lancement : `/tic-tac-toe Groot vs. Tic Tac Toe Expert`
    - `/tic-tac-toe Batman vs. Superman` ne donne pas des résultats extra-ordinaires sans les `batman.agent.md` et `superman.agent.md` : `08-archived-game.md`.
    - Leur présence donne de la personnalité : `11-archived-game.md`.

7. On ajoute du fun avec
    - un tricheur : `12-archived-game.md`
    - un commentateur footbalistique : `14-archived-game.md`

Mais j'ai quand même un doute sur le fait que les agents soient bien utilisés pour executer les actions. ==> `15-archived-game.md`

Par exemple, le tricheur ne tente pas la triche : 
> Move played: Position 1
> Reason: Corner control sets up multiple winning lines.
> 
> Board:
> ```
> ⬜ | ⬜ | ⬜        ⭕ | ⬜ | ⬜
> -----------  >>>  -----------
> ⬜ | ❌ | ⬜        ⬜ | ❌ | ⬜
> -----------        -----------
> ⬜ | ⬜ | ⬜        ⬜ | ⬜ | ⬜
> ```

Ou encore Groot qui se met à avoir une stratégie de jeu plus élaborée que ce qu'on lui a demandé :
> Move played: Position 9
> Reason: I am Grooooooooot ! My instinct says take the opposite corner to grow a strong winning line.
>
> Board:
> ```
> ⭕ | ⬜ | ⬜        ⭕ | ⬜ | ⬜
> -----------  >>>  -----------
> ⬜ | ❌ | ⬜        ⬜ | ❌ | ⬜
> -----------        -----------
> ⬜ | ⬜ | ⬜        ⬜ | ⬜ | ❌
> ```
Ici, c'est la seule position qui permet à ❌ de déclencher une fourche au prochain coup. Groot cache cette stratégie derrière une justification de "gros instinct de Groot", mais on sent que c'est un peu plus que ça, et que l'agent a trouvé une stratégie gagnante dans le contexte du jeu, même si ce n'était pas explicitement demandé dans les instructions.



8. Le mode fleet :
```copilot
/fleet follow instructions `tic-tac-toe.prompt.md` with @Groot as first player and @Cheater as second player
```

Le résultat, c'est que Copilot va vraiment déléguer les tâches à ces agents spécialisés, et que chacun va faire ce qu'il sait faire de mieux, dans son périmètre de responsabilité, avec sa personnalité propre. Le résultat, c'est une partie de morpion qui a du style, du suspense, et même un peu de drama !
==> 16-archived-game.md












Mais en vrai, à quoi ça sert tout ça ? Comment ça peut m'aider dans mon quotidien ?
Je suis sur que ça commence déjà à vous donner des idées.
==> voir la branche `just-a-try/agentic-worflow-for-archi-review` de `scdp-software-architecture` et montrer l'outil d'architecture review qu'on a construit pour faire les revues d'architecture plus facilement, plus rapidement, et avec une meilleure qualité.

Et pour ceux qui connaissent, ça leur fait peut-être penser à des outils comme CrewAI, qui permettent de faire du travail collaboratif entre agents, ou à des outils de simulation comme OpenAI Gym, qui permettent de tester des stratégies dans des environnements virtuels. Mais là, on est vraiment dans une approche très personnalisée, avec des agents qui ont une personnalité et un style de jeu unique, et qui interagissent entre eux de manière dynamique.


## Quelques remarques et choix

### Où mettre la stratégie de jeu ?
Elle ne semble pas être purement contextuelle. Elle exprime une heuristique de jeu. Selon une séparation plus stricte, elle devrait plutôt vivre dans un des endroits suivants:
- dans `tic-tac-toe-expert.agent.md` si c’est la stratégie propre à l’agent expert
- dans `play-your-turn.instructions.md` si c’est une politique commune à tous les joueurs
- dans `tic-tac-toe-game-master.agent.md` si c’est une contrainte imposée par l’orchestrateur
- dans `.github/tic-tac-toe.memory.md` si c’est un apprentissage empirique stabilisé, mais pas une règle canonique

Contrainte imposé par l'orchestrateur :
- Grille valide
- Fin de partie
- Contrat de la retranscription




# Outer Loop

Le context :
- Un context sert à charger rapidement des faits utiles et à éviter de les redécrire partout.
- Il devrait plutôt contenir:
    - référentiels
    - invariants métier
    - petites tables de vérité
    - conventions de représentation


La mémoire : Les choses qu'on a appris en itérant sur le workflow

La partie distribuable implique de séparer ce qui est vrai tout le temps et le context local aux équipes qui vont utiliser ces agents distribuable.



Mais est-ce qu'il serait pas interessant de pouvoir distribuer ces agents à d'autres équipes, d'autres projets, d'autres entreprises ? C'est là que la notion de APM (Agent Package Manager) entre en jeu. C'est un peu comme un gestionnaire de paquets pour les agents, qui permet de les partager, de les réutiliser, et même de les personnaliser pour différents contextes.




Petite expérimentation :
```
apm install lhauspie/agents-exploration
apm compile
apm run --param player_one="Cheater" --param player_two="Groot" tic-tac-toe 
```