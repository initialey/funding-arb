# Paper trading status

Run #168 at 2026-11-03 21:43 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, INTCUSDT, BZUSDT, SOXSUSDT.

| metric | value |
|---|---|
| equity | 9,915.06 USDT |
| return since start | -0.85% (57.2 days) |
| annualised | -5.42% |
| realized (closed pairs) | -83.71 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 4 / 10 |
| free cash | 5,916.29 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BTCUSDT | yes |  | 0.0100% | 77,966.8000 | 77,989.3000 | 0.0000 | -0.0291 | 0.50% | 154,487.5622 | 98.1% |
| QQQUSDT | yes |  | 0.0108% | 690.0600 | 690.1200 | 0.4472 | 0.0359 | 0.49% | 1,391.3433 | 101.6% |
| UNIUSDT | yes |  | 0.0100% | 7.1920 | 7.1920 | 0.3032 | 0.0709 | 0.51% | 14.1771 | 97.1% |
| ZECUSDT | yes |  | 0.0100% | 1,235.8300 | 1,236.5700 | 0.2322 | 0.7140 | 0.47% | 2,534.5672 | 105.1% |
| BZUSDT | no |  | -0.0026% | 104.4800 | 104.4800 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0092% | 0.0756 | 0.0757 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0090% | 2,296.9900 | 2,297.8000 | - | - | - | - | - |
| INTCUSDT | no |  | 0.0086% | 62.1500 | 62.1500 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0076% | 93.8000 | 93.8300 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 78.2200 | 78.2200 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0014% | 50.1600 | 50.1200 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0071% | 1.2855 | 1.2858 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
