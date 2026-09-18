# Paper trading status

Run #34 at 2026-09-18 19:00 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, UNIUSDT, OPENAIUSDT, DOGEUSDT, BNBUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,989.18 USDT |
| return since start | -0.11% (11.0 days) |
| annualised | -3.57% |
| realized (closed pairs) | -8.48 USDT |
| funding received this run | 0.0523 USDT |
| open pairs | 3 / 10 |
| free cash | 6,991.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes | OPEN | 0.0100% | 764.3000 | 764.5000 | 0.0000 | 0.0000 | 0.50% | 1,520.9950 | 99.0% |
| NEARUSDT | yes |  | 0.0100% | 3.7576 | 3.7570 | 0.0523 | -0.1417 | 0.55% | 7.1514 | 90.3% |
| UNIUSDT | yes | OPEN | 0.0100% | 8.8790 | 8.8780 | 0.0000 | 0.0000 | 0.50% | 17.6697 | 99.0% |
| BTCUSDT | no |  | 0.0047% | 80,893.2600 | 80,924.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0086% | 0.0873 | 0.0873 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0056% | 2,610.9300 | 2,612.3500 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,496.4000 | 882.9000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0078% | 112.2600 | 112.2600 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0059% | 1.3864 | 1.3865 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0237% | 1,458.8100 | 1,459.0800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
