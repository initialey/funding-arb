# Paper trading status

Run #220 at 2026-11-26 18:21 UTC. Threshold 0.010% per funding interval, signal = mean of last 3 settled rates. Universe: BTCUSDT, ETHUSDT, SOLUSDT, SOXLUSDT, ZECUSDT, MUUSDT, DOGEUSDT, SOXSUSDT, QQQUSDT, SKHYUSDT.

| metric | value |
|---|---|
| equity | 9,895.15 USDT |
| return since start | -1.05% (80.0 days) |
| annualised | -4.78% |
| realized (closed pairs) | -104.88 USDT |
| funding received this run | 0.0970 USDT |
| open pairs | 3 / 10 |
| free cash | 6,895.12 USDT |
| skipped symbols | 0 |

## Positions & risk

| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |
|---|---|---|---|---|---|---|---|---|---|---|
| EVAAUSDT | yes |  | 0.0100% | 2.3622 | 2.3583 | 3.1547 | -0.8774 | 0.37% | 5.5692 | 135.8% |
| PIEVERSEUSDT | yes |  | 0.0240% | 4.0122 | 4.0096 | 0.9937 | -0.9840 | 0.61% | 7.2794 | 81.4% |
| ZECUSDT | yes | OPEN | 0.0100% | 702.2400 | 702.4400 | 0.0000 | 0.0000 | 0.50% | 1,397.4925 | 99.0% |
| BTCUSDT | no |  | 0.0068% | 60,491.6000 | 60,517.1000 | - | - | - | - | - |
| DOGEUSDT | no |  | 0.0078% | 0.0569 | 0.0569 | - | - | - | - | - |
| ETHUSDT | no |  | 0.0045% | 1,691.7600 | 1,692.5200 | - | - | - | - | - |
| MUUSDT | no |  | 0.0000% | 607.3600 | 607.5100 | - | - | - | - | - |
| QQQUSDT | no |  | 0.0009% | 636.8300 | 636.8400 | - | - | - | - | - |
| SKHYUSDT | no |  | 0.0000% | 110.8300 | 110.8200 | - | - | - | - | - |
| SOLUSDT | no |  | 0.0064% | 71.1000 | 71.1200 | - | - | - | - | - |
| SOXLUSDT | no |  | -0.0076% | 32.9000 | 32.9000 | - | - | - | - | - |
| SOXSUSDT | no |  | -0.0116% | 60.5100 | 60.4700 | - | - | - | - | - |

![equity](paper_equity.png)

_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. Liq. distance = how far mark must rise before liquidation._
