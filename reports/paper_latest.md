# Paper trading status

Run #130 at 2026-10-21 20:05 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, SPCXUSDT, XRPUSDT, SOXSUSDT, NEARUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,929.06 USDT |
| return since start | -0.71% (44.1 days) |
| annualised | -5.87% |
| realized (closed pairs) | -70.19 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,929.81 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes | OPEN | 0.0100% | 5.2909 | 5.2940 | 0.0000 | 0.0000 | 0.50% | 10.5292 | 99.0% |
| BNBUSDT | no |  | 0.0007% | 748.3500 | 748.8000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0051% | 84,520.3900 | 84,554.6000 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0062% | 2,493.8500 | 2,494.4100 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0009% | 108.1800 | 108.2000 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0125% | 103.3600 | 103.2000 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0037% | 44.4400 | 44.4400 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 159.2900 | 155.4700 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0073% | 1.3865 | 1.3869 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0003% | 1,358.0300 | 1,357.9200 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
