# Paper trading status

Run #182 at 2026-11-09 06:10 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, SOXSUSDT, QQQUSDT, OPENAIUSDT.

| metric | value |
|---|---|
| equity | 9,905.59 USDT |
| return since start | -0.94% (62.5 days) |
| annualised | -5.51% |
| realized (closed pairs) | -94.89 USDT |
| funding received this run | 0.4109 USDT |
| open pairs | 2 / 10 |
| free cash | 7,905.11 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| SOXSUSDT | yes | OPEN | 0.0202% | 73.4800 | 73.5000 | 0.0000 | 0.0000 | 0.50% | 146.2289 | 99.0% |
| ZECUSDT | yes |  | 0.0787% | 1,214.8700 | 1,216.2000 | 1.5763 | 0.4107 | 0.41% | 2,674.1692 | 120.1% |
| BTCUSDT | no |  | 0.0064% | 74,502.1400 | 74,526.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0087% | 0.0691 | 0.0691 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0010% | 2,129.0800 | 2,130.0500 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,321.3600 | 769.8000 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0000% | 658.1000 | 658.1300 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0083% | 86.4900 | 86.5200 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0403% | 44.4200 | 44.4400 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0056% | 1.0958 | 1.0964 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
