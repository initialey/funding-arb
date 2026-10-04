# Paper trading status

Run #79 at 2026-10-04 05:43 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SANDUSDT, BNBUSDT, WLDUSDT, DOGEUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,959.21 USDT |
| return since start | -0.41% (26.5 days) |
| annualised | -5.62% |
| realized (closed pairs) | -39.66 USDT |
| funding received this run | 0.1005 USDT |
| open pairs | 2 / 10 |
| free cash | 7,960.34 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 4.8803 | 4.8790 | 0.0519 | -0.0499 | 0.54% | 9.3508 | 91.6% |
| ZECUSDT | yes |  | 0.0100% | 1,341.1200 | 1,341.9600 | 0.2372 | 0.1283 | 0.47% | 2,748.8557 | 105.0% |
| BNBUSDT | no |  | 0.0007% | 787.0000 | 787.2000 | - | - | - | - | - |
| BTCUSDT | no |  | -0.0003% | 84,863.1500 | 84,904.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0049% | 0.0929 | 0.0929 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0020% | 2,694.9800 | 2,695.9600 | - | - | - | - | - |
| SANDUSDT | no |  | -0.5071% | 0.0780 | 0.0783 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0006% | 120.9400 | 120.9900 | - | - | - | - | - |
| WLDUSDT | no |  | 0.0077% | 0.5928 | 0.5932 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0008% | 1.4920 | 1.4926 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
