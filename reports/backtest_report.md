# Funding carry backtest

Generated 2026-09-21 06:05 UTC. Data: 10 symbols, 5,630 funding events, 2026-03-12 → 2026-09-21.

Capital 10,000 USDT, 10 slots × 1,000 USDT, leg notional 500 USDT, leverage 1x. Cost per fill 0.075% (taker 0.055% + spread 0.020%), round trip 0.30% of leg notional. Signal: mean of last 3 settled rates.

## Threshold comparison (full sample, in-sample)

| threshold / interval | APR | max DD | exposure days | slot util. | trades | funding PnL | costs | net PnL |
|---|---|---|---|---|---|---|---|---|
| 0.005% | **-9.74%** | -5.15% | 97.9% | 6.9% | 371 | 41.74 | 556.50 | -514.76 |
| 0.010% | **-2.13%** | -1.12% | 50.5% | 1.6% | 86 | 16.58 | 129.00 | -112.42 |
| 0.020% | **0.00%** | 0.00% | 0.0% | 0.0% | 0 | 0.00 | 0.00 | 0.00 |

![equity](backtest_equity.png)

## Per-symbol breakdown (threshold 0.020%)

| symbol | events | trades | held ratio | mean rate | funding PnL | costs | net PnL | APR on slot |
|---|---|---|---|---|---|---|---|---|
| AVAXUSDT | 540 | 0 | 0.0% | 0.0021% | 0.00 | 0.00 | 0.00 | 0.00% |
| BNBUSDT | 580 | 0 | 0.0% | 0.0030% | 0.00 | 0.00 | 0.00 | 0.00% |
| BTCUSDT | 580 | 0 | 0.0% | 0.0019% | 0.00 | 0.00 | 0.00 | 0.00% |
| DOGEUSDT | 580 | 0 | 0.0% | 0.0024% | 0.00 | 0.00 | 0.00 | 0.00% |
| ETHUSDT | 580 | 0 | 0.0% | 0.0017% | 0.00 | 0.00 | 0.00 | 0.00% |
| NEARUSDT | 540 | 0 | 0.0% | 0.0031% | 0.00 | 0.00 | 0.00 | 0.00% |
| OPENAIUSDT | 490 | 0 | 0.0% | 0.0027% | 0.00 | 0.00 | 0.00 | 0.00% |
| SOLUSDT | 580 | 0 | 0.0% | 0.0000% | 0.00 | 0.00 | 0.00 | 0.00% |
| XRPUSDT | 580 | 0 | 0.0% | 0.0020% | 0.00 | 0.00 | 0.00 | 0.00% |
| ZECUSDT | 580 | 0 | 0.0% | -0.0028% | 0.00 | 0.00 | 0.00 | 0.00% |

## Walk-forward (out-of-sample)

Train 60d → test 30d, step 30d. Stitched OOS: **APR 0.00%**, max DD 0.00%, exposure days 0.0%, trades 0, net PnL 0.00 USDT over 133 days.

| train start | train end | test end | chosen threshold | train APR | test APR | test max DD | test trades |
|---|---|---|---|---|---|---|---|
| 2026-03-12 | 2026-05-11 | 2026-06-10 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-04-11 | 2026-06-10 | 2026-07-10 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-05-11 | 2026-07-10 | 2026-08-09 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-06-10 | 2026-08-09 | 2026-09-08 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-07-10 | 2026-09-08 | 2026-09-21 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |

## Assumptions

- Spot long and perp short are equal notional; basis / mark-to-market between legs is assumed to net to zero.
- Funding PnL = leg notional × funding rate for every settlement while in position (short receives positive rates).
- Notional is fixed per slot (no compounding); APR = net PnL / capital × 365 / days.
- Signal uses only settled rates (no look-ahead). A position open at the end of the sample is closed and charged exit costs.
