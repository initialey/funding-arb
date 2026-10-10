# Paper trading status

Run #97 at 2026-10-10 14:26 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, XRPUSDT, ZECUSDT, MAGICUSDT, NEARUSDT, ADAUSDT, DOGEUSDT, WLDUSDT.

| metric | value |
|---|---|
| equity | 9,952.87 USDT |
| return since start | -0.47% (32.9 days) |
| annualised | -5.23% |
| realized (closed pairs) | -46.38 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,953.62 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| MAGICUSDT | yes | OPEN | 0.0141% | 0.1056 | 0.1066 | 0.0000 | 0.0000 | 0.50% | 0.2101 | 99.0% |
| ADAUSDT | no |  | 0.0069% | 0.2556 | 0.2558 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0010% | 82,836.3500 | 82,868.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0007% | 0.0861 | 0.0862 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0032% | 2,499.5300 | 2,500.5900 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0096% | 5.3945 | 5.3960 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0009% | 110.0600 | 110.1200 | - | - | - | - | - |
| WLDUSDT | no |  | 0.0042% | 0.5434 | 0.5436 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0016% | 1.4059 | 1.4067 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0078% | 1,231.5700 | 1,232.0700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
