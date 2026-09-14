# Paper trading status

Run #21 at 2026-09-14 14:59 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, OPENAIUSDT, SOXLUSDT, FILUSDT, DOGEUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,992.64 USDT |
| return since start | -0.07% (6.9 days) |
| annualised | -3.90% |
| realized (closed pairs) | -7.20 USDT |
| funding received this run | 0.1026 USDT |
| open pairs | 1 / 10 |
| free cash | 8,992.80 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes |  | 0.0270% | 0.5302 | 0.5310 | 0.4758 | 0.1204 | 0.44% | 1.1328 | 113.6% |
| BNBUSDT | no |  | 0.0094% | 721.4500 | 721.9000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0069% | 78,520.2700 | 78,560.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0011% | 0.0838 | 0.0838 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0037% | 2,501.9300 | 2,503.4500 | - | - | - | - | - |
| FILUSDT | no |  | 0.0060% | 0.9864 | 0.9867 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,438.0900 | 864.6000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0043% | 101.6000 | 101.6700 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0173% | 101.2600 | 101.2600 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0021% | 1.3994 | 1.3998 | - | - | - | - | - |
| ZECUSDT | no | CLOSE | 0.0086% | 1,141.8600 | 1,142.6600 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
