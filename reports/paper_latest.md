# Paper trading status

Run #44 at 2026-09-22 04:46 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, PEPEUSDT, SUIUSDT, UNIUSDT, ADAUSDT.

| metric | value |
|---|---|
| equity | 9,983.29 USDT |
| return since start | -0.17% (14.5 days) |
| annualised | -4.22% |
| realized (closed pairs) | -15.66 USDT |
| funding received this run | 0.1525 USDT |
| open pairs | 3 / 10 |
| free cash | 6,984.34 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes |  | 0.0100% | 787.2000 | 787.4000 | 0.0489 | 0.0331 | 0.48% | 1,602.0896 | 103.5% |
| UNIUSDT | yes |  | 0.0100% | 8.8760 | 8.8800 | 0.4960 | 0.2816 | 0.50% | 17.6697 | 99.1% |
| XRPUSDT | yes |  | 0.0100% | 1.5151 | 1.5150 | 0.4596 | -0.1114 | 0.58% | 2.8098 | 85.4% |
| ADAUSDT | no |  | 0.0091% | 0.2472 | 0.2474 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0044% | 85,464.1500 | 85,500.9000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0083% | 0.1016 | 0.1016 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0006% | 2,728.7400 | 2,729.2100 | - | - | - | - | - |
| PEPEUSDT | no |  | 0.0086% | 0.0000 | 0.0000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0078% | 116.5100 | 116.5200 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0088% | 1.0248 | 1.0252 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0056% | 1,461.5300 | 1,462.0300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
