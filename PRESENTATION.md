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


# Quelques remarques et choix

## Où mettre la stratégie de jeu ?
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