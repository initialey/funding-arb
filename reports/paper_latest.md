# Paper trading status

Run #62 at 2026-09-28 05:15 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, QNTUSDT, WLDUSDT, DOGEUSDT, NEARUSDT, SUIUSDT.

| metric | value |
|---|---|
| equity | 9,966.77 USDT |
| return since start | -0.33% (20.5 days) |
| annualised | -5.92% |
| realized (closed pairs) | -32.06 USDT |
| funding received this run | 0.1406 USDT |
| open pairs | 2 / 10 |
| free cash | 7,967.94 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 5.2159 | 5.2180 | 0.0478 | -0.1053 | 0.46% | 10.8589 | 108.2% |
| WLDUSDT | yes |  | 0.0100% | 0.5231 | 0.5232 | 0.2039 | 0.1852 | 0.48% | 1.0633 | 103.3% |
| BTCUSDT | no |  | -0.0008% | 83,303.8000 | 83,340.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0085% | 0.0939 | 0.0939 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0077% | 2,650.3800 | 2,651.6500 | - | - | - | - | - |
| QNTUSDT | no |  | -0.0155% | 254.9900 | 255.3100 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0012% | 119.4700 | 119.5100 | - | - | - | - | - |
| SUIUSDT | no | CLOSE | 0.0097% | 1.2122 | 1.2123 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0100% | 1.4861 | 1.4867 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0063% | 1,556.7800 | 1,557.3800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
