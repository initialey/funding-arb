# Paper trading status

Run #37 at 2026-09-19 18:34 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, UNIUSDT, ADAUSDT, BNBUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,987.83 USDT |
| return since start | -0.12% (12.0 days) |
| annualised | -3.69% |
| realized (closed pairs) | -8.48 USDT |
| funding received this run | 0.2994 USDT |
| open pairs | 6 / 10 |
| free cash | 3,991.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | yes |  | 0.0100% | 0.2291 | 0.2292 | 0.0507 | -0.0259 | 0.51% | 0.4496 | 96.2% |
| BNBUSDT | yes |  | 0.0100% | 762.2000 | 762.6000 | 0.1500 | 0.1312 | 0.50% | 1,520.9950 | 99.6% |
| NEARUSDT | yes |  | 0.0100% | 3.6200 | 3.6200 | 0.2051 | -0.0561 | 0.51% | 7.1514 | 97.6% |
| SOLUSDT | yes |  | 0.0100% | 110.9800 | 111.0000 | 0.0989 | -0.0860 | 0.49% | 224.2587 | 102.1% |
| UNIUSDT | yes |  | 0.0100% | 8.6390 | 8.6390 | 0.1499 | 0.0548 | 0.47% | 17.6697 | 104.5% |
| XRPUSDT | yes |  | 0.0100% | 1.4267 | 1.4270 | 0.1012 | 0.0347 | 0.51% | 2.8098 | 96.9% |
| BTCUSDT | no |  | 0.0072% | 81,408.8000 | 81,444.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0099% | 0.0896 | 0.0896 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0067% | 2,637.9200 | 2,639.0100 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0017% | 1,480.5700 | 1,480.5700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
