# Paper trading status

Run #87 at 2026-10-07 05:49 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SPCXUSDT, ADAUSDT, DOGEUSDT, SOXLUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,955.19 USDT |
| return since start | -0.45% (29.5 days) |
| annualised | -5.54% |
| realized (closed pairs) | -44.62 USDT |
| funding received this run | 0.0799 USDT |
| open pairs | 1 / 10 |
| free cash | 8,955.38 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 5.0336 | 5.0330 | 0.5338 | 0.0274 | 0.58% | 9.3508 | 85.8% |
| ADAUSDT | no | CLOSE | 0.0085% | 0.2572 | 0.2574 | - | - | - | - | - |
| BNBUSDT | no |  | -0.0001% | 769.1000 | 769.6000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0012% | 84,222.0000 | 84,260.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0059% | 0.0904 | 0.0904 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0048% | 2,617.5000 | 2,618.5100 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0030% | 118.7200 | 118.8000 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 163.6000 | 163.6200 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 169.4600 | 163.1900 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0045% | 1.4700 | 1.4709 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0070% | 1,322.3800 | 1,322.7400 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
