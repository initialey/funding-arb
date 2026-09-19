# Paper trading status

Run #35 at 2026-09-19 04:31 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, UNIUSDT, OPENAIUSDT, DOGEUSDT, NEARUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,988.03 USDT |
| return since start | -0.12% (11.4 days) |
| annualised | -3.82% |
| realized (closed pairs) | -8.48 USDT |
| funding received this run | 0.1515 USDT |
| open pairs | 5 / 10 |
| free cash | 4,991.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes |  | 0.0100% | 762.6500 | 762.8000 | 0.0499 | -0.0324 | 0.50% | 1,520.9950 | 99.4% |
| NEARUSDT | yes |  | 0.0100% | 3.7218 | 3.7220 | 0.1041 | -0.0298 | 0.54% | 7.1514 | 92.2% |
| SOLUSDT | yes | OPEN | 0.0100% | 112.6900 | 112.7300 | 0.0000 | 0.0000 | 0.50% | 224.2587 | 99.0% |
| UNIUSDT | yes |  | 0.0100% | 8.8390 | 8.8400 | 0.0498 | 0.1124 | 0.50% | 17.6697 | 99.9% |
| XRPUSDT | yes | OPEN | 0.0100% | 1.4119 | 1.4121 | 0.0000 | 0.0000 | 0.50% | 2.8098 | 99.0% |
| BTCUSDT | no |  | 0.0062% | 81,054.7700 | 81,088.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0092% | 0.0875 | 0.0875 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0072% | 2,621.6200 | 2,622.6300 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,498.9300 | 883.3000 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0094% | 1,535.7300 | 1,536.3600 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
