# Paper trading status

Run #126 at 2026-10-20 13:31 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, SOXSUSDT, NEARUSDT, QQQUSDT, WLDUSDT.

| metric | value |
|---|---|
| equity | 9,930.16 USDT |
| return since start | -0.70% (42.8 days) |
| annualised | -5.95% |
| realized (closed pairs) | -68.68 USDT |
| funding received this run | 0.0497 USDT |
| open pairs | 1 / 10 |
| free cash | 8,931.32 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ZECUSDT | yes |  | 0.0100% | 1,141.9200 | 1,141.1700 | 0.0497 | -0.4609 | 0.49% | 2,284.2786 | 100.0% |
| BTCUSDT | no |  | 0.0061% | 81,327.1400 | 81,355.6000 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0066% | 2,387.6400 | 2,388.6500 | - | - | - | - | - |
| NEARUSDT | no |  | -0.0000% | 4.6739 | 4.6760 | - | - | - | - | - |
| QQQUSDT | no | CLOSE | 0.0000% | 715.5400 | 715.3300 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0009% | 104.2000 | 104.2400 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 93.5100 | 93.5000 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 49.2300 | 49.2400 | - | - | - | - | - |
| WLDUSDT | no |  | 0.0034% | 0.5496 | 0.5498 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0062% | 1.2957 | 1.2964 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
