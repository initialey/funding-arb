# Paper trading status

Run #6 at 2026-09-09 12:56 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, ADAUSDT, DOTUSDT, SUIUSDT, SPCXUSDT.

| metric | value |
|---|---|
| equity | 9,996.55 USDT |
| return since start | -0.03% (1.8 days) |
| annualised | -7.01% |
| realized (closed pairs) | -2.72 USDT |
| funding received this run | 0.0482 USDT |
| open pairs | 1 / 10 |
| free cash | 8,997.28 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| DOTUSDT | yes |  | 0.0100% | 1.1720 | 1.1728 | 0.0482 | -0.0280 | 0.47% | 2.4179 | 106.3% |
| ADAUSDT | no |  | 0.0067% | 0.2207 | 0.2209 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0039% | 79,574.6000 | 79,613.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0047% | 0.0914 | 0.0915 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0053% | 2,510.6500 | 2,512.1000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0040% | 104.7100 | 104.7900 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 151.5900 | 144.8400 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0062% | 0.8194 | 0.8196 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0089% | 1.4375 | 1.4383 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0093% | 1,266.7300 | 1,263.8400 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
