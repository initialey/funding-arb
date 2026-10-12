# Funding carry backtest

Generated 2026-10-12 07:11 UTC. Data: 10 symbols, 6,287 funding events, 2026-03-12 → 2026-10-12.

Capital 10,000 USDT, 10 slots × 1,000 USDT, leg notional 500 USDT, leverage 1x. Cost per fill 0.075% (taker 0.055% + spread 0.020%), round trip 0.30% of leg notional. Signal: mean of last 3 settled rates.

## Threshold comparison (full sample, in-sample)

| threshold / interval | APR | max DD | exposure days | slot util. | trades | funding PnL | costs | net PnL |
|---|---|---|---|---|---|---|---|---|
| 0.005% | **-10.51%** | -6.16% | 98.6% | 9.1% | 445 | 51.26 | 667.50 | -616.24 |
| 0.010% | **-3.86%** | -2.26% | 72.1% | 2.7% | 164 | 19.53 | 246.00 | -226.47 |
| 0.020% | **-0.11%** | -0.07% | 4.2% | 0.1% | 5 | 0.81 | 7.50 | -6.69 |

![equity](backtest_equity.png)

## Per-symbol breakdown (threshold 0.020%)

| symbol | events | trades | held ratio | mean rate | funding PnL | costs | net PnL | APR on slot |
|---|---|---|---|---|---|---|---|---|
| ADAUSDT | 643 | 0 | 0.0% | 0.0025% | 0.00 | 0.00 | 0.00 | 0.00% |
| BNBUSDT | 643 | 0 | 0.0% | 0.0031% | 0.00 | 0.00 | 0.00 | 0.00% |
| BTCUSDT | 643 | 0 | 0.0% | 0.0018% | 0.00 | 0.00 | 0.00 | 0.00% |
| DOGEUSDT | 643 | 0 | 0.0% | 0.0027% | 0.00 | 0.00 | 0.00 | 0.00% |
| ETHUSDT | 643 | 0 | 0.0% | 0.0018% | 0.00 | 0.00 | 0.00 | 0.00% |
| NEARUSDT | 603 | 0 | 0.0% | 0.0035% | 0.00 | 0.00 | 0.00 | 0.00% |
| XRPUSDT | 643 | 0 | 0.0% | 0.0023% | 0.00 | 0.00 | 0.00 | 0.00% |
| SOLUSDT | 643 | 0 | 0.0% | 0.0002% | 0.00 | 0.00 | 0.00 | 0.00% |
| ZECUSDT | 643 | 0 | 0.0% | -0.0017% | 0.00 | 0.00 | 0.00 | 0.00% |
| MAGICUSDT | 540 | 5 | 3.0% | -0.0007% | 0.81 | 7.50 | -6.69 | -1.36% |

## Walk-forward (out-of-sample)

Train 60d → test 30d, step 30d. Stitched OOS: **APR -0.16%**, max DD -0.07%, exposure days 5.8%, trades 5, net PnL -6.69 USDT over 154 days.

| train start | train end | test end | chosen threshold | train APR | test APR | test max DD | test trades |
|---|---|---|---|---|---|---|---|
| 2026-03-12 | 2026-05-11 | 2026-06-10 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-04-11 | 2026-06-10 | 2026-07-10 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-05-11 | 2026-07-10 | 2026-08-09 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-06-10 | 2026-08-09 | 2026-09-08 | 0.020% | 0.00% | -0.17% | -0.01% | 1 |
| 2026-07-10 | 2026-09-08 | 2026-10-08 | 0.020% | -0.08% | -0.66% | -0.05% | 4 |
| 2026-08-09 | 2026-10-08 | 2026-10-12 | 0.020% | -0.41% | 0.00% | 0.00% | 0 |

## Assumptions

- Spot long and perp short are equal notional; basis / mark-to-market between legs is assumed to net to zero.
- Funding PnL = leg notional × funding rate for every settlement while in position (short receives positive rates).
- Notional is fixed per slot (no compounding); APR = net PnL / capital × 365 / days.
- Signal uses only settled rates (no look-ahead). A position open at the end of the sample is closed and charged exit costs.
