# Paper trading status

Run #217 at 2026-11-25 00:35 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, SOXSUSDT, DOGEUSDT, QQQUSDT, ZECUSDT, SNXXUSDT, ANTUSDT.

| metric | value |
|---|---|
| equity | 9,895.99 USDT |
| return since start | -1.04% (78.3 days) |
| annualised | -4.85% |
| realized (closed pairs) | -104.88 USDT |
| funding received this run | 0.1583 USDT |
| open pairs | 2 / 10 |
| free cash | 7,895.12 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0100% | 2.0976 | 2.0992 | 2.9091 | 0.1251 | 0.30% | 5.5692 | 165.5% |
| PIEVERSEUSDT | yes |  | 0.0100% | 3.0501 | 3.0461 | 0.3671 | -1.0243 | 0.36% | 7.2794 | 138.7% |
| ANTUSDT | no |  | 0.0000% | 79.7400 | 79.7400 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0006% | 59,567.6000 | 59,592.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | -0.0008% | 0.0551 | 0.0551 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0017% | 1,671.3600 | 1,672.0000 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0030% | 636.7700 | 636.7300 | - | - | - | - | - |
| SNXXUSDT | no |  | 0.0000% | 1.5830 | 1.5830 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0066% | 69.6500 | 69.6900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 32.0600 | 32.0400 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0010% | 62.0200 | 62.0400 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0041% | 735.6000 | 735.7100 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
