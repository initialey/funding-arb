# Paper trading status

Run #206 at 2026-11-19 17:19 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, DOGEUSDT, SOXSUSDT, ANTUSDT, MUUSDT, QQQUSDT.

| metric | value |
|---|---|
| equity | 9,898.43 USDT |
| return since start | -1.02% (73.0 days) |
| annualised | -5.08% |
| realized (closed pairs) | -100.48 USDT |
| funding received this run | 0.1833 USDT |
| open pairs | 1 / 10 |
| free cash | 8,899.52 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0100% | 5.1307 | 5.1241 | 1.2368 | -1.5716 | 5.50% | 5.5692 | 8.5% |
| ANTUSDT | no |  | 0.0000% | 95.7600 | 95.8200 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0029% | 62,319.0600 | 62,343.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0047% | 0.0580 | 0.0580 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0045% | 1,752.8600 | 1,753.5800 | - | - | - | - | - |
| MUUSDT | no |  | 0.0057% | 694.4300 | 693.9900 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0018% | 650.1500 | 650.1100 | - | - | - | - | - |
| SOLUSDT | no |  | -0.0009% | 72.8300 | 72.8500 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 45.6300 | 45.6200 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 62.8500 | 62.8200 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0090% | 904.7200 | 904.7700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
