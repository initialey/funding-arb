# Paper trading status

Run #161 at 2026-11-01 05:53 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, TRXUSDT, PEPEUSDT, QQQUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,919.05 USDT |
| return since start | -0.81% (54.5 days) |
| annualised | -5.42% |
| realized (closed pairs) | -80.20 USDT |
| funding received this run | 0.0432 USDT |
| open pairs | 1 / 10 |
| free cash | 8,919.80 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes | OPEN | 0.0100% | 4.3798 | 4.3800 | 0.0000 | 0.0000 | 0.50% | 8.7160 | 99.0% |
| BTCUSDT | no | CLOSE | 0.0095% | 77,837.6000 | 77,860.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0038% | 0.0758 | 0.0758 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0006% | 2,267.3000 | 2,268.2300 | - | - | - | - | - |
| PEPEUSDT | no |  | 0.0056% | 0.0000 | 0.0000 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0057% | 697.0100 | 697.0500 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0039% | 95.6400 | 95.6800 | - | - | - | - | - |
| TRXUSDT | no |  | -0.0370% | 0.3117 | 0.3117 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0029% | 1.2543 | 1.2548 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0055% | 1,246.9700 | 1,247.6700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
