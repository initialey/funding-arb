# Paper trading status

Run #117 at 2026-10-17 12:08 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SOXLUSDT, SOXSUSDT, NEARUSDT, BNBUSDT, DOGEUSDT.

| metric | value |
|---|---|
| equity | 9,934.25 USDT |
| return since start | -0.66% (39.8 days) |
| annualised | -6.04% |
| realized (closed pairs) | -64.48 USDT |
| funding received this run | 0.0510 USDT |
| open pairs | 2 / 10 |
| free cash | 7,935.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| SOXLUSDT | yes |  | 0.0132% | 94.0700 | 94.0700 | 0.0000 | 0.1590 | 0.50% | 187.4826 | 99.3% |
| ZECUSDT | yes |  | 0.0100% | 1,166.8800 | 1,167.3800 | 0.1014 | -0.0357 | 0.52% | 2,275.8607 | 95.0% |
| BNBUSDT | no |  | 0.0084% | 720.3000 | 720.8000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0050% | 81,522.3000 | 81,558.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0036% | 0.0801 | 0.0802 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0041% | 2,431.4700 | 2,432.4800 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0077% | 5.0938 | 5.0960 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0017% | 104.3000 | 104.3500 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 49.1900 | 49.1800 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0025% | 1.3040 | 1.3046 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
