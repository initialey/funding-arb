# Paper trading status

Run #149 at 2026-10-28 05:29 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, DOGEUSDT, BNBUSDT, SOXSUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,924.96 USDT |
| return since start | -0.75% (50.5 days) |
| annualised | -5.43% |
| realized (closed pairs) | -74.29 USDT |
| funding received this run | 0.0344 USDT |
| open pairs | 1 / 10 |
| free cash | 8,925.71 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| XRPUSDT | yes | OPEN | 0.0100% | 1.3288 | 1.3293 | 0.0000 | 0.0000 | 0.50% | 2.6444 | 99.0% |
| BNBUSDT | no | CLOSE | 0.0089% | 745.5000 | 745.9000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0094% | 80,916.1000 | 80,952.8000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0042% | 0.0798 | 0.0798 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0076% | 2,355.7900 | 2,356.6600 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0003% | 725.4900 | 725.5600 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0050% | 102.0200 | 102.0600 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 104.0100 | 104.0800 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0027% | 41.3900 | 41.3700 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0025% | 1,315.7900 | 1,316.4900 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
