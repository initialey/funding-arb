# Paper trading status

Run #208 at 2026-11-20 16:54 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ANTUSDT, SOXSUSDT, DOGEUSDT, ZECUSDT, QQQUSDT, MUUSDT.

| metric | value |
|---|---|
| equity | 9,899.87 USDT |
| return since start | -1.00% (74.0 days) |
| annualised | -4.94% |
| realized (closed pairs) | -100.48 USDT |
| funding received this run | 0.2068 USDT |
| open pairs | 2 / 10 |
| free cash | 7,899.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0179% | 5.7864 | 5.7894 | 1.7623 | 0.0927 | inf% | 5.5692 | -3.8% |
| MUUSDT | yes | OPEN | 0.0108% | 605.5900 | 606.5100 | 0.0000 | 0.0000 | 0.50% | 1,205.1542 | 99.0% |
| ANTUSDT | no |  | 0.0000% | 86.0900 | 86.1400 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0014% | 59,442.1000 | 59,468.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | -0.0018% | 0.0540 | 0.0540 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0016% | 1,642.9700 | 1,644.0900 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0009% | 622.9000 | 622.9500 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0009% | 69.3600 | 69.4100 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0014% | 34.1800 | 34.1400 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 79.0700 | 79.2200 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0077% | 764.2400 | 764.2000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
