# Paper trading status

Run #179 at 2026-11-08 05:52 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, DOGEUSDT, OPENAIUSDT, ONEUSDT, LTCUSDT.

| metric | value |
|---|---|
| equity | 9,905.32 USDT |
| return since start | -0.95% (61.5 days) |
| annualised | -5.62% |
| realized (closed pairs) | -94.89 USDT |
| funding received this run | 0.0469 USDT |
| open pairs | 1 / 10 |
| free cash | 8,905.11 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ZECUSDT | yes |  | 0.0272% | 1,260.4700 | 1,261.9800 | 0.4833 | 0.4745 | 0.44% | 2,674.1692 | 112.2% |
| BTCUSDT | no |  | 0.0069% | 75,794.1000 | 75,812.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0070% | 0.0712 | 0.0713 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0042% | 2,234.2200 | 2,234.7300 | - | - | - | - | - |
| LTCUSDT | no |  | 0.0013% | 52.2400 | 52.2700 | - | - | - | - | - |
| ONEUSDT | no |  | -0.0440% | 0.0020 | 0.0020 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,305.5300 | 766.2000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0075% | 89.2100 | 89.2600 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 45.8600 | 45.8800 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0083% | 1.1629 | 1.1633 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
