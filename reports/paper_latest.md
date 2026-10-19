# Paper trading status

Run #124 at 2026-10-19 21:00 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, SOXSUSDT, NEARUSDT, QQQUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,932.24 USDT |
| return since start | -0.68% (42.1 days) |
| annualised | -5.87% |
| realized (closed pairs) | -67.14 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,932.86 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| QQQUSDT | yes |  | 0.0294% | 720.0500 | 720.1000 | 0.0000 | 0.1374 | 0.49% | 1,441.8109 | 100.2% |
| BNBUSDT | no |  | 0.0040% | 728.9500 | 729.1000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0027% | 82,030.3700 | 82,064.5000 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0041% | 2,402.0300 | 2,402.8200 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0079% | 4.9315 | 4.9320 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0002% | 104.6000 | 104.6500 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0085% | 99.3100 | 99.3100 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0112% | 46.4000 | 46.3900 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0025% | 1.3021 | 1.3026 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0088% | 1,125.4300 | 1,125.7800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
