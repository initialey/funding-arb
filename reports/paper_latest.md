# Paper trading status

Run #207 at 2026-11-20 07:01 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ANTUSDT, SOXSUSDT, DOGEUSDT, ZECUSDT, QQQUSDT, OPENAIUSDT.

| metric | value |
|---|---|
| equity | 9,900.79 USDT |
| return since start | -0.99% (73.5 days) |
| annualised | -4.92% |
| realized (closed pairs) | -100.48 USDT |
| funding received this run | 0.3187 USDT |
| open pairs | 1 / 10 |
| free cash | 8,899.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0179% | 5.3108 | 5.3157 | 1.5555 | 0.4684 | 9.28% | 5.5692 | 4.9% |
| ANTUSDT | no |  | 0.0000% | 91.5000 | 91.5100 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0031% | 61,986.3700 | 62,012.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0042% | 0.0577 | 0.0577 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0044% | 1,748.7900 | 1,749.7400 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,232.8700 | 724.4000 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0014% | 640.2500 | 640.1600 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0001% | 72.8500 | 72.8600 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 42.5400 | 42.5800 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 67.0700 | 67.0200 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0090% | 857.2600 | 857.7400 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
