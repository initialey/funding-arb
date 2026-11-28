# Paper trading status

Run #224 at 2026-11-28 16:48 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, QQQUSDT, EVAAUSDT, SOXSUSDT, LTCUSDT.

| metric | value |
|---|---|
| equity | 9,894.59 USDT |
| return since start | -1.05% (82.0 days) |
| annualised | -4.69% |
| realized (closed pairs) | -104.18 USDT |
| funding received this run | 0.1047 USDT |
| open pairs | 2 / 10 |
| free cash | 7,895.82 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes | OPEN | 0.0110% | 2.1291 | 2.1317 | 0.0000 | 0.0000 | 0.50% | 4.2370 | 99.0% |
| PIEVERSEUSDT | yes |  | 0.0114% | 3.8300 | 3.8266 | 1.3362 | -1.0646 | 0.55% | 7.2794 | 90.1% |
| BTCUSDT | no |  | 0.0045% | 59,615.6300 | 59,646.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0011% | 0.0565 | 0.0565 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0012% | 1,653.7700 | 1,654.6100 | - | - | - | - | - |
| LTCUSDT | no |  | 0.0013% | 43.9600 | 44.0000 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0000% | 647.6200 | 647.7200 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0016% | 70.7100 | 70.7300 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 35.9400 | 35.9600 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 54.1500 | 54.1300 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0078% | 725.3200 | 725.7000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
