# Paper trading status

Run #26 at 2026-09-16 04:43 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, XRPUSDT, ZECUSDT, OPENAIUSDT, DOGEUSDT, BNBUSDT, SOXLUSDT, SPCXUSDT.

| metric | value |
|---|---|
| equity | 9,992.12 USDT |
| return since start | -0.08% (8.5 days) |
| annualised | -3.40% |
| realized (closed pairs) | -7.20 USDT |
| funding received this run | 0.0320 USDT |
| open pairs | 1 / 10 |
| free cash | 8,992.80 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes |  | 0.0100% | 0.3647 | 0.3645 | 0.6533 | -0.5809 | 0.24% | 1.1328 | 210.6% |
| BNBUSDT | no |  | 0.0041% | 715.6000 | 715.8000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0055% | 75,972.9500 | 76,003.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0055% | 0.0805 | 0.0806 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0011% | 2,408.3700 | 2,409.6500 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,452.0900 | 865.0000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0046% | 97.5400 | 97.5900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 104.3600 | 104.3800 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 144.1300 | 137.6400 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0048% | 1.3073 | 1.3082 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0093% | 1,147.3800 | 1,147.7000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
