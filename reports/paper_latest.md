# Paper trading status

Run #57 at 2026-09-26 13:01 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, XRPUSDT, ZECUSDT, NEARUSDT, DOGEUSDT, SUIUSDT, ADAUSDT, SPCXUSDT.

| metric | value |
|---|---|
| equity | 9,973.42 USDT |
| return since start | -0.27% (18.8 days) |
| annualised | -5.16% |
| realized (closed pairs) | -25.83 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,974.17 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes | OPEN | 0.0100% | 4.8535 | 4.8580 | 0.0000 | 0.0000 | 0.50% | 9.6587 | 99.0% |
| ADAUSDT | no |  | 0.0038% | 0.2557 | 0.2559 | - | - | - | - | - |
| BTCUSDT | no |  | -0.0015% | 84,016.0000 | 84,058.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0043% | 0.0974 | 0.0974 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0078% | 2,688.3800 | 2,689.5400 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0039% | 121.0900 | 121.1400 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 148.7000 | 142.0400 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0092% | 1.1717 | 1.1724 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0063% | 1.5439 | 1.5442 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0092% | 1,543.1600 | 1,543.8300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
