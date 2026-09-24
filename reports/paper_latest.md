# Paper trading status

Run #51 at 2026-09-24 13:30 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, NEARUSDT, UNIUSDT, BCHUSDT, SPCXUSDT.

| metric | value |
|---|---|
| equity | 9,976.76 USDT |
| return since start | -0.23% (16.8 days) |
| annualised | -5.04% |
| realized (closed pairs) | -22.81 USDT |
| funding received this run | 0.0640 USDT |
| open pairs | 1 / 10 |
| free cash | 8,977.19 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BCHUSDT | yes |  | 0.0100% | 335.2400 | 335.5700 | 0.1450 | 0.1715 | 0.45% | 703.3433 | 109.8% |
| BTCUSDT | no |  | 0.0045% | 83,824.1000 | 83,845.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0003% | 0.0939 | 0.0939 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0040% | 2,661.9700 | 2,663.4400 | - | - | - | - | - |
| NEARUSDT | no | CLOSE | 0.0051% | 4.4826 | 4.4850 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0011% | 114.6100 | 114.6700 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 147.2900 | 141.1400 | - | - | - | - | - |
| UNIUSDT | no |  | 0.0080% | 9.1450 | 9.1530 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0025% | 1.4953 | 1.4967 | - | - | - | - | - |
| ZECUSDT | no | CLOSE | 0.0095% | 1,506.7500 | 1,507.3400 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
