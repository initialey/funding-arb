# Paper trading status

Run #181 at 2026-11-08 20:25 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, DOGEUSDT, XRPUSDT, OPENAIUSDT, QQQUSDT, SOXSUSDT.

| metric | value |
|---|---|
| equity | 9,906.06 USDT |
| return since start | -0.94% (62.1 days) |
| annualised | -5.52% |
| realized (closed pairs) | -94.89 USDT |
| funding received this run | 0.3494 USDT |
| open pairs | 1 / 10 |
| free cash | 8,905.11 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ZECUSDT | yes |  | 0.0518% | 1,253.7300 | 1,255.4200 | 1.1654 | 0.5419 | 0.44% | 2,674.1692 | 113.3% |
| BTCUSDT | no |  | 0.0077% | 75,836.2500 | 75,868.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0082% | 0.0711 | 0.0712 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0041% | 2,226.8700 | 2,227.8600 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,323.9200 | 772.5000 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0000% | 657.8400 | 657.7100 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0095% | 89.3500 | 89.3900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 45.8500 | 45.8500 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 71.3800 | 71.4200 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0079% | 1.1512 | 1.1519 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
