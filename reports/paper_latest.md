# Paper trading status

Run #215 at 2026-11-23 20:05 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, SOXSUSDT, ZECUSDT, QQQUSDT, DOGEUSDT, OPENAIUSDT, MUUSDT.

| metric | value |
|---|---|
| equity | 9,896.40 USDT |
| return since start | -1.04% (77.1 days) |
| annualised | -4.90% |
| realized (closed pairs) | -103.83 USDT |
| funding received this run | 0.3779 USDT |
| open pairs | 3 / 10 |
| free cash | 6,896.17 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0199% | 2.9976 | 2.9988 | 2.7424 | -0.0152 | 0.58% | 5.5692 | 85.8% |
| PIEVERSEUSDT | yes |  | 0.0105% | 3.6188 | 3.6164 | 0.1567 | -0.8950 | 0.49% | 7.2794 | 101.2% |
| QQQUSDT | yes |  | 0.0116% | 650.1900 | 650.1900 | 0.4999 | -0.0084 | 0.55% | 1,240.2189 | 90.7% |
| BTCUSDT | no |  | 0.0023% | 61,199.2000 | 61,222.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0043% | 0.0567 | 0.0567 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0004% | 1,728.0800 | 1,729.3000 | - | - | - | - | - |
| MUUSDT | no |  | 0.0027% | 701.0300 | 701.1500 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,235.9700 | 726.6000 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0005% | 72.9800 | 73.0400 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 42.2900 | 42.2800 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0109% | 52.1900 | 52.2500 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0038% | 800.8800 | 801.1500 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
