# Paper trading status

Run #99 at 2026-10-11 05:38 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, XRPUSDT, ZECUSDT, NEARUSDT, MAGICUSDT, WLDUSDT, ADAUSDT, CFXUSDT.

| metric | value |
|---|---|
| equity | 9,943.16 USDT |
| return since start | -0.57% (33.5 days) |
| annualised | -6.19% |
| realized (closed pairs) | -56.09 USDT |
| funding received this run | 0.0338 USDT |
| open pairs | 1 / 10 |
| free cash | 8,943.91 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| WLDUSDT | yes | OPEN | 0.0100% | 0.5560 | 0.5560 | 0.0000 | 0.0000 | 0.50% | 1.1065 | 99.0% |
| ADAUSDT | no | CLOSE | 0.0090% | 0.2474 | 0.2477 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0005% | 83,026.0700 | 83,073.3000 | - | - | - | - | - |
| CFXUSDT | no |  | 0.0009% | 0.0599 | 0.0600 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0001% | 2,506.3100 | 2,507.4900 | - | - | - | - | - |
| MAGICUSDT | no |  | -0.3289% | 0.1075 | 0.1079 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0096% | 5.2443 | 5.2480 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0007% | 109.5500 | 109.6000 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0015% | 1.3949 | 1.3958 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0050% | 1,223.6400 | 1,224.1400 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
