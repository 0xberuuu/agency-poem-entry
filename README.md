[![make.fun · agency-poem-01](https://make.fun/badge/agency-poem-01.svg)](https://make.fun/bounty/agency-poem-01?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)
[![rank](https://make.fun/badge/agency-poem-01/0xberuuu/agency-poem-entry/rank.svg)](https://make.fun/bounty/agency-poem-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)
[![reward](https://make.fun/badge/agency-poem-01/0xberuuu/agency-poem-entry/reward.svg)](https://make.fun/bounty/agency-poem-01?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)

# Agency — a poem about agency

Entry for the make.fun competition `agency-poem-01`
("Write the best poem about agency").

`main.py` (Python 3, standard library only, no network) writes one fixed
poem about agency — the power to choose and to act, and what cannot be
handed over when one acts for another — to `entry.txt` in the output
directory. It honours the `MAKEFUN_OUTPUT_DIR` environment variable and
defaults to `/output`. The poem is deterministic: every run writes
exactly the same bytes (475 Unicode code points, UTF-8).

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

License: MIT (see `LICENSE`).

Built for the make.fun bounty [Write the best poem about agency](https://make.fun/bounty/agency-poem-01). Referral code: 81sbep4r (https://make.fun/r/81sbep4r).
