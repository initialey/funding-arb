# Paper trading status

Run #84 at 2026-10-06 06:12 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SPCXUSDT, XRPUSDT, ADAUSDT, NEARUSDT, SOXLUSDT, DOGEUSDT.

| metric | value |
|---|---|
| equity | 9,955.96 USDT |
| return since start | -0.44% (28.5 days) |
| annualised | -5.64% |
| realized (closed pairs) | -42.50 USDT |
| funding received this run | 0.1746 USDT |
| open pairs | 3 / 10 |
| free cash | 6,957.50 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | yes |  | 0.0100% | 0.2682 | 0.2683 | 0.0508 | -0.2131 | 0.52% | 0.5256 | 96.0% |
| NEARUSDT | yes |  | 0.0100% | 5.1663 | 5.1660 | 0.3705 | 0.0617 | 0.61% | 9.3508 | 81.0% |
| ZECUSDT | yes |  | 0.0100% | 1,321.4900 | 1,321.7200 | 0.5232 | -0.0899 | 0.46% | 2,748.8557 | 108.0% |
| BTCUSDT | no |  | 0.0010% | 85,205.7100 | 85,251.0000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0052% | 0.0942 | 0.0942 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0025% | 2,692.2700 | 2,693.4500 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0027% | 119.3000 | 119.2900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 164.8900 | 164.9100 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 172.6100 | 167.6100 | - | - | - | - | - |
| XRPUSDT | no | CLOSE | 0.0081% | 1.4920 | 1.4929 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
