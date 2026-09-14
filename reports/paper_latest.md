# Paper trading status

Run #20 at 2026-09-14 04:48 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, OPENAIUSDT, BNBUSDT, DOGEUSDT, FILUSDT, SOXLUSDT.

| metric | value |
|---|---|
| equity | 9,993.17 USDT |
| return since start | -0.07% (6.5 days) |
| annualised | -3.86% |
| realized (closed pairs) | -6.00 USDT |
| funding received this run | 0.2612 USDT |
| open pairs | 2 / 10 |
| free cash | 7,994.00 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes |  | 0.0254% | 0.5358 | 0.5366 | 0.4036 | 0.1496 | 0.44% | 1.1328 | 111.4% |
| ZECUSDT | yes |  | 0.0100% | 1,118.0200 | 1,118.4300 | 0.0504 | 0.0621 | 0.51% | 2,206.9453 | 97.4% |
| BNBUSDT | no |  | 0.0062% | 723.4000 | 723.7000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0069% | 77,618.7000 | 77,645.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0023% | 0.0840 | 0.0840 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0054% | 2,514.8500 | 2,515.6000 | - | - | - | - | - |
| FILUSDT | no |  | 0.0070% | 0.9688 | 0.9692 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,425.1600 | 856.0000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0018% | 101.1700 | 101.2200 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0173% | 112.2500 | 112.2500 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0014% | 1.3771 | 1.3775 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
