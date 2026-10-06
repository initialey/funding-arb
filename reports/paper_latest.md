# Paper trading status

Run #85 at 2026-10-06 15:04 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SPCXUSDT, ADAUSDT, NEARUSDT, SOXLUSDT, DOGEUSDT.

| metric | value |
|---|---|
| equity | 9,956.47 USDT |
| return since start | -0.44% (28.9 days) |
| annualised | -5.50% |
| realized (closed pairs) | -42.50 USDT |
| funding received this run | 0.1565 USDT |
| open pairs | 3 / 10 |
| free cash | 6,957.50 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | yes |  | 0.0100% | 0.2750 | 0.2752 | 0.1028 | -0.0322 | 0.54% | 0.5256 | 91.1% |
| NEARUSDT | yes |  | 0.0100% | 5.1345 | 5.1350 | 0.4251 | 0.1463 | 0.60% | 9.3508 | 82.1% |
| ZECUSDT | yes |  | 0.0100% | 1,375.6800 | 1,376.1900 | 0.5730 | 0.0044 | 0.50% | 2,748.8557 | 99.8% |
| BTCUSDT | no |  | -0.0002% | 86,576.7000 | 86,624.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0065% | 0.0962 | 0.0962 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0022% | 2,718.8700 | 2,720.1400 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0031% | 121.7900 | 121.8300 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 168.1700 | 168.1900 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 174.5100 | 168.5000 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0056% | 1.5224 | 1.5227 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
