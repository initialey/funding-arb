# Paper trading status

Run #90 at 2026-10-08 05:54 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, NEARUSDT, DOGEUSDT, SOXLUSDT, SPCXUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,954.60 USDT |
| return since start | -0.45% (30.5 days) |
| annualised | -5.43% |
| realized (closed pairs) | -44.62 USDT |
| funding received this run | 0.1043 USDT |
| open pairs | 2 / 10 |
| free cash | 7,955.38 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 5.3943 | 5.3950 | 0.7017 | 0.1722 | 0.67% | 9.3508 | 73.3% |
| ZECUSDT | yes |  | 0.0100% | 1,239.9600 | 1,240.0700 | 0.0469 | -0.2031 | 0.44% | 2,630.5871 | 112.2% |
| BNBUSDT | no |  | -0.0040% | 768.4500 | 768.7000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0023% | 82,747.9000 | 82,793.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0090% | 0.0872 | 0.0873 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0013% | 2,564.8000 | 2,566.1800 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0049% | 115.1000 | 115.1400 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 157.0300 | 157.0400 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 168.0100 | 162.5000 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0033% | 1.4017 | 1.4022 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
