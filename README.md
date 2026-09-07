# funding-arb

Paper-trading validation of the **spot-long + perpetual-short funding carry** on USDT perps.
Real public market data, zero orders: the code base contains no order, position or
account endpoint and needs no API key (enforced by `tests/test_safety.py`).

## Exchange

`config.toml → [exchange] name` selects the data source. Both adapters implement the same
read-only interface (`src/data/exchange.py`), so the backtest and paper trader are venue-agnostic.

| adapter | funding history | reachable from GitHub-hosted runners | notes |
|---|---|---|---|
| `gate` (default) | 180 days | yes | Gate.io v4 public API, `BTC_USDT` contracts, 8h funding |
| `bybit` | 365 days | **no** – api.bybit.com answers 403 to US IPs | use from a non-US machine or a self-hosted runner |

The `diagnose-egress` workflow (manual) prints which exchange APIs a runner can reach and
how deep Gate's history goes.

Gate also lists tokenised stocks and commodities (gold, crude, SK Hynix, SanDisk…) as USDT perps,
often with 4h or 1h funding. `[universe] exclude` and `funding_interval_s = 28800` keep the
universe to standard 8h crypto contracts.

## What it answers

*If I had held 10,000 USDT in equal spot-long / perp-short pairs across the 10 most
traded USDT perps, entering when the trailing 3-settlement mean funding is above a
threshold and exiting when it falls below, what would the realised APR, drawdown and
time-in-market have been after fees and spread?* Phase 1 backtests one year of
history; phase 2 keeps a virtual book running every 8 hours and reports margin ratio
and distance to liquidation.

## Layout

```
config.toml                 capital, costs, thresholds, walk-forward windows
src/config.py               typed loader
src/data/                   exchange (interface), gate_client, bybit_client/bybit_source, universe, fetch -> Parquet
src/backtest/               strategy signal, engine, metrics, walk-forward, Markdown/PNG report
src/paper/                  SQLite schema, position/margin math, 8h runner, report
src/notify/telegram.py      optional Telegram push
scripts/fetch_data.py       1y funding history + daily klines -> data/*.parquet
scripts/run_backtest.py     threshold comparison + walk-forward -> reports/backtest_report.md
scripts/run_paper.py        one paper step -> paper.db, reports/paper_latest.md, Telegram
.github/workflows/          paper_trade.yml (cron every 8h) and backtest.yml (weekly + manual)
tests/                      unit tests with an in-memory market-data source and synthetic funding data
```

## Quick start

```bash
pip install -r requirements.txt
pytest -q

python scripts/fetch_data.py          # up to 1 year (180 d on Gate), 10 symbols, ~100 GET calls
python scripts/run_backtest.py        # writes reports/backtest_report.md + backtest_equity.png
python scripts/run_paper.py --no-notify
```

Telegram: set `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID` (env vars or repo secrets). Unset means no notification, nothing else changes.

## Model and assumptions

| item | value |
|---|---|
| capital | 10,000 USDT split into 10 slots of 1,000 USDT |
| legs | 500 USDT spot long + 500 USDT perp short at 1x (margin = notional) |
| signal | mean of the last 3 **settled** funding rates; rate at time *t* is never used to decide *t* |
| entry / exit | signal ≥ threshold / signal < threshold; thresholds compared: 0.005 %, 0.01 %, 0.02 % per interval |
| funding PnL | leg notional × rate at every settlement while held (short receives positive rates, pays negative) |
| costs | per fill 0.055 % taker + 0.02 % spread; a round trip is 4 fills (spot buy, perp sell, spot sell, perp buy) = 0.30 % of leg notional |
| basis | mark-to-market between spot and perp assumed to net to zero in the backtest; the paper trader tracks it as `basis MTM` |
| sizing | fixed notional per slot, no compounding; APR = net PnL / capital × 365 / days |
| walk-forward | train 60 d → test 30 d, step 30 d (4 windows on 180 d); threshold with best in-sample APR is applied out-of-sample; OOS segments are stitched |

Outputs: annualised return, max drawdown (fraction of capital), exposure-days ratio
(days with ≥1 pair open), slot utilisation, trade count, per-symbol breakdown, walk-forward table.

## Paper trader

Every 8 hours (10 minutes after the 00/08/16 UTC settlement) the workflow:

1. refreshes the universe (core BTC/ETH/SOL + top turnover, USDT linear perps),
2. fetches recent funding history and linear/spot tickers per symbol,
3. credits funding for settlements since the last step on each open pair,
4. applies the entry/exit rule and records virtual `OPEN` / `CLOSE` trades,
5. snapshots **margin ratio** and **liquidation price / distance** for the isolated perp short
   (`liq = entry × (1 + 1/L) / (1 + MMR)`, MMR 0.5 % by default),
6. writes `paper.db`, `reports/paper_latest.md`, `reports/paper_equity.png`, pushes a Telegram summary and commits.

Fetch failures are retried with back-off; a symbol that still fails is skipped, logged in the
`skips` table and left untouched until the next run.

## Dashboard (GitHub Pages)

`docs/index.html` is a static dashboard that reads `docs/data/backtest.json` and
`docs/data/paper.json`, both written by the scripts and committed by the workflows.
Enable it once: **Settings → Pages → Source: Deploy from a branch → `master` / `/docs`**.
The page then lives at `https://<owner>.github.io/funding-arb/` and refreshes itself
every time a workflow commits new data (a few minutes after each run).

Tabs: *ペーパートレード* (equity, positions, margin ratio, liquidation distance, recent
trades) and *バックテスト* (threshold comparison, equity curves, per-symbol breakdown,
walk-forward table). Until the first run each tab shows how to trigger it.

## Data

`data/funding_history.parquet` (`symbol, ts, funding_rate`) and `data/klines_daily.parquet`
are refreshed by the backtest workflow and merged incrementally. `data/universe.json` records
the symbols used and anything skipped.

## Safety

- HTTP clients accept only `GET`: Bybit on paths under `/v5/market/`, Gate on an explicit allow-list of five public endpoints; anything else raises before a request is made.
- No API key, secret or signature anywhere. Telegram is the only outbound POST.
- `tests/test_safety.py` greps `src/` for order/position/account endpoints and signed-request headers of both venues.
