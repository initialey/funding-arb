# Paper trading status

Run #43 at 2026-09-21 20:24 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, SUIUSDT, UNIUSDT, PEPEUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,983.97 USDT |
| return since start | -0.16% (14.1 days) |
| annualised | -4.15% |
| realized (closed pairs) | -15.66 USDT |
| funding received this run | 0.1896 USDT |
| open pairs | 3 / 10 |
| free cash | 6,984.34 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes | OPEN | 0.0100% | 805.0500 | 805.2000 | 0.0000 | 0.0000 | 0.50% | 1,602.0896 | 99.0% |
| UNIUSDT | yes |  | 0.0100% | 8.8290 | 8.8420 | 0.4460 | 0.7881 | 0.49% | 17.6697 | 100.1% |
| XRPUSDT | yes |  | 0.0100% | 1.5191 | 1.5200 | 0.4060 | 0.2425 | 0.58% | 2.8098 | 85.0% |
| ADAUSDT | no | CLOSE | 0.0091% | 0.2467 | 0.2469 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0030% | 86,941.5300 | 86,991.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0075% | 0.1008 | 0.1009 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0019% | 2,799.0200 | 2,800.0000 | - | - | - | - | - |
| PEPEUSDT | no |  | 0.0041% | 0.0000 | 0.0000 | - | - | - | - | - |
| SOLUSDT | no | CLOSE | 0.0089% | 119.3500 | 119.4000 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0047% | 1.0292 | 1.0298 | - | - | - | - | - |
| ZECUSDT | no | CLOSE | 0.0073% | 1,478.4300 | 1,478.7800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
