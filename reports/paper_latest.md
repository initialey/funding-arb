# Paper trading status

Run #150 at 2026-10-28 15:03 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, DOGEUSDT, BNBUSDT, SOXSUSDT, SKHYUSDT.

| metric | value |
|---|---|
| equity | 9,925.04 USDT |
| return since start | -0.75% (50.9 days) |
| annualised | -5.38% |
| realized (closed pairs) | -74.29 USDT |
| funding received this run | 0.0495 USDT |
| open pairs | 1 / 10 |
| free cash | 8,925.71 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| XRPUSDT | yes |  | 0.0100% | 1.3151 | 1.3157 | 0.0495 | 0.0396 | 0.49% | 2.6444 | 101.1% |
| BNBUSDT | no |  | 0.0089% | 749.3000 | 749.4000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0085% | 80,641.8100 | 80,671.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0054% | 0.0793 | 0.0793 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0073% | 2,334.9500 | 2,335.9100 | - | - | - | - | - |
| SKHYUSDT | no |  | 0.0000% | 161.9200 | 161.9100 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0034% | 101.0600 | 101.0900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 103.5700 | 103.6200 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0027% | 41.5600 | 41.5200 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0001% | 1,277.8700 | 1,278.2300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
