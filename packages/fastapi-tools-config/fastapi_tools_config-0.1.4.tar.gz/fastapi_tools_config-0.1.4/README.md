### Settings


```python
# in app.config module

from fastapi_tools import config 


class MySettings:
    param1: int
    param2: str


settings = config.setup(MySettings)
```