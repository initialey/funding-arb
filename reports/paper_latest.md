# Paper trading status

Run #17 at 2026-09-13 04:39 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, LSKUSDT, XRPUSDT, OPENAIUSDT, BNBUSDT, UNIUSDT, DOGEUSDT.

| metric | value |
|---|---|
| equity | 9,990.94 USDT |
| return since start | -0.09% (5.5 days) |
| annualised | -6.07% |
| realized (closed pairs) | -6.00 USDT |
| funding received this run | 0.0538 USDT |
| open pairs | 1 / 10 |
| free cash | 8,994.00 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes |  | 0.0100% | 0.6126 | 0.6106 | 0.0538 | -2.3710 | 0.58% | 1.1328 | 84.9% |
| BNBUSDT | no |  | 0.0047% | 726.3500 | 726.6000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0045% | 77,192.0000 | 77,222.4000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0019% | 0.0846 | 0.0846 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0059% | 2,519.7800 | 2,520.6200 | - | - | - | - | - |
| LSKUSDT | no |  | -0.8839% | 1.0527 | 1.0654 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,488.1200 | 893.3000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0021% | 101.6600 | 101.7100 | - | - | - | - | - |
| UNIUSDT | no |  | -0.0159% | 6.3670 | 6.3660 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0024% | 1.3634 | 1.3641 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0032% | 1,139.6600 | 1,140.0300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
