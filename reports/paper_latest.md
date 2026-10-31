# Paper trading status

Run #159 at 2026-10-31 14:28 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, DOGEUSDT, XRPUSDT, QQQUSDT, PEPEUSDT, INTCUSDT.

| metric | value |
|---|---|
| equity | 9,921.75 USDT |
| return since start | -0.78% (53.9 days) |
| annualised | -5.30% |
| realized (closed pairs) | -75.47 USDT |
| funding received this run | 0.0521 USDT |
| open pairs | 3 / 10 |
| free cash | 6,924.53 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BTCUSDT | yes | OPEN | 0.0100% | 77,399.2000 | 77,406.7000 | 0.0000 | 0.0000 | 0.50% | 154,028.2587 | 99.0% |
| INTCUSDT | yes |  | 0.0162% | 64.9700 | 64.9800 | 0.2387 | -0.7354 | 0.48% | 132.0199 | 103.2% |
| ZECUSDT | yes |  | 0.0100% | 1,279.9000 | 1,279.6900 | 0.1033 | -0.1407 | 0.54% | 2,443.6418 | 90.9% |
| DOGEUSDT | no |  | 0.0040% | 0.0752 | 0.0753 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0033% | 2,247.9400 | 2,248.8600 | - | - | - | - | - |
| PEPEUSDT | no |  | -0.0204% | 0.0000 | 0.0000 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0085% | 694.8700 | 694.9300 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0026% | 95.5500 | 95.5800 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 77.3400 | 77.3500 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0002% | 1.2455 | 1.2459 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
