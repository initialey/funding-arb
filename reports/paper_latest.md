# Paper trading status

Run #123 at 2026-10-19 15:32 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, SOXSUSDT, NEARUSDT, QQQUSDT, BNBUSDT.

| metric | value |
|---|---|
| equity | 9,932.11 USDT |
| return since start | -0.68% (41.9 days) |
| annualised | -5.91% |
| realized (closed pairs) | -67.14 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,932.86 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| QQQUSDT | yes | OPEN | 0.0294% | 724.5100 | 724.3600 | 0.0000 | 0.0000 | 0.50% | 1,441.8109 | 99.0% |
| BNBUSDT | no |  | 0.0008% | 726.5500 | 726.8000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0025% | 82,217.6500 | 82,249.7000 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0035% | 2,408.6700 | 2,409.6600 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0073% | 4.9229 | 4.9280 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0012% | 104.6000 | 104.7000 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0140% | 104.2600 | 104.3000 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0045% | 43.8100 | 43.8300 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0011% | 1.3052 | 1.3059 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0088% | 1,130.4500 | 1,130.3600 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
