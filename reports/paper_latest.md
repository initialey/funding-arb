# Paper trading status

Run #70 at 2026-10-01 05:43 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SOXLUSDT, NEARUSDT, DOGEUSDT, QNTUSDT, SUIUSDT.

| metric | value |
|---|---|
| equity | 9,963.71 USDT |
| return since start | -0.36% (23.5 days) |
| annualised | -5.64% |
| realized (closed pairs) | -35.54 USDT |
| funding received this run | 0.0363 USDT |
| open pairs | 1 / 10 |
| free cash | 8,964.46 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes | OPEN | 0.0100% | 5.4734 | 5.4770 | 0.0000 | 0.0000 | 0.50% | 10.8923 | 99.0% |
| BTCUSDT | no |  | 0.0050% | 84,228.9000 | 84,278.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | -0.0009% | 0.0958 | 0.0958 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0027% | 2,714.9400 | 2,716.1600 | - | - | - | - | - |
| QNTUSDT | no |  | -0.0212% | 292.3900 | 292.5600 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0001% | 119.3400 | 119.3800 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 158.5800 | 158.5000 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0030% | 1.1725 | 1.1729 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0073% | 1.5082 | 1.5089 | - | - | - | - | - |
| ZECUSDT | no | CLOSE | 0.0091% | 1,437.3400 | 1,437.9500 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
