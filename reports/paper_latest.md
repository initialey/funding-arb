# Paper trading status

Run #177 at 2026-11-07 14:51 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, OPENAIUSDT, SOXSUSDT, SPCXUSDT.

| metric | value |
|---|---|
| equity | 9,904.92 USDT |
| return since start | -0.95% (60.9 days) |
| annualised | -5.70% |
| realized (closed pairs) | -94.89 USDT |
| funding received this run | 0.0476 USDT |
| open pairs | 1 / 10 |
| free cash | 8,905.11 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ZECUSDT | yes |  | 0.0100% | 1,278.7800 | 1,280.1300 | 0.1460 | 0.4137 | 0.45% | 2,674.1692 | 109.1% |
| BTCUSDT | no |  | 0.0056% | 75,957.0000 | 75,980.8000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0082% | 0.0720 | 0.0720 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0021% | 2,246.9200 | 2,247.9300 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,293.6200 | 763.8000 | - | - | - | - | - |
| QQQUSDT | no | CLOSE | 0.0039% | 657.9700 | 657.9900 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0068% | 90.0700 | 90.1000 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 45.6200 | 45.6200 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 71.6400 | 71.6500 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 135.1500 | 132.6400 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0057% | 1.1672 | 1.1677 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
