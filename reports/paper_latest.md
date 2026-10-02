# Paper trading status

Run #75 at 2026-10-02 20:40 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SPCXUSDT, DOGEUSDT, NEARUSDT, SOXLUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,961.78 USDT |
| return since start | -0.38% (25.1 days) |
| annualised | -5.55% |
| realized (closed pairs) | -36.65 USDT |
| funding received this run | 0.0466 USDT |
| open pairs | 2 / 10 |
| free cash | 7,963.35 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| XRPUSDT | yes | OPEN | 0.0100% | 1.4739 | 1.4750 | 0.0000 | 0.0000 | 0.50% | 2.9331 | 99.0% |
| ZECUSDT | yes |  | 0.0100% | 1,286.7900 | 1,286.9200 | 0.0466 | -0.1215 | 0.44% | 2,748.8557 | 113.6% |
| BNBUSDT | no |  | 0.0018% | 765.1500 | 765.7000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0029% | 84,365.3000 | 84,413.3000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0077% | 0.0915 | 0.0916 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0043% | 2,666.6300 | 2,668.2200 | - | - | - | - | - |
| NEARUSDT | no |  | -0.0167% | 4.6599 | 4.6580 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0035% | 117.9800 | 118.0200 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 163.8000 | 163.7400 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0036% | 158.8900 | 151.7300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
