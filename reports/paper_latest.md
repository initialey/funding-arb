# Paper trading status

Run #199 at 2026-11-16 06:15 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, DOGEUSDT, SOXLUSDT, ZECUSDT, SOXSUSDT, XRPUSDT, EVAAUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,901.43 USDT |
| return since start | -0.99% (69.5 days) |
| annualised | -5.18% |
| realized (closed pairs) | -97.07 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 2 / 10 |
| free cash | 7,902.93 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes | OPEN | 0.0243% | 2.7985 | 2.7997 | 0.0000 | 0.0000 | 0.50% | 5.5692 | 99.0% |
| SOXLUSDT | yes | OPEN | 0.0170% | 52.0000 | 52.0300 | 0.0000 | 0.0000 | 0.50% | 103.4826 | 99.0% |
| BTCUSDT | no |  | -0.0010% | 64,309.4000 | 64,344.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | -0.0031% | 0.0585 | 0.0585 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0020% | 1,808.1000 | 1,808.8200 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0054% | 671.8000 | 671.8500 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0085% | 70.9000 | 70.9900 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0037% | 56.4900 | 56.4700 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0044% | 0.9505 | 0.9511 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0006% | 878.1900 | 878.4300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
