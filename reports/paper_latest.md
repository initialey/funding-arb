# Paper trading status

Run #180 at 2026-11-08 15:04 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, DOGEUSDT, XRPUSDT, OPENAIUSDT, ONEUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,905.94 USDT |
| return since start | -0.94% (61.9 days) |
| annualised | -5.55% |
| realized (closed pairs) | -94.89 USDT |
| funding received this run | 0.3327 USDT |
| open pairs | 1 / 10 |
| free cash | 8,905.11 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ZECUSDT | yes |  | 0.0474% | 1,270.1700 | 1,272.4700 | 0.8160 | 0.7677 | 0.45% | 2,674.1692 | 110.5% |
| BTCUSDT | no |  | 0.0094% | 75,989.1800 | 76,027.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0060% | 0.0713 | 0.0714 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0054% | 2,238.5700 | 2,239.7400 | - | - | - | - | - |
| ONEUSDT | no |  | -0.0452% | 0.0019 | 0.0019 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,333.3800 | 774.6000 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0000% | 657.7600 | 657.7900 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0083% | 89.5200 | 89.5500 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 46.2700 | 46.2800 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0091% | 1.1580 | 1.1585 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
