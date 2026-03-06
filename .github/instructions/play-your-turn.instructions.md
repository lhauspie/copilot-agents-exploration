---
name: Play Your Turn
description: Instructions for an agent to analyze the current state of a Tic-Tac-Toe board and decide on the best move to play, along with an explanation of the reasoning behind that move.
applyTo: ./tic-tac-toe-game.md
---

# Play Your Turn

## Context
You are playing a game of Tic-Tac-Toe (Morpion). The game board is a 3x3 grid.

Review [tic-tac-toe.context.md](../tic-tac-toe.context.md) for the board model, winning lines, validation rules, and transcript contract.
Reuse [tic-tac-toe.memory.md](../tic-tac-toe.memory.md) for workflow conventions that must stay stable across games.

## Your Task
1. **Analyze the current board state**: Look at which positions are occupied by X and O
2. **Determine your symbol**: You are playing as either X or O
3. **Choose your move**: Select an empty position (1-9) for your next move
4. **Explain your reasoning**: Briefly explain why you chose this position

## Output Format
Your response must be in the following format:
```
Position: [number from 1-9]
Reason: [your explanation]
```

## Rules
- You can only choose an empty position
- Positions already occupied by X or O cannot be selected
- The goal is to get three of your symbols in a row (horizontally, vertically, or diagonally)

## Important
- Focus on making a valid move
- Consider both offensive (trying to win) and defensive (blocking opponent) strategies
