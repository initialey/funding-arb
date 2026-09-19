# Paper trading status

Run #36 at 2026-09-19 12:27 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, UNIUSDT, DOGEUSDT, OPENAIUSDT, NEARUSDT, ADAUSDT.

| metric | value |
|---|---|
| equity | 9,987.96 USDT |
| return since start | -0.12% (11.8 days) |
| annualised | -3.73% |
| realized (closed pairs) | -8.48 USDT |
| funding received this run | 0.2526 USDT |
| open pairs | 6 / 10 |
| free cash | 3,991.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | yes | OPEN | 0.0100% | 0.2259 | 0.2260 | 0.0000 | 0.0000 | 0.50% | 0.4496 | 99.0% |
| BNBUSDT | yes |  | 0.0100% | 768.5500 | 769.0000 | 0.1002 | 0.1628 | 0.51% | 1,520.9950 | 97.9% |
| NEARUSDT | yes |  | 0.0100% | 3.6387 | 3.6400 | 0.1547 | 0.1245 | 0.51% | 7.1514 | 96.5% |
| SOLUSDT | yes |  | 0.0100% | 111.8100 | 111.8400 | 0.0496 | -0.0430 | 0.49% | 224.2587 | 100.6% |
| UNIUSDT | yes |  | 0.0100% | 9.1390 | 9.1410 | 0.1012 | 0.1706 | 0.53% | 17.6697 | 93.3% |
| XRPUSDT | yes |  | 0.0100% | 1.4306 | 1.4310 | 0.0507 | 0.0699 | 0.51% | 2.8098 | 96.4% |
| BTCUSDT | no |  | 0.0073% | 81,245.2000 | 81,277.0000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0091% | 0.0883 | 0.0883 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0080% | 2,642.5000 | 2,643.5900 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,501.0000 | 888.0000 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0084% | 1,538.0400 | 1,538.4300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
