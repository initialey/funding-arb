# Paper trading status

Run #61 at 2026-09-27 19:44 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, WLDUSDT, QNTUSDT, NEARUSDT, DOGEUSDT, SUIUSDT.

| metric | value |
|---|---|
| equity | 9,967.79 USDT |
| return since start | -0.32% (20.1 days) |
| annualised | -5.86% |
| realized (closed pairs) | -30.49 USDT |
| funding received this run | 0.0821 USDT |
| open pairs | 3 / 10 |
| free cash | 6,969.51 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| NEARUSDT | yes | OPEN | 0.0100% | 5.4566 | 5.4600 | 0.0000 | 0.0000 | 0.50% | 10.8589 | 99.0% |
| SUIUSDT | yes | OPEN | 0.0100% | 1.2726 | 1.2731 | 0.0000 | 0.0000 | 0.50% | 2.5325 | 99.0% |
| WLDUSDT | yes |  | 0.0100% | 0.5599 | 0.5602 | 0.1549 | 0.3789 | 0.55% | 1.0633 | 89.9% |
| BTCUSDT | no |  | -0.0005% | 84,726.1900 | 84,776.3000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0090% | 0.0972 | 0.0972 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0077% | 2,692.0100 | 2,693.3100 | - | - | - | - | - |
| QNTUSDT | no |  | -0.0160% | 187.3800 | 187.3700 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0027% | 123.0500 | 123.1000 | - | - | - | - | - |
| UNIUSDT | no | CLOSE | 0.0087% | 9.7450 | 9.7480 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0093% | 1.5337 | 1.5343 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0063% | 1,603.4600 | 1,604.3800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
