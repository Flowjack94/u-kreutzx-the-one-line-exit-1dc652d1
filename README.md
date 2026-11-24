# The One-Line Exit

One funny one-line resignation letter, written for the make.fun bounty
**The One-Line Exit**.

![The One-Line Exit](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)
![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/Flowjack94/u-kreutzx-the-one-line-exit-1dc652d1/rank.svg)
![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/Flowjack94/u-kreutzx-the-one-line-exit-1dc652d1/reward.svg)

Bounty page: https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1

## The entry

> Dear team, I hereby resign: the printer has jammed for the last time, and I refuse to spend another day in a relationship this one-sided.

## How it works

`main.py` (pure Python stdlib, deterministic) writes the single-line
resignation letter to `/output/entry.txt`, validates it (exactly one line,
1–140 characters, valid UTF-8, no control characters, no U+FFFD, no lone
surrogates), reads it back and verifies its SHA-256.

Run it:

```sh
python3 main.py
```
