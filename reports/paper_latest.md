# Paper trading status

Run #213 at 2026-11-22 16:11 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, PIEVERSEUSDT, ZECUSDT, EVAAUSDT, DOGEUSDT, SOXLUSDT, QQQUSDT, XRPUSDT.

| metric | value |
|---|---|
| equity | 9,897.21 USDT |
| return since start | -1.03% (75.9 days) |
| annualised | -4.94% |
| realized (closed pairs) | -103.83 USDT |
| funding received this run | 0.4939 USDT |
| open pairs | 3 / 10 |
| free cash | 6,896.17 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0234% | 2.5188 | 2.5229 | 2.4237 | 0.5393 | 0.41% | 5.5692 | 121.1% |
| PIEVERSEUSDT | yes | OPEN | 0.0100% | 3.6579 | 3.6621 | 0.0000 | 0.0000 | 0.50% | 7.2794 | 99.0% |
| QQQUSDT | yes |  | 0.0215% | 626.6500 | 626.6700 | 0.3232 | 0.0080 | 0.51% | 1,240.2189 | 97.9% |
| BTCUSDT | no |  | 0.0019% | 60,989.0000 | 61,010.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0042% | 0.0554 | 0.0554 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0013% | 1,718.8300 | 1,719.2400 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0007% | 70.3500 | 70.3900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 33.7600 | 33.7600 | - | - | - | - | - |
| SOXSUSDT | no | CLOSE | 0.0000% | 75.5100 | 75.5100 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0033% | 0.9262 | 0.9266 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0039% | 794.3100 | 793.9800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
