# Paper trading status

Run #216 at 2026-11-24 09:44 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, SOXSUSDT, ZECUSDT, DOGEUSDT, QQQUSDT, OPENAIUSDT, MUUSDT.

| metric | value |
|---|---|
| equity | 9,896.95 USDT |
| return since start | -1.03% (77.7 days) |
| annualised | -4.84% |
| realized (closed pairs) | -104.88 USDT |
| funding received this run | 0.2188 USDT |
| open pairs | 2 / 10 |
| free cash | 7,895.12 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0140% | 2.5676 | 2.5669 | 2.8341 | -0.3216 | 0.42% | 5.5692 | 116.9% |
| PIEVERSEUSDT | yes |  | 0.0131% | 3.1716 | 3.1792 | 0.2837 | 0.5405 | 0.38% | 7.2794 | 129.5% |
| BTCUSDT | no |  | 0.0027% | 60,157.6000 | 60,182.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0006% | 0.0558 | 0.0559 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0001% | 1,689.7500 | 1,690.5900 | - | - | - | - | - |
| MUUSDT | no |  | 0.0000% | 681.2200 | 680.1700 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,213.7700 | 707.9000 | - | - | - | - | - |
| QQQUSDT | no | CLOSE | 0.0016% | 646.6800 | 646.6600 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0024% | 70.9500 | 70.9900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 39.9400 | 39.9200 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0094% | 52.9900 | 53.0000 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0060% | 747.9900 | 748.3100 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
