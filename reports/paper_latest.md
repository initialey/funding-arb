# Paper trading status

Run #76 at 2026-10-03 05:10 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SPCXUSDT, DOGEUSDT, SANDUSDT, SOXSUSDT, WLDUSDT.

| metric | value |
|---|---|
| equity | 9,959.97 USDT |
| return since start | -0.40% (25.5 days) |
| annualised | -5.74% |
| realized (closed pairs) | -38.31 USDT |
| funding received this run | 0.0330 USDT |
| open pairs | 2 / 10 |
| free cash | 7,961.69 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| WLDUSDT | yes | OPEN | 0.0100% | 0.5701 | 0.5702 | 0.0000 | 0.0000 | 0.50% | 1.1345 | 99.0% |
| ZECUSDT | yes |  | 0.0100% | 1,316.8600 | 1,316.4500 | 0.0942 | -0.3208 | 0.46% | 2,748.8557 | 108.7% |
| BTCUSDT | no |  | 0.0027% | 84,532.3900 | 84,572.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0043% | 0.0931 | 0.0931 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0045% | 2,674.6800 | 2,675.9800 | - | - | - | - | - |
| SANDUSDT | no |  | -0.7238% | 0.0816 | 0.0823 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0015% | 119.2300 | 119.2700 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0050% | 29.8200 | 29.8300 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0015% | 159.0100 | 151.6000 | - | - | - | - | - |
| XRPUSDT | no | CLOSE | 0.0057% | 1.4870 | 1.4877 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
