# Paper trading status

Run #4 at 2026-09-08 19:24 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, SUIUSDT, BNBUSDT, ADAUSDT, WLDUSDT.

| metric | value |
|---|---|
| equity | 9,997.28 USDT |
| return since start | -0.03% (1.1 days) |
| annualised | -9.32% |
| realized (closed pairs) | -2.72 USDT |
| funding received this run | 0.0475 USDT |
| open pairs | 0 / 10 |
| free cash | 9,997.28 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | no |  | 0.0048% | 0.2215 | 0.2215 | - | - | - | - | - |
| BNBUSDT | no | CLOSE | 0.0098% | 748.9000 | 749.3000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0034% | 78,362.1600 | 78,403.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0033% | 0.0897 | 0.0898 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0067% | 2,483.2900 | 2,484.2700 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0060% | 103.1900 | 103.2200 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0059% | 0.8125 | 0.8129 | - | - | - | - | - |
| WLDUSDT | no |  | 0.0067% | 0.4720 | 0.4721 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0078% | 1.4276 | 1.4284 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0010% | 1,154.2600 | 1,154.6300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
