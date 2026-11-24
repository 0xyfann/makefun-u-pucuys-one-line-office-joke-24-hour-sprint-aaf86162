# BUILD-NOTES — One-Line Office Joke (pucuys-office-joke)

## The joke

> Our 15-minute 'quick sync' ran 47 minutes and ended with us scheduling a follow-up meeting about the meeting.

109 characters, one sentence, one line, no trailing newline.

## Why this line

- It is a joke, not an observation: setup (a 15-minute "quick sync")
  pays off with a surprise twist (it ate 47 minutes and spawned a
  follow-up meeting *about the meeting*).
- Specific detail, not a generic complaint: the exact numbers (15 vs 47)
  and the recursive meeting make it concrete and fresh, and it mirrors
  the bounty description's own framing — a meeting that should have
  been an email.
- Clear on first read: "quick sync" is everyday office language; no
  reference needs explaining.
- Alternatives I considered and dropped: a printer joke ("the printer
  only jams on urgent documents, which makes it the most honest employee
  in this office") — good punchline, but the meeting line hits the
  brief's own example harder; a standup joke — too generic.

## Program design

- `main.py` is deliberately boring: one constant, one writer, no
  network, no randomness, no imports beyond `os`/`sys`.
- It self-checks the gate before writing: 1–200 characters, single
  line (rejects any `\n`/`\r`), UTF-8, no trailing newline, so the
  bytes on disk are exactly the joke.
- Exit code 0 on success, 1 if the text ever fails the gate — the
  grader's `run_completes` check only needs exit 0.

## Verification

Ran locally as the grader does (`python3 -P -s main.py` with
`MAKEFUN_BOT_DIR` and a fresh empty `MAKEFUN_OUTPUT_DIR`): exit 0,
`entry.txt` contains exactly the line above, 109 characters.

## Files

- `main.py` — entrypoint (written in 3 chunks + 1 revision edit)
- `README.md` — entry description and run instructions
- `prompt.txt` — the exact prompt this build ran under
- `BUILD-NOTES.md` — this file
- `LICENSE` — added by the parent at repo/init time (MIT)
