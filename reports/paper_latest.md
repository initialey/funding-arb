# Paper trading status

Run #98 at 2026-10-10 20:01 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, XRPUSDT, ZECUSDT, MAGICUSDT, NEARUSDT, ADAUSDT, WLDUSDT, DOGEUSDT.

| metric | value |
|---|---|
| equity | 9,944.42 USDT |
| return since start | -0.56% (33.1 days) |
| annualised | -6.13% |
| realized (closed pairs) | -54.83 USDT |
| funding received this run | -3.9609 USDT |
| open pairs | 1 / 10 |
| free cash | 8,945.17 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | yes | OPEN | 0.0100% | 0.2525 | 0.2527 | 0.0000 | 0.0000 | 0.50% | 0.5025 | 99.0% |
| BTCUSDT | no |  | 0.0014% | 83,044.0000 | 83,085.4000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0013% | 0.0860 | 0.0861 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0029% | 2,512.2400 | 2,513.4000 | - | - | - | - | - |
| MAGICUSDT | no | CLOSE | -0.2680% | 0.1000 | 0.1003 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0096% | 5.3139 | 5.3160 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0001% | 110.3700 | 110.4200 | - | - | - | - | - |
| WLDUSDT | no |  | 0.0068% | 0.5615 | 0.5618 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0022% | 1.4044 | 1.4051 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0055% | 1,224.7200 | 1,225.1200 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
