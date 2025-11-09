import logging, sys, json, time

def setup_logging():
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)s %(name)s %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S%z'
    )
    handler.setFormatter(formatter)
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(handler)

class RequestTimerMiddleware:
    def __init__(self, app):
        self.app = app
        self.logger = logging.getLogger("timing")

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        start = time.perf_counter()
        async def send_wrapper(event):
            if event["type"] == "http.response.start":
                duration = (time.perf_counter() - start) * 1000
                self.logger.info(json.dumps({
                    "path": scope.get("path"),
                    "method": scope["method"],
                    "duration_ms": round(duration, 2)
                }))
            await send(event)
        await self.app(scope, receive, send_wrapper)
