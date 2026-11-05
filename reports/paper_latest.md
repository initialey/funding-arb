# Paper trading status

Run #172 at 2026-11-05 16:24 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, INTCUSDT, SOXSUSDT, XRPUSDT, MUUSDT.

| metric | value |
|---|---|
| equity | 9,910.23 USDT |
| return since start | -0.90% (58.9 days) |
| annualised | -5.56% |
| realized (closed pairs) | -87.92 USDT |
| funding received this run | 0.1927 USDT |
| open pairs | 4 / 10 |
| free cash | 5,912.08 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| MUUSDT | yes | OPEN | 0.0181% | 708.6900 | 708.6700 | 0.0000 | 0.0000 | 0.50% | 1,410.3284 | 99.0% |
| SOXLUSDT | yes | OPEN | 0.0239% | 49.1700 | 49.1900 | 0.0000 | 0.0000 | 0.50% | 97.8507 | 99.0% |
| UNIUSDT | yes |  | 0.0100% | 6.9340 | 6.9380 | 0.6145 | 0.3491 | 0.47% | 14.1771 | 104.5% |
| XRPUSDT | yes |  | 0.0100% | 1.2584 | 1.2587 | 0.1449 | 0.0414 | 0.46% | 2.6263 | 108.7% |
| BTCUSDT | no |  | 0.0093% | 76,989.1500 | 77,005.0000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0075% | 0.0727 | 0.0728 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0067% | 2,284.5600 | 2,284.2800 | - | - | - | - | - |
| INTCUSDT | no |  | 0.0095% | 55.4300 | 55.4700 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0033% | 91.5400 | 91.5800 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0106% | 73.9700 | 74.1300 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0064% | 1,286.1000 | 1,286.2500 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
