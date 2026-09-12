# Paper trading status

Run #16 at 2026-09-12 18:19 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, BNBUSDT, OPENAIUSDT, DOGEUSDT, UNIUSDT, UAIUSDT.

| metric | value |
|---|---|
| equity | 9,993.25 USDT |
| return since start | -0.07% (5.0 days) |
| annualised | -4.91% |
| realized (closed pairs) | -6.00 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,994.00 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes | OPEN | 0.0100% | 0.5692 | 0.5699 | 0.0000 | 0.0000 | 0.50% | 1.1328 | 99.0% |
| BNBUSDT | no |  | 0.0034% | 730.0000 | 730.5000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0031% | 77,106.8000 | 77,133.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0019% | 0.0848 | 0.0848 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0034% | 2,522.1300 | 2,523.0100 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,486.8700 | 908.8000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0010% | 101.6600 | 101.7100 | - | - | - | - | - |
| UNIUSDT | no |  | -0.0099% | 6.2890 | 6.2950 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0018% | 1.3633 | 1.3641 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0031% | 1,132.2600 | 1,132.7400 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
