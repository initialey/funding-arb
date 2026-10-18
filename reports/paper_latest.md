# Paper trading status

Run #120 at 2026-10-18 12:34 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, NEARUSDT, SOXLUSDT, BNBUSDT, WLDUSDT, SANDUSDT.

| metric | value |
|---|---|
| equity | 9,933.58 USDT |
| return since start | -0.66% (40.8 days) |
| annualised | -5.94% |
| realized (closed pairs) | -65.83 USDT |
| funding received this run | 0.0492 USDT |
| open pairs | 1 / 10 |
| free cash | 8,934.17 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ZECUSDT | yes |  | 0.0100% | 1,125.6100 | 1,125.9600 | 0.2504 | -0.0922 | 0.48% | 2,275.8607 | 102.2% |
| BNBUSDT | no |  | -0.0038% | 722.3500 | 722.7000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0029% | 81,936.1700 | 81,975.7000 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0036% | 2,413.0600 | 2,414.0700 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0048% | 4.9062 | 4.9090 | - | - | - | - | - |
| SANDUSDT | no |  | -0.6681% | 0.0610 | 0.0612 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0031% | 104.0400 | 104.1100 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0015% | 92.6000 | 92.6000 | - | - | - | - | - |
| WLDUSDT | no |  | -0.0092% | 0.4950 | 0.4956 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0027% | 1.2951 | 1.2958 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
