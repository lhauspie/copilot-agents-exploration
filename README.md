# 🎮 AI Agent Tic-Tac-Toe

Ce dépôt met en place un agent de Tic-Tac-Toe distribuable, construit selon les principes de l'article GitHub Copilot sur les agentic primitives et le context engineering.

## 📁 Structure

```text
agents-exploration/
├── .github/
│   ├── agents/
│   │   ├── batman.agent.md
│   │   ├── groot.agent.md
│   │   ├── superman.agent.md
│   │   ├── tic-tac-toe-expert.agent.md
│   │   └── tic-tac-toe-game-master.agent.md
│   ├── instructions/
│   │   └── play-your-turn.instructions.md
│   ├── tic-tac-toe.context.md
│   ├── tic-tac-toe.memory.md
│   └── prompts/
│       ├── tic-tac-toe.prompt.md
│       └── tic-tac-toe-plays/
│           ├── o-play.prompt.md
│           └── x-play.prompt.md
├── AGENTS.md
├── apm.yml
└── README.md
```

## 🧱 Primitives Agentiques

### Agent spécialisé

`Tic Tac Toe Game Master` orchestre une partie complète : il contrôle le flux, affecte X et O, délègue les coups, valide chaque réponse et écrit la transcription dans `tic-tac-toe-game.md`.

### Instructions ciblées

`play-your-turn.instructions.md` définit le contrat de sortie et les règles minimales communes à tous les joueurs. Elle reste modulaire et réutilisable par les prompts de tour.

### Prompts réutilisables

- `tic-tac-toe.prompt.md` est le workflow complet pour jouer une partie.
- `tic-tac-toe-plays/x-play.prompt.md` et `tic-tac-toe-plays/o-play.prompt.md` sont les workflows unitaires pour chaque symbole.

### Contexte et mémoire

- `.github/tic-tac-toe.context.md` centralise uniquement les faits du domaine: numérotage du plateau, lignes gagnantes, règles de validation et conventions de transcript.
- `.github/tic-tac-toe.memory.md` garde uniquement les décisions de workflow qui doivent rester stables d'une exécution à l'autre.
- `AGENTS.md` fournit un contrat portable pour les runtimes qui consomment le standard `AGENTS.md`.

### Stratégie des joueurs

La stratégie n'est pas portée par les fichiers de contexte partagés. Elle appartient aux agents eux-mêmes.

- `tic-tac-toe-expert.agent.md` contient la politique de jeu optimale.
- `Batman`, `Superman` et `Groot` gardent leur style propre sans polluer le contexte commun.

## 🚀 Utilisation dans VS Code

Pour lancer une partie depuis l'éditeur, invoquez le prompt d'orchestration et fournissez deux joueurs :

```text
#tic-tac-toe
```

Variables attendues par le workflow :

- `{{player_one}}`
- `{{player_two}}`

Exemples de duels utiles :

- `Batman` vs `Superman`
- `Groot` vs `Tic Tac Toe Expert`
- `Superman` vs `Tic Tac Toe Expert`

## 📦 Distribution avec APM

APM : https://github.com/microsoft/apm

### Prérequis : Installer APM

```bash
curl -sSL https://raw.githubusercontent.com/microsoft/apm/main/install.sh | sh
```

### Distribute then Execute

Le dépôt inclut maintenant un manifeste `apm.yml` pour l'exécution outer loop, conformément à l'article.

Exemple de cycle de distribution :
```bash
apm install
apm compile
apm run copilot-tic-tac-toe --param player_one="Batman" --param player_two="Tic Tac Toe Expert"
```

Scripts fournis :

- `copilot-tic-tac-toe`
- `copilot-tic-tac-toe-debug`

## 🎯 Ce que le package garantit

- Contexte minimum mais suffisant pour chaque étape
- Validation stricte des coups avant écriture
- Réutilisation des mêmes briques entre VS Code et CLI
- Séparation claire entre contexte, mémoire, contrat commun et stratégie d'agent
- Base portable pour partage d'équipe et automatisation

## 📖 Références

- [GitHub Blog - How to build reliable AI workflows with agentic primitives and context engineering](https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)
- [VS Code - Customize AI in Visual Studio Code](https://code.visualstudio.com/docs/copilot/copilot-customization)
- [PROSE - Tooling: Scaling Agent Primitives](https://danielmeppiel.github.io/awesome-ai-native/docs/tooling/)
