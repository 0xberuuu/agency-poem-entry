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
