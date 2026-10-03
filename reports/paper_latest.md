# Paper trading status

Run #77 at 2026-10-03 13:19 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SANDUSDT, SPCXUSDT, DOGEUSDT, WLDUSDT, SUIUSDT.

| metric | value |
|---|---|
| equity | 9,960.39 USDT |
| return since start | -0.40% (25.8 days) |
| annualised | -5.60% |
| realized (closed pairs) | -38.31 USDT |
| funding received this run | 0.1004 USDT |
| open pairs | 2 / 10 |
| free cash | 7,961.69 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| WLDUSDT | yes |  | 0.0100% | 0.6063 | 0.6067 | 0.0532 | 0.2575 | 0.57% | 1.1345 | 87.1% |
| ZECUSDT | yes |  | 0.0100% | 1,303.9000 | 1,303.6700 | 0.1414 | -0.2540 | 0.45% | 2,748.8557 | 110.8% |
| BTCUSDT | no |  | 0.0000% | 84,773.6600 | 84,816.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0010% | 0.0925 | 0.0926 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0022% | 2,678.5000 | 2,679.6600 | - | - | - | - | - |
| SANDUSDT | no |  | -0.7545% | 0.0756 | 0.0760 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0001% | 119.3800 | 119.4200 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 159.2700 | 154.8300 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0013% | 1.1784 | 1.1791 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0035% | 1.4831 | 1.4838 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
