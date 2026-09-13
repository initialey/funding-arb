# Paper trading status

Run #19 at 2026-09-13 18:45 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, BNBUSDT, DOGEUSDT, UNIUSDT, SOXLUSDT, FILUSDT.

| metric | value |
|---|---|
| equity | 9,991.81 USDT |
| return since start | -0.08% (6.0 days) |
| annualised | -4.95% |
| realized (closed pairs) | -6.00 USDT |
| funding received this run | 0.0912 USDT |
| open pairs | 2 / 10 |
| free cash | 7,994.00 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes |  | 0.0138% | 0.4993 | 0.4989 | 0.1927 | -0.8907 | 0.39% | 1.1328 | 126.9% |
| ZECUSDT | yes | OPEN | 0.0100% | 1,108.9900 | 1,109.2600 | 0.0000 | 0.0000 | 0.50% | 2,206.9453 | 99.0% |
| BNBUSDT | no |  | 0.0046% | 721.1500 | 721.3000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0064% | 77,346.5000 | 77,380.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0022% | 0.0845 | 0.0845 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0073% | 2,507.8500 | 2,508.7400 | - | - | - | - | - |
| FILUSDT | no |  | 0.0055% | 0.9976 | 0.9982 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0040% | 101.1800 | 101.2300 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0093% | 117.6200 | 117.6100 | - | - | - | - | - |
| UNIUSDT | no |  | -0.0076% | 6.3430 | 6.3470 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0019% | 1.3567 | 1.3575 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
