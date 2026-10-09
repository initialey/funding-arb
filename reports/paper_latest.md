# Paper trading status

Run #93 at 2026-10-09 06:00 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SOXLUSDT, DOGEUSDT, ADAUSDT, NEARUSDT, SOXSUSDT.

| metric | value |
|---|---|
| equity | 9,953.62 USDT |
| return since start | -0.46% (31.5 days) |
| annualised | -5.37% |
| realized (closed pairs) | -46.38 USDT |
| funding received this run | 0.0217 USDT |
| open pairs | 0 / 10 |
| free cash | 9,953.62 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | no |  | -0.0030% | 0.2374 | 0.2377 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0017% | 82,337.4000 | 82,378.0000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0019% | 0.0852 | 0.0852 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0014% | 2,490.8700 | 2,492.0600 | - | - | - | - | - |
| NEARUSDT | no | CLOSE | 0.0059% | 4.8456 | 4.8470 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0036% | 110.2900 | 110.3500 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 148.2600 | 148.1300 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 32.5200 | 32.5600 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0024% | 1.3963 | 1.3972 | - | - | - | - | - |
| ZECUSDT | no | CLOSE | 0.0091% | 1,218.9100 | 1,219.5800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
