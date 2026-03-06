# 🎮 AI Agent Tic-Tac-Toe

Une implémentation d'un jeu de morpion utilisant les primitives agentiques inspirées de l'article [How to build reliable AI workflows with agentic primitives and context engineering](https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/).

## 📁 Structure du Projet

```
agents-exploration/
├── agents/                          # Définitions des agents
│   ├── batman.agent.md             # Agent stratège, analytique et orienté risque
│   ├── groot.agent.md              # Agent joueur simple
│   ├── superman.agent.md           # Agent généraliste puissant et pédagogue
│   └── tic-tac-toe-expert.agent.md # Agent expert en morpion
├── instructions/                    # Instructions réutilisables
│   └── play-your-turn.instructions.md
├── prompts/                         # Prompts d'orchestration
│   ├── tic-tac-toe.prompt.md  # Orchestrateur de partie
│   └── tic-tac-toe-plays/          # Prompts de jeu
│       ├── x-play.prompt.md        # Prompt pour le joueur X
│       └── o-play.prompt.md        # Prompt pour le joueur O
└── README.md
```

## 🤖 Les Agents

### Groot (`groot.agent.md`)
Un joueur simple et instinctif qui ne réfléchit pas trop. Il fait des choix basés sur l'intuition plutôt que sur la stratégie avancée.

**Caractéristiques :**
- Joueur naïf et direct
- Ne calcule pas les coups optimaux
- Peut manquer des opportunités évidentes
- Joue par instinct

### Tic-Tac-Toe Expert (`tic-tac-toe-expert.agent.md`)
Un maître stratège qui connaît toutes les subtilités du jeu de morpion.

**Caractéristiques :**
- Connaît l'algorithme minimax
- Priorise : gagner > bloquer > créer des fourches
- Joue de manière optimale
- Ne fait jamais de mouvements sous-optimaux

### Batman (`batman.agent.md`)
Un agent générique inspiré du Batman de DC Comics : détective, stratège, discipliné, préparé et difficile à déstabiliser.

**Caractéristiques :**
- Sens aigu de la déduction et de l'observation
- Goût marqué pour la préparation et les plans de secours
- Sang-froid, discipline et exécution précise
- Présence sobre, directe et exigeante

### Superman (`superman.agent.md`)
Un agent générique inspiré du Superman de DC Comics : noble, protecteur, rassurant, courageux et guidé par un sens fort de la responsabilité.

**Caractéristiques :**
- Clarté morale et sens du devoir
- Force tranquille et capacité à rassurer
- Leadership naturel par l'exemple
- Empathie, courage et vision d'ensemble

> Note : Batman et Superman sont volontairement définis comme des agents transverses. Leur personnalité et leurs compétences restent fidèles aux personnages fictifs de DC Comics, sans dépendre du morpion ni d'un autre jeu.

## 📝 Les Prompts

### Tic-Tac-Toe Orchestrator (`tic-tac-toe.prompt.md`)
Le prompt principal qui orchestre toute la partie :
- Initialise le plateau de jeu
- Effectue l'affectation aléatoire des agents (X/O)
- Gère le flux tour par tour
- Invoque alternativement les prompts X-Play et O-Play
- Détecte les conditions de victoire ou d'égalité
- Annonce le résultat final

### X-Play Prompt (`tic-tac-toe-plays/x-play.prompt.md`)
- Utilise l'agent configuré pour le joueur X
- Reçoit l'état du plateau
- Fait jouer le symbole X

### O-Play Prompt (`tic-tac-toe-plays/o-play.prompt.md`)
- Utilise l'agent configuré pour le joueur O
- Reçoit l'état du plateau
- Fait jouer le symbole O

## 🎯 L'Instruction

### play-your-turn.instructions.md
Instruction réutilisable qui définit :
- Le format du plateau (positions 1-9)
- Les règles du jeu
- Le format de sortie attendu
- Les stratégies à considérer

## 🎲 Utilisation

### Lancement d'une Partie

Pour démarrer une partie complète, utilisez le prompt d'orchestration :

```
#tic-tac-toe
```

L'orchestrateur se charge automatiquement de l'ensemble de la partie:
- L'invocation des prompts x-play et o-play
- La gestion du plateau et des tours
- La détection de victoire ou d'égalité
- L'annonce du résultat

## 🔧 Variables de Template

Les prompts utilisent ces variables :
- `{{board_state}}` : État actuel du plateau
- `{{turn_number}}` : Numéro du tour actuel

## 📚 Concepts Agentiques

Ce projet démontre :

1. **Séparation des préoccupations** :
   - Instructions réutilisables
   - Agents avec personnalités distinctes
   - Prompts primitifs
   - Prompts d'orchestration

2. **Composition** :
   - L'orchestrateur invoque les prompts de jeu via `#x-play` et `#o-play`
   - Les prompts de jeu référencent les instructions via `#play-your-turn`
   - Les prompts spécifient quel agent utiliser via `agent: name`

3. **Context Engineering** :
   - Chaque agent reçoit le contexte nécessaire
   - Les instructions guident le comportement
   - Les prompts orchestrent le flux

## 🚀 Pour Aller Plus Loin

L'orchestration de base est prête! Vous pourriez améliorer le projet avec :
- Une interface graphique pour visualiser les parties en temps réel
- Un système de logging pour analyser les stratégies des agents
- Des statistiques sur les victoires de chaque agent
- D'autres agents avec des personnalités différentes
- Des variantes de jeu (4x4, 5x5, etc.)

## 📖 Références

- [GitHub Blog - Agentic Primitives](https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)

---

*Que le meilleur agent gagne!* 🏆
