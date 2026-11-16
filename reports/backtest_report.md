# Funding carry backtest

Generated 2026-11-16 07:49 UTC. Data: 10 symbols, 6,265 funding events, 2026-03-12 → 2026-11-16.

Capital 10,000 USDT, 10 slots × 1,000 USDT, leg notional 500 USDT, leverage 1x. Cost per fill 0.075% (taker 0.055% + spread 0.020%), round trip 0.30% of leg notional. Signal: mean of last 3 settled rates.

## Threshold comparison (full sample, in-sample)

| threshold / interval | APR | max DD | exposure days | slot util. | trades | funding PnL | costs | net PnL |
|---|---|---|---|---|---|---|---|---|
| 0.005% | **-5.39%** | -3.68% | 94.8% | 9.1% | 316 | 106.17 | 474.00 | -367.83 |
| 0.010% | **-1.16%** | -0.80% | 77.6% | 4.2% | 102 | 73.85 | 153.00 | -79.15 |
| 0.020% | **-0.25%** | -0.26% | 18.4% | 0.4% | 27 | 23.18 | 40.50 | -17.32 |

![equity](backtest_equity.png)

## Per-symbol breakdown (threshold 0.020%)

| symbol | events | trades | held ratio | mean rate | funding PnL | costs | net PnL | APR on slot |
|---|---|---|---|---|---|---|---|---|
| BTCUSDT | 748 | 0 | 0.0% | 0.0024% | 0.00 | 0.00 | 0.00 | 0.00% |
| DOGEUSDT | 748 | 0 | 0.0% | 0.0029% | 0.00 | 0.00 | 0.00 | 0.00% |
| ETHUSDT | 748 | 0 | 0.0% | 0.0021% | 0.00 | 0.00 | 0.00 | 0.00% |
| SOLUSDT | 748 | 0 | 0.0% | 0.0006% | 0.00 | 0.00 | 0.00 | 0.00% |
| XRPUSDT | 748 | 0 | 0.0% | 0.0026% | 0.00 | 0.00 | 0.00 | 0.00% |
| ZECUSDT | 748 | 1 | 0.9% | -0.0003% | 1.31 | 1.50 | -0.19 | -0.03% |
| SOXSUSDT | 456 | 1 | 0.7% | -0.0015% | 0.00 | 1.50 | -1.50 | -0.36% |
| QQQUSDT | 224 | 3 | 4.0% | 0.0019% | 0.54 | 4.50 | -3.96 | -1.94% |
| EVAAUSDT | 540 | 8 | 7.6% | 0.0124% | 6.17 | 12.00 | -5.83 | -1.18% |
| SOXLUSDT | 557 | 14 | 9.9% | 0.0138% | 15.16 | 21.00 | -5.84 | -1.15% |

## Walk-forward (out-of-sample)

Train 60d → test 30d, step 30d. Stitched OOS: **APR -1.14%**, max DD -0.68%, exposure days 51.6%, trades 66, net PnL -58.99 USDT over 189 days.

| train start | train end | test end | chosen threshold | train APR | test APR | test max DD | test trades |
|---|---|---|---|---|---|---|---|
| 2026-03-12 | 2026-05-11 | 2026-06-10 | 0.020% | 0.00% | 0.49% | -0.05% | 5 |
| 2026-04-11 | 2026-06-10 | 2026-07-10 | 0.020% | 0.24% | -0.75% | -0.07% | 8 |
| 2026-05-11 | 2026-07-10 | 2026-08-09 | 0.010% | 0.28% | -1.53% | -0.12% | 15 |
| 2026-06-10 | 2026-08-09 | 2026-09-08 | 0.010% | -0.43% | -3.92% | -0.32% | 27 |
| 2026-07-10 | 2026-09-08 | 2026-10-08 | 0.020% | -0.39% | 0.00% | 0.00% | 0 |
| 2026-08-09 | 2026-10-08 | 2026-11-07 | 0.020% | 0.00% | -0.84% | -0.07% | 5 |
| 2026-09-08 | 2026-11-07 | 2026-11-16 | 0.020% | -0.42% | -2.33% | -0.05% | 6 |

## Assumptions

- Spot long and perp short are equal notional; basis / mark-to-market between legs is assumed to net to zero.
- Funding PnL = leg notional × funding rate for every settlement while in position (short receives positive rates).
- Notional is fixed per slot (no compounding); APR = net PnL / capital × 365 / days.
- Signal uses only settled rates (no look-ahead). A position open at the end of the sample is closed and charged exit costs.
