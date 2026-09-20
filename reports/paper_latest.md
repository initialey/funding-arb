# Paper trading status

Run #39 at 2026-09-20 13:01 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, AVAXUSDT, ONEUSDT, UNIUSDT, PEPEUSDT.

| metric | value |
|---|---|
| equity | 9,985.69 USDT |
| return since start | -0.14% (12.8 days) |
| annualised | -4.08% |
| realized (closed pairs) | -11.04 USDT |
| funding received this run | 0.2991 USDT |
| open pairs | 6 / 10 |
| free cash | 3,988.96 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| ADAUSDT | yes |  | 0.0100% | 0.2220 | 0.2221 | 0.1487 | -0.1060 | 0.48% | 0.4496 | 102.5% |
| NEARUSDT | yes |  | 0.0100% | 3.7437 | 3.7440 | 0.3055 | -0.0162 | 0.54% | 7.1514 | 91.0% |
| SOLUSDT | yes |  | 0.0100% | 108.3500 | 108.4000 | 0.1952 | 0.0512 | 0.46% | 224.2587 | 107.0% |
| UNIUSDT | yes |  | 0.0100% | 8.6410 | 8.6410 | 0.2482 | 0.0548 | 0.47% | 17.6697 | 104.5% |
| XRPUSDT | yes |  | 0.0100% | 1.3799 | 1.3805 | 0.1989 | 0.1432 | 0.48% | 2.8098 | 103.6% |
| ZECUSDT | yes | OPEN | 0.0100% | 1,454.5800 | 1,454.6900 | 0.0000 | 0.0000 | 0.50% | 2,894.6866 | 99.0% |
| AVAXUSDT | no | CLOSE | 0.0099% | 10.4260 | 10.4300 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0081% | 80,488.2000 | 80,513.4000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0065% | 0.0851 | 0.0852 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0039% | 2,580.4800 | 2,581.3800 | - | - | - | - | - |
| ONEUSDT | no |  | -0.3742% | 0.0038 | 0.0046 | - | - | - | - | - |
| PEPEUSDT | no |  | 0.0068% | 0.0000 | 0.0000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
