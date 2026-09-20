# Paper trading status

Run #38 at 2026-09-20 04:47 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, AVAXUSDT, UNIUSDT, ADAUSDT, ONEUSDT.

| metric | value |
|---|---|
| equity | 9,987.25 USDT |
| return since start | -0.13% (12.5 days) |
| annualised | -3.73% |
| realized (closed pairs) | -9.56 USDT |
| funding received this run | 0.2612 USDT |
| open pairs | 6 / 10 |
| free cash | 3,990.44 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | yes |  | 0.0100% | 0.2209 | 0.2211 | 0.0996 | 0.0944 | 0.48% | 0.4496 | 103.5% |
| AVAXUSDT | yes | OPEN | 0.0100% | 9.5800 | 9.5830 | 0.0000 | 0.0000 | 0.50% | 19.0647 | 99.0% |
| NEARUSDT | yes |  | 0.0100% | 3.4770 | 3.4800 | 0.2534 | 0.3635 | 0.47% | 7.1514 | 105.7% |
| SOLUSDT | yes |  | 0.0100% | 108.8300 | 108.8700 | 0.1471 | 0.0061 | 0.47% | 224.2587 | 106.1% |
| UNIUSDT | yes |  | 0.0100% | 8.8160 | 8.8150 | 0.1995 | -0.0004 | 0.49% | 17.6697 | 100.4% |
| XRPUSDT | yes |  | 0.0100% | 1.3800 | 1.3802 | 0.1501 | 0.0016 | 0.48% | 2.8098 | 103.6% |
| BNBUSDT | no | CLOSE | 0.0078% | 747.4500 | 748.0000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0080% | 80,347.1000 | 80,379.3000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0099% | 0.0854 | 0.0854 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0053% | 2,578.5600 | 2,579.6400 | - | - | - | - | - |
| ONEUSDT | no |  | -0.3805% | 0.0037 | 0.0040 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0009% | 1,453.2100 | 1,453.4800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
