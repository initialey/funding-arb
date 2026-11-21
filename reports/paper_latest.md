# Paper trading status

Run #209 at 2026-11-21 06:56 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, SOXSUSDT, ANTUSDT, QQQUSDT, MUUSDT.

| metric | value |
|---|---|
| equity | 9,898.13 USDT |
| return since start | -1.02% (74.5 days) |
| annualised | -4.99% |
| realized (closed pairs) | -100.48 USDT |
| funding received this run | 0.1595 USDT |
| open pairs | 2 / 10 |
| free cash | 7,899.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0100% | 6.1227 | 6.1202 | 1.8717 | -0.9154 | inf% | 5.5692 | -9.0% |
| MUUSDT | yes |  | 0.0110% | 605.6500 | 605.4900 | 0.0502 | -0.8904 | 0.50% | 1,205.1542 | 99.0% |
| ANTUSDT | no |  | 0.0000% | 87.0900 | 87.0900 | - | - | - | - | - |
| BTCUSDT | no |  | -0.0016% | 57,699.5000 | 57,733.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | -0.0023% | 0.0536 | 0.0536 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0056% | 1,636.1300 | 1,636.5800 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0016% | 617.6200 | 617.9500 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0068% | 68.0600 | 68.1100 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0014% | 32.7200 | 32.7300 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 78.8000 | 78.8100 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0052% | 731.5700 | 731.9900 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
