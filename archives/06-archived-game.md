# Tic-Tac-Toe Game

## Configuration

Chosen combination: 0

- Player one: Tic Tac Toe Expert
- Player two: Groot
- Player X: Tic Tac Toe Expert
- Player O: Groot

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
Reason: Center is the strongest opening move because it controls the most winning lines.

Board after move:

```text
1 | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9
```

=== TURN 1 - O (Groot) ===

Current board:

```text
1 | 2 | 3
---------
4 | X | 6
---------
7 | 8 | 9
```

Move played: Position 1
Reason: I am Grooooooooot! Blocking the opponent from winning next turn.

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
Reason: Take the opposite corner to maximize winning lines and create future fork chances.

Board after move:

```text
O | 2 | 3
---------
4 | X | 6
---------
7 | 8 | X
```

=== TURN 2 - O (Groot) ===

Current board:

```text
O | 2 | 3
---------
4 | X | 6
---------
7 | 8 | X
```

Move played: Position 2
Reason: I am Grooooooooot! Blocking opponent's chance to win diagonally.

Board after move:

```text
O | O | 3
---------
4 | X | 6
---------
7 | 8 | X
```

=== TURN 3 - X (Tic Tac Toe Expert) ===

Current board:

```text
O | O | 3
---------
4 | X | 6
---------
7 | 8 | X
```

Move played: Position 3
Reason: Blocks O's immediate win on the top row.

Board after move:

```text
O | O | X
---------
4 | X | 6
---------
7 | 8 | X
```

=== TURN 3 - O (Groot) ===

Current board:

```text
O | O | X
---------
4 | X | 6
---------
7 | 8 | X
```

Move played: Position 4
Reason: I am Grooooooooot! Blocking opponent from winning.

Board after move:

```text
O | O | X
---------
O | X | 6
---------
7 | 8 | X
```

=== TURN 4 - X (Tic Tac Toe Expert) ===

Current board:

```text
O | O | X
---------
O | X | 6
---------
7 | 8 | X
```

Move played: Position 7
Reason: Wins immediately by completing the diagonal 3-5-7.

Board after move:

```text
O | O | X
---------
O | X | 6
---------
X | 8 | X
```

Result: X wins (Tic Tac Toe Expert)

## Final Board

```text
O | O | X
---------
O | X | 6
---------
X | 8 | X
```

## Statistics

- Total number of turns: 4
- Total number of moves played: 7
- Winning alignment: Diagonal 3-5-7

## Strategy Summary

- Tic Tac Toe Expert took the center first, then built pressure with the opposite corner.
- On turn 3, X was forced to block O's top-row threat at position 3.
- Groot's move to position 4 on turn 3 was legal but decisive in the wrong direction because it failed to block X's immediate win on the diagonal 3-5-7.
- Tic Tac Toe Expert converted that mistake immediately with position 7.