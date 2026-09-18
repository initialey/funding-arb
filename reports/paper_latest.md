# Paper trading status

Run #33 at 2026-09-18 12:56 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, UNIUSDT, OPENAIUSDT, BNBUSDT, DOGEUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,990.77 USDT |
| return since start | -0.09% (10.8 days) |
| annualised | -3.12% |
| realized (closed pairs) | -8.48 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,991.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes | OPEN | 0.0100% | 3.5936 | 3.5940 | 0.0000 | 0.0000 | 0.50% | 7.1514 | 99.0% |
| BNBUSDT | no |  | 0.0083% | 745.9500 | 746.3000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0044% | 78,011.8100 | 78,048.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0073% | 0.0854 | 0.0854 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0039% | 2,502.1700 | 2,503.1100 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,485.1300 | 877.4000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0032% | 105.7700 | 105.8000 | - | - | - | - | - |
| UNIUSDT | no |  | 0.0031% | 8.6160 | 8.6140 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0032% | 1.3237 | 1.3244 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0354% | 1,463.6000 | 1,463.8700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
