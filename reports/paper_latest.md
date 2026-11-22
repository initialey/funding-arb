# Paper trading status

Run #212 at 2026-11-22 06:35 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, DOGEUSDT, UNIUSDT, EVAAUSDT, QQQUSDT, LTCUSDT.

| metric | value |
|---|---|
| equity | 9,895.28 USDT |
| return since start | -1.05% (75.5 days) |
| annualised | -5.06% |
| realized (closed pairs) | -102.48 USDT |
| funding received this run | 0.1606 USDT |
| open pairs | 3 / 10 |
| free cash | 6,897.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0100% | 3.4130 | 3.4009 | 2.1534 | -2.4223 | 0.78% | 5.5692 | 63.2% |
| QQQUSDT | yes |  | 0.0178% | 621.7700 | 621.7700 | 0.0996 | -0.0080 | 0.50% | 1,240.2189 | 99.5% |
| SOXSUSDT | yes |  | 0.0157% | 78.5300 | 78.5400 | 0.0000 | 0.1921 | 0.50% | 155.7612 | 98.3% |
| BTCUSDT | no |  | -0.0024% | 59,058.1700 | 59,088.3000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0038% | 0.0541 | 0.0542 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0028% | 1,660.7800 | 1,661.6300 | - | - | - | - | - |
| LTCUSDT | no |  | -0.0031% | 39.0500 | 39.0900 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0087% | 69.0200 | 69.0600 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0079% | 32.5800 | 32.5900 | - | - | - | - | - |
| UNIUSDT | no |  | 0.0024% | 4.6090 | 4.6110 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0036% | 784.7200 | 785.1700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
