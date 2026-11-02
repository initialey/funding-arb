# Paper trading status

Run #165 at 2026-11-02 18:13 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, DOGEUSDT, XRPUSDT, BZUSDT, QQQUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,917.05 USDT |
| return since start | -0.83% (56.0 days) |
| annualised | -5.41% |
| realized (closed pairs) | -81.13 USDT |
| funding received this run | 0.5161 USDT |
| open pairs | 4 / 10 |
| free cash | 5,918.87 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| QQQUSDT | yes |  | 0.0270% | 693.2900 | 693.2900 | 0.2881 | -0.0071 | 0.49% | 1,391.3433 | 100.7% |
| SOLUSDT | yes | OPEN | 0.0100% | 92.3100 | 92.3200 | 0.0000 | 0.0000 | 0.50% | 183.7015 | 99.0% |
| UNIUSDT | yes |  | 0.0100% | 7.1650 | 7.1660 | 0.1515 | 0.1408 | 0.51% | 14.1771 | 97.9% |
| ZECUSDT | yes |  | 0.0100% | 1,187.9900 | 1,188.2700 | 0.0933 | 0.5168 | 0.44% | 2,534.5672 | 113.3% |
| BNBUSDT | no |  | 0.0095% | 700.6000 | 700.8000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0079% | 77,262.2900 | 77,285.2000 | - | - | - | - | - |
| BZUSDT | no |  | -0.0023% | 103.6500 | 103.6200 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0091% | 0.0741 | 0.0742 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0072% | 2,261.7800 | 2,262.8600 | - | - | - | - | - |
| NEARUSDT | no | CLOSE | 0.0059% | 3.9421 | 3.9450 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 74.2100 | 74.1600 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0079% | 1.2430 | 1.2438 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
