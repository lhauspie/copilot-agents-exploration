1. Présenter le "three-part framework" de Copilot
2. Construire des agents avec une personnalité et un périmètre précis
    - Groot, Je s'appelle Groot : .github/agents/tic-tac-toe-expert.agent.md
    - Expert tic-tact-toe : .github/agents/tic-tac-toe-expert.agent.md
    - On pourrait demander à ces agents de jouer aux échecs, au puissance 4, ou autre.
        - Groot serais constent dans sa simplicité
        - L'Expert pourrait être très mauvais aux autres jeux, voire pire, penser qu'il joue au morpion.
    - Outil limité à ce qu'ils ont le droit de faire (analyse Jira, push GitHub)
3. Ecrire des instructions réutilisables : La documentation à suivre
    - Comment jouer un tour de morpion : .github/instructions/play-tic-tac-toe-turn.instructions.md
    - Comment jouer un tour de puisscance 4 : ...
4. Ecrire des prompts réutilisables : Une action unitaire à réaliser
    - Que fait le joueur O quand c'est son tour : .github/prompts/tic-tac-toe-plays/o-play.prompt.md
    - Que fait le joueur X quand c'est son tour : .github/prompts/tic-tac-toe-plays/x-play.prompt.md
    - Peu importe que ce soit X ou O qui joue, le principe reste le même : play-tic-tac-toe-turn.instructions.md
    - On peut voir ça comme une fonction avec des paramètres
5. Ecrire un prompt d'orchestration : Le programme dans son ensemble
    - Boucle, condition d'arrêt, logique globale : `.github/prompts/tic-tac-toe.prompt.md`
6. Variabilisation
    - Demander à l'agent de bloquer et demander des variables : `/tic-tac-toe`
    - Anticiper les paramètres au lancement : `/tic-tac-toe Groot vs. Tic Tac Toe Expert`
