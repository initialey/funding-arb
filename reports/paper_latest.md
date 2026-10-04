# Paper trading status

Run #81 at 2026-10-04 19:33 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SANDUSDT, DOGEUSDT, BNBUSDT, NEARUSDT, SUIUSDT.

| metric | value |
|---|---|
| equity | 9,958.43 USDT |
| return since start | -0.42% (27.1 days) |
| annualised | -5.61% |
| realized (closed pairs) | -39.66 USDT |
| funding received this run | 0.1013 USDT |
| open pairs | 3 / 10 |
| free cash | 6,960.34 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes | OPEN | 0.0100% | 789.0000 | 789.3000 | 0.0000 | 0.0000 | 0.50% | 1,570.1493 | 99.0% |
| NEARUSDT | yes |  | 0.0100% | 4.9689 | 4.9680 | 0.1567 | -0.0057 | 0.56% | 9.3508 | 88.2% |
| ZECUSDT | yes |  | 0.0100% | 1,336.4900 | 1,336.5500 | 0.3338 | -0.1533 | 0.47% | 2,748.8557 | 105.7% |
| BTCUSDT | no |  | 0.0010% | 85,487.8000 | 85,526.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0080% | 0.0955 | 0.0956 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0028% | 2,702.8300 | 2,704.2200 | - | - | - | - | - |
| SANDUSDT | no |  | -0.2328% | 0.0749 | 0.0749 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0021% | 121.4500 | 121.4800 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0074% | 1.2191 | 1.2195 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0055% | 1.5080 | 1.5087 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
