# Paper trading status

Run #178 at 2026-11-07 20:10 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, DOGEUSDT, OPENAIUSDT, ONEUSDT, SOXSUSDT.

| metric | value |
|---|---|
| equity | 9,905.41 USDT |
| return since start | -0.95% (61.1 days) |
| annualised | -5.65% |
| realized (closed pairs) | -94.89 USDT |
| funding received this run | 0.2904 USDT |
| open pairs | 1 / 10 |
| free cash | 8,905.11 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ZECUSDT | yes |  | 0.0272% | 1,264.8600 | 1,266.7500 | 0.4364 | 0.6156 | 0.44% | 2,674.1692 | 111.4% |
| BTCUSDT | no |  | 0.0069% | 75,761.7000 | 75,787.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0070% | 0.0717 | 0.0718 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0033% | 2,233.8500 | 2,234.6200 | - | - | - | - | - |
| ONEUSDT | no |  | -0.0165% | 0.0023 | 0.0023 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,296.7800 | 767.9000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0079% | 89.6300 | 89.6500 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 46.3400 | 46.3400 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 70.6000 | 70.5900 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0061% | 1.1621 | 1.1627 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
