# Paper trading status

Run #164 at 2026-11-02 05:53 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, SOXLUSDT, BNBUSDT, XRPUSDT, UNIUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,917.03 USDT |
| return since start | -0.83% (55.5 days) |
| annualised | -5.46% |
| realized (closed pairs) | -80.20 USDT |
| funding received this run | 0.0994 USDT |
| open pairs | 4 / 10 |
| free cash | 5,919.80 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 4.2539 | 4.2550 | 0.1470 | 0.1034 | 0.47% | 8.7160 | 104.9% |
| QQQUSDT | yes | OPEN | 0.0275% | 699.1500 | 699.1600 | 0.0000 | 0.0000 | 0.50% | 1,391.3433 | 99.0% |
| UNIUSDT | yes |  | 0.0100% | 7.2490 | 7.2470 | 0.0509 | -0.0690 | 0.52% | 14.1771 | 95.6% |
| ZECUSDT | yes | OPEN | 0.0100% | 1,273.6200 | 1,272.5100 | 0.0000 | 0.0000 | 0.50% | 2,534.5672 | 99.0% |
| BNBUSDT | no |  | 0.0076% | 710.4500 | 710.9000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0083% | 78,352.3600 | 78,380.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0078% | 0.0759 | 0.0759 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0020% | 2,291.5700 | 2,292.2600 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0096% | 94.9400 | 94.9500 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0035% | 82.3200 | 82.3500 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0057% | 1.2543 | 1.2546 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
