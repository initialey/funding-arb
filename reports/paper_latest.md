# Paper trading status

Run #28 at 2026-09-16 19:31 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, OPENAIUSDT, DOGEUSDT, SPCXUSDT, BNBUSDT, ADAUSDT.

| metric | value |
|---|---|
| equity | 9,992.20 USDT |
| return since start | -0.08% (9.1 days) |
| annualised | -3.14% |
| realized (closed pairs) | -7.20 USDT |
| funding received this run | 0.0316 USDT |
| open pairs | 1 / 10 |
| free cash | 8,992.80 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes |  | 0.0100% | 0.3593 | 0.3591 | 0.7161 | -0.5664 | 0.23% | 1.1328 | 215.3% |
| ADAUSDT | no |  | 0.0050% | 0.1914 | 0.1916 | - | - | - | - | - |
| BNBUSDT | no |  | 0.0000% | 714.3000 | 714.4000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0029% | 75,436.9000 | 75,481.0000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0044% | 0.0795 | 0.0795 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0008% | 2,383.0100 | 2,383.5200 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,473.0100 | 887.9000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0043% | 97.2100 | 97.2800 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 150.0100 | 143.1400 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0028% | 1.2832 | 1.2835 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0016% | 1,280.6000 | 1,281.9800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
