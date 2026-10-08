# Paper trading status

Run #91 at 2026-10-08 15:32 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, NEARUSDT, DOGEUSDT, SOXLUSDT, ADAUSDT, SPCXUSDT.

| metric | value |
|---|---|
| equity | 9,955.01 USDT |
| return since start | -0.45% (30.9 days) |
| annualised | -5.31% |
| realized (closed pairs) | -44.62 USDT |
| funding received this run | 0.0939 USDT |
| open pairs | 2 / 10 |
| free cash | 7,955.38 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 4.7564 | 4.7590 | 0.7524 | 0.3629 | 0.51% | 9.3508 | 96.6% |
| ZECUSDT | yes |  | 0.0100% | 1,143.0800 | 1,143.4600 | 0.0901 | -0.0819 | 0.38% | 2,630.5871 | 130.1% |
| ADAUSDT | no |  | -0.0005% | 0.2345 | 0.2347 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0033% | 81,229.4000 | 81,234.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0087% | 0.0835 | 0.0836 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0010% | 2,456.8500 | 2,457.5800 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0054% | 108.8900 | 108.8900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 151.4000 | 151.4100 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 164.6900 | 160.1800 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0034% | 1.3524 | 1.3533 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
