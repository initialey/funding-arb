# Paper trading status

Run #89 at 2026-10-07 21:14 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, XRPUSDT, ZECUSDT, DOGEUSDT, NEARUSDT, SPCXUSDT, SOXLUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,954.72 USDT |
| return since start | -0.45% (30.1 days) |
| annualised | -5.48% |
| realized (closed pairs) | -44.62 USDT |
| funding received this run | 0.0572 USDT |
| open pairs | 2 / 10 |
| free cash | 7,955.38 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes |  | 0.0100% | 5.3791 | 5.3800 | 0.6443 | 0.1933 | 0.67% | 9.3508 | 73.8% |
| ZECUSDT | yes | OPEN | 0.0100% | 1,321.8700 | 1,322.5600 | 0.0000 | 0.0000 | 0.50% | 2,630.5871 | 99.0% |
| BNBUSDT | no |  | -0.0028% | 770.4500 | 770.8000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0016% | 83,327.3000 | 83,361.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0090% | 0.0887 | 0.0888 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0028% | 2,570.9900 | 2,572.7300 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0065% | 116.0800 | 116.1300 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 158.8300 | 158.8300 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 168.1100 | 163.1900 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0008% | 1.4196 | 1.4205 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
