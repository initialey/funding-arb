# Paper trading status

Run #101 at 2026-10-11 20:12 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, XRPUSDT, ZECUSDT, NEARUSDT, MAGICUSDT, ADAUSDT, DOGEUSDT, WLDUSDT.

| metric | value |
|---|---|
| equity | 9,941.76 USDT |
| return since start | -0.58% (34.1 days) |
| annualised | -6.23% |
| realized (closed pairs) | -57.39 USDT |
| funding received this run | 0.0531 USDT |
| open pairs | 1 / 10 |
| free cash | 8,942.61 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 5.6715 | 5.6720 | 0.0531 | -0.1523 | 0.57% | 10.6189 | 87.2% |
| ADAUSDT | no |  | 0.0072% | 0.2532 | 0.2534 | - | - | - | - | - |
| BTCUSDT | no |  | -0.0013% | 83,663.0000 | 83,692.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0037% | 0.0869 | 0.0869 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0023% | 2,536.9500 | 2,538.1900 | - | - | - | - | - |
| MAGICUSDT | no |  | -0.1184% | 0.1357 | 0.1358 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0032% | 111.2700 | 111.3100 | - | - | - | - | - |
| WLDUSDT | no |  | 0.0069% | 0.5620 | 0.5623 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0007% | 1.4069 | 1.4077 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0095% | 1,274.9700 | 1,275.6900 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
