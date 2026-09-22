# Paper trading status

Run #45 at 2026-09-22 13:22 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, PEPEUSDT, NEARUSDT, UNIUSDT, SOXLUSDT.

| metric | value |
|---|---|
| equity | 9,980.87 USDT |
| return since start | -0.19% (14.8 days) |
| annualised | -4.71% |
| realized (closed pairs) | -15.66 USDT |
| funding received this run | 0.1557 USDT |
| open pairs | 5 / 10 |
| free cash | 4,984.34 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes |  | 0.0100% | 789.6000 | 789.6000 | 0.0979 | -0.0914 | 0.48% | 1,602.0896 | 102.9% |
| NEARUSDT | yes | OPEN | 0.0100% | 4.5506 | 4.5540 | 0.0000 | 0.0000 | 0.50% | 9.0559 | 99.0% |
| PEPEUSDT | yes | OPEN | 0.0100% | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.50% | 0.0000 | 99.0% |
| UNIUSDT | yes |  | 0.0100% | 9.1970 | 9.1840 | 0.5478 | -0.6738 | 0.54% | 17.6697 | 92.1% |
| XRPUSDT | yes |  | 0.0100% | 1.5493 | 1.5492 | 0.5145 | -0.1131 | 0.61% | 2.8098 | 81.4% |
| BTCUSDT | no |  | 0.0055% | 85,929.7500 | 85,965.3000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0083% | 0.1001 | 0.1002 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0040% | 2,747.9200 | 2,749.2400 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0078% | 117.3100 | 117.3900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 136.6300 | 136.6700 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0056% | 1,515.4200 | 1,515.2700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
