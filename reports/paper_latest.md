# Paper trading status

Run #160 at 2026-10-31 19:55 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, SOXLUSDT, PEPEUSDT, BNBUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,920.43 USDT |
| return since start | -0.80% (54.1 days) |
| annualised | -5.37% |
| realized (closed pairs) | -78.89 USDT |
| funding received this run | 0.0439 USDT |
| open pairs | 1 / 10 |
| free cash | 8,921.11 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BTCUSDT | yes |  | 0.0100% | 77,529.8700 | 77,540.5000 | 0.0501 | 0.0201 | 0.50% | 154,028.2587 | 98.7% |
| BNBUSDT | no |  | -0.0046% | 705.5500 | 706.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0040% | 0.0758 | 0.0758 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0032% | 2,252.0200 | 2,253.0800 | - | - | - | - | - |
| INTCUSDT | no | CLOSE | 0.0094% | 64.9300 | 64.9300 | - | - | - | - | - |
| PEPEUSDT | no |  | 0.0095% | 0.0000 | 0.0000 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0085% | 695.1200 | 695.1200 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0005% | 95.7600 | 95.8100 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 77.1300 | 77.1200 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0018% | 1.2511 | 1.2512 | - | - | - | - | - |
| ZECUSDT | no | CLOSE | 0.0063% | 1,273.5000 | 1,273.8000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
