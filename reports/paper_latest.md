# Paper trading status

Run #137 at 2026-10-24 04:27 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, SOXLUSDT, DOGEUSDT, XRPUSDT, BNBUSDT, SOXSUSDT, PEPEUSDT.

| metric | value |
|---|---|
| equity | 9,927.54 USDT |
| return since start | -0.72% (46.4 days) |
| annualised | -5.69% |
| realized (closed pairs) | -71.71 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,928.29 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes | OPEN | 0.0100% | 739.2500 | 739.5000 | 0.0000 | 0.0000 | 0.50% | 1,471.1443 | 99.0% |
| BTCUSDT | no |  | 0.0067% | 80,823.6400 | 80,861.6000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0031% | 0.0788 | 0.0788 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0050% | 2,379.4100 | 2,380.3000 | - | - | - | - | - |
| PEPEUSDT | no |  | 0.0049% | 0.0000 | 0.0000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0069% | 102.5600 | 102.6000 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 84.1500 | 84.1600 | - | - | - | - | - |
| SOXSUSDT | no |  | 0.0000% | 52.1700 | 52.1800 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0069% | 1.2899 | 1.2906 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0037% | 1,172.7700 | 1,173.2200 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
