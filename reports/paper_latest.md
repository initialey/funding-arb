# Paper trading status

Run #115 at 2026-10-16 19:31 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SOXLUSDT, SOXSUSDT, NEARUSDT, DOGEUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,935.32 USDT |
| return since start | -0.65% (39.1 days) |
| annualised | -6.04% |
| realized (closed pairs) | -63.18 USDT |
| funding received this run | 0.0088 USDT |
| open pairs | 2 / 10 |
| free cash | 7,936.82 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes | OPEN | 0.0100% | 4.9969 | 4.9990 | 0.0000 | 0.0000 | 0.50% | 9.9441 | 99.0% |
| ZECUSDT | yes | OPEN | 0.0100% | 1,143.6200 | 1,144.1900 | 0.0000 | 0.0000 | 0.50% | 2,275.8607 | 99.0% |
| BNBUSDT | no |  | 0.0087% | 721.7000 | 722.1000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0071% | 81,518.4000 | 81,553.5000 | - | - | - | - | - |
| DOGEUSDT | no | CLOSE | 0.0073% | 0.0801 | 0.0802 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0038% | 2,413.5600 | 2,414.4200 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0001% | 103.2800 | 103.3900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 95.7600 | 95.7200 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 48.5800 | 48.5600 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0064% | 1.3006 | 1.3016 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
