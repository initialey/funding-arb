# Paper trading status

Run #47 at 2026-09-23 04:38 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, XRPUSDT, UNIUSDT, DOGEUSDT, BCHUSDT, SOXLUSDT, NEARUSDT.

| metric | value |
|---|---|
| equity | 9,981.49 USDT |
| return since start | -0.19% (15.4 days) |
| annualised | -4.37% |
| realized (closed pairs) | -17.06 USDT |
| funding received this run | 0.2548 USDT |
| open pairs | 5 / 10 |
| free cash | 4,982.94 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| BNBUSDT | yes |  | 0.0100% | 796.6500 | 796.9000 | 0.1963 | 0.0631 | 0.49% | 1,602.0896 | 101.1% |
| PEPEUSDT | yes |  | 0.0100% | 0.0000 | 0.0000 | 0.1003 | 0.8123 | 0.52% | 0.0000 | 95.9% |
| UNIUSDT | yes |  | 0.0100% | 10.5030 | 10.5010 | 0.6587 | -0.0460 | 0.72% | 17.6697 | 68.2% |
| XRPUSDT | yes |  | 0.0100% | 1.6460 | 1.6459 | 0.6290 | -0.1180 | 0.70% | 2.8098 | 70.7% |
| ZECUSDT | yes | OPEN | 0.0100% | 1,603.7900 | 1,604.2100 | 0.0000 | 0.0000 | 0.50% | 3,191.6219 | 99.0% |
| BCHUSDT | no |  | 0.0056% | 339.7500 | 339.8800 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0057% | 87,094.3100 | 87,148.5000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0061% | 0.1036 | 0.1036 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0068% | 2,779.8900 | 2,781.4100 | - | - | - | - | - |
| NEARUSDT | no | CLOSE | 0.0093% | 4.3309 | 4.3340 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0034% | 119.3700 | 119.4400 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 151.0700 | 151.0800 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
