# Paper trading status

Run #88 at 2026-10-07 15:30 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, SOXLUSDT, BNBUSDT, ADAUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,955.51 USDT |
| return since start | -0.44% (29.9 days) |
| annualised | -5.43% |
| realized (closed pairs) | -44.62 USDT |
| funding received this run | 0.0533 USDT |
| open pairs | 1 / 10 |
| free cash | 8,955.38 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 5.0081 | 5.0100 | 0.5871 | 0.2930 | 0.57% | 9.3508 | 86.7% |
| ADAUSDT | no |  | 0.0032% | 0.2533 | 0.2535 | - | - | - | - | - |
| BNBUSDT | no |  | -0.0026% | 766.8000 | 767.3000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0003% | 83,071.7000 | 83,105.0000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0068% | 0.0883 | 0.0883 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0030% | 2,561.2700 | 2,562.1100 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0026% | 116.1600 | 116.1900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 155.4500 | 155.4600 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0030% | 1.4250 | 1.4258 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0070% | 1,317.4100 | 1,317.4800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
