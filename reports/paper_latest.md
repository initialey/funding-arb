# Paper trading status

Run #214 at 2026-11-23 07:24 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, PIEVERSEUSDT, ZECUSDT, DOGEUSDT, EVAAUSDT, QQQUSDT, SOXSUSDT.

| metric | value |
|---|---|
| equity | 9,893.88 USDT |
| return since start | -1.06% (76.6 days) |
| annualised | -5.06% |
| realized (closed pairs) | -103.83 USDT |
| funding received this run | 0.2742 USDT |
| open pairs | 3 / 10 |
| free cash | 6,896.17 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0260% | 2.9580 | 2.9517 | 2.5185 | -1.3516 | 0.56% | 5.5692 | 88.3% |
| PIEVERSEUSDT | yes |  | 0.0100% | 3.7101 | 3.7019 | 0.0507 | -1.7012 | 0.51% | 7.2794 | 96.2% |
| QQQUSDT | yes |  | 0.0233% | 629.2200 | 629.2200 | 0.4519 | -0.0081 | 0.51% | 1,240.2189 | 97.1% |
| BTCUSDT | no |  | 0.0029% | 61,445.3100 | 61,478.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0018% | 0.0557 | 0.0557 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0018% | 1,723.9100 | 1,724.5300 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0014% | 72.1200 | 72.1700 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 35.5400 | 35.5700 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 70.4700 | 70.5100 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0006% | 788.2800 | 788.7200 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
