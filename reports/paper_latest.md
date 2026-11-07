# Paper trading status

Run #176 at 2026-11-07 05:50 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, SOXSUSDT, XRPUSDT, SPCXUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,905.33 USDT |
| return since start | -0.95% (60.5 days) |
| annualised | -5.71% |
| realized (closed pairs) | -93.64 USDT |
| funding received this run | 0.0956 USDT |
| open pairs | 2 / 10 |
| free cash | 7,906.36 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| QQQUSDT | yes |  | 0.0146% | 658.2000 | 658.2100 | 0.0576 | 0.1725 | 0.49% | 1,318.4677 | 100.3% |
| ZECUSDT | yes |  | 0.0100% | 1,311.5200 | 1,312.1400 | 0.0985 | 0.1399 | 0.48% | 2,674.1692 | 103.9% |
| BTCUSDT | no |  | 0.0063% | 75,991.3100 | 76,021.3000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0080% | 0.0720 | 0.0720 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0036% | 2,247.7100 | 2,248.8300 | - | - | - | - | - |
| MUUSDT | no | CLOSE | 0.0035% | 692.6900 | 692.7000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0060% | 90.1800 | 90.2200 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 45.6700 | 45.6600 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 71.6400 | 71.6400 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 135.2700 | 132.6100 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0070% | 1.1620 | 1.1624 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
