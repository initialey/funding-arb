# Paper trading status

Run #103 at 2026-10-12 17:47 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, NEARUSDT, SOXSUSDT, SOXLUSDT, DOGEUSDT, SPCXUSDT.

| metric | value |
|---|---|
| equity | 9,940.67 USDT |
| return since start | -0.59% (35.0 days) |
| annualised | -6.19% |
| realized (closed pairs) | -58.81 USDT |
| funding received this run | 0.1639 USDT |
| open pairs | 1 / 10 |
| free cash | 8,941.19 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 5.4497 | 5.4520 | 0.2106 | 0.0241 | 0.52% | 10.6189 | 94.9% |
| BTCUSDT | no |  | 0.0017% | 82,451.3000 | 82,485.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0064% | 0.0848 | 0.0848 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0024% | 2,507.8400 | 2,508.8600 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0026% | 107.5100 | 107.5600 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 128.7700 | 128.7800 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 37.2400 | 37.2400 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 164.1600 | 160.0000 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0032% | 1.3601 | 1.3610 | - | - | - | - | - |
| ZECUSDT | no | CLOSE | 0.0078% | 1,240.1700 | 1,240.6300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
