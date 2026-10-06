# Paper trading status

Run #86 at 2026-10-06 20:56 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SPCXUSDT, ADAUSDT, NEARUSDT, SOXLUSDT, DOGEUSDT.

| metric | value |
|---|---|
| equity | 9,955.86 USDT |
| return since start | -0.44% (29.1 days) |
| annualised | -5.53% |
| realized (closed pairs) | -43.42 USDT |
| funding received this run | 0.1113 USDT |
| open pairs | 2 / 10 |
| free cash | 7,956.58 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | yes |  | 0.0100% | 0.2712 | 0.2714 | 0.1542 | -0.0086 | 0.53% | 0.5256 | 93.8% |
| NEARUSDT | yes |  | 0.0100% | 5.1784 | 5.1790 | 0.4802 | 0.1577 | 0.61% | 9.3508 | 80.6% |
| BTCUSDT | no |  | -0.0011% | 85,588.8000 | 85,625.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0043% | 0.0936 | 0.0936 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0012% | 2,697.5900 | 2,698.4900 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0007% | 121.0700 | 121.1000 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 164.2700 | 164.2800 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 171.6300 | 167.1000 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0056% | 1.5018 | 1.5023 | - | - | - | - | - |
| ZECUSDT | no | CLOSE | 0.0070% | 1,344.1700 | 1,344.6000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
