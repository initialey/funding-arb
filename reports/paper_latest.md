# Paper trading status

Run #69 at 2026-09-30 20:46 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, QNTUSDT, NEARUSDT, DOGEUSDT, SOXLUSDT, SUIUSDT.

| metric | value |
|---|---|
| equity | 9,965.12 USDT |
| return since start | -0.35% (23.1 days) |
| annualised | -5.51% |
| realized (closed pairs) | -34.13 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,965.87 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ZECUSDT | yes | OPEN | 0.0100% | 1,425.0700 | 1,425.5000 | 0.0000 | 0.0000 | 0.50% | 2,835.9602 | 99.0% |
| BTCUSDT | no |  | 0.0031% | 83,657.8600 | 83,684.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0012% | 0.0945 | 0.0945 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0049% | 2,679.5500 | 2,680.8200 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0094% | 5.3413 | 5.3450 | - | - | - | - | - |
| QNTUSDT | no |  | -0.0226% | 282.9200 | 283.2000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0016% | 118.0600 | 118.1300 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 148.2300 | 148.2500 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0048% | 1.1611 | 1.1619 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0077% | 1.4915 | 1.4922 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
