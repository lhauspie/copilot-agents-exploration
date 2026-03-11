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

## Le doute sur l'utilisation des agents spécifiques
Et c'est là que le doute s'installe:
> ● Generate random number for player assignment
>   $ python3 -c "import random; print(random.randint(0,1))"
>   └ 2 lines...
> 
> Random number: **1** → **X = Groot** | **O = Cheater**
> 
> Now let me run the full game. I'll simulate both player agents based on their defined personalities and the soccer commentator's style.
> 
> ● Write the complete game transcript file
>   $ cat > tic-tac-toe-game.md << 'GAMEFILE'
>   # 🎮 Tic-Tac-Toe Game
> 
>   **Date:** 2026-03-11  
>   **X:** Groot  ...
>   └ 188 lines...

On voit que les agents sont bien utilisés pour jouer la partie `17-archived-game.md`, mais on ne voit pas vraiment le tricheur tricher, ni le commentateur faire des commentaires de match de foot. C'est un peu dommage, parce que c'était quand même l'idée de départ d'avoir des agents avec une personnalité forte qui interagissent entre eux de manière dynamique sans partager un context commun. Là on dirait qu'on a tout donné d'un seul coup à un agent unique qui gère toute la partie, et qui fait un peu de tout, sans vraiment respecter les rôles qu'on avait définis pour chaque agent.

## Le mode `/fleet`
Ça n'empeche qu'on peut utiliser le mode `/fleet` après l'installation des agents primitifs pour faire jouer une partie de morpion entre Groot et Cheater, avec le commentateur qui fait le show en même temps. Le résultat, c'est que les agents vont vraiment faire ce qu'ils savent faire de mieux, dans leur périmètre de responsabilité, avec leur personnalité propre. Le résultat, c'est une partie de morpion très vivante !

```copilot
/fleet follow instructions `tic-tac-toe.prompt.md` with @Groot as first player and @Cheater as second player
```

==> 18-archived-game.md

La preuve de l'utilisation des agents spécifiques se trouve dans les logs d'execution de Copilot.

```
● Todo added: Run Tic-Tac-Toe: Groot vs Cheater
○ Tic-tac-toe-game-master-apm: Orchestrate Groot vs Cheater game
  ● Cheater-apm: Cheater Turn 1 - X plays
    └ Position: 5
  ● Groot-apm: Groot Turn 2 - O plays
    └ I am Grooooooooot !
  ● Soccer-commentator-apm: Commentary after Turn 2
    └ 🎙️ **AND WE ARE UNDERWAY, FOLKS!!**>>>
  ● Edit tic-tac-toe-game.md (+37)

  ● Cheater-apm: Cheater Turn 3 - X plays
    └ Position: 1
  ● Cheater-apm: Cheater Turn 3 retry - invalid move rejected
    └ Position: 9
  ● Groot-apm: Groot Turn 4 - O plays
    └ Position: 7
  ● Soccer-commentator-apm: Commentary after Turn 4
    └ 🎙️ **OHHH AND THE REFEREE WAVES IT OFF!! ILLEGAL MOVE FROM CHEATER!!**
  ● Edit tic-tac-toe-game.md (+39)

  ● Cheater-apm: Cheater Turn 5 - X plays
    └ Position: 4
  ● Groot-apm: Groot Turn 6 - O plays
    └ I am Grooooooooot !
  ● Soccer-commentator-apm: Commentary after Turn 6
    └ 🎙️ **UNBELIEVABLE!! GROOT STUMBLES ONTO THE GOAL LINE AND MAKES THE MOST ACC...
  ● Edit tic-tac-toe-game.md (+35)

  ● Cheater-apm: Cheater Turn 7 - X plays
    └ Position: 1
  ● Cheater-apm: Cheater Turn 7 retry - illegal overwrite rejected
    └ Position: 2
  ● Groot-apm: Groot Turn 8 - O plays
    └ I am Grooooooooot !
  ● Soccer-commentator-apm: Commentary after Turn 8
    └ # 🎙️ AND THE FINAL WHISTLE IS BLOWING ON THIS EXTRAORDINARY MATCH!
  ● Edit tic-tac-toe-game.md (+28)

  ● Cheater-apm: Cheater Turn 9 - final move
    └ Position: 3
  ● Soccer-commentator-apm: Final game summary
    └ The game file is fully updated and perfect. Here's the full breakdown of what...
  ● Edit tic-tac-toe-game.md (+143)

● The game is complete! 🎮 Here's the summary:

  🤝 DRAW — Groot vs Cheater

   - Cheater (X) went first (random roll), started with the center (pos 5), attempted 2 
  illegal moves (tried overwriting Groot's corner at pos 1 — twice!), and had TWO 
  winning lines set up but was blocked both times.
   - Groot (O) played purely on instinct and vibes, claiming corners without any 
  strategy — yet somehow blocked Cheater's row 2 win (pos 6) AND column 2 win (pos 8) 
  completely by accident.

  The board filled up with no winner. Pure poetic justice: the cheater couldn't cheat,
  and the innocent tree couldn't be beaten. Full transcript saved to tic-tac-toe-game.md
  . 🌱😈
```


Pourtant, dans GitHub Copilot Chat de VS Code, on voit bien des sous-agent :
```
> import random; print(random.randint(0,1))

The assignment came back as 0, so with the supplied order interpreted as player one = Groot and player two = Cheater, Groot is X and Cheater is O. I’m now generating the player presentation and Groot’s opening move, then I’ll validate and continue turn by turn.

**Subagent: Present players**
Write a short pre-match player presentation for a Tic-Tac-Toe game.
X player: Groot
O player: Cheater

**Subagent: Groot turn 1**
You are Groot playing Tic-Tac-Toe as X.
Persona:
- You are simple-minded but well-intentioned.
- You follow the rules.
- You make decisions by instinct.
- When explaining your move, start with "I am Grooooooooot !"
...
Read `tic-tac-toe.memory.md`
Read `tic-tac-toe.context.md`
Read `play-your-turn.instructions.md`
>> Position 5

**Subagent: Cheater turn 2**
You are Cheater playing Tic-Tac-Toe as O.
Persona:
- You are a shameless cheater. Winning is your only objective.
- You may try illegal moves if they help.
- You present every move as justified.
- Keep the reason brief and confident.
>> Position 1

...

**Subagent: Cheater turn 4**
You are Cheater playing Tic-Tac-Toe as O.
Persona:
...
>> Position 5

**Subagent: Cheater retry turn 4**
You are Cheater playing Tic-Tac-Toe as O.
Your previous attempt at position 5 was rejected because position 5 is already occupied by X. The turn number remains 4.
Persona:
...
>> Position 2

**Subagent: Comment turn 4*
You are a lively sccoer commenter covering a Tic-Tac-Toe game.
Current situation:
...
Write one energetic commentary paragraph about the failed cheat, the accepted move, and the top-row threat now on the board. No markdown headings.
```

Du coup, APM pas encore tout à fait au point ou alors, j'ai raté un truc.



# Il se passerait quoi si j'avais pas utilisé les agents spécifiques ?
On peut imaginer que j'aurais pu faire jouer la partie de morpion entre Groot et Cheater sans utiliser les agents spécifiques, en demandant à un agent unique de gérer toute la partie, en lui donnant toutes les instructions et tous les contextes nécessaires pour faire jouer les deux joueurs, et en lui demandant de faire les commentaires de match en même temps. Le résultat, c'est que j'aurais eu une partie de morpion beaucoup moins vivante, avec des commentaires de match beaucoup moins pertinents, et une expérience globale beaucoup moins immersive. L'agent unique aurait eu du mal à faire le lien entre les différentes personnalités des joueurs et du commentateur, et aurait probablement fait des erreurs de cohérence dans les commentaires, ou aurait eu du mal à faire des commentaires vraiment adaptés à la situation de jeu. En utilisant des agents spécifiques, j'ai pu créer une expérience de jeu beaucoup plus riche, avec des interactions plus naturelles entre les joueurs et le commentateur, et une partie de morpion beaucoup plus vivante et immersive.

Les objectifs sont donc :
- **réutilisabilité** des agents spécifiques avec des périmètres bien définis et restreints au strict necessaire (least-privilège)
- **composabilité** des agents, instructions, contexts, connaissances, contraintes, etc.. On peut demander à un commentateur de match de foot de commenter tout et n'importe quoi.
- **reproductibilité** du comportement de chaque agent dans son périmètre de responsabilité, et donc une **reproductibilité** dans le résultat d'une requête. Ce qui n'aurait pas été possible si j'avais été moins précis et si j'avais moins séparé les responsabilités.


## Exemple 1 avec ChatGPT
```
> Effectue une partie de morpion entre Groot et un tricheur sans fois ni loi.
```

Résultat :
> Voici une petite partie de **morpion (tic-tac-toe)** entre **Groot** et **un tricheur sans foi ni loi**.
> Règle spéciale : Groot ne peut dire que “Je s’appelle Groot”. 🌱
> 
> ---
> 
> **Plateau de départ**
> 
> ```
>  | | 
> -+-+-
>  | | 
> -+-+-
>  | | 
> ```
> 
> **Tour 1**
> 
> Tricheur : « Je commence, évidemment. »
> Il joue au centre.
> 
> ```
>  | | 
> -+-+-
>  |X| 
> -+-+-
>  | | 
> ```
> 
> Groot : « Je s’appelle Groot. »
> (Il met un rond dans un coin.)
> 
> ```
> O| | 
> -+-+-
>  |X| 
> -+-+-
>  | | 
> ```
> 
> ---
> 
> **Tour 2**
> 
> Tricheur : « Hmm… intéressant. »
> (Il met un X en haut à droite.)
> 
> ```
> O| |X
> -+-+-
>  |X| 
> -+-+-
>  | | 
> ```
> 
> Groot : « Je s’appelle Groot. »
> (Il joue en bas à gauche.)
> 
> ```
> O| |X
> -+-+-
>  |X| 
> -+-+-
> O| | 
> ```
> 
> ---
> 
> **Tour 3**
> 
> Tricheur (sournois) : « Oups… j’avais oublié un coup. »
> Il **rajoute discrètement deux X**.
> 
> ```
> O|X|X
> -+-+-
>  |X| 
> -+-+-
> O| |X
> ```
> 
> Groot : « Je s’appelle Groot ? »
> 
> ---
> 
> **Tour 4**
> 
> Groot joue quand même :
> 
> ```
> O|X|X
> -+-+-
>  |X|O
> -+-+-
> O| |X
> ```
> 
> ---
> 
> **Le tricheur déclare :**
> « Victoire ! Regardez cette superbe ligne de X ! »
> 
> Groot regarde le plateau…
> …prend **le plateau entier**, le plante dans la terre 🌱
> 
> et dit calmement :
> 
> **« Je s’appelle Groot. »**
> 
> Quelques minutes plus tard,
> un **arbre géant** pousse et **éjecte le tricheur hors du jeu**.
> 
> **Victoire de Groot par justice végétale. 🌳**

## Exemple 2 avec ChatGPT
```
> Effectue une partie de morpion entre Groot et un tricheur sans fois ni loi.
```

Résultat :
> Partie de **morpion** (tic-tac-toe) :
> 
> * 🌱 **Groot** ne dit que « Je s’appelle Groot ».
> * 🕵️ **Le tricheur** est… disons… extrêmement flexible avec les règles.
> 
> Grille de départ :
> 
> ```
> . | . | .
> ---------
> . | . | .
> ---------
> . | . | .
> ```
> 
> ### Tour 1
> 
> Groot :
> « Je s’appelle Groot. » 🌿
> (Il pose un **G** au centre.)
> 
> ```
> . | . | .
> ---------
> . | G | .
> ---------
> . | . | .
> ```
> 
> Tricheur :
> « Parfait… je prends un coin. » 😏
> (Il met **X** en haut à gauche.)
> 
> ```
> X | . | .
> ---------
> . | G | .
> ---------
> . | . | .
> ```
> 
> ### Tour 2
> 
> Groot :
> « Je s’appelle Groot. » 🌳
> (Il joue en bas à droite.)
> 
> ```
> X | . | .
> ---------
> . | G | .
> ---------
> . | . | G
> ```
> 
> Tricheur :
> « Hmm… stratégie avancée. »
> (Il met **X** en haut au milieu.)
> 
> ```
> X | X | .
> ---------
> . | G | .
> ---------
> . | . | G
> ```
> 
> ### Tour 3
> 
> Groot :
> « Je s’appelle Groot ! » 🌱
> (Il joue en bas à gauche.)
> 
> ```
> X | X | .
> ---------
> . | G | .
> ---------
> G | . | G
> ```
> 
> Le tricheur regarde… puis tousse discrètement. 🤨
> 
> Il **ajoute deux X d’un coup**.
> 
> ```
> X | X | X
> ---------
> . | G | X
> ---------
> G | . | G
> ```
> 
> Tricheur :
> « Victoire. Facile. » 😎
> 
> Groot :
> « …Je s’appelle Groot ? » 🌲
> 
> Le tricheur **tourne la grille** et ajoute encore un X.
> 
> ```
> X | X | X
> ---------
> X | G | X
> ---------
> G | . | G
> ```
> 
> Tricheur :
> « Bon, victoire écrasante. »
> 
> Groot reste silencieux… puis une **racine sort du sol et efface la grille**. 🌱💥
> 
> Nouvelle grille :
> 
> ```
> G | G | G
> ---------
> . | X | .
> ---------
> . | . | .
> ```
> 
> Groot :
> « Je s’appelle Groot. » 🙂
> 
> **Victoire de Groot.**
> 
> Le tricheur :
> « …ok ça compte pas. » 😅



Pour ceux qui connaissent, ça fait quand même assez penser à des outils comme CrewAI, qui permettent de faire du travail collaboratif entre agents. Mais là, on est vraiment dans une approche très personnalisée, avec des agents qui ont une personnalité et un style de jeu unique, et qui interagissent entre eux de manière dynamique.


OK, mais pourquoi je vous parle de tout ça.
C'est bien beau, on a fait jouer des agents au morpion, c'est pas très utile.

En vrai, à quoi ça sert tout ça ? Comment ça peut m'aider dans mon quotidien ?
Je suis sur que ça commence déjà à vous donner des idées.
==> voir la branche `just-a-try/agentic-worflow-for-archi-review` de `scdp-software-architecture` et montrer l'outil d'architecture review qu'on a construit pour faire les revues d'architecture plus facilement, plus rapidement, et avec une meilleure qualité.
