# Funding carry backtest

Generated 2026-10-26 05:55 UTC. Data: 10 symbols, 6,474 funding events, 2026-03-12 → 2026-10-26.

Capital 10,000 USDT, 10 slots × 1,000 USDT, leg notional 500 USDT, leverage 1x. Cost per fill 0.075% (taker 0.055% + spread 0.020%), round trip 0.30% of leg notional. Signal: mean of last 3 settled rates.

## Threshold comparison (full sample, in-sample)

| threshold / interval | APR | max DD | exposure days | slot util. | trades | funding PnL | costs | net PnL |
|---|---|---|---|---|---|---|---|---|
| 0.005% | **-9.10%** | -5.69% | 97.8% | 9.1% | 430 | 76.44 | 645.00 | -568.56 |
| 0.010% | **-2.38%** | -1.49% | 71.6% | 2.4% | 126 | 40.09 | 189.00 | -148.91 |
| 0.020% | **-0.07%** | -0.13% | 11.4% | 0.2% | 13 | 15.16 | 19.50 | -4.34 |

![equity](backtest_equity.png)

## Per-symbol breakdown (threshold 0.020%)

| symbol | events | trades | held ratio | mean rate | funding PnL | costs | net PnL | APR on slot |
|---|---|---|---|---|---|---|---|---|
| BNBUSDT | 685 | 0 | 0.0% | 0.0032% | 0.00 | 0.00 | 0.00 | 0.00% |
| BTCUSDT | 685 | 0 | 0.0% | 0.0020% | 0.00 | 0.00 | 0.00 | 0.00% |
| DOGEUSDT | 685 | 0 | 0.0% | 0.0027% | 0.00 | 0.00 | 0.00 | 0.00% |
| ETHUSDT | 685 | 0 | 0.0% | 0.0020% | 0.00 | 0.00 | 0.00 | 0.00% |
| LTCUSDT | 540 | 0 | 0.0% | 0.0028% | 0.00 | 0.00 | 0.00 | 0.00% |
| NEARUSDT | 645 | 0 | 0.0% | 0.0037% | 0.00 | 0.00 | 0.00 | 0.00% |
| SOLUSDT | 685 | 0 | 0.0% | 0.0002% | 0.00 | 0.00 | 0.00 | 0.00% |
| XRPUSDT | 685 | 0 | 0.0% | 0.0023% | 0.00 | 0.00 | 0.00 | 0.00% |
| ZECUSDT | 685 | 0 | 0.0% | -0.0012% | 0.00 | 0.00 | 0.00 | 0.00% |
| SOXLUSDT | 494 | 13 | 10.7% | 0.0156% | 15.16 | 19.50 | -4.34 | -0.96% |

## Walk-forward (out-of-sample)

Train 60d → test 30d, step 30d. Stitched OOS: **APR -0.09%**, max DD -0.13%, exposure days 15.4%, trades 13, net PnL -4.34 USDT over 168 days.

| train start | train end | test end | chosen threshold | train APR | test APR | test max DD | test trades |
|---|---|---|---|---|---|---|---|
| 2026-03-12 | 2026-05-11 | 2026-06-10 | 0.020% | 0.00% | 0.49% | -0.05% | 5 |
| 2026-04-11 | 2026-06-10 | 2026-07-10 | 0.020% | 0.24% | -0.70% | -0.06% | 6 |
| 2026-05-11 | 2026-07-10 | 2026-08-09 | 0.020% | -0.11% | -0.32% | -0.03% | 2 |
| 2026-06-10 | 2026-08-09 | 2026-09-08 | 0.020% | -0.51% | 0.00% | 0.00% | 0 |
| 2026-07-10 | 2026-09-08 | 2026-10-08 | 0.020% | -0.16% | 0.00% | 0.00% | 0 |
| 2026-08-09 | 2026-10-08 | 2026-10-26 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |

## Assumptions

- Spot long and perp short are equal notional; basis / mark-to-market between legs is assumed to net to zero.
- Funding PnL = leg notional × funding rate for every settlement while in position (short receives positive rates).
- Notional is fixed per slot (no compounding); APR = net PnL / capital × 365 / days.
- Signal uses only settled rates (no look-ahead). A position open at the end of the sample is closed and charged exit costs.
