# Paper trading status

Run #151 at 2026-10-28 20:59 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, XRPUSDT, DOGEUSDT, BNBUSDT, SOXSUSDT, SKHYUSDT.

| metric | value |
|---|---|
| equity | 9,925.09 USDT |
| return since start | -0.75% (51.1 days) |
| annualised | -5.35% |
| realized (closed pairs) | -74.29 USDT |
| funding received this run | 0.0501 USDT |
| open pairs | 1 / 10 |
| free cash | 8,925.71 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| XRPUSDT | yes |  | 0.0100% | 1.3311 | 1.3317 | 0.0996 | 0.0373 | 0.50% | 2.6444 | 98.7% |
| BNBUSDT | no |  | 0.0089% | 755.3500 | 755.4000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0084% | 81,289.7200 | 81,325.3000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0071% | 0.0803 | 0.0803 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0076% | 2,359.8200 | 2,360.8800 | - | - | - | - | - |
| SKHYUSDT | no |  | 0.0000% | 160.2800 | 160.2800 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0062% | 102.5100 | 102.5300 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 102.7300 | 102.8400 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 41.6300 | 41.6300 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0036% | 1,298.6300 | 1,299.3700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
