# Paper trading status

Run #40 at 2026-09-20 18:43 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, AVAXUSDT, DOGEUSDT, NEARUSDT, UNIUSDT, ONEUSDT.

| metric | value |
|---|---|
| equity | 9,985.54 USDT |
| return since start | -0.14% (13.0 days) |
| annualised | -4.05% |
| realized (closed pairs) | -12.13 USDT |
| funding received this run | 0.2915 USDT |
| open pairs | 5 / 10 |
| free cash | 4,987.87 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | yes |  | 0.0100% | 0.2274 | 0.2276 | 0.1991 | 0.2195 | 0.51% | 0.4496 | 97.7% |
| SOLUSDT | yes |  | 0.0100% | 109.8900 | 109.9300 | 0.2440 | 0.0044 | 0.48% | 224.2587 | 104.1% |
| UNIUSDT | yes |  | 0.0100% | 8.6870 | 8.6850 | 0.2971 | -0.0575 | 0.48% | 17.6697 | 103.4% |
| XRPUSDT | yes |  | 0.0100% | 1.4073 | 1.4079 | 0.2488 | 0.1419 | 0.50% | 2.8098 | 99.7% |
| ZECUSDT | yes |  | 0.0100% | 1,470.7700 | 1,471.0900 | 0.0506 | 0.0718 | 0.51% | 2,894.6866 | 96.8% |
| AVAXUSDT | no |  | 0.0069% | 11.1780 | 11.1980 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0077% | 81,178.5000 | 81,213.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0055% | 0.0869 | 0.0869 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0027% | 2,631.8100 | 2,632.5300 | - | - | - | - | - |
| NEARUSDT | no | CLOSE | 0.0092% | 4.0255 | 4.0270 | - | - | - | - | - |
| ONEUSDT | no |  | -0.4891% | 0.0037 | 0.0047 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
