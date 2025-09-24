# ji-async-http-utils

Small async helpers for HTTP clients, with a focus on practical concurrency for aiohttp.

This package provides utilities to:
- Iterate responses with controlled concurrency
- Stream results in completion order while mapping back to inputs
- Handle retries (respecting Retry-After) and timeouts
- Show progress bars via tqdm

## Install

Requires Python 3.10+.

```bash
pip install ji-async-http-utils
```

Direct dependencies: `aiohttp`, `httpx`, `tqdm`.


## Quickstart

Basic list with `base_url` and a progress label:

```python
from ji_async_http_utils.aiohttp import iter_requests

async def main():
    async for user_id, data in iter_requests(
        base_url="https://api.example.com/users",
        items=[1, 2, 3, 4, 5],
        max_concurrency=16,
        pbar="Fetching users",
    ):
        print(user_id, data["name"])  # default yields parsed JSON
```

## Usage Examples (aiohttp)

### Single request with `request`

```python
import aiohttp
from ji_async_http_utils.aiohttp import request

async def main():
    async with aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=15.0)
    ) as session:
        resp = await request(
            url="https://jsonplaceholder.typicode.com/todos/1",
            session=session,
        )  # raises for non-2xx after retries
        async with resp:
            data = await resp.json()
        print(data["title"])  # e.g., "delectus aut autem"
```

### Session helper: `ensure_session`

`ensure_session` is an async context manager that yields a usable
`aiohttp.ClientSession`.

Modes (mutually exclusive):
- Creation: `ensure_session(timeout=..., max_concurrency=...)` creates a new session
  and closes it on exit.
- Reuse: `ensure_session(session=existing)` yields your session unchanged and does
  not close it on exit.

```python
import aiohttp
from ji_async_http_utils.aiohttp import ensure_session, request

async def main():
    # Option A: create a managed session for this block
    async with ensure_session(
        timeout=aiohttp.ClientTimeout(total=20),
        max_concurrency=32,
    ) as session:
        resp = await request(url="https://httpbin.org/json", session=session)
        async with resp:
            data = await resp.json()
        print(data)

    # Option B: reuse an existing session you manage elsewhere
    async with aiohttp.ClientSession() as s:
        async with ensure_session(session=s) as session:
            resp = await request(url="https://httpbin.org/get", session=session)
            async with resp:
                print(resp.status)
```

### Multiple requests with `iter_requests`

```python
async def main():
    async for i, data in iter_requests(
        base_url="https://example.com/docs",
        items=range(1, 101),
        pbar="Docs",
    ):
        # default assumes JSON; for non-JSON endpoints, pass on_result
        ...
```

### Retry policy and `raise_on_error`

```python
async def main():
    async for i, data in iter_requests(
        base_url="https://api.example.com/items",
        items=range(1, 101),
        retries=3,                # retry 3 times on 429/5xx or client/timeout
        raise_on_error=True,      # raise on failure instead of yielding Exception
        pbar="Items",
    ):
        # data is parsed JSON here
        ...
```

### Custom headers and query params

```python
async def main():
    async for i, data in iter_requests(
        base_url="https://api.example.com/items",
        items=range(1, 6),
        headers={"Authorization": "Bearer TOKEN"},
        params={"expand": "details"},
        pbar=True,
    ):
        ...
```

### Provide your own session (connection reuse, custom connector)

```python
import aiohttp
from ji_async_http_utils.aiohttp import iter_requests

async def main():
    timeout = aiohttp.ClientTimeout(total=30)
    connector = aiohttp.TCPConnector(limit=64)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        async for key, data in iter_requests(
            base_url="https://api.example.com/resources",
            items=["a", "b", "c"],
            session=session,   # reuse this session
            max_concurrency=32,
            pbar=True,
        ):  # early breaks are safe; pending tasks are cancelled
            ...
```

### Progress bar on/off

```python
# On with label
async for k, data in iter_requests(..., pbar="Downloading"): ...

# On without label
async for k, data in iter_requests(..., pbar=True): ...

# Off (default)
async for k, data in iter_requests(...): ...
```

### Using request_fn (no base_url): build requests per-item

```python
from ji_async_http_utils.aiohttp import iter_requests
import aiohttp

async def make_request(session: aiohttp.ClientSession, item: tuple[int, str]):
    # item can be any type; you decide how to build the request
    item_id, slug = item
    url = f"https://example.com/{slug}/{item_id}"
    return await session.get(url)

async def main():
    items = [(1, "alpha"), (2, "beta"), (3, "gamma")]
    async for item, data in iter_requests(
        request_fn=make_request,  # base_url must be None in this mode
        items=items,
        max_concurrency=10,
        pbar="Custom requests",
    ):
        # Gotcha avoidance: do not consume the body inside on_result if you
        # plan to read it here. Always consume/release exactly once.
        print(item, data)
```

### Hooks: on_result and on_error

```python
async def on_error(item, exc):
    # Called right before a failed request raises after retries.
    print("FAIL", item, type(exc).__name__)

async for item, data in iter_requests(
    base_url="https://api.example.com/jobs",
    items=range(1, 51),
    on_error=on_error,  # keep default JSON results, but hook errors
    pbar=True,
):
    ...
```

### Using `raise_on_error=True` with a result transformer

When you want exceptions to raise immediately and your code consumes transformed results only:

```python
from ji_async_http_utils.aiohttp import iter_requests

async def to_json(item, resp):
    async with resp:
        return await resp.json()

async for item, data in iter_requests(
    base_url="https://api.example.com/items",
    items=range(1, 6),
    on_result=to_json,
    raise_on_error=True,   # no on_error allowed in this mode
):
    # data is guaranteed to be successful JSON here
    print(item, data)
```

### Timeout control

```python
import aiohttp
from ji_async_http_utils.aiohttp import iter_requests

# Use a float (seconds) for total timeout when the function creates the session
async for item, data in iter_requests(
    base_url="https://example.com",
    items=range(10),
    timeout=15.0,
):
    ...

# Or provide a full ClientTimeout
async for item, data in iter_requests(
    base_url="https://example.com",
    items=range(10),
    timeout=aiohttp.ClientTimeout(total=120, connect=5),
):
    ...
```


## Usage Examples (httpx)

Basic client lifecycle with `lifespan` and `request`

```python
from ji_async_http_utils.httpx import lifespan, request, get_client

async def main():
    async with lifespan():
        # Simple GET with optional headers/params; raises for non-2xx by default
        res = await request(
            "https://httpbin.org/get",
            method="GET",
            params={"q": "hello"},
            headers={"X-Demo": "1"},
        )
        print(res.status_code, res.json())

        # Or use the client directly
        r2 = await get_client().post("https://httpbin.org/post", json={"ok": True})
        print(r2.status_code)
```

Allow specific non-2xx without raising

```python
from ji_async_http_utils.httpx import lifespan, request

async def main():
    async with lifespan():
        # 404 is allowed here and will not raise
        res = await request(
            "https://httpbin.org/status/404",
            raise_on_status_except_for=[404],
        )
        print(res.status_code)
```

Synchronous entrypoint using `run_in_lifespan`

```python
from ji_async_http_utils.httpx import run_in_lifespan, get_client

@run_in_lifespan
async def main() -> None:
    res = await get_client().get("https://httpbin.org/uuid")
    print(res.json()["uuid"])  # prints a UUID

main()  # runs with a managed client lifecycle
```

Configure connection limits (throughput) with `set_client`

```python
import httpx
from ji_async_http_utils.httpx import lifespan, run_in_lifespan

# Option A: use lifespan and a factory that sets limits
async def main():
    async with lifespan(
        set_client=lambda: httpx.AsyncClient(
            transport=httpx.AsyncHTTPTransport(
                limits=httpx.Limits(
                    max_connections=32,          # global connections cap
                    max_keepalive_connections=16, # pooled keep-alive sockets
                )
            ),
            timeout=httpx.Timeout(30.0),
            follow_redirects=True,
        )
    ):
        ...

# Option B: decorator form
@run_in_lifespan(
    set_client=lambda: httpx.AsyncClient(
        transport=httpx.AsyncHTTPTransport(
            limits=httpx.Limits(max_connections=32, max_keepalive_connections=16)
        )
    )
)
async def cli_entry():
    ...
```


## API Overview (aiohttp)

Exports from `ji_async_http_utils.aiohttp`:

- `iter_requests(items=..., ...) -> AsyncIterator[tuple[item, JSON | BaseException]]`
- `request(url=..., session=..., ...) -> aiohttp.ClientResponse` (always raises on failure)
- `ensure_session(session=existing)` or `ensure_session(timeout=..., max_concurrency=...)` -> Async context manager yielding `ClientSession`

Key parameters:

- `max_concurrency`: cap in-flight requests (default 32)
- `base_url` or `request_fn`: mutually exclusive ways to issue requests
- `timeout`: total timeout (defaults to 60s if we create the session)
- `method`: HTTP method literal ("GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS", "TRACE", "CONNECT")
- `pbar`: progress toggle/label. `True` enables without a label; a string sets the label; `False` disables
- `raise_on_error`: when `True`, failures are raised; when `False` (default), failures are yielded as Exceptions (only for `iter_requests`)
- `retries`: retry count for retryable statuses/exceptions (429/5xx, client/timeouts)
- `retry_statuses`: customize which HTTP status codes trigger a retry (default: 429, 500, 502, 503, 504)
- `on_result` / `on_error`: async hooks for side effects

Return types:
- Default (no `on_result`): yields parsed JSON (alias `JSON`), not `ClientResponse`.
- With `on_result`: yields `ResultT` returned by your callback.
- When `raise_on_error=False` (default), failures are yielded as `Exception` (only for `iter_requests`).
- When `raise_on_error=True`, failures raise immediately and are not yielded (only for `iter_requests`).

Type-safety constraints (overloads guide editors):

- Provide exactly one of `base_url` or `request_fn`.
- If `raise_on_error=True`, then `on_error` must be `None` (ignored when raising).
- If `on_error` is provided, `raise_on_error` must be `False`.


## API Overview (httpx)

Exports from `ji_async_http_utils.httpx`:

- `lifespan(*, set_client: Optional[Callable[[], httpx.AsyncClient]] = None) -> AsyncIterator[httpx.AsyncClient]`: context manager that creates/sets an AsyncClient (or uses your factory) in a ContextVar for helpers.
- `get_client() -> httpx.AsyncClient`: returns the context-scoped client; raises if called outside `lifespan()` or `run_in_lifespan`.
- `create_client() -> httpx.AsyncClient`: constructs the default client (30s timeout, follow_redirects=True, response logging hook).
- `request(url, *, method="GET", headers=None, params=None, json=None, data=None, raise_on_status_except_for=None) -> httpx.Response`: Request helper that raises for non-2xx unless allowed.
- `run_in_lifespan(func=None, *, set_client: Optional[Callable[[], httpx.AsyncClient]] = None) -> ...`: decorator that runs an async function inside a managed `lifespan` and returns a sync callable.

## Gotchas & Best Practices

- aiohttp/iter_requests:
  - Response handling: When `on_result` is `None` (default), the helper reads `resp.json()` and closes the response for you; you receive parsed JSON (`JSON`). When you provide `on_result`, you receive the raw `ClientResponse` in that callback and must read/close it there.
  - Error handling: Results are yielded in completion order. Failures are yielded as `Exception` values when `raise_on_error=False` (default) and are raised immediately when `True`.
  - Concurrency: Start with 16–32 in-flight requests; tune by observing 95th percentile latency and error codes (429/5xx). Internal session uses `TCPConnector(limit=max_concurrency)`.
  - Arguments: Provide exactly one of `base_url` or `request_fn`. Overloads guide correct usage in editors.
  - Early termination: Safe to break out of the loop — pending tasks are cancelled and the session/progress bar are cleaned up.
  - Sessions: Reuse a single `ClientSession` (pass `session=`) to benefit from connection pooling when making many calls.

- httpx helpers:
  - Always call `get_client()` or `request()` inside `async with lifespan(): ...` or via a function decorated with `@run_in_lifespan`. Otherwise `get_client()` raises to avoid leaking a global client.
  - `request` raises for non-2xx by default; use `raise_on_status_except_for` to allow specific codes (e.g., `[404]`).
  - The default client (via `create_client`/`lifespan`) uses a 30s timeout, follows redirects, and logs responses to the console.
  - Concurrency vs. connection limits: HTTPX does not queue requests for you. Limit in-flight tasks with your own semaphore/worker pool if needed, and set connection limits with `httpx.Limits(max_connections=..., max_keepalive_connections=...)` via a custom client factory passed to `set_client`.


## License

This project is licensed under the MIT License. See the LICENSE file for details.
