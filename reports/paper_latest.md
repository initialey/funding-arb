# Paper trading status

Run #146 at 2026-10-27 04:54 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, DOGEUSDT, XRPUSDT, BNBUSDT, QQQUSDT, SOXSUSDT.

| metric | value |
|---|---|
| equity | 9,926.23 USDT |
| return since start | -0.74% (49.5 days) |
| annualised | -5.44% |
| realized (closed pairs) | -73.02 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,926.98 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes | OPEN | 0.0100% | 736.7500 | 737.0000 | 0.0000 | 0.0000 | 0.50% | 1,466.1692 | 99.0% |
| BTCUSDT | no |  | 0.0078% | 79,656.1000 | 79,671.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0030% | 0.0774 | 0.0774 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0052% | 2,310.3100 | 2,311.0400 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0000% | 712.8900 | 712.8600 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0088% | 100.0100 | 100.0500 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 90.3200 | 90.3400 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 48.3700 | 48.3400 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0081% | 1.2965 | 1.2971 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0072% | 1,219.9200 | 1,220.5000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
