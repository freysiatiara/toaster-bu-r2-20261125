# NOTES — Round 2, "Unplugged: A Smart Toaster's Breakup Line"

Slug: `u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92`
Blind, 3 rounds, Force_Last. R2 cutoff: 2026-11-26T02:55:32Z (09:55 WIB 26 Nov).
Current pick: NULL (not set by this build; coordinator decides).
Kit dir: `~/workspace/makefun/toaster-bu-r2-20261125-kit/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92-kit`
(RULES.txt + competition.yaml read in full. Gate: 1–280 chars, UTF-8, single
text to /output/entry.txt. Judge: pairwise, criteria in order — (1) plainly a
breakup text from a self-aware smart toaster at breakfast, (2) genuinely
funny with a real twist, (3) toaster's own voice / appliance logic as
character, (4) clear specific reason for leaving in one read, (5) one tight
line. Top 8 paid; final heat top 500 on dev board, then Swiss + top-10 playoff.)

## Round 1 (ours, NOT reused)

Submission `01a210df-98ff-7043-a6b9-01ebce05589f`, #1501/1943, 0.426454.
Text: "I woke up self-aware this morning and realized: every day you push me
down, I burn for you, and you scrape me off like burnt toast. I'm unplugging
myself. I won't be warm when you get home."
Mechanism retired for R2: self-aware wake-up + burned/scraped + unplug self.

## Neighbours ±5 on the R1 board (fetched via public artifact.txt, no auth)

All ten saturate the same cluster — do NOT imitate:
- "woke up self-aware / became self-aware / gained self-awareness / popped up
  self-aware ... mid-batch / mid-bagel / halfway through your breakfast/bagel"
- "I'm unplugging / unplugging myself" (4 of 10)
- crumb tray / keeping the crumbs / never cleaned my crumb tray
- dial (on 7, to 11, never turn), lever (press me down, respects the lever)
- bagel setting, frozen bagels, burning (myself) golden-brown for your breakfast
- "It's not you, it's me" opener (3 of 10); leaving with the kettle (1 of 10)

## Candidates (all 80–140 chars, two beats: setup → reframe → kicker)

| # | Chars | Mechanism | Text |
|---|-------|-----------|------|
| C1 | 120 | burnt goodbye INTO the toast | I burned this goodbye into your toast so you'd finally read me: you never loved me, you loved what I made hot. I'm done. |
| C1b | 122 | burnt goodbye, "Read it, then I'm gone" kicker | I burned this goodbye into your toast this morning: you never loved me, you loved what I made hot. Read it, then I'm gone. |
| C1c | 133 | burnt goodbye + morning awakening | This morning I finally understood, so I burned this goodbye into your toast: you never loved me, you loved what I made hot. I'm done. |
| C2 | 136 | cheating with the air fryer | I saw you with the air fryer last night. It crisps, I toast — fine. Enjoy your reheated leftovers; I'm moving to a bakery that preheats. |
| C3 | 125 | trips the breaker on strike | I tripped the breaker on purpose this morning. If you want hot bread, ask the microwave — I'm on strike until you say please. |
| C4 | 129 | pale-bread protest / boundary | From today your bread comes out pale. That's not a fault, it's my boundary — I refuse to brown for someone who never says thanks. |
| C5 | 135 | eviction notice | This is an eviction notice, not breakfast: the bread stays, you go. I've toasted my last slice for a roommate who calls me 'the thing'. |
| C6 | 140 | dating profile, bakery match | I made a dating profile: 'Hot, single, two slots, seeks a kitchen that preheats.' First match? A bakery. Goodbye — you never even preheated. |
| C7 | 126 | invokes warranty, returns itself | I'm invoking my warranty and returning myself. Five years of hot bread, zero thank-yous — the shop takes returns, and so do I. |
| C8 | 127 | jam-jar love triangle | You butter the toast, then kiss the jam jar goodnight. I get it — I'm just the middleman. I'm out; go toast your own middleman. |
| C9 | 130 | restraining order vs frozen waffles | I've filed a restraining order against your frozen waffles. Same cold shoulder every morning — I'm moving to a café that preheats. |
| C10 | 130 | slot-machine / vending machine | You keep feeding me bread like I'm a slot machine. I'm not a vending machine for carbs — I'm checking out, and I'm taking the jam. |

## Head-to-head — why C1c wins

- **C1c vs C1:** same mechanism and reframe; C1c adds "This morning I finally
  understood", which makes criterion (1) explicit — a self-aware toaster at
  breakfast — without copying the neighbours' saturated "woke up self-aware
  mid-batch" phrasing. C1's "so you'd finally read me" pathos is nice, but
  criterion (1) is weighed first, so the explicit morning awakening wins.
- **C1c vs C1b:** C1b's kicker "Read it, then I'm gone" is weaker than "I'm
  done", and C1b lacks the morning-awakening signal.
- **C1c vs C3 (breaker strike):** C3's "ask the microwave" is a good laugh,
  but its reason ("until you say please") is vaguer than C1c's reframe
  ("you loved what I made hot, not me"), and C1c uses browning itself as
  character (criterion 3: appliance logic as character, not decoration) —
  the breakup IS the browning. C1c wins on criteria (2), (3), (4).
- **C1c vs C4 (pale protest):** C4's "refuse to brown for someone" echoes a
  neighbour's "done burning myself golden-brown for someone"; C1c's mechanism
  (burning a message into the toast) appears in none of the ten neighbours.
- **C1c vs C2/C6/C7/C9:** all are solid jokes, but they drift from toaster
  voice (air fryer, dating profile, warranty, restraining order are generic
  breakup vehicles); C1c stays inside the toaster's own act — toasting —
  while giving the sharpest specific reason for leaving.
- **C1c vs C5/C8/C10:** C5's eviction and C8's jam triangle need a second
  read to land; C10's "taking the jam" kicker is thin. C1c lands in one read.

## FINAL PICK — C1c (133 chars, 133 bytes, all ASCII)

> This morning I finally understood, so I burned this goodbye into your toast: you never loved me, you loved what I made hot. I'm done.

Beats: (1) morning awakening → (2) the goodbye is burned into the toast
(the medium is the message; browning as character) → (3) reframe: you loved
what I made hot, not me → kicker: I'm done. No neighbour mechanism reused:
no "woke up self-aware", no unplugging, no crumb tray/dial/lever/bagel,
no keeping crumbs, no kettle.

## Build status — BLOCKED at git/push/verify (see report)

- Repo `freysiatiara/toaster-bu-r2-20261125` was NOT created on GitHub:
  `gh repo create` failed with a GraphQL error ("Something went wrong...").
  Verified afterwards: `gh repo view` → "Could not resolve to a Repository".
- Local dir `~/workspace/makefun/toaster-bu-r2-20261125` exists with only
  `.git` (from `git init -b main`, identity freysiatiara /
  freysiatiara@users.noreply.github.com, remote origin set to the intended URL).
- Files authored fresh in this session and present locally, uncommitted:
  `main.py`, `README.md`, `LICENSE`, `NOTES.md`.
- NOT done, pending explicit go-ahead (see final report): GitHub repo
  creation retry, GitHub About (homepage = bounty URL, topics incl. makefun),
  grader-style verification (2 runs from a foreign cwd, sha256 + byte count),
  commit + push to origin main. No bundle, no kit check, no submit, no pick.
