# Queue Deep Dive

Queue problems show up when work must be handled in arrival order.

Common interview shapes:

- fixed-size rolling windows over streams
- recent-event counting
- simulations where the oldest pending element must leave first
- BFS traversal, which is covered separately under `search/bfs`

## `moving_average_from_data_stream`

Maintains the average over the most recent fixed-size window.

- Enqueue the new value.
- Evict the oldest value when the window grows too large.
- Keep a running sum so each update stays constant time.
- Big O: `O(1)` amortized per update, `O(window_size)` space.

## `number_of_recent_calls`

Counts timestamps within the last 3000 milliseconds.

- Enqueue the new request.
- Pop expired requests from the front until the window is valid again.
- Interview approach: this is a queue-backed sliding time window.
- Big O: `O(1)` amortized per call because each timestamp enters and leaves once.
