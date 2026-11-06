# Paper trading status

Run #175 at 2026-11-06 21:27 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, SOXSUSDT, DOGEUSDT, QQQUSDT, XRPUSDT, SPCXUSDT.

| metric | value |
|---|---|
| equity | 9,906.16 USDT |
| return since start | -0.94% (60.2 days) |
| annualised | -5.69% |
| realized (closed pairs) | -92.37 USDT |
| funding received this run | 0.0824 USDT |
| open pairs | 3 / 10 |
| free cash | 6,907.63 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| MUUSDT | yes |  | 0.0123% | 693.0000 | 693.1600 | 0.1787 | 0.1267 | 0.48% | 1,410.3284 | 103.5% |
| QQQUSDT | yes |  | 0.0195% | 657.8300 | 657.8600 | 0.0328 | 0.1876 | 0.49% | 1,318.4677 | 100.4% |
| ZECUSDT | yes |  | 0.0100% | 1,334.4400 | 1,335.2600 | 0.0497 | 0.2127 | 0.49% | 2,674.1692 | 100.4% |
| BTCUSDT | no |  | 0.0054% | 75,791.1300 | 75,819.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0070% | 0.0727 | 0.0727 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0028% | 2,227.9100 | 2,229.0700 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0038% | 89.8900 | 89.9200 | - | - | - | - | - |
| SOXLUSDT | no | CLOSE | 0.0000% | 46.0400 | 46.0400 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 70.9700 | 70.9900 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0026% | 135.4100 | 133.2100 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0092% | 1.1773 | 1.1778 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
