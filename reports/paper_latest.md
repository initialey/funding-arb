# Paper trading status

Run #174 at 2026-11-06 15:52 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, SOXSUSDT, DOGEUSDT, QQQUSDT, INTCUSDT, XRPUSDT.

| metric | value |
|---|---|
| equity | 9,906.17 USDT |
| return since start | -0.94% (59.9 days) |
| annualised | -5.72% |
| realized (closed pairs) | -90.73 USDT |
| funding received this run | 0.0723 USDT |
| open pairs | 4 / 10 |
| free cash | 5,909.27 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| MUUSDT | yes |  | 0.0168% | 697.3200 | 697.3200 | 0.1787 | 0.0139 | 0.48% | 1,410.3284 | 102.2% |
| QQQUSDT | yes | OPEN | 0.0187% | 662.5300 | 662.3100 | 0.0000 | 0.0000 | 0.50% | 1,318.4677 | 99.0% |
| SOXLUSDT | yes |  | 0.0119% | 46.4100 | 46.4000 | 0.0000 | -0.2935 | 0.45% | 97.8507 | 110.8% |
| ZECUSDT | yes | OPEN | 0.0100% | 1,343.7700 | 1,344.0200 | 0.0000 | 0.0000 | 0.50% | 2,674.1692 | 99.0% |
| BTCUSDT | no |  | 0.0072% | 75,800.4600 | 75,827.4000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0080% | 0.0730 | 0.0730 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0060% | 2,230.4100 | 2,231.5800 | - | - | - | - | - |
| INTCUSDT | no | CLOSE | 0.0030% | 56.0900 | 56.0900 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0025% | 90.6400 | 90.6800 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 70.4800 | 70.6000 | - | - | - | - | - |
| XRPUSDT | no | CLOSE | 0.0098% | 1.1861 | 1.1864 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
