# Paper trading status

Run #173 at 2026-11-06 06:29 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, SOXSUSDT, DOGEUSDT, INTCUSDT, QQQUSDT, MUUSDT.

| metric | value |
|---|---|
| equity | 9,909.04 USDT |
| return since start | -0.91% (59.5 days) |
| annualised | -5.58% |
| realized (closed pairs) | -88.35 USDT |
| funding received this run | 0.2175 USDT |
| open pairs | 4 / 10 |
| free cash | 5,911.65 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| INTCUSDT | yes | OPEN | 0.0102% | 54.0700 | 54.0400 | 0.0000 | 0.0000 | 0.50% | 107.6020 | 99.0% |
| MUUSDT | yes |  | 0.0255% | 686.3900 | 686.4800 | 0.1487 | 0.0772 | 0.47% | 1,410.3284 | 105.5% |
| SOXLUSDT | yes |  | 0.0239% | 45.2000 | 45.2000 | 0.0000 | -0.1869 | 0.43% | 97.8507 | 116.5% |
| XRPUSDT | yes |  | 0.0100% | 1.1975 | 1.1981 | 0.1903 | 0.1585 | 0.42% | 2.6263 | 119.3% |
| BTCUSDT | no |  | 0.0091% | 75,642.7300 | 75,670.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0079% | 0.0717 | 0.0717 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0062% | 2,226.9900 | 2,227.7900 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0080% | 654.8600 | 654.9800 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0022% | 89.7600 | 89.8000 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0102% | 72.6900 | 72.7800 | - | - | - | - | - |
| UNIUSDT | no | CLOSE | 0.0083% | 6.9500 | 6.9550 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0078% | 1,270.7100 | 1,269.8000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
