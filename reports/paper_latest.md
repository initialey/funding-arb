# Paper trading status

Run #83 at 2026-10-05 17:05 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, SPCXUSDT, ADAUSDT, DOGEUSDT, SOXLUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,956.82 USDT |
| return since start | -0.43% (28.0 days) |
| annualised | -5.64% |
| realized (closed pairs) | -41.22 USDT |
| funding received this run | 0.1997 USDT |
| open pairs | 4 / 10 |
| free cash | 5,958.78 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | yes | OPEN | 0.0100% | 0.2641 | 0.2643 | 0.0000 | 0.0000 | 0.50% | 0.5256 | 99.0% |
| NEARUSDT | yes |  | 0.0100% | 4.9809 | 4.9840 | 0.3155 | 0.4202 | 0.56% | 9.3508 | 87.7% |
| XRPUSDT | yes | OPEN | 0.0100% | 1.4883 | 1.4886 | 0.0000 | 0.0000 | 0.50% | 2.9618 | 99.0% |
| ZECUSDT | yes |  | 0.0100% | 1,294.4800 | 1,294.4600 | 0.4754 | -0.1768 | 0.44% | 2,748.8557 | 112.4% |
| BNBUSDT | no |  | 0.0089% | 786.2000 | 786.4000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0032% | 85,199.2000 | 85,236.8000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0056% | 0.0942 | 0.0942 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0036% | 2,692.7300 | 2,694.0700 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0035% | 119.3600 | 119.4400 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 162.0100 | 162.0200 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 167.6100 | 161.5700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
