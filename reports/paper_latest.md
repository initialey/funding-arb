# Paper trading status

Run #187 at 2026-11-11 16:04 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, SOXSUSDT, OPENAIUSDT, XRPUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,903.52 USDT |
| return since start | -0.96% (64.9 days) |
| annualised | -5.42% |
| realized (closed pairs) | -95.73 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,904.27 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| QQQUSDT | yes | OPEN | 0.0136% | 691.8500 | 691.8200 | 0.0000 | 0.0000 | 0.50% | 1,376.8159 | 99.0% |
| BTCUSDT | no |  | 0.0087% | 74,003.4900 | 74,038.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0031% | 0.0690 | 0.0690 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0018% | 2,072.8000 | 2,073.9500 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,308.8700 | 757.2000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0069% | 84.6600 | 84.6900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 67.0500 | 66.9900 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 44.6400 | 44.6900 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0096% | 1.0685 | 1.0690 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0048% | 991.4300 | 991.8000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
