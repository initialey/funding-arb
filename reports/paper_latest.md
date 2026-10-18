# Paper trading status

Run #121 at 2026-10-18 18:35 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SOXLUSDT, NEARUSDT, DOGEUSDT, BNBUSDT, SANDUSDT.

| metric | value |
|---|---|
| equity | 9,933.35 USDT |
| return since start | -0.67% (41.0 days) |
| annualised | -5.93% |
| realized (closed pairs) | -65.83 USDT |
| funding received this run | 0.0474 USDT |
| open pairs | 1 / 10 |
| free cash | 8,934.17 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ZECUSDT | yes |  | 0.0100% | 1,083.7200 | 1,083.4100 | 0.2977 | -0.3715 | 0.45% | 2,275.8607 | 110.0% |
| BNBUSDT | no |  | -0.0010% | 711.0500 | 711.3000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0032% | 81,094.5100 | 81,128.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | -0.0010% | 0.0775 | 0.0776 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0026% | 2,362.2100 | 2,363.2100 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0034% | 4.7584 | 4.7600 | - | - | - | - | - |
| SANDUSDT | no |  | -0.5884% | 0.0587 | 0.0590 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0031% | 102.0800 | 102.1300 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0240% | 89.4900 | 89.4900 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0024% | 1.2718 | 1.2727 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
