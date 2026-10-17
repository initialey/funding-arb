# Paper trading status

Run #118 at 2026-10-17 18:25 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, NEARUSDT, SOXLUSDT, BNBUSDT, WLDUSDT, DOGEUSDT.

| metric | value |
|---|---|
| equity | 9,934.28 USDT |
| return since start | -0.66% (40.0 days) |
| annualised | -5.99% |
| realized (closed pairs) | -64.48 USDT |
| funding received this run | 0.0496 USDT |
| open pairs | 2 / 10 |
| free cash | 7,935.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| SOXLUSDT | yes |  | 0.0132% | 93.9600 | 93.9700 | 0.0000 | 0.2119 | 0.50% | 187.4826 | 99.5% |
| ZECUSDT | yes |  | 0.0100% | 1,134.1800 | 1,134.5100 | 0.1510 | -0.1028 | 0.49% | 2,275.8607 | 100.7% |
| BNBUSDT | no |  | 0.0013% | 715.5000 | 715.8000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0049% | 81,504.1500 | 81,538.0000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0036% | 0.0797 | 0.0797 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0047% | 2,417.7300 | 2,418.6600 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0077% | 4.9290 | 4.9320 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0010% | 103.7600 | 103.8100 | - | - | - | - | - |
| WLDUSDT | no |  | 0.0049% | 0.4982 | 0.4982 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0004% | 1.2962 | 1.2968 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
