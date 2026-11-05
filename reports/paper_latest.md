# Paper trading status

Run #171 at 2026-11-05 06:34 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, SOXSUSDT, XRPUSDT, INTCUSDT, SPCXUSDT.

| metric | value |
|---|---|
| equity | 9,911.65 USDT |
| return since start | -0.88% (58.5 days) |
| annualised | -5.51% |
| realized (closed pairs) | -87.92 USDT |
| funding received this run | 0.1351 USDT |
| open pairs | 2 / 10 |
| free cash | 7,912.08 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UNIUSDT | yes |  | 0.0100% | 7.6250 | 7.6300 | 0.5172 | 0.4261 | 0.58% | 14.1771 | 85.9% |
| XRPUSDT | yes |  | 0.0100% | 1.3078 | 1.3082 | 0.0495 | 0.0764 | 0.49% | 2.6263 | 100.8% |
| BTCUSDT | no |  | 0.0059% | 80,438.8600 | 80,465.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0051% | 0.0765 | 0.0766 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0062% | 2,424.4700 | 2,425.8900 | - | - | - | - | - |
| INTCUSDT | no |  | 0.0062% | 56.4900 | 56.4900 | - | - | - | - | - |
| SOLUSDT | no | CLOSE | 0.0088% | 95.9100 | 95.9500 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 60.4600 | 60.4600 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0004% | 64.1700 | 64.1500 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 133.2900 | 131.4000 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0086% | 1,320.7500 | 1,321.2700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
