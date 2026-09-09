# Paper trading status

Run #5 at 2026-09-09 04:33 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, DOGEUSDT, SUIUSDT, BNBUSDT, ADAUSDT, DOTUSDT.

| metric | value |
|---|---|
| equity | 9,996.53 USDT |
| return since start | -0.03% (1.4 days) |
| annualised | -8.76% |
| realized (closed pairs) | -2.72 USDT |
| funding received this run | 0.0000 USDT |
| open pairs | 1 / 10 |
| free cash | 8,997.28 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| DOTUSDT | yes | OPEN | 0.0100% | 1.2150 | 1.2159 | 0.0000 | 0.0000 | 0.50% | 2.4179 | 99.0% |
| ADAUSDT | no |  | 0.0053% | 0.2191 | 0.2193 | - | - | - | - | - |
| BNBUSDT | no |  | 0.0098% | 751.3000 | 751.7000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0042% | 78,852.5000 | 78,893.7000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0037% | 0.0903 | 0.0904 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0071% | 2,496.3900 | 2,497.4700 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0049% | 103.8900 | 103.9400 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0062% | 0.8156 | 0.8158 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0084% | 1.4287 | 1.4290 | - | - | - | - | - |
| ZECUSDT | no |  | -0.0050% | 1,215.1900 | 1,216.0300 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
