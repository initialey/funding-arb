# Paper trading status

Run #156 at 2026-10-30 15:00 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, SOXLUSDT, XRPUSDT, BNBUSDT, PEPEUSDT, INTCUSDT.

| metric | value |
|---|---|
| equity | 9,923.78 USDT |
| return since start | -0.76% (52.9 days) |
| annualised | -5.26% |
| realized (closed pairs) | -75.47 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,924.53 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| INTCUSDT | yes | OPEN | 0.0273% | 66.3400 | 66.4500 | 0.0000 | 0.0000 | 0.50% | 132.0199 | 99.0% |
| BNBUSDT | no |  | -0.0034% | 698.7500 | 699.0000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0044% | 77,210.6000 | 77,221.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0007% | 0.0757 | 0.0757 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0030% | 2,236.7200 | 2,237.7600 | - | - | - | - | - |
| PEPEUSDT | no |  | 0.0057% | 0.0000 | 0.0000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0001% | 94.5100 | 94.4900 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 80.0700 | 80.0400 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0014% | 1.2440 | 1.2443 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0071% | 1,239.3100 | 1,240.0900 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
