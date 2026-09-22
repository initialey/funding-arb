# Paper trading status

Run #46 at 2026-09-22 19:43 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, XRPUSDT, ZECUSDT, DOGEUSDT, SOXLUSDT, UNIUSDT, PEPEUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,981.90 USDT |
| return since start | -0.18% (15.1 days) |
| annualised | -4.38% |
| realized (closed pairs) | -15.66 USDT |
| funding received this run | 0.2542 USDT |
| open pairs | 5 / 10 |
| free cash | 4,984.34 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes |  | 0.0100% | 786.7500 | 786.9000 | 0.1468 | 0.0021 | 0.48% | 1,602.0896 | 103.6% |
| NEARUSDT | yes |  | 0.0100% | 4.3553 | 4.3580 | 0.0479 | -0.0608 | 0.46% | 9.0559 | 107.9% |
| PEPEUSDT | yes |  | 0.0100% | 0.0000 | 0.0000 | 0.0495 | -0.2043 | 0.49% | 0.0000 | 101.0% |
| UNIUSDT | yes |  | 0.0100% | 9.1960 | 9.1980 | 0.5996 | 0.1710 | 0.54% | 17.6697 | 92.1% |
| XRPUSDT | yes |  | 0.0100% | 1.5865 | 1.5867 | 0.5707 | -0.0088 | 0.64% | 2.8098 | 77.1% |
| BTCUSDT | no |  | 0.0067% | 86,380.3800 | 86,425.4000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0070% | 0.1001 | 0.1001 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0071% | 2,755.2100 | 2,756.6000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0050% | 118.3100 | 118.3700 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 151.2200 | 151.2800 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0083% | 1,525.6100 | 1,525.8500 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
