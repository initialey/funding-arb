# Paper trading status

Run #2 at 2026-09-08 04:27 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, WLDUSDT, SUIUSDT, ADAUSDT, OPENAIUSDT.

| metric | value |
|---|---|
| equity | 9,997.81 USDT |
| return since start | -0.02% (0.4 days) |
| annualised | n/a (<1 day) |
| realized (closed pairs) | -1.39 USDT |
| funding received this run | 0.0743 USDT |
| open pairs | 1 / 10 |
| free cash | 8,998.61 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes |  | 0.0100% | 744.9000 | 745.1000 | 0.0503 | -0.1024 | 0.51% | 1,474.5274 | 97.9% |
| ADAUSDT | no | CLOSE | 0.0083% | 0.2178 | 0.2179 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0011% | 78,812.9000 | 78,844.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0093% | 0.0898 | 0.0898 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0066% | 2,482.8500 | 2,483.6800 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,471.1100 | 903.4000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0064% | 103.2200 | 103.2600 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0030% | 0.8191 | 0.8195 | - | - | - | - | - |
| WLDUSDT | no |  | 0.0053% | 0.4708 | 0.4709 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0064% | 1.3951 | 1.3956 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0078% | 1,128.1800 | 1,127.9100 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
