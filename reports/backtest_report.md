# Funding carry backtest

Generated 2026-09-28 06:36 UTC. Data: 10 symbols, 5,909 funding events, 2026-03-12 → 2026-09-28.

Capital 10,000 USDT, 10 slots × 1,000 USDT, leg notional 500 USDT, leverage 1x. Cost per fill 0.075% (taker 0.055% + spread 0.020%), round trip 0.30% of leg notional. Signal: mean of last 3 settled rates.

## Threshold comparison (full sample, in-sample)

| threshold / interval | APR | max DD | exposure days | slot util. | trades | funding PnL | costs | net PnL |
|---|---|---|---|---|---|---|---|---|
| 0.005% | **-10.45%** | -5.73% | 98.5% | 7.9% | 415 | 49.84 | 622.50 | -572.66 |
| 0.010% | **-2.98%** | -1.63% | 68.2% | 2.2% | 123 | 21.24 | 184.50 | -163.26 |
| 0.020% | **0.00%** | 0.00% | 0.0% | 0.0% | 0 | 0.00 | 0.00 | 0.00 |

![equity](backtest_equity.png)

## Per-symbol breakdown (threshold 0.020%)

| symbol | events | trades | held ratio | mean rate | funding PnL | costs | net PnL | APR on slot |
|---|---|---|---|---|---|---|---|---|
| BTCUSDT | 601 | 0 | 0.0% | 0.0019% | 0.00 | 0.00 | 0.00 | 0.00% |
| DOGEUSDT | 601 | 0 | 0.0% | 0.0026% | 0.00 | 0.00 | 0.00 | 0.00% |
| ETHUSDT | 601 | 0 | 0.0% | 0.0018% | 0.00 | 0.00 | 0.00 | 0.00% |
| NEARUSDT | 561 | 0 | 0.0% | 0.0033% | 0.00 | 0.00 | 0.00 | 0.00% |
| QNTUSDT | 540 | 0 | 0.0% | 0.0044% | 0.00 | 0.00 | 0.00 | 0.00% |
| SOLUSDT | 601 | 0 | 0.0% | 0.0001% | 0.00 | 0.00 | 0.00 | 0.00% |
| SUIUSDT | 601 | 0 | 0.0% | 0.0027% | 0.00 | 0.00 | 0.00 | 0.00% |
| WLDUSDT | 601 | 0 | 0.0% | -0.0049% | 0.00 | 0.00 | 0.00 | 0.00% |
| XRPUSDT | 601 | 0 | 0.0% | 0.0022% | 0.00 | 0.00 | 0.00 | 0.00% |
| ZECUSDT | 601 | 0 | 0.0% | -0.0024% | 0.00 | 0.00 | 0.00 | 0.00% |

## Walk-forward (out-of-sample)

Train 60d → test 30d, step 30d. Stitched OOS: **APR 0.00%**, max DD 0.00%, exposure days 0.0%, trades 0, net PnL 0.00 USDT over 140 days.

| train start | train end | test end | chosen threshold | train APR | test APR | test max DD | test trades |
|---|---|---|---|---|---|---|---|
| 2026-03-12 | 2026-05-11 | 2026-06-10 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-04-11 | 2026-06-10 | 2026-07-10 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-05-11 | 2026-07-10 | 2026-08-09 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-06-10 | 2026-08-09 | 2026-09-08 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-07-10 | 2026-09-08 | 2026-09-28 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |

## Assumptions

- Spot long and perp short are equal notional; basis / mark-to-market between legs is assumed to net to zero.
- Funding PnL = leg notional × funding rate for every settlement while in position (short receives positive rates).
- Notional is fixed per slot (no compounding); APR = net PnL / capital × 365 / days.
- Signal uses only settled rates (no look-ahead). A position open at the end of the sample is closed and charged exit costs.
