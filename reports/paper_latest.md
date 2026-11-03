# Paper trading status

Run #166 at 2026-11-03 06:37 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, INTCUSDT, BZUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,916.35 USDT |
| return since start | -0.84% (56.5 days) |
| annualised | -5.40% |
| realized (closed pairs) | -82.32 USDT |
| funding received this run | 0.2062 USDT |
| open pairs | 4 / 10 |
| free cash | 5,917.68 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| INTCUSDT | yes | OPEN | 0.0123% | 60.6100 | 60.6200 | 0.0000 | 0.0000 | 0.50% | 120.6169 | 99.0% |
| QQQUSDT | yes |  | 0.0243% | 682.9300 | 682.9700 | 0.3599 | 0.0216 | 0.48% | 1,391.3433 | 103.7% |
| UNIUSDT | yes |  | 0.0100% | 6.9910 | 6.9940 | 0.2005 | 0.2795 | 0.48% | 14.1771 | 102.8% |
| ZECUSDT | yes |  | 0.0100% | 1,135.5600 | 1,136.2700 | 0.1379 | 0.6678 | 0.40% | 2,534.5672 | 123.2% |
| BTCUSDT | no |  | 0.0085% | 76,754.6000 | 76,769.9000 | - | - | - | - | - |
| BZUSDT | no |  | -0.0038% | 105.8700 | 105.8700 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0083% | 0.0739 | 0.0739 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0094% | 2,253.1900 | 2,253.8600 | - | - | - | - | - |
| SOLUSDT | no | CLOSE | 0.0094% | 91.8500 | 91.9100 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 69.6500 | 69.7200 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0065% | 1.2511 | 1.2515 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
