# Paper trading status

Run #7 at 2026-09-09 19:14 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, SPCXUSDT, SOXLUSDT, BNBUSDT, SUIUSDT.

| metric | value |
|---|---|
| equity | 9,996.82 USDT |
| return since start | -0.03% (2.1 days) |
| annualised | -5.65% |
| realized (closed pairs) | -2.72 USDT |
| funding received this run | 0.0463 USDT |
| open pairs | 1 / 10 |
| free cash | 8,997.28 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| DOTUSDT | yes |  | 0.0100% | 1.1260 | 1.1273 | 0.0946 | 0.1916 | 0.43% | 2.4179 | 114.7% |
| BNBUSDT | no |  | 0.0033% | 740.8000 | 741.2000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0046% | 78,455.2200 | 78,485.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0063% | 0.0885 | 0.0885 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0055% | 2,481.1700 | 2,482.3100 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0037% | 103.1600 | 103.2000 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 125.4800 | 125.4900 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 148.0000 | 141.3300 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0016% | 0.7981 | 0.7985 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0065% | 1.4165 | 1.4174 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0004% | 1,259.1100 | 1,259.9300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
