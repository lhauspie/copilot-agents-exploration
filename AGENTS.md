# AGENTS

This repository packages Tic-Tac-Toe agent primitives so they can be reused in VS Code and distributed to other runtimes.

## Core Entry Points

- `.github/agents/tic-tac-toe-game-master.agent.md`: specialist orchestrator for complete games.
- `.github/prompts/tic-tac-toe.prompt.md`: reusable workflow entry point for a full match.
- `.github/prompts/tic-tac-toe-plays/x-play.prompt.md`: unit workflow for player X.
- `.github/prompts/tic-tac-toe-plays/o-play.prompt.md`: unit workflow for player O.
- `.github/instructions/play-your-turn.instructions.md`: deterministic move contract.

## Shared Context

- `.github/tic-tac-toe.context.md`: board numbering, winning lines, validation rules, and transcript conventions.
- `.github/tic-tac-toe.memory.md`: workflow decisions that must stay stable across games.

## Responsibility Split

- Shared context files describe the game and the transcript, not a player's strategy.
- Shared instructions define the common turn contract.
- Player agents own their own decision policies and playing style.

## Execution Rules

- Write the match transcript to `tic-tac-toe-game.md` at the repository root.
- Validate every move before mutating the board.
- Preserve move reasons exactly as returned by the player agent.
- If either player name is missing, stop and request it.
- If a move is invalid, re-ask the same player without incrementing the turn.

## Distribution

- `apm.yml` is the package manifest for outer-loop execution.
- `apm run copilot-tic-tac-toe --param player_one="Batman" --param player_two="Tic Tac Toe Expert"` is the intended packaged entry point.