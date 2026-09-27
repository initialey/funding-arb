# Paper trading status

Run #60 at 2026-09-27 13:53 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, WLDUSDT, DOGEUSDT, QNTUSDT, NEARUSDT, UNIUSDT.

| metric | value |
|---|---|
| equity | 9,969.82 USDT |
| return since start | -0.30% (19.8 days) |
| annualised | -5.55% |
| realized (closed pairs) | -28.88 USDT |
| funding received this run | 0.0643 USDT |
| open pairs | 2 / 10 |
| free cash | 7,971.12 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UNIUSDT | yes | OPEN | 0.0100% | 9.8430 | 9.8490 | 0.0000 | 0.0000 | 0.50% | 19.5881 | 99.0% |
| WLDUSDT | yes |  | 0.0100% | 0.5746 | 0.5746 | 0.1025 | 0.1007 | 0.58% | 1.0633 | 85.0% |
| BTCUSDT | no |  | -0.0013% | 84,846.5000 | 84,882.4000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0075% | 0.0975 | 0.0975 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0055% | 2,705.0200 | 2,706.2800 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0068% | 5.2010 | 5.2030 | - | - | - | - | - |
| QNTUSDT | no |  | -0.0090% | 160.7900 | 160.8000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0041% | 122.8300 | 122.8700 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0093% | 1.5288 | 1.5295 | - | - | - | - | - |
| ZECUSDT | no | CLOSE | 0.0073% | 1,649.3600 | 1,650.2300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
