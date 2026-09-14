# Paper trading status

Run #22 at 2026-09-14 20:16 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, OPENAIUSDT, SOXLUSDT, DOGEUSDT, BNBUSDT, BZUSDT.

| metric | value |
|---|---|
| equity | 9,989.80 USDT |
| return since start | -0.10% (7.1 days) |
| annualised | -5.25% |
| realized (closed pairs) | -7.20 USDT |
| funding received this run | 0.0417 USDT |
| open pairs | 1 / 10 |
| free cash | 8,992.80 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes |  | 0.0234% | 0.4751 | 0.4726 | 0.5175 | -2.7688 | 0.36% | 1.1328 | 138.4% |
| BNBUSDT | no |  | 0.0059% | 730.1000 | 730.1000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0065% | 79,279.3900 | 79,317.5000 | - | - | - | - | - |
| BZUSDT | no |  | -0.1675% | 101.0300 | 101.0300 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0009% | 0.0856 | 0.0856 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0044% | 2,580.4000 | 2,581.4300 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,468.9300 | 883.0000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0015% | 104.3100 | 104.3000 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0080% | 101.8400 | 101.8600 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0026% | 1.4800 | 1.4803 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0053% | 1,208.2900 | 1,208.1100 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
