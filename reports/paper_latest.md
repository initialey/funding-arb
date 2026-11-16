# Paper trading status

Run #200 at 2026-11-16 18:24 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, SOXSUSDT, DOGEUSDT, ZECUSDT, EVAAUSDT, SNXXUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,901.38 USDT |
| return since start | -0.99% (70.0 days) |
| annualised | -5.14% |
| realized (closed pairs) | -97.07 USDT |
| funding received this run | 0.1461 USDT |
| open pairs | 3 / 10 |
| free cash | 6,902.93 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0256% | 3.4078 | 3.4107 | 0.1461 | 0.2569 | 0.78% | 5.5692 | 63.4% |
| SNXXUSDT | yes | OPEN | 0.0136% | 3.0160 | 3.0170 | 0.0000 | 0.0000 | 0.50% | 6.0020 | 99.0% |
| SOXLUSDT | yes |  | 0.0197% | 49.7900 | 49.8500 | 0.0000 | 0.3005 | 0.46% | 103.4826 | 107.8% |
| BTCUSDT | no |  | 0.0007% | 64,893.6000 | 64,919.0000 | - | - | - | - | - |
| DOGEUSDT | no |  | -0.0040% | 0.0594 | 0.0595 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0021% | 1,817.7400 | 1,818.1700 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0073% | 664.7500 | 664.7900 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0041% | 71.3400 | 71.4300 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 58.3200 | 58.2800 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0023% | 887.6100 | 888.0400 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
