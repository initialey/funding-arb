# Paper trading status

Run #27 at 2026-09-16 13:27 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, OPENAIUSDT, DOGEUSDT, BNBUSDT, ADAUSDT, SPCXUSDT.

| metric | value |
|---|---|
| equity | 9,992.34 USDT |
| return since start | -0.08% (8.8 days) |
| annualised | -3.17% |
| realized (closed pairs) | -7.20 USDT |
| funding received this run | 0.0313 USDT |
| open pairs | 1 / 10 |
| free cash | 8,992.80 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes |  | 0.0100% | 0.3562 | 0.3562 | 0.6846 | -0.3963 | 0.23% | 1.1328 | 218.0% |
| ADAUSDT | no |  | 0.0067% | 0.1926 | 0.1929 | - | - | - | - | - |
| BNBUSDT | no |  | 0.0044% | 712.0000 | 712.3000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0040% | 75,780.4500 | 75,814.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0049% | 0.0792 | 0.0792 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0006% | 2,402.1000 | 2,402.9000 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,490.8300 | 897.5000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0051% | 97.3600 | 97.4000 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 144.9000 | 138.5600 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0035% | 1.2783 | 1.2789 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0060% | 1,233.2600 | 1,233.1800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
