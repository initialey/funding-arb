# Paper trading status

Run #219 at 2026-11-26 08:05 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, SOXSUSDT, MUUSDT, QQQUSDT, DOGEUSDT, ZECUSDT, ANTUSDT.

| metric | value |
|---|---|
| equity | 9,892.72 USDT |
| return since start | -1.07% (79.6 days) |
| annualised | -4.92% |
| realized (closed pairs) | -104.88 USDT |
| funding received this run | 0.4298 USDT |
| open pairs | 2 / 10 |
| free cash | 7,895.12 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0100% | 2.9012 | 2.8961 | 3.1125 | -1.1330 | 0.54% | 5.5692 | 92.0% |
| PIEVERSEUSDT | yes |  | 0.0345% | 3.8465 | 3.8230 | 0.9388 | -3.8115 | 0.55% | 7.2794 | 89.2% |
| ANTUSDT | no |  | 0.0000% | 83.4800 | 83.5000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0057% | 60,598.1700 | 60,616.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0042% | 0.0565 | 0.0565 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0025% | 1,690.1700 | 1,690.6600 | - | - | - | - | - |
| MUUSDT | no |  | 0.0000% | 611.8700 | 612.1600 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0009% | 636.8500 | 636.8400 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0014% | 70.9300 | 70.9500 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0076% | 33.1400 | 33.1600 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0116% | 60.0900 | 60.0600 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0090% | 746.5000 | 746.7200 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
