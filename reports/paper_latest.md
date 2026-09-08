# Paper trading status

Run #3 at 2026-09-08 12:50 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, BNBUSDT, SUIUSDT, WLDUSDT, OPENAIUSDT.

| metric | value |
|---|---|
| equity | 9,997.85 USDT |
| return since start | -0.02% (0.8 days) |
| annualised | n/a (<1 day) |
| realized (closed pairs) | -1.39 USDT |
| funding received this run | 0.0507 USDT |
| open pairs | 1 / 10 |
| free cash | 8,998.61 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes |  | 0.0100% | 751.4000 | 751.6000 | 0.1010 | -0.1045 | 0.51% | 1,474.5274 | 96.2% |
| BTCUSDT | no |  | 0.0026% | 78,328.6500 | 78,359.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0070% | 0.0892 | 0.0893 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0075% | 2,471.9700 | 2,473.2300 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,523.2500 | 933.0000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0064% | 103.1600 | 103.1800 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0030% | 0.8129 | 0.8131 | - | - | - | - | - |
| WLDUSDT | no |  | 0.0078% | 0.4742 | 0.4746 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0070% | 1.3970 | 1.3975 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0078% | 1,159.5400 | 1,160.1200 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
