# Paper trading status

Run #102 at 2026-10-12 05:48 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, NEARUSDT, MAGICUSDT, DOGEUSDT, ADAUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,941.31 USDT |
| return since start | -0.59% (34.5 days) |
| annualised | -6.21% |
| realized (closed pairs) | -57.39 USDT |
| funding received this run | 0.0553 USDT |
| open pairs | 2 / 10 |
| free cash | 7,942.61 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 5.9058 | 5.9090 | 0.1085 | 0.0924 | 0.62% | 10.6189 | 79.8% |
| ZECUSDT | yes | OPEN | 0.0100% | 1,335.5800 | 1,336.1900 | 0.0000 | 0.0000 | 0.50% | 2,657.8706 | 99.0% |
| ADAUSDT | no |  | 0.0082% | 0.2542 | 0.2543 | - | - | - | - | - |
| BNBUSDT | no |  | -0.0004% | 752.7500 | 753.2000 | - | - | - | - | - |
| BTCUSDT | no |  | -0.0007% | 83,948.8900 | 83,991.4000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0067% | 0.0876 | 0.0876 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0008% | 2,562.7400 | 2,563.8600 | - | - | - | - | - |
| MAGICUSDT | no |  | -0.0638% | 0.1203 | 0.1205 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0024% | 112.8500 | 112.9000 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0008% | 1.4135 | 1.4142 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
