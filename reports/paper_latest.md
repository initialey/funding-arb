# Paper trading status

Run #23 at 2026-09-15 04:46 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SOXLUSDT, BNBUSDT, DOGEUSDT, OPENAIUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,992.10 USDT |
| return since start | -0.08% (7.5 days) |
| annualised | -3.87% |
| realized (closed pairs) | -7.20 USDT |
| funding received this run | 0.0367 USDT |
| open pairs | 1 / 10 |
| free cash | 8,992.80 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes |  | 0.0118% | 0.4182 | 0.4181 | 0.5542 | -0.4974 | 0.29% | 1.1328 | 170.9% |
| BNBUSDT | no |  | 0.0046% | 720.5000 | 720.7000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0059% | 77,597.1000 | 77,632.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0013% | 0.0832 | 0.0833 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0048% | 2,492.8900 | 2,494.3400 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,449.6000 | 880.5000 | - | - | - | - | - |
| QQQUSDT | no |  | -0.0094% | 708.4900 | 708.5300 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0026% | 101.3200 | 101.3700 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 101.7800 | 101.7900 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0050% | 1.4155 | 1.4163 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0002% | 1,147.9400 | 1,148.0200 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
