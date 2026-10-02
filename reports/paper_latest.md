# Paper trading status

Run #73 at 2026-10-02 05:27 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, MUUSDT, NEARUSDT, MOVRUSDT, DOGEUSDT.

| metric | value |
|---|---|
| equity | 9,963.35 USDT |
| return since start | -0.37% (24.5 days) |
| annualised | -5.46% |
| realized (closed pairs) | -36.65 USDT |
| funding received this run | -0.0857 USDT |
| open pairs | 0 / 10 |
| free cash | 9,963.35 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BTCUSDT | no |  | 0.0005% | 86,324.5000 | 86,356.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0056% | 0.0961 | 0.0962 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0020% | 2,726.5300 | 2,727.4600 | - | - | - | - | - |
| MOVRUSDT | no |  | -0.0332% | 2.2380 | 2.2474 | - | - | - | - | - |
| MUUSDT | no |  | 0.0000% | 1,092.1300 | 1,092.1400 | - | - | - | - | - |
| NEARUSDT | no | CLOSE | 0.0004% | 4.9642 | 4.9710 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0004% | 122.7300 | 122.7700 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 156.0300 | 156.0100 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0071% | 1.5210 | 1.5214 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0094% | 1,393.6600 | 1,393.2100 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
