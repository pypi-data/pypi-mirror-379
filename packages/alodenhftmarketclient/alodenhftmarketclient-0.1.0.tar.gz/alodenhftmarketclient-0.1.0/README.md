# market-client (Python)

A high‑level Python client for the HFT Simulator gateway (server/) that mirrors the website's behavior but hides the server details.
- Automatically performs handshake and login
- Keeps a persistent CMD WebSocket session
- Optionally auto-subscribes to the MD stream and maintains simple in‑memory state (symbols, book snapshots)
- Provides high‑level helpers (get_symbols, get_book, place_order, list_orders)
- Minimizes HTTP usage: performs requests over a persistent CMD WebSocket session
- MD-driven book maintenance and candle aggregation with minimal refreshes

## Install

This package depends on `httpx` and `websockets`.

- With pip (editable for local dev):

```
python3 -m venv .venv
. .venv/bin/activate
pip install -e ./market-client
```

Or install directly:

```
pip install httpx>=0.24 websockets>=10
```

## Quickstart (high‑level)

```python
import asyncio
from market_client import MarketClient

async def main():
    # One call connects: handshake -> CMD -> login -> MD
    client = await MarketClient.connect("http://localhost:8000", connect_md=True)

    # High-level helpers
    symbols = await client.get_symbols()
    print("symbols:", symbols[:3])

    book = await client.get_book(symbols[0]["sym"], depth=10)
    print("book:", book)

    # Candles: configure and read
    await client.configure_candles(symbols[0]["sym"], interval_ms=1000, depth=50)
    print("candles:", client.get_candles(symbols[0]["sym"])[:3])

    # Orders
    # await client.place_order(sym, side="buy", price="100.00", qty=1)
    # orders = await client.list_orders()
    # print("orders:", orders)

    await client.aclose()

asyncio.run(main())
```

See `examples/simple.py` for a runnable sample.

## Notes
- The client auto-fills the JSON envelope (`type`, `ver`, `msg_id`, `ts`) and matches responses by `corr_id`.
- Tokens are handled automatically by `connect()`.
- When `connect_md=True`, the client starts a background task to process MD events and keeps a simple book snapshot per symbol. Future iterations can extend this to persistent candles, etc.

## API

- `await MarketClient.connect(base_url, connect_md=True, on_md_event=None, on_cmd_event=None)`
  - Performs handshake, opens CMD, logs in, and optionally subscribes to MD.
- High‑level methods
  - `await get_symbols(force_refresh=False)` -> list of `{ sym, tick, min_qty, lot, status }`
  - `await get_book(sym, depth=20)` -> `{ sym, seq, bids, asks }` (arrays)
  - `await configure_candles(sym, interval_ms=1000, depth=50)` -> seeds window; MD updates candles
  - `get_candles(sym)` -> list of OHLC entries suitable for charting
  - `await send(op, payload={}, as_role=None, timeout=5.0)` -> generic WS request/response helper
  - `await place_order(sym, side, price, qty, tif='GTC')` -> payload dict
  - `await cancel_order(order_id)` -> payload dict
  - `await list_orders()` -> list of order dicts
  - `book_snapshot(sym, depth=20)` -> current in-memory book from MD
  - `best_bid_ask(sym)` -> dict with top-of-book `{bid, ask}`

Low‑level access (still available if needed):
- `handshake()`, `api_request()`, `open_cmd()`, `open_md()`

Request session class
- `RequestSession`: alias of the request-capable CMD WebSocket session used internally for minimal-latency requests.

## Server assumptions
- Matches the FastAPI server under `server/` with routes:
  - `POST /auth/handshake`
  - `POST /api/request`
  - `WS /ws/cmd`
  - `WS /ws/md`
