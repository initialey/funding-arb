# Paper trading status

Run #8 at 2026-09-10 04:32 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, ZECUSDT, DOGEUSDT, XRPUSDT, UNIUSDT, BNBUSDT, SPCXUSDT, SOXLUSDT.

| metric | value |
|---|---|
| equity | 9,995.21 USDT |
| return since start | -0.05% (2.4 days) |
| annualised | -7.15% |
| realized (closed pairs) | -4.04 USDT |
| funding received this run | 0.0325 USDT |
| open pairs | 1 / 10 |
| free cash | 8,995.96 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| UNIUSDT | yes | OPEN | 0.0100% | 6.0800 | 6.0860 | 0.0000 | 0.0000 | 0.50% | 12.0995 | 99.0% |
| BNBUSDT | no |  | -0.0004% | 722.5500 | 723.0000 | - | - | - | - | - |
| BTCUSDT | no |  | 0.0043% | 78,377.3000 | 78,410.2000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0042% | 0.0860 | 0.0860 | - | - | - | - | - |
| DOTUSDT | no | CLOSE | 0.0090% | 1.1110 | 1.1118 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0040% | 2,478.7000 | 2,479.7600 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0016% | 102.0900 | 102.1500 | - | - | - | - | - |
| SOXLUSDT | no |  | 0.0000% | 123.9000 | 123.9000 | - | - | - | - | - |
| SPCXUSDT | no |  | 0.0000% | 147.2500 | 140.6900 | - | - | - | - | - |
| XRPUSDT | no |  | 0.0031% | 1.3921 | 1.3929 | - | - | - | - | - |
| ZECUSDT | no |  | 0.0047% | 1,250.9900 | 1,251.7000 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
