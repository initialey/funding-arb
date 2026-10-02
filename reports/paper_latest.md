# Paper trading status

Run #74 at 2026-10-02 14:42 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, SOXLUSDT, SPCXUSDT, MUUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,962.60 USDT |
| return since start | -0.37% (24.9 days) |
| annualised | -5.49% |
| realized (closed pairs) | -36.65 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,963.35 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ZECUSDT | yes | OPEN | 0.0100% | 1,381.3000 | 1,381.8000 | 0.0000 | 0.0000 | 0.50% | 2,748.8557 | 99.0% |
| BTCUSDT | no |  | 0.0024% | 85,997.6000 | 86,030.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0061% | 0.0961 | 0.0961 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0037% | 2,726.9100 | 2,727.9500 | - | - | - | - | - |
| MUUSDT | no |  | 0.0000% | 1,092.4800 | 1,092.3500 | - | - | - | - | - |
| NEARUSDT | no |  | -0.0167% | 4.9178 | 4.9160 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0027% | 121.4200 | 121.4700 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 168.9300 | 168.9700 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0036% | 157.4800 | 150.1600 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0083% | 1.5268 | 1.5272 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
