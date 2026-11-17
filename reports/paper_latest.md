# Paper trading status

Run #201 at 2026-11-17 07:46 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, SOXSUSDT, ZECUSDT, DOGEUSDT, SNXXUSDT, EVAAUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,896.59 USDT |
| return since start | -1.03% (70.6 days) |
| annualised | -5.35% |
| realized (closed pairs) | -100.48 USDT |
| funding received this run | 0.3152 USDT |
| open pairs | 1 / 10 |
| free cash | 8,899.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0223% | 4.1220 | 4.1090 | 0.4613 | -2.6373 | 1.40% | 5.5692 | 35.1% |
| BTCUSDT | no |  | 0.0018% | 64,589.8000 | 64,625.4000 | - | - | - | - | - |
| DOGEUSDT | no |  | -0.0065% | 0.0590 | 0.0590 | - | - | - | - | - |
| ETHUSDT | no |  | -0.0031% | 1,827.0000 | 1,827.8400 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0000% | 663.1900 | 663.2500 | - | - | - | - | - |
| SNXXUSDT | no | CLOSE | 0.0019% | 2.9890 | 2.9890 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0050% | 72.8500 | 72.9100 | - | - | - | - | - |
| SOXLUSDT | no | CLOSE | 0.0000% | 50.1600 | 50.1600 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 57.5900 | 57.5500 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0021% | 924.3700 | 924.7300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
