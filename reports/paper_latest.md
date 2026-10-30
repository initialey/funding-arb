# Paper trading status

Run #157 at 2026-10-30 20:42 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, DOGEUSDT, ZECUSDT, XRPUSDT, PEPEUSDT, BNBUSDT, INTCUSDT.

| metric | value |
|---|---|
| equity | 9,922.61 USDT |
| return since start | -0.77% (53.1 days) |
| annualised | -5.32% |
| realized (closed pairs) | -75.47 USDT |
| funding received this run | 0.1002 USDT |
| open pairs | 2 / 10 |
| free cash | 7,924.53 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| INTCUSDT | yes |  | 0.0340% | 65.5100 | 65.5500 | 0.1002 | -0.5164 | 0.49% | 132.0199 | 101.5% |
| ZECUSDT | yes | OPEN | 0.0100% | 1,227.9300 | 1,228.0600 | 0.0000 | 0.0000 | 0.50% | 2,443.6418 | 99.0% |
| BNBUSDT | no |  | -0.0129% | 699.3000 | 700.0000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0060% | 76,974.9000 | 76,970.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | -0.0018% | 0.0754 | 0.0755 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0041% | 2,239.4300 | 2,239.8600 | - | - | - | - | - |
| PEPEUSDT | no |  | -0.0231% | 0.0000 | 0.0000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0023% | 95.0000 | 95.0600 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 77.4700 | 77.4900 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0020% | 1.2493 | 1.2499 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
