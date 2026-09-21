# Paper trading status

Run #42 at 2026-09-21 15:04 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, SUIUSDT, OPENAIUSDT, NEARUSDT, ADAUSDT.

| metric | value |
|---|---|
| equity | 9,985.60 USDT |
| return since start | -0.14% (13.9 days) |
| annualised | -3.78% |
| realized (closed pairs) | -12.13 USDT |
| funding received this run | 0.2620 USDT |
| open pairs | 5 / 10 |
| free cash | 4,987.87 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | yes |  | 0.0100% | 0.2451 | 0.2452 | 0.3047 | -0.0668 | 0.59% | 0.4496 | 83.4% |
| SOLUSDT | yes |  | 0.0100% | 118.6400 | 118.5100 | 0.3461 | -0.7634 | 0.56% | 224.2587 | 89.0% |
| UNIUSDT | yes |  | 0.0100% | 8.8500 | 8.8530 | 0.3963 | 0.2251 | 0.50% | 17.6697 | 99.7% |
| XRPUSDT | yes |  | 0.0100% | 1.5003 | 1.5014 | 0.3522 | 0.3142 | 0.57% | 2.8098 | 87.3% |
| ZECUSDT | yes |  | 0.0100% | 1,515.7700 | 1,516.5300 | 0.1553 | 0.2218 | 0.54% | 2,894.6866 | 91.0% |
| BTCUSDT | no |  | 0.0050% | 85,900.8200 | 85,960.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0072% | 0.0976 | 0.0976 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0001% | 2,737.9800 | 2,739.1700 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0092% | 4.0905 | 4.0890 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,599.6400 | 903.2000 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0047% | 1.0369 | 1.0369 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
