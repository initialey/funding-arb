# Paper trading status

Run #63 at 2026-09-28 16:43 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, QNTUSDT, XRPUSDT, NEARUSDT, DOGEUSDT, SOXLUSDT, SPCXUSDT.

| metric | value |
|---|---|
| equity | 9,966.68 USDT |
| return since start | -0.33% (21.0 days) |
| annualised | -5.80% |
| realized (closed pairs) | -32.91 USDT |
| funding received this run | 0.1165 USDT |
| open pairs | 1 / 10 |
| free cash | 8,967.09 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 4.9177 | 4.9230 | 0.1379 | 0.2047 | 0.41% | 10.8589 | 120.8% |
| BTCUSDT | no |  | 0.0004% | 83,653.6000 | 83,682.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0029% | 0.0942 | 0.0942 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0021% | 2,681.4500 | 2,682.2400 | - | - | - | - | - |
| QNTUSDT | no |  | -0.0270% | 233.9700 | 233.9100 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0012% | 119.1500 | 119.1500 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0186% | 142.1700 | 142.2000 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 147.3900 | 140.4100 | - | - | - | - | - |
| WLDUSDT | no | CLOSE | 0.0052% | 0.4946 | 0.4949 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0058% | 1.4995 | 1.5005 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0094% | 1,529.0400 | 1,529.2300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
