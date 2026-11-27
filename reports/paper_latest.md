# Paper trading status

Run #221 at 2026-11-27 08:14 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, SOXSUSDT, QQQUSDT, SKHYUSDT, MUUSDT.

| metric | value |
|---|---|
| equity | 9,895.52 USDT |
| return since start | -1.04% (80.6 days) |
| annualised | -4.73% |
| realized (closed pairs) | -104.18 USDT |
| funding received this run | 0.2703 USDT |
| open pairs | 1 / 10 |
| free cash | 8,895.82 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| PIEVERSEUSDT | yes |  | 0.0100% | 4.0219 | 4.0217 | 1.1036 | -0.6578 | 0.61% | 7.2794 | 81.0% |
| BTCUSDT | no |  | 0.0038% | 61,811.1000 | 61,843.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0058% | 0.0583 | 0.0583 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0057% | 1,734.8100 | 1,735.3900 | - | - | - | - | - |
| EVAAUSDT | no | CLOSE | 0.0098% | 2.2313 | 2.2349 | - | - | - | - | - |
| MUUSDT | no |  | 0.0000% | 640.6200 | 640.6600 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0015% | 651.4800 | 651.5700 | - | - | - | - | - |
| SKHYUSDT | no |  | -0.0354% | 117.1000 | 117.1000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0054% | 73.1800 | 73.2300 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 36.3600 | 36.3800 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0005% | 53.8500 | 53.7800 | - | - | - | - | - |
| ZECUSDT | no | CLOSE | 0.0085% | 747.2200 | 747.1700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
