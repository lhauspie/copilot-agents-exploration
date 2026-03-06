from dataclasses import dataclass
from typing import List, Optional, Tuple

# Board indices 0-8 correspond to positions 1-9
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6),             # diags
]


@dataclass
class MoveRecord:
    turn_number: int
    player: str
    position: int
    reason: str
    board_before: str
    board_after: str


def check_winner(board: List[str]) -> Optional[str]:
    for a, b, c in WIN_LINES:
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]
    if all(c != ' ' for c in board):
        return 'Draw'
    return None


def board_str(board: List[str]) -> str:
    out = []
    for r in range(3):
        row = []
        for c in range(3):
            idx = r * 3 + c
            if board[idx] == ' ':
                row.append(str(idx + 1))
            else:
                row.append(board[idx])
        out.append(' '.join(row))
    return '\n'.join(out)


def find_immediate_win(board: List[str], player: str) -> Optional[int]:
    for i in range(9):
        if board[i] != ' ':
            continue
        board[i] = player
        if check_winner(board) == player:
            board[i] = ' '
            return i
        board[i] = ' '
    return None


def count_forks(board: List[str], player: str) -> List[int]:
    forks = []
    for i in range(9):
        if board[i] != ' ':
            continue
        board[i] = player
        win_moves = 0
        for j in range(9):
            if board[j] != ' ':
                continue
            board[j] = player
            if check_winner(board) == player:
                win_moves += 1
            board[j] = ' '
        board[i] = ' '
        if win_moves >= 2:
            forks.append(i)
    return forks


def choose_move(board: List[str], player: str) -> Tuple[int, str]:
    opponent = 'O' if player == 'X' else 'X'

    # 1. Win immediately if possible
    win_pos = find_immediate_win(board, player)
    if win_pos is not None:
        return win_pos, 'Win immediately by completing a three-in-a-row.'

    # 2. Block opponent's winning move
    block_pos = find_immediate_win(board, opponent)
    if block_pos is not None:
        return block_pos, "Block opponent's immediate winning threat."

    # 3. Create a fork
    forks = count_forks(board, player)
    if forks:
        return forks[0], 'Create a fork with two future winning threats.'

    # 4. Block opponent's fork
    opp_forks = count_forks(board, opponent)
    if opp_forks:
        # If multiple, try to block in a way that also creates a threat
        # but for determinism just take the first.
        return opp_forks[0], "Block opponent's potential fork."

    # 5. Take the center if available
    if board[4] == ' ':
        return 4, 'Take the center for maximum control.'

    # Helper: corners and sides
    corners = [0, 2, 6, 8]
    sides = [1, 3, 5, 7]

    # 6. Take a corner opposite to opponent's corner
    opposite_map = {0: 8, 2: 6, 6: 2, 8: 0}
    for oc, opp in opposite_map.items():
        if board[oc] == opponent and board[opp] == ' ':
            return opp, "Take the corner opposite opponent's corner."\

    # 7. Take any available corner
    for c in corners:
        if board[c] == ' ':
            return c, 'Take an available corner.'

    # 8. Take any available side
    for s in sides:
        if board[s] == ' ':
            return s, 'Take an available side.'

    # Should never reach here
    for i in range(9):
        if board[i] == ' ':
            return i, 'Last remaining move.'
    raise RuntimeError('No moves left')


def play_game() -> Tuple[List[MoveRecord], str, Optional[Tuple[int, int, int]]]:
    board = [' '] * 9
    moves: List[MoveRecord] = []
    player = 'X'
    turn_number = 1
    winning_line: Optional[Tuple[int, int, int]] = None

    while True:
        result = check_winner(board)
        if result is not None:
            break

        board_before = board_str(board)
        pos, reason = choose_move(board, player)
        board[pos] = player
        board_after = board_str(board)

        moves.append(MoveRecord(
            turn_number=turn_number,
            player=player,
            position=pos + 1,
            reason=reason,
            board_before=board_before,
            board_after=board_after,
        ))

        # Check if this move ended the game and record winning line
        winner = check_winner(board)
        if winner in ('X', 'O'):
            for line in WIN_LINES:
                a, b, c = line
                if board[a] == board[b] == board[c] == winner:
                    winning_line = line
                    break

        # Swap player and increment full turn when O just played
        if player == 'O':
            turn_number += 1
        player = 'O' if player == 'X' else 'X'

    final_result = check_winner(board)
    return moves, final_result, winning_line


if __name__ == '__main__':
    moves, final_result, winning_line = play_game()
    print('RESULT:', final_result)
    print('WIN_LINE:', winning_line)
    print('MOVES:')
    for m in moves:
        print('---')
        print('turnNumber:', m.turn_number)
        print('player:', m.player)
        print('position:', m.position)
        print('reason:', m.reason)
        print('boardBefore:')
        print(m.board_before)
        print('boardAfter:')
        print(m.board_after)
