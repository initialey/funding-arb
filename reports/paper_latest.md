# Paper trading status

Run #41 at 2026-09-21 04:48 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, AVAXUSDT, DOGEUSDT, NEARUSDT, OPENAIUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,985.71 USDT |
| return since start | -0.14% (13.5 days) |
| annualised | -3.87% |
| realized (closed pairs) | -12.13 USDT |
| funding received this run | 0.2532 USDT |
| open pairs | 5 / 10 |
| free cash | 4,987.87 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | yes |  | 0.0100% | 0.2323 | 0.2324 | 0.2505 | 0.0367 | 0.53% | 0.4496 | 93.5% |
| SOLUSDT | yes |  | 0.0100% | 111.5700 | 111.6000 | 0.2935 | -0.0426 | 0.49% | 224.2587 | 101.0% |
| UNIUSDT | yes |  | 0.0100% | 8.7680 | 8.7690 | 0.3465 | 0.1119 | 0.49% | 17.6697 | 101.5% |
| XRPUSDT | yes |  | 0.0100% | 1.4205 | 1.4211 | 0.2991 | 0.1412 | 0.51% | 2.8098 | 97.8% |
| ZECUSDT | yes |  | 0.0100% | 1,530.2100 | 1,530.4900 | 0.1032 | 0.0565 | 0.55% | 2,894.6866 | 89.2% |
| AVAXUSDT | no |  | 0.0069% | 11.5650 | 11.5750 | - | - | - | - | - |
| BNBUSDT | no |  | 0.0088% | 774.7500 | 775.0000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0060% | 81,414.0200 | 81,441.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0037% | 0.0884 | 0.0884 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0022% | 2,666.0500 | 2,667.5100 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0092% | 4.4091 | 4.4190 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,551.6800 | 894.1000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
