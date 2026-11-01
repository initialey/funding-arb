# Paper trading status

Run #162 at 2026-11-01 14:59 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, BNBUSDT, SOXLUSDT, TRXUSDT, PEPEUSDT.

| metric | value |
|---|---|
| equity | 9,919.27 USDT |
| return since start | -0.81% (54.9 days) |
| annualised | -5.37% |
| realized (closed pairs) | -80.20 USDT |
| funding received this run | 0.0499 USDT |
| open pairs | 1 / 10 |
| free cash | 8,919.80 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 4.3723 | 4.3740 | 0.0499 | 0.1713 | 0.50% | 8.7160 | 99.3% |
| BNBUSDT | no |  | 0.0017% | 716.4500 | 716.9000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0095% | 78,010.3000 | 78,037.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0044% | 0.0758 | 0.0758 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0012% | 2,270.5900 | 2,271.8100 | - | - | - | - | - |
| PEPEUSDT | no |  | 0.0056% | 0.0000 | 0.0000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0070% | 94.9800 | 94.9900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 78.5900 | 78.5700 | - | - | - | - | - |
| TRXUSDT | no |  | -0.0201% | 0.3111 | 0.3112 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0022% | 1.2529 | 1.2536 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0055% | 1,242.5000 | 1,243.1800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
