# Paper trading status

Run #202 at 2026-11-17 17:34 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, SOXSUSDT, ZECUSDT, DOGEUSDT, SNXXUSDT, QQQUSDT, EVAAUSDT.

| metric | value |
|---|---|
| equity | 9,898.49 USDT |
| return since start | -1.02% (71.0 days) |
| annualised | -5.22% |
| realized (closed pairs) | -100.48 USDT |
| funding received this run | 0.1454 USDT |
| open pairs | 1 / 10 |
| free cash | 8,899.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0224% | 3.3490 | 3.3455 | 0.6067 | -0.8815 | 0.74% | 5.5692 | 66.3% |
| BTCUSDT | no |  | 0.0008% | 63,660.4500 | 63,684.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | -0.0062% | 0.0584 | 0.0585 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0027% | 1,780.6700 | 1,781.4200 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0000% | 656.4500 | 656.3900 | - | - | - | - | - |
| SNXXUSDT | no |  | 0.0026% | 2.8230 | 2.8240 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0113% | 72.2200 | 72.2300 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 48.2000 | 48.1500 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 59.9200 | 60.0000 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0011% | 926.9000 | 927.6300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
