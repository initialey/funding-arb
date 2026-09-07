# Funding carry backtest

Generated 2026-09-07 17:25 UTC. Data: 10 symbols, 5,400 funding events, 2026-03-12 → 2026-09-07.

Capital 10,000 USDT, 10 slots × 1,000 USDT, leg notional 500 USDT, leverage 1x. Cost per fill 0.075% (taker 0.055% + spread 0.020%), round trip 0.30% of leg notional. Signal: mean of last 3 settled rates.

## Threshold comparison (full sample, in-sample)

| threshold / interval | APR | max DD | exposure days | slot util. | trades | funding PnL | costs | net PnL |
|---|---|---|---|---|---|---|---|---|
| 0.005% | **-10.49%** | -5.16% | 93.9% | 6.8% | 368 | 35.72 | 552.00 | -516.28 |
| 0.010% | **-2.56%** | -1.26% | 45.6% | 1.2% | 91 | 10.40 | 136.50 | -126.10 |
| 0.020% | **0.00%** | 0.00% | 0.0% | 0.0% | 0 | 0.00 | 0.00 | 0.00 |

![equity](backtest_equity.png)

## Per-symbol breakdown (threshold 0.020%)

| symbol | events | trades | held ratio | mean rate | funding PnL | costs | net PnL | APR on slot |
|---|---|---|---|---|---|---|---|---|
| ADAUSDT | 540 | 0 | 0.0% | 0.0021% | 0.00 | 0.00 | 0.00 | 0.00% |
| BNBUSDT | 540 | 0 | 0.0% | 0.0028% | 0.00 | 0.00 | 0.00 | 0.00% |
| BTCUSDT | 540 | 0 | 0.0% | 0.0016% | 0.00 | 0.00 | 0.00 | 0.00% |
| DOGEUSDT | 540 | 0 | 0.0% | 0.0023% | 0.00 | 0.00 | 0.00 | 0.00% |
| ETHUSDT | 540 | 0 | 0.0% | 0.0016% | 0.00 | 0.00 | 0.00 | 0.00% |
| SOLUSDT | 540 | 0 | 0.0% | -0.0001% | 0.00 | 0.00 | 0.00 | 0.00% |
| SUIUSDT | 540 | 0 | 0.0% | 0.0025% | 0.00 | 0.00 | 0.00 | 0.00% |
| WLDUSDT | 540 | 0 | 0.0% | -0.0059% | 0.00 | 0.00 | 0.00 | 0.00% |
| XRPUSDT | 540 | 0 | 0.0% | 0.0018% | 0.00 | 0.00 | 0.00 | 0.00% |
| ZECUSDT | 540 | 0 | 0.0% | -0.0029% | 0.00 | 0.00 | 0.00 | 0.00% |

## Walk-forward (out-of-sample)

Train 60d → test 30d, step 30d. Stitched OOS: **APR 0.00%**, max DD 0.00%, exposure days 0.0%, trades 0, net PnL 0.00 USDT over 120 days.

| train start | train end | test end | chosen threshold | train APR | test APR | test max DD | test trades |
|---|---|---|---|---|---|---|---|
| 2026-03-12 | 2026-05-11 | 2026-06-10 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-04-11 | 2026-06-10 | 2026-07-10 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-05-11 | 2026-07-10 | 2026-08-09 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |
| 2026-06-10 | 2026-08-09 | 2026-09-07 | 0.020% | 0.00% | 0.00% | 0.00% | 0 |

## Assumptions

- Spot long and perp short are equal notional; basis / mark-to-market between legs is assumed to net to zero.
- Funding PnL = leg notional × funding rate for every settlement while in position (short receives positive rates).
- Notional is fixed per slot (no compounding); APR = net PnL / capital × 365 / days.
- Signal uses only settled rates (no look-ahead). A position open at the end of the sample is closed and charged exit costs.
