# Paper trading status

Run #147 at 2026-10-27 14:22 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, DOGEUSDT, BNBUSDT, SNXXUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,926.28 USDT |
| return since start | -0.74% (49.9 days) |
| annualised | -5.40% |
| realized (closed pairs) | -73.02 USDT |
| funding received this run | 0.0504 USDT |
| open pairs | 1 / 10 |
| free cash | 8,926.98 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes |  | 0.0100% | 741.9500 | 742.2000 | 0.0504 | -0.0012 | 0.51% | 1,466.1692 | 97.6% |
| BTCUSDT | no |  | 0.0095% | 80,024.9500 | 80,048.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0038% | 0.0776 | 0.0776 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0078% | 2,320.5100 | 2,321.1000 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0000% | 716.4200 | 716.4800 | - | - | - | - | - |
| SNXXUSDT | no |  | 0.0000% | 8.7480 | 8.7570 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0092% | 100.1200 | 100.1800 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 95.4200 | 95.4500 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0089% | 1.3114 | 1.3117 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0074% | 1,267.0900 | 1,267.8800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
