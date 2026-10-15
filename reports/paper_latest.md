# Paper trading status

Run #111 at 2026-10-15 13:21 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, DOGEUSDT, BNBUSDT, SOXSUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,939.16 USDT |
| return since start | -0.61% (37.8 days) |
| annualised | -5.87% |
| realized (closed pairs) | -60.09 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,939.91 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ZECUSDT | yes | OPEN | 0.0100% | 1,091.6700 | 1,092.1900 | 0.0000 | 0.0000 | 0.50% | 2,172.4776 | 99.0% |
| BNBUSDT | no |  | 0.0056% | 718.1000 | 718.4000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0051% | 80,358.4900 | 80,393.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0067% | 0.0791 | 0.0791 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0040% | 2,345.1000 | 2,346.3300 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0098% | 4.6077 | 4.6100 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0003% | 101.5800 | 101.6300 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 99.7500 | 99.7800 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 46.7900 | 46.7700 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0009% | 1.2974 | 1.2978 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
