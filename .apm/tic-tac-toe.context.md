# Tic-Tac-Toe Context Helper

## Board Representation
The board positions are numbered from 1 to 9:
```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

## Winning Lines

- Rows: `1-2-3`, `4-5-6`, `7-8-9`
- Columns: `1-4-7`, `2-5-8`, `3-6-9`
- Diagonals: `1-5-9`, `3-5-7`

## Board Validity Checklist

- Every occupied cell must contain only `X` or `O`.
- The number of `X` moves can exceed `O` by at most 1.
- `O` can never have more moves than `X`.
- Both players cannot win at the same time.

## Transcript Contract

- The running game transcript lives in `tic-tac-toe-game.md` at the workspace root.
- Each turn must show the board before and after the move.
- Each move reason must be copied exactly as returned by the playing agent.