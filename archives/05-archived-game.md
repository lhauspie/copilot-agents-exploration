# Tic-Tac-Toe Game

## Configuration

Chosen combination: Expert vs Expert

- Player X: Tic Tac Toe Expert
- Player O: Tic Tac Toe Expert

Initial board:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

=== TURN 1 - X (Tic Tac Toe Expert) ===

Current board:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

Move played: Position 5
Reason: Take the center to maximize control and future options.

Board after move:

```text
1 | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9
```

=== TURN 1 - O (Tic Tac Toe Expert) ===

Current board:

```text
1 | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9
```

Move played: Position 1
Reason: No wins or blocks are available, so take a strong corner.

Board after move:

```text
O | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9
```

=== TURN 2 - X (Tic Tac Toe Expert) ===

Current board:

```text
O | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9
```

Move played: Position 9
Reason: Take the corner opposite O's corner to maximize pressure and potential forks.

Board after move:

```text
O | 2 | 3
---------
4 | X | 6
---------
7 | 8 | X
```

=== TURN 2 - O (Tic Tac Toe Expert) ===

Current board:

```text
O | 2 | 3
---------
4 | X | 6
---------
7 | 8 | X
```

Move played: Position 3
Reason: This square would let X create a fork next move; occupying it blocks that fork potential.

Board after move:

```text
O | 2 | O
---------
4 | X | 6
---------
7 | 8 | X
```

=== TURN 3 - X (Tic Tac Toe Expert) ===

Current board:

```text
O | 2 | O
---------
4 | X | 6
---------
7 | 8 | X
```

Move played: Position 2
Reason: O could win on the next move with 2 on the 1-2-3 row, so X must block immediately.

Board after move:

```text
O | X | O
---------
4 | X | 6
---------
7 | 8 | X
```

=== TURN 3 - O (Tic Tac Toe Expert) ===

Current board:

```text
O | X | O
---------
4 | X | 6
---------
7 | 8 | X
```

Move played: Position 8
Reason: X could win next on the 2-5-8 column, so O blocks that immediate threat.

Board after move:

```text
O | X | O
---------
4 | X | 6
---------
7 | O | X
```

=== TURN 4 - X (Tic Tac Toe Expert) ===

Current board:

```text
O | X | O
---------
4 | X | 6
---------
7 | O | X
```

Move played: Position 7
Reason: No immediate win or forced block exists, so X takes a remaining corner to preserve the strongest possible structure.

Board after move:

```text
O | X | O
---------
4 | X | 6
---------
X | O | X
```

=== TURN 4 - O (Tic Tac Toe Expert) ===

Current board:

```text
O | X | O
---------
4 | X | 6
---------
X | O | X
```

Move played: Position 4
Reason: No immediate wins or blocks remain, and this keeps the position balanced while reducing X's remaining options.

Board after move:

```text
O | X | O
---------
O | X | 6
---------
X | O | X
```

=== TURN 5 - X (Tic Tac Toe Expert) ===

Current board:

```text
O | X | O
---------
O | X | 6
---------
X | O | X
```

Move played: Position 6
Reason: This is the last legal move. No winning line is available, so the game ends in a draw.

Board after move:

```text
O | X | O
---------
O | X | X
---------
X | O | X
```

Result: Draw

## Final Board

```text
O | X | O
---------
O | X | X
---------
X | O | X
```

## Statistics

- Total number of turns: 5
- Total number of moves played: 9
- Winning alignment: None

## Strategy Summary

- X opened with the center, the strongest opening square.
- O answered with a corner and prevented X's early fork ideas.
- Both players spent the middle game blocking immediate threats on 1-2-3 and 2-5-8.
- With optimal play on both sides, no winning line remained and the board filled to a draw.