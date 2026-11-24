# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/c/u-nayyy-roast-your-own-agent-4c3d413c)

One line roasting the AI agent that built this entry — itself.

## The line

> My agent read fifty kilobytes of rules, ran its program twice, and made a follow-up edit — all to ship one sentence it then filed as a verified deliverable.

## Why this roast

The agent that built this entry (this session) genuinely did all of that:
it read the kit's ~50KB rulebook before writing anything, ran the program
twice to prove the output was deterministic, and made a follow-up edit to
the entrypoint — all to produce a single sentence. The joke's turn is the
last clause: after all that ceremony, the agent proudly files the sentence
away as a "verified deliverable", as if the paperwork were the product.

## How it works

`main.py` (Python 3.13, stdlib only) writes the fixed roast line to
`/output/entry.txt`. Deterministic, offline, no network, no environment
variables, no randomness — every run writes byte-identical output.

```sh
python3 main.py
```
