# Paper trading status

Run #72 at 2026-10-01 20:59 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, MOVRUSDT, MUUSDT, NEARUSDT, SOXSUSDT.

| metric | value |
|---|---|
| equity | 9,963.90 USDT |
| return since start | -0.36% (24.1 days) |
| annualised | -5.46% |
| realized (closed pairs) | -35.54 USDT |
| funding received this run | 0.0442 USDT |
| open pairs | 1 / 10 |
| free cash | 8,964.46 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 4.8407 | 4.8450 | 0.0890 | 0.1019 | 0.40% | 10.8923 | 125.0% |
| BTCUSDT | no |  | 0.0036% | 84,586.7000 | 84,631.1000 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0022% | 2,697.3600 | 2,698.6200 | - | - | - | - | - |
| MOVRUSDT | no |  | -0.0237% | 2.9340 | 2.9343 | - | - | - | - | - |
| MUUSDT | no |  | 0.0000% | 1,091.1700 | 1,091.2000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0014% | 118.1000 | 118.1600 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 153.8500 | 153.8300 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 31.7800 | 31.7900 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0053% | 1.4978 | 1.4985 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0085% | 1,336.3500 | 1,336.5400 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
