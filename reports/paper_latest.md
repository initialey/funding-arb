# Paper trading status

Run #24 at 2026-09-15 13:28 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, BZUSDT, BNBUSDT, SOXLUSDT, OPENAIUSDT, DOGEUSDT.

| metric | value |
|---|---|
| equity | 9,992.26 USDT |
| return since start | -0.08% (7.8 days) |
| annualised | -3.62% |
| realized (closed pairs) | -7.20 USDT |
| funding received this run | 0.0334 USDT |
| open pairs | 1 / 10 |
| free cash | 8,992.80 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UAIUSDT | yes |  | 0.0100% | 0.3808 | 0.3808 | 0.5877 | -0.3786 | 0.25% | 1.1328 | 197.5% |
| BNBUSDT | no |  | 0.0001% | 720.7000 | 721.0000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0055% | 76,946.4000 | 76,980.4000 | - | - | - | - | - |
| BZUSDT | no |  | -0.1631% | 101.7800 | 101.7800 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0025% | 0.0831 | 0.0831 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0043% | 2,478.7100 | 2,479.1600 | - | - | - | - | - |
| OPENAIUSDT | no |  | 0.0000% | 1,479.2400 | 889.1000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0019% | 100.9100 | 100.9500 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 104.3000 | 104.3500 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0044% | 1.4341 | 1.4353 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0005% | 1,135.8200 | 1,136.6800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
