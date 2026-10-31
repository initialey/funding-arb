# Paper trading status

Run #158 at 2026-10-31 05:27 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, INTCUSDT, XRPUSDT, PEPEUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,922.86 USDT |
| return since start | -0.77% (53.5 days) |
| annualised | -5.26% |
| realized (closed pairs) | -75.47 USDT |
| funding received this run | 0.1897 USDT |
| open pairs | 2 / 10 |
| free cash | 7,924.53 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| INTCUSDT | yes |  | 0.0366% | 64.9200 | 64.9300 | 0.2387 | -0.7347 | 0.48% | 132.0199 | 103.4% |
| ZECUSDT | yes |  | 0.0100% | 1,257.2000 | 1,258.0100 | 0.0512 | 0.2756 | 0.52% | 2,443.6418 | 94.4% |
| BNBUSDT | no |  | -0.0130% | 702.4000 | 702.9000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0060% | 77,221.5800 | 77,220.0000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0012% | 0.0752 | 0.0753 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0054% | 2,240.1900 | 2,241.1600 | - | - | - | - | - |
| PEPEUSDT | no |  | -0.0204% | 0.0000 | 0.0000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0052% | 95.9800 | 96.0200 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 77.4500 | 77.4600 | - | - | - | - | - |
| XRPUSDT | no |  | -0.0025% | 1.2451 | 1.2455 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
