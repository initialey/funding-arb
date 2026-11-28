# Paper trading status

Run #222 at 2026-11-28 00:00 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, SOXSUSDT, ZECUSDT, DOGEUSDT, QQQUSDT, SKHYUSDT, XRPUSDT.

| metric | value |
|---|---|
| equity | 9,895.40 USDT |
| return since start | -1.05% (81.3 days) |
| annualised | -4.70% |
| realized (closed pairs) | -104.18 USDT |
| funding received this run | 0.1278 USDT |
| open pairs | 1 / 10 |
| free cash | 8,895.82 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| PIEVERSEUSDT | yes |  | 0.0114% | 3.8661 | 3.8639 | 1.2315 | -0.9065 | 0.56% | 7.2794 | 88.3% |
| BTCUSDT | no |  | 0.0041% | 59,893.3000 | 59,921.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0036% | 0.0577 | 0.0578 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0048% | 1,661.6100 | 1,662.4800 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0024% | 650.9900 | 651.0300 | - | - | - | - | - |
| SKHYUSDT | no |  | -0.1706% | 117.9000 | 117.7900 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0042% | 71.6200 | 71.6500 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 35.8300 | 35.8300 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0005% | 54.3100 | 54.3200 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0066% | 0.9483 | 0.9488 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0081% | 736.0000 | 736.2600 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
