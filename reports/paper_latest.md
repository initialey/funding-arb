# Paper trading status

Run #18 at 2026-09-13 13:17 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, BNBUSDT, UNIUSDT, DOGEUSDT, OPENAIUSDT, UAIUSDT.

| metric | value |
|---|---|
| equity | 9,991.97 USDT |
| return since start | -0.08% (5.8 days) |
| annualised | -5.05% |
| realized (closed pairs) | -6.00 USDT |
| funding received this run | 0.0477 USDT |
| open pairs | 1 / 10 |
| free cash | 8,994.00 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes |  | 0.0102% | 0.5123 | 0.5114 | 0.1015 | -1.3871 | 0.41% | 1.1328 | 121.1% |
| BNBUSDT | no |  | 0.0031% | 715.3500 | 715.5000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0060% | 76,716.3300 | 76,751.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0020% | 0.0834 | 0.0835 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0078% | 2,475.0500 | 2,475.9900 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,393.7100 | 856.4000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0045% | 99.7400 | 99.7800 | - | - | - | - | - |
| UNIUSDT | no |  | -0.0140% | 6.2500 | 6.2520 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0033% | 1.3395 | 1.3404 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0076% | 1,088.8700 | 1,090.1400 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
