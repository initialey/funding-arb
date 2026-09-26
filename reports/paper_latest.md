# Paper trading status

Run #58 at 2026-09-26 19:11 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, XRPUSDT, ZECUSDT, WLDUSDT, DOGEUSDT, NEARUSDT, SUIUSDT, LTCUSDT.

| metric | value |
|---|---|
| equity | 9,971.02 USDT |
| return since start | -0.29% (19.1 days) |
| annualised | -5.55% |
| realized (closed pairs) | -27.48 USDT |
| funding received this run | 0.0015 USDT |
| open pairs | 2 / 10 |
| free cash | 7,972.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| WLDUSDT | yes | OPEN | 0.0100% | 0.5343 | 0.5342 | 0.0000 | 0.0000 | 0.50% | 1.0633 | 99.0% |
| ZECUSDT | yes | OPEN | 0.0100% | 1,563.0300 | 1,563.6300 | 0.0000 | 0.0000 | 0.50% | 3,110.5075 | 99.0% |
| BTCUSDT | no |  | -0.0019% | 83,968.0000 | 84,017.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0051% | 0.0972 | 0.0973 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0065% | 2,684.7700 | 2,686.0000 | - | - | - | - | - |
| LTCUSDT | no |  | 0.0049% | 71.9000 | 71.9200 | - | - | - | - | - |
| NEARUSDT | no | CLOSE | 0.0068% | 4.8330 | 4.8360 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0016% | 121.2400 | 121.3000 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0092% | 1.1623 | 1.1630 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0095% | 1.5246 | 1.5252 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
