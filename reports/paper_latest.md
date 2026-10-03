# Paper trading status

Run #78 at 2026-10-03 19:11 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SANDUSDT, WLDUSDT, BNBUSDT, DOGEUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,958.93 USDT |
| return since start | -0.41% (26.1 days) |
| annualised | -5.75% |
| realized (closed pairs) | -39.66 USDT |
| funding received this run | 0.0871 USDT |
| open pairs | 2 / 10 |
| free cash | 7,960.34 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes | OPEN | 0.0100% | 4.6988 | 4.6980 | 0.0000 | 0.0000 | 0.50% | 9.3508 | 99.0% |
| ZECUSDT | yes |  | 0.0100% | 1,305.2300 | 1,305.4200 | 0.1887 | -0.1022 | 0.45% | 2,748.8557 | 110.6% |
| BNBUSDT | no |  | -0.0034% | 789.9500 | 790.2000 | - | - | - | - | - |
| BTCUSDT | no |  | -0.0010% | 84,822.1400 | 84,865.0000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0015% | 0.0930 | 0.0931 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0015% | 2,682.7700 | 2,683.8500 | - | - | - | - | - |
| SANDUSDT | no |  | -0.5783% | 0.0735 | 0.0740 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0004% | 119.6900 | 119.7800 | - | - | - | - | - |
| WLDUSDT | no | CLOSE | 0.0092% | 0.5898 | 0.5900 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0003% | 1.4872 | 1.4881 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
