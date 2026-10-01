# Paper trading status

Run #71 at 2026-10-01 15:24 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, MUUSDT, NEARUSDT, MOVRUSDT, DOGEUSDT.

| metric | value |
|---|---|
| equity | 9,963.90 USDT |
| return since start | -0.36% (23.9 days) |
| annualised | -5.51% |
| realized (closed pairs) | -35.54 USDT |
| funding received this run | 0.0448 USDT |
| open pairs | 1 / 10 |
| free cash | 8,964.46 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 4.9021 | 4.9070 | 0.0448 | 0.1530 | 0.41% | 10.8923 | 122.2% |
| BTCUSDT | no |  | 0.0045% | 84,136.3700 | 84,180.3000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0016% | 0.0946 | 0.0947 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0018% | 2,690.9500 | 2,692.3400 | - | - | - | - | - |
| MOVRUSDT | no |  | -0.0119% | 2.6340 | 2.6285 | - | - | - | - | - |
| MUUSDT | no |  | 0.0000% | 1,048.8700 | 1,049.1600 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0007% | 117.6900 | 117.7400 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 148.9900 | 149.0100 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0070% | 1.4906 | 1.4909 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0085% | 1,383.3300 | 1,383.6500 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
