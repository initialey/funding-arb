# Paper trading status

Run #54 at 2026-09-25 13:40 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, NEARUSDT, BNBUSDT, SPCXUSDT, SOXLUSDT.

| metric | value |
|---|---|
| equity | 9,974.93 USDT |
| return since start | -0.25% (17.8 days) |
| annualised | -5.13% |
| realized (closed pairs) | -24.32 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,975.68 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes | OPEN | 0.0100% | 774.6000 | 775.1000 | 0.0000 | 0.0000 | 0.50% | 1,541.4925 | 99.0% |
| BTCUSDT | no |  | 0.0009% | 84,087.0700 | 84,111.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0085% | 0.0981 | 0.0981 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0037% | 2,702.3600 | 2,703.3400 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0033% | 5.1376 | 5.1380 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0021% | 119.8000 | 119.8500 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 151.7900 | 151.9600 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 148.2800 | 141.5100 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0014% | 1.5945 | 1.5953 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0072% | 1,597.3800 | 1,599.0800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
