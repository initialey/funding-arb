# Paper trading status

Run #167 at 2026-11-03 16:08 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, INTCUSDT, BZUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,914.95 USDT |
| return since start | -0.85% (56.9 days) |
| annualised | -5.45% |
| realized (closed pairs) | -83.71 USDT |
| funding received this run | 0.3231 USDT |
| open pairs | 4 / 10 |
| free cash | 5,916.29 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BTCUSDT | yes | OPEN | 0.0100% | 77,630.0000 | 77,656.9000 | 0.0000 | 0.0000 | 0.50% | 154,487.5622 | 99.0% |
| QQQUSDT | yes |  | 0.0108% | 689.8100 | 689.7700 | 0.4472 | -0.0357 | 0.49% | 1,391.3433 | 101.7% |
| UNIUSDT | yes |  | 0.0100% | 7.3170 | 7.3180 | 0.3032 | 0.1423 | 0.53% | 14.1771 | 93.8% |
| ZECUSDT | yes |  | 0.0100% | 1,201.4500 | 1,201.8700 | 0.2322 | 0.5765 | 0.45% | 2,534.5672 | 111.0% |
| BZUSDT | no |  | -0.0026% | 103.2300 | 103.2200 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0092% | 0.0753 | 0.0754 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0090% | 2,296.5100 | 2,297.2600 | - | - | - | - | - |
| INTCUSDT | no | CLOSE | 0.0086% | 61.7700 | 61.7900 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0076% | 93.4300 | 93.4800 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 76.3200 | 76.2900 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0071% | 1.2783 | 1.2789 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
