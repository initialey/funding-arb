# Paper trading status

Run #50 at 2026-09-24 04:39 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, NEARUSDT, DOGEUSDT, BCHUSDT, UNIUSDT, SUIUSDT.

| metric | value |
|---|---|
| equity | 9,977.40 USDT |
| return since start | -0.23% (16.4 days) |
| annualised | -5.01% |
| realized (closed pairs) | -20.22 USDT |
| funding received this run | 0.2089 USDT |
| open pairs | 3 / 10 |
| free cash | 6,979.78 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BCHUSDT | yes |  | 0.0100% | 341.8500 | 341.8200 | 0.0975 | -0.3433 | 0.47% | 703.3433 | 105.7% |
| NEARUSDT | yes | OPEN | 0.0100% | 4.4160 | 4.4170 | 0.0000 | 0.0000 | 0.50% | 8.7881 | 99.0% |
| ZECUSDT | yes |  | 0.0100% | 1,509.1500 | 1,509.4800 | 0.1453 | -0.0203 | 0.44% | 3,191.6219 | 111.5% |
| BNBUSDT | no | CLOSE | 0.0098% | 767.4000 | 767.7000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0053% | 83,840.4200 | 83,872.8000 | - | - | - | - | - |
| DOGEUSDT | no |  | -0.0007% | 0.0934 | 0.0935 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0042% | 2,674.3000 | 2,675.7700 | - | - | - | - | - |
| PEPEUSDT | no | CLOSE | 0.0086% | 0.0000 | 0.0000 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0001% | 114.8100 | 114.8800 | - | - | - | - | - |
| SUIUSDT | no |  | 0.0062% | 0.9596 | 0.9602 | - | - | - | - | - |
| UNIUSDT | no | CLOSE | 0.0094% | 9.2370 | 9.2420 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0045% | 1.4940 | 1.4944 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
