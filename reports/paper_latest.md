# Paper trading status

Run #92 at 2026-10-08 21:16 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, SOXLUSDT, NEARUSDT, ADAUSDT, SOXSUSDT.

| metric | value |
|---|---|
| equity | 9,955.01 USDT |
| return since start | -0.45% (31.1 days) |
| annualised | -5.27% |
| realized (closed pairs) | -44.62 USDT |
| funding received this run | 0.0930 USDT |
| open pairs | 2 / 10 |
| free cash | 7,955.38 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 4.5429 | 4.5450 | 0.8007 | 0.3058 | 0.47% | 9.3508 | 105.8% |
| ZECUSDT | yes |  | 0.0100% | 1,179.3600 | 1,179.6800 | 0.1347 | -0.1118 | 0.40% | 2,630.5871 | 123.1% |
| ADAUSDT | no |  | 0.0012% | 0.2345 | 0.2347 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0032% | 81,723.1100 | 81,763.3000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0062% | 0.0843 | 0.0843 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0009% | 2,472.9900 | 2,474.0400 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0015% | 109.9400 | 110.0300 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 142.6600 | 142.6600 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 33.7800 | 33.7900 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0037% | 1.3788 | 1.3795 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
