# Paper trading status

Run #119 at 2026-10-18 04:21 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SOXLUSDT, NEARUSDT, BNBUSDT, DOGEUSDT, WLDUSDT.

| metric | value |
|---|---|
| equity | 9,933.64 USDT |
| return since start | -0.66% (40.4 days) |
| annualised | -5.99% |
| realized (closed pairs) | -65.83 USDT |
| funding received this run | 0.0283 USDT |
| open pairs | 1 / 10 |
| free cash | 8,934.17 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ZECUSDT | yes |  | 0.0100% | 1,146.4600 | 1,147.0700 | 0.2012 | 0.0169 | 0.50% | 2,275.8607 | 98.5% |
| BNBUSDT | no |  | -0.0009% | 720.8500 | 721.3000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0038% | 81,869.7000 | 81,906.4000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0020% | 0.0795 | 0.0796 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0028% | 2,421.7200 | 2,422.8400 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0030% | 5.0113 | 5.0130 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0040% | 104.1900 | 104.2300 | - | - | - | - | - |
| SOXLUSDT | no | CLOSE | -0.0015% | 91.5500 | 91.5500 | - | - | - | - | - |
| WLDUSDT | no |  | -0.0013% | 0.4941 | 0.4946 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0020% | 1.2998 | 1.3005 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
