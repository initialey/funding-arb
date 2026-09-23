# Paper trading status

Run #49 at 2026-09-23 19:39 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, UNIUSDT, DOGEUSDT, BCHUSDT, NEARUSDT, SUIUSDT.

| metric | value |
|---|---|
| equity | 9,980.43 USDT |
| return since start | -0.20% (16.1 days) |
| annualised | -4.44% |
| realized (closed pairs) | -17.69 USDT |
| funding received this run | 0.2564 USDT |
| open pairs | 5 / 10 |
| free cash | 4,982.31 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BCHUSDT | yes |  | 0.0100% | 347.5500 | 347.6300 | 0.0492 | -0.1928 | 0.48% | 703.3433 | 102.4% |
| BNBUSDT | yes |  | 0.0100% | 766.8500 | 767.2000 | 0.2924 | 0.1286 | 0.45% | 1,602.0896 | 108.9% |
| PEPEUSDT | yes |  | 0.0100% | 0.0000 | 0.0000 | 0.1924 | 0.2799 | 0.40% | 0.0000 | 125.1% |
| UNIUSDT | yes |  | 0.0100% | 9.1820 | 9.1870 | 0.7641 | 0.3398 | 0.54% | 17.6697 | 92.4% |
| ZECUSDT | yes |  | 0.0100% | 1,516.9300 | 1,517.0900 | 0.0982 | -0.0739 | 0.45% | 3,191.6219 | 110.4% |
| BTCUSDT | no |  | 0.0063% | 84,425.9100 | 84,469.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0004% | 0.0924 | 0.0924 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0053% | 2,673.9800 | 2,675.4300 | - | - | - | - | - |
| NEARUSDT | no |  | 0.0093% | 4.3800 | 4.3820 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0002% | 114.5700 | 114.5700 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0076% | 0.9641 | 0.9646 | - | - | - | - | - |
| XRPUSDT | no | CLOSE | 0.0077% | 1.4988 | 1.4996 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
