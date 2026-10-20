# Paper trading status

Run #125 at 2026-10-20 04:40 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, SOXSUSDT, QQQUSDT, BNBUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,931.46 USDT |
| return since start | -0.69% (42.5 days) |
| annualised | -5.89% |
| realized (closed pairs) | -67.14 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 2 / 10 |
| free cash | 7,932.86 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| QQQUSDT | yes |  | 0.0181% | 718.1600 | 718.1600 | 0.0000 | 0.1026 | 0.49% | 1,441.8109 | 100.8% |
| ZECUSDT | yes | OPEN | 0.0100% | 1,147.8500 | 1,148.1600 | 0.0000 | 0.0000 | 0.50% | 2,284.2786 | 99.0% |
| BNBUSDT | no |  | 0.0067% | 730.5500 | 730.9000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0042% | 82,044.1200 | 82,087.7000 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0064% | 2,411.6100 | 2,412.6900 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0049% | 4.8231 | 4.8250 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0003% | 105.1700 | 105.2100 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 95.8600 | 95.8800 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 48.0800 | 48.0800 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0043% | 1.3057 | 1.3063 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
