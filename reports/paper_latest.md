# Paper trading status

Run #25 at 2026-09-15 19:40 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, XRPUSDT, ZECUSDT, OPENAIUSDT, BNBUSDT, DOGEUSDT, SOXLUSDT, BZUSDT.

| metric | value |
|---|---|
| equity | 9,992.24 USDT |
| return since start | -0.08% (8.1 days) |
| annualised | -3.51% |
| realized (closed pairs) | -7.20 USDT |
| funding received this run | 0.0336 USDT |
| open pairs | 1 / 10 |
| free cash | 8,992.80 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes |  | 0.0100% | 0.3820 | 0.3820 | 0.6212 | -0.4326 | 0.25% | 1.1328 | 196.5% |
| BNBUSDT | no |  | 0.0036% | 719.5000 | 719.8000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0061% | 76,019.3000 | 76,054.4000 | - | - | - | - | - |
| BZUSDT | no |  | -0.0709% | 103.0500 | 103.0300 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0033% | 0.0809 | 0.0809 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0034% | 2,408.4400 | 2,409.5700 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,442.7900 | 872.8000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0011% | 97.9500 | 97.9900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 102.1900 | 102.1900 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0064% | 1.3048 | 1.3056 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0039% | 1,139.3900 | 1,140.0000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
