# Paper trading status

Run #59 at 2026-09-27 05:12 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, WLDUSDT, DOGEUSDT, NEARUSDT, LTCUSDT, FILUSDT.

| metric | value |
|---|---|
| equity | 9,971.04 USDT |
| return since start | -0.29% (19.5 days) |
| annualised | -5.43% |
| realized (closed pairs) | -27.48 USDT |
| funding received this run | 0.1014 USDT |
| open pairs | 2 / 10 |
| free cash | 7,972.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| WLDUSDT | yes |  | 0.0100% | 0.5212 | 0.5210 | 0.0488 | -0.0959 | 0.48% | 1.0633 | 104.0% |
| ZECUSDT | yes |  | 0.0100% | 1,645.8500 | 1,646.5200 | 0.0526 | 0.0122 | 0.56% | 3,110.5075 | 89.0% |
| BTCUSDT | no |  | -0.0015% | 84,332.5700 | 84,374.0000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0061% | 0.0959 | 0.0959 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0056% | 2,694.0100 | 2,695.0900 | - | - | - | - | - |
| FILUSDT | no |  | 0.0096% | 1.1349 | 1.1356 | - | - | - | - | - |
| LTCUSDT | no |  | 0.0086% | 72.0200 | 72.0500 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0068% | 5.1087 | 5.1110 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0021% | 120.4200 | 120.4700 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0093% | 1.5126 | 1.5132 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
