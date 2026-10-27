# Paper trading status

Run #148 at 2026-10-27 20:38 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, DOGEUSDT, BNBUSDT, QQQUSDT, SNXXUSDT.

| metric | value |
|---|---|
| equity | 9,926.40 USDT |
| return since start | -0.74% (50.1 days) |
| annualised | -5.36% |
| realized (closed pairs) | -73.02 USDT |
| funding received this run | 0.0507 USDT |
| open pairs | 1 / 10 |
| free cash | 8,926.98 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes |  | 0.0100% | 746.6500 | 747.0000 | 0.1010 | 0.0656 | 0.51% | 1,466.1692 | 96.4% |
| BTCUSDT | no |  | 0.0094% | 80,605.4100 | 80,635.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0038% | 0.0782 | 0.0782 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0081% | 2,340.8100 | 2,342.1000 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0000% | 722.1200 | 722.1500 | - | - | - | - | - |
| SNXXUSDT | no |  | 0.0000% | 8.8870 | 8.8910 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0067% | 100.9200 | 100.9400 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 98.8700 | 98.8700 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0090% | 1.3197 | 1.3203 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0063% | 1,293.2000 | 1,293.9100 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
