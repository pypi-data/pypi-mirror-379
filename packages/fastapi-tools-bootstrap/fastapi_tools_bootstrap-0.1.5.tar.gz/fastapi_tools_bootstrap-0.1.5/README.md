### Bootstrap

```python
from fastapi import FastAPI
from fastapi_tools import bootstrap


@bootstrap.on_exit(kind=["server"])
async def shutdown1(app: FastAPI) -> None:
    print("Shutdown")
    
@bootstrap.on_exit
async def shutdown2(app: FastAPI) -> None:
    print("Shutdown")
    
    
app = FastAPI(lifespan=bootstrap.lifespan("server"))
```