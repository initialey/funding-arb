# Paper trading status

Run #152 at 2026-10-29 05:38 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, DOGEUSDT, XRPUSDT, BNBUSDT, SOXSUSDT, LTCUSDT.

| metric | value |
|---|---|
| equity | 9,925.15 USDT |
| return since start | -0.75% (51.5 days) |
| annualised | -5.31% |
| realized (closed pairs) | -74.29 USDT |
| funding received this run | 0.0490 USDT |
| open pairs | 1 / 10 |
| free cash | 8,925.71 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| XRPUSDT | yes |  | 0.0100% | 1.3019 | 1.3025 | 0.1486 | 0.0414 | 0.48% | 2.6444 | 103.1% |
| BNBUSDT | no |  | 0.0100% | 756.8000 | 757.1000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0065% | 80,283.3700 | 80,320.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0086% | 0.0789 | 0.0789 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0070% | 2,325.9600 | 2,326.9500 | - | - | - | - | - |
| LTCUSDT | no |  | 0.0025% | 57.9900 | 58.0000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0061% | 100.5700 | 100.6200 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 100.7100 | 100.7200 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 42.4200 | 42.4400 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0017% | 1,250.6300 | 1,251.2700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
