# Paper trading status

Run #114 at 2026-10-16 13:12 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SOXLUSDT, SOXSUSDT, NEARUSDT, BNBUSDT, DOGEUSDT.

| metric | value |
|---|---|
| equity | 9,937.35 USDT |
| return since start | -0.63% (38.8 days) |
| annualised | -5.89% |
| realized (closed pairs) | -61.90 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,938.10 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| DOGEUSDT | yes | OPEN | 0.0100% | 0.0817 | 0.0818 | 0.0000 | 0.0000 | 0.50% | 0.1627 | 99.0% |
| BNBUSDT | no |  | 0.0065% | 727.7500 | 728.1000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0065% | 82,010.9000 | 82,040.7000 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0027% | 2,462.5200 | 2,463.3700 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0078% | 5.2332 | 5.2350 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0030% | 105.5200 | 105.5600 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 102.9200 | 102.9200 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 45.6200 | 45.6500 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0067% | 1.3343 | 1.3350 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0077% | 1,217.7400 | 1,217.9500 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
