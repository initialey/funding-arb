# Paper trading status

Run #48 at 2026-09-23 13:35 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, UNIUSDT, BCHUSDT, DOGEUSDT, SUIUSDT, ADAUSDT.

| metric | value |
|---|---|
| equity | 9,980.63 USDT |
| return since start | -0.19% (15.8 days) |
| annualised | -4.47% |
| realized (closed pairs) | -17.06 USDT |
| funding received this run | 0.2566 USDT |
| open pairs | 6 / 10 |
| free cash | 3,982.94 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BCHUSDT | yes | OPEN | 0.0100% | 353.4300 | 353.6500 | 0.0000 | 0.0000 | 0.50% | 703.3433 | 99.0% |
| BNBUSDT | yes |  | 0.0100% | 780.3500 | 780.6000 | 0.2447 | 0.0650 | 0.47% | 1,602.0896 | 105.3% |
| PEPEUSDT | yes |  | 0.0100% | 0.0000 | 0.0000 | 0.1482 | 0.0925 | 0.46% | 0.0000 | 107.9% |
| UNIUSDT | yes |  | 0.0100% | 9.5250 | 9.5210 | 0.7124 | -0.1649 | 0.58% | 17.6697 | 85.5% |
| XRPUSDT | yes |  | 0.0100% | 1.5731 | 1.5741 | 0.6847 | 0.2752 | 0.63% | 2.8098 | 78.6% |
| ZECUSDT | yes |  | 0.0100% | 1,633.4600 | 1,634.1500 | 0.0509 | 0.0817 | 0.52% | 3,191.6219 | 95.4% |
| ADAUSDT | no |  | 0.0069% | 0.2480 | 0.2481 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0040% | 85,546.7200 | 85,597.8000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0040% | 0.0993 | 0.0993 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0050% | 2,713.4500 | 2,714.8900 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0017% | 116.5700 | 116.6600 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0076% | 1.0086 | 1.0089 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
