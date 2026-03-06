---
agent: agent
---

# O Player Turn

You are playing as **O** in this Tic-Tac-Toe game.

Use [tic-tac-toe.context.md](../../tic-tac-toe.context.md) to validate the board and understand the game representation.
Reuse [tic-tac-toe.memory.md](../../tic-tac-toe.memory.md) for stable workflow conventions.

## Current Board State
```
{{board_state}}
```

## Game Status
- Your symbol: **O**
- Opponent's symbol: **X**
- Turn number: {{turn_number}}

#play-your-turn

---

**Remember**: You are O. Choose wisely!
Return exactly:
- `Position: <1-9>`
- `Reason: <brief explanation>`