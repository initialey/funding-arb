# Funding carry backtest

Generated 2026-09-14 06:00 UTC. Data: 10 symbols, 5,290 funding events, 2026-03-12 → 2026-09-14.

Capital 10,000 USDT, 10 slots × 1,000 USDT, leg notional 500 USDT, leverage 1x. Cost per fill 0.075% (taker 0.055% + spread 0.020%), round trip 0.30% of leg notional. Signal: mean of last 3 settled rates.

## Threshold comparison (full sample, in-sample)

| threshold / interval | APR | max DD | exposure days | slot util. | trades | funding PnL | costs | net PnL |
|---|---|---|---|---|---|---|---|---|
| 0.005% | **-8.17%** | -4.16% | 97.3% | 6.9% | 318 | 60.80 | 477.00 | -416.20 |
| 0.010% | **-1.31%** | -0.67% | 73.3% | 2.3% | 71 | 39.61 | 106.50 | -66.89 |
| 0.020% | **-0.09%** | -0.13% | 13.9% | 0.2% | 13 | 15.16 | 19.50 | -4.34 |

![equity](backtest_equity.png)

## Per-symbol breakdown (threshold 0.020%)

| symbol | events | trades | held ratio | mean rate | funding PnL | costs | net PnL | APR on slot |
|---|---|---|---|---|---|---|---|---|
| BNBUSDT | 559 | 0 | 0.0% | 0.0029% | 0.00 | 0.00 | 0.00 | 0.00% |
| BTCUSDT | 559 | 0 | 0.0% | 0.0017% | 0.00 | 0.00 | 0.00 | 0.00% |
| DOGEUSDT | 559 | 0 | 0.0% | 0.0023% | 0.00 | 0.00 | 0.00 | 0.00% |
| ETHUSDT | 559 | 0 | 0.0% | 0.0017% | 0.00 | 0.00 | 0.00 | 0.00% |
| FILUSDT | 540 | 0 | 0.0% | 0.0009% | 0.00 | 0.00 | 0.00 | 0.00% |
| OPENAIUSDT | 469 | 0 | 0.0% | 0.0028% | 0.00 | 0.00 | 0.00 | 0.00% |
| SOLUSDT | 559 | 0 | 0.0% | -0.0001% | 0.00 | 0.00 | 0.00 | 0.00% |
| XRPUSDT | 559 | 0 | 0.0% | 0.0018% | 0.00 | 0.00 | 0.00 | 0.00% |
| ZECUSDT | 559 | 0 | 0.0% | -0.0027% | 0.00 | 0.00 | 0.00 | 0.00% |
| SOXLUSDT | 368 | 13 | 14.4% | 0.0211% | 15.16 | 19.50 | -4.34 | -1.29% |

## Walk-forward (out-of-sample)

Train 60d → test 30d, step 30d. Stitched OOS: **APR -0.35%**, max DD -0.21%, exposure days 40.2%, trades 21, net PnL -12.18 USDT over 126 days.

| train start | train end | test end | chosen threshold | train APR | test APR | test max DD | test trades |
|---|---|---|---|---|---|---|---|
| 2026-03-12 | 2026-05-11 | 2026-06-10 | 0.020% | 0.00% | 0.49% | -0.05% | 5 |
| 2026-04-11 | 2026-06-10 | 2026-07-10 | 0.020% | 0.24% | -0.70% | -0.06% | 6 |
| 2026-05-11 | 2026-07-10 | 2026-08-09 | 0.010% | -0.02% | -1.29% | -0.11% | 10 |
| 2026-06-10 | 2026-08-09 | 2026-09-08 | 0.020% | -0.51% | 0.00% | 0.00% | 0 |
| 2026-07-10 | 2026-09-08 | 2026-09-14 | 0.020% | -0.16% | 0.00% | 0.00% | 0 |

## Assumptions

- Spot long and perp short are equal notional; basis / mark-to-market between legs is assumed to net to zero.
- Funding PnL = leg notional × funding rate for every settlement while in position (short receives positive rates).
- Notional is fixed per slot (no compounding); APR = net PnL / capital × 365 / days.
- Signal uses only settled rates (no look-ahead). A position open at the end of the sample is closed and charged exit costs.
