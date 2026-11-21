# Paper trading status

Run #210 at 2026-11-21 16:05 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, SOXSUSDT, QQQUSDT, UNIUSDT, OPENAIUSDT.

| metric | value |
|---|---|
| equity | 9,896.35 USDT |
| return since start | -1.04% (74.9 days) |
| annualised | -5.05% |
| realized (closed pairs) | -102.48 USDT |
| funding received this run | 0.2796 USDT |
| open pairs | 3 / 10 |
| free cash | 6,897.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0100% | 6.1769 | 6.1739 | 2.0924 | -1.0088 | inf% | 5.5692 | -9.8% |
| QQQUSDT | yes | OPEN | 0.0119% | 623.2100 | 623.2200 | 0.0000 | 0.0000 | 0.50% | 1,240.2189 | 99.0% |
| SOXSUSDT | yes | OPEN | 0.0157% | 78.2700 | 78.2500 | 0.0000 | 0.0000 | 0.50% | 155.7612 | 99.0% |
| BTCUSDT | no |  | -0.0039% | 59,799.9000 | 59,818.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0013% | 0.0550 | 0.0550 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0083% | 1,679.4800 | 1,679.8000 | - | - | - | - | - |
| MUUSDT | no | CLOSE | 0.0072% | 610.5900 | 610.7900 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,175.3600 | 712.3000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0140% | 70.1200 | 70.1500 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0079% | 32.7700 | 32.7800 | - | - | - | - | - |
| UNIUSDT | no |  | -0.0091% | 4.6960 | 4.6990 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0011% | 787.6600 | 787.6800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
