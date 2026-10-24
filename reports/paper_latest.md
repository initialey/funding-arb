# Paper trading status

Run #138 at 2026-10-24 12:37 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, SOXLUSDT, NEARUSDT, BNBUSDT, LTCUSDT.

| metric | value |
|---|---|
| equity | 9,927.80 USDT |
| return since start | -0.72% (46.8 days) |
| annualised | -5.63% |
| realized (closed pairs) | -71.71 USDT |
| funding received this run | 0.0495 USDT |
| open pairs | 1 / 10 |
| free cash | 8,928.29 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes |  | 0.0100% | 731.9500 | 732.5000 | 0.0495 | 0.2045 | 0.49% | 1,471.1443 | 101.0% |
| BTCUSDT | no |  | 0.0068% | 80,773.8000 | 80,806.3000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0008% | 0.0776 | 0.0777 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0076% | 2,369.8000 | 2,370.7700 | - | - | - | - | - |
| LTCUSDT | no |  | -0.0008% | 56.5500 | 56.5800 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0050% | 4.4943 | 4.4950 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0084% | 101.6400 | 101.6800 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 84.3300 | 84.3400 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0064% | 1.2862 | 1.2869 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0077% | 1,160.1100 | 1,160.6000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
