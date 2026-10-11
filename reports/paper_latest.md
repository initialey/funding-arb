# Paper trading status

Run #100 at 2026-10-11 14:52 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, XRPUSDT, ZECUSDT, MAGICUSDT, NEARUSDT, CFXUSDT, WLDUSDT, ADAUSDT.

| metric | value |
|---|---|
| equity | 9,941.86 USDT |
| return since start | -0.58% (33.9 days) |
| annualised | -6.26% |
| realized (closed pairs) | -57.39 USDT |
| funding received this run | 0.0414 USDT |
| open pairs | 1 / 10 |
| free cash | 8,942.61 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes | OPEN | 0.0100% | 5.3360 | 5.3380 | 0.0000 | 0.0000 | 0.50% | 10.6189 | 99.0% |
| ADAUSDT | no |  | 0.0077% | 0.2483 | 0.2485 | - | - | - | - | - |
| BTCUSDT | no |  | -0.0005% | 83,106.1100 | 83,143.4000 | - | - | - | - | - |
| CFXUSDT | no |  | 0.0033% | 0.0706 | 0.0706 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0024% | 2,505.4600 | 2,506.5500 | - | - | - | - | - |
| MAGICUSDT | no |  | -0.4043% | 0.1297 | 0.1295 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0024% | 109.6500 | 109.7000 | - | - | - | - | - |
| WLDUSDT | no | CLOSE | 0.0094% | 0.5681 | 0.5683 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0022% | 1.3998 | 1.4005 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0070% | 1,233.0100 | 1,233.1600 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
