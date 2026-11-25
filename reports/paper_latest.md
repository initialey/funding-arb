# Paper trading status

Run #218 at 2026-11-25 18:37 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, SOXSUSDT, QQQUSDT, DOGEUSDT, ZECUSDT, ANTUSDT, MUUSDT.

| metric | value |
|---|---|
| equity | 9,896.11 USDT |
| return since start | -1.04% (79.0 days) |
| annualised | -4.80% |
| realized (closed pairs) | -104.88 USDT |
| funding received this run | 0.3453 USDT |
| open pairs | 2 / 10 |
| free cash | 7,895.12 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0100% | 2.7901 | 2.7898 | 3.0088 | -0.2672 | 0.50% | 5.5692 | 99.6% |
| PIEVERSEUSDT | yes |  | 0.0205% | 3.4924 | 3.4901 | 0.6127 | -0.8615 | 0.46% | 7.2794 | 108.4% |
| ANTUSDT | no |  | 0.0000% | 84.1700 | 84.2000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0036% | 59,734.4700 | 59,746.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0018% | 0.0550 | 0.0550 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0029% | 1,684.7800 | 1,684.9400 | - | - | - | - | - |
| MUUSDT | no |  | 0.0078% | 584.5200 | 584.4200 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0030% | 630.7400 | 630.8200 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0031% | 69.5700 | 69.6100 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 30.0200 | 30.0000 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0010% | 65.9800 | 66.0400 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0059% | 747.3600 | 747.3800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
