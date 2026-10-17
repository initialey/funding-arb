# Paper trading status

Run #116 at 2026-10-17 04:16 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SOXLUSDT, SOXSUSDT, BNBUSDT, NEARUSDT, DOGEUSDT.

| metric | value |
|---|---|
| equity | 9,934.17 USDT |
| return since start | -0.66% (39.4 days) |
| annualised | -6.09% |
| realized (closed pairs) | -64.48 USDT |
| funding received this run | 0.0948 USDT |
| open pairs | 2 / 10 |
| free cash | 7,935.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| SOXLUSDT | yes | OPEN | 0.0132% | 94.2100 | 94.1800 | 0.0000 | 0.0000 | 0.50% | 187.4826 | 99.0% |
| ZECUSDT | yes |  | 0.0100% | 1,153.2700 | 1,154.0800 | 0.0504 | 0.1028 | 0.51% | 2,275.8607 | 97.3% |
| BNBUSDT | no |  | 0.0099% | 722.5000 | 722.9000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0060% | 81,503.1000 | 81,540.3000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0048% | 0.0804 | 0.0805 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0041% | 2,425.9100 | 2,427.0100 | - | - | - | - | - |
| NEARUSDT | no | CLOSE | 0.0096% | 5.0941 | 5.0980 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0007% | 104.7100 | 104.7800 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 49.1100 | 49.1300 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0062% | 1.3073 | 1.3080 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
