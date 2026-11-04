# Paper trading status

Run #170 at 2026-11-04 16:13 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, SOXSUSDT, INTCUSDT, XRPUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,911.84 USDT |
| return since start | -0.88% (57.9 days) |
| annualised | -5.55% |
| realized (closed pairs) | -86.52 USDT |
| funding received this run | 0.1675 USDT |
| open pairs | 3 / 10 |
| free cash | 6,913.48 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| SOLUSDT | yes | OPEN | 0.0100% | 97.2000 | 97.2300 | 0.0000 | 0.0000 | 0.50% | 193.4328 | 99.0% |
| UNIUSDT | yes |  | 0.0100% | 7.7760 | 7.7770 | 0.4637 | 0.1468 | 0.60% | 14.1771 | 82.3% |
| XRPUSDT | yes | OPEN | 0.0100% | 1.3197 | 1.3199 | 0.0000 | 0.0000 | 0.50% | 2.6263 | 99.0% |
| BTCUSDT | no | CLOSE | 0.0066% | 80,614.1000 | 80,639.3000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0052% | 0.0777 | 0.0778 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0075% | 2,442.0400 | 2,443.0600 | - | - | - | - | - |
| INTCUSDT | no |  | 0.0076% | 57.9700 | 57.9600 | - | - | - | - | - |
| QQQUSDT | no | CLOSE | 0.0048% | 695.1000 | 695.1900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 65.7300 | 65.6500 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 59.2100 | 59.1900 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0099% | 1,319.0900 | 1,318.5200 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
