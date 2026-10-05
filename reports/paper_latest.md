# Paper trading status

Run #82 at 2026-10-05 05:28 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, ADAUSDT, DOGEUSDT, BNBUSDT, SANDUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,957.74 USDT |
| return since start | -0.42% (27.5 days) |
| annualised | -5.61% |
| realized (closed pairs) | -41.22 USDT |
| funding received this run | 0.1341 USDT |
| open pairs | 2 / 10 |
| free cash | 7,958.78 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 4.9629 | 4.9630 | 0.2095 | 0.1006 | 0.56% | 9.3508 | 88.4% |
| ZECUSDT | yes |  | 0.0100% | 1,320.6700 | 1,320.5000 | 0.3817 | -0.2345 | 0.46% | 2,748.8557 | 108.1% |
| ADAUSDT | no |  | 0.0054% | 0.2666 | 0.2667 | - | - | - | - | - |
| BNBUSDT | no | CLOSE | 0.0089% | 789.7500 | 789.9000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0015% | 85,492.4900 | 85,524.4000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0069% | 0.0951 | 0.0951 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0027% | 2,696.3200 | 2,697.2400 | - | - | - | - | - |
| SANDUSDT | no |  | -0.0925% | 0.0721 | 0.0722 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0056% | 120.1500 | 120.1900 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0088% | 1.5008 | 1.5010 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
