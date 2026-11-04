# Paper trading status

Run #169 at 2026-11-04 06:05 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, INTCUSDT, SOXSUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,915.08 USDT |
| return since start | -0.85% (57.5 days) |
| annualised | -5.39% |
| realized (closed pairs) | -84.15 USDT |
| funding received this run | 0.2118 USDT |
| open pairs | 3 / 10 |
| free cash | 6,915.85 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BTCUSDT | yes |  | 0.0100% | 77,818.7500 | 77,858.6000 | 0.0501 | 0.0830 | 0.50% | 154,487.5622 | 98.5% |
| QQQUSDT | yes |  | 0.0102% | 684.9200 | 685.0100 | 0.5104 | 0.0574 | 0.48% | 1,391.3433 | 103.1% |
| UNIUSDT | yes |  | 0.0100% | 7.3080 | 7.3130 | 0.3545 | 0.4230 | 0.53% | 14.1771 | 94.0% |
| DOGEUSDT | no |  | 0.0082% | 0.0746 | 0.0747 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0083% | 2,292.9800 | 2,293.5700 | - | - | - | - | - |
| INTCUSDT | no |  | 0.0039% | 60.2700 | 60.2700 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0082% | 92.8700 | 92.8900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 75.0900 | 75.1300 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0014% | 52.3300 | 52.2500 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0090% | 1.2763 | 1.2768 | - | - | - | - | - |
| ZECUSDT | no | CLOSE | 0.0099% | 1,252.3900 | 1,253.2600 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
