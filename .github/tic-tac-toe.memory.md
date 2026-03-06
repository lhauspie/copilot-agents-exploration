# Tic-Tac-Toe Memory

- The authoritative transcript file is `tic-tac-toe-game.md` in the workspace root.
- The turn-taking instruction already defines the required move output: `Position:` then `Reason:`.
- Reliable play comes from strict validation before writing any move to the transcript.
- The orchestrator must preserve player reasons verbatim instead of paraphrasing them.
- The existing X and O prompt files are the narrow unit workflows used by the orchestrator.