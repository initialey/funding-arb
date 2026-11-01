# Paper trading status

Run #163 at 2026-11-01 20:27 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, BNBUSDT, XRPUSDT, UNIUSDT, SOXLUSDT, PEPEUSDT.

| metric | value |
|---|---|
| equity | 9,918.62 USDT |
| return since start | -0.81% (55.1 days) |
| annualised | -5.39% |
| realized (closed pairs) | -80.20 USDT |
| funding received this run | 0.0485 USDT |
| open pairs | 2 / 10 |
| free cash | 7,919.80 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 4.2489 | 4.2510 | 0.0984 | 0.2176 | 0.47% | 8.7160 | 105.1% |
| UNIUSDT | yes | OPEN | 0.0100% | 7.1240 | 7.1230 | 0.0000 | 0.0000 | 0.50% | 14.1771 | 99.0% |
| BNBUSDT | no |  | 0.0060% | 707.8500 | 708.3000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0085% | 77,729.3000 | 77,759.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0065% | 0.0750 | 0.0751 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0012% | 2,256.1800 | 2,257.1400 | - | - | - | - | - |
| PEPEUSDT | no |  | 0.0061% | 0.0000 | 0.0000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0087% | 93.9700 | 94.0100 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0035% | 77.6800 | 77.6600 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0040% | 1.2469 | 1.2475 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0092% | 1,214.3300 | 1,214.9800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
