# Paper trading status

Run #211 at 2026-11-21 21:37 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, DOGEUSDT, UNIUSDT, SOXSUSDT, XRPUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,895.81 USDT |
| return since start | -1.04% (75.2 days) |
| annualised | -5.06% |
| realized (closed pairs) | -102.48 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 3 / 10 |
| free cash | 6,897.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0100% | 6.4337 | 6.4274 | 2.0924 | -1.6178 | inf% | 5.5692 | -13.4% |
| QQQUSDT | yes |  | 0.0119% | 623.8900 | 623.9000 | 0.0000 | -0.0000 | 0.50% | 1,240.2189 | 98.8% |
| SOXSUSDT | yes |  | 0.0157% | 77.6100 | 77.6000 | 0.0000 | 0.0628 | 0.49% | 155.7612 | 100.7% |
| BTCUSDT | no |  | -0.0039% | 60,380.3000 | 60,415.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0013% | 0.0552 | 0.0552 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0083% | 1,685.4400 | 1,686.1200 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0140% | 70.4500 | 70.4900 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0079% | 32.9800 | 32.9800 | - | - | - | - | - |
| UNIUSDT | no |  | -0.0091% | 4.7150 | 4.7170 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0021% | 0.9298 | 0.9304 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0011% | 792.9500 | 793.2300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
