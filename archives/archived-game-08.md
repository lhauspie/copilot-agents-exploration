# Tic-Tac-Toe Game: Batman vs. Superman

## Game Initialization

Random assignment result: `0`

- Player One: Batman
- Player Two: Superman
- X: Batman
- O: Superman

Initial board:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

=== TURN 1 - X (Batman) ===

Current board:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

Move played: Position 5
Reason: Taking the center creates the most winning lines and keeps future fork options open.

Board after move:

```text
1 | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9
```

=== TURN 1 - O (Superman) ===

Current board:

```text
1 | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9
```

Move played: Position 1
Reason: A corner is the strongest reply to a center opening because it preserves counterplay and reduces immediate tactical risks.

Board after move:

```text
O | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9
```

=== TURN 2 - X (Batman) ===

Current board:

```text
O | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9
```

Move played: Position 9
Reason: The opposite corner maximizes pressure and threatens future fork patterns around the center.

Board after move:

```text
O | 2 | 3
---------
4 | X | 6
---------
7 | 8 | X
```

=== TURN 2 - O (Superman) ===

Current board:

```text
O | 2 | 3
---------
4 | X | 6
---------
7 | 8 | X
```

Move played: Position 3
Reason: This corner blocks the most dangerous fork pattern and keeps the game in a drawable state.

Board after move:

```text
O | 2 | O
---------
4 | X | 6
---------
7 | 8 | X
```

=== TURN 3 - X (Batman) ===

Current board:

```text
O | 2 | O
---------
4 | X | 6
---------
7 | 8 | X
```

Move played: Position 7
Reason: This creates immediate pressure on the bottom row and forces a defensive response.

Board after move:

```text
O | 2 | O
---------
4 | X | 6
---------
X | 8 | X
```

=== TURN 3 - O (Superman) ===

Current board:

```text
O | 2 | O
---------
4 | X | 6
---------
X | 8 | X
```

Move played: Position 8
Reason: Batman threatens to complete 7-8-9 next move, so blocking that line is mandatory.

Board after move:

```text
O | 2 | O
---------
4 | X | 6
---------
X | O | X
```

=== TURN 4 - X (Batman) ===

Current board:

```text
O | 2 | O
---------
4 | X | 6
---------
X | O | X
```

Move played: Position 4
Reason: This is the strongest active move because it sets up the only remaining immediate threat on the middle row.

Board after move:

```text
O | 2 | O
---------
X | X | 6
---------
X | O | X
```

=== TURN 4 - O (Superman) ===

Current board:

```text
O | 2 | O
---------
X | X | 6
---------
X | O | X
```

Move played: Position 6
Reason: Batman is threatening 4-5-6, so this block is forced.

Board after move:

```text
O | 2 | O
---------
X | X | O
---------
X | O | X
```

=== TURN 5 - X (Batman) ===

Current board:

```text
O | 2 | O
---------
X | X | O
---------
X | O | X
```

Move played: Position 2
Reason: This is the last open square; it keeps the board legal but does not create a winning line for either player.

Board after move:

```text
O | X | O
---------
X | X | O
---------
X | O | X
```

## Game Conclusion

Result: Draw

Final board:

```text
O | X | O
---------
X | X | O
---------
X | O | X
```

Statistics:

- Total turns: 5
- Total moves played: 9
- Winning alignment: None

Strategy summary:

- Batman opened with the center and then used the opposite corner to create long-term tactical pressure.
- Superman found the correct defensive corner on turn 2, which prevented the classic center-corner fork from becoming decisive.
- The rest of the game was a sequence of forced threats and blocks, leading to a correct draw with no legal winning continuation for either side.