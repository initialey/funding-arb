# Paper trading status

Run #183 at 2026-11-09 18:41 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, SOXSUSDT, XRPUSDT, QQQUSDT, MUUSDT.

| metric | value |
|---|---|
| equity | 9,905.53 USDT |
| return since start | -0.94% (63.0 days) |
| annualised | -5.47% |
| realized (closed pairs) | -94.89 USDT |
| funding received this run | 0.0359 USDT |
| open pairs | 2 / 10 |
| free cash | 7,905.11 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| SOXSUSDT | yes |  | 0.0202% | 56.5800 | 56.6300 | 0.0000 | 0.2354 | 0.31% | 146.2289 | 158.4% |
| ZECUSDT | yes |  | 0.0330% | 1,175.7600 | 1,176.1800 | 1.6122 | 0.0749 | 0.39% | 2,674.1692 | 127.4% |
| BTCUSDT | no |  | 0.0075% | 74,649.0000 | 74,673.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0063% | 0.0699 | 0.0700 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0009% | 2,125.2900 | 2,126.1600 | - | - | - | - | - |
| MUUSDT | no |  | 0.0000% | 729.7100 | 729.7200 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0000% | 678.2100 | 678.2300 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0060% | 86.6200 | 86.6600 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0403% | 55.4100 | 55.4200 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0042% | 1.0952 | 1.0958 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
