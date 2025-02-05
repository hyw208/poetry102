from fastapi import FastAPI

def app():
    from other_package.abc import func_abc
    from poetry102.xyz import func_xyz
    _api = FastAPI()

    @_api.get("/")
    async def root():
        return {"message": "Hello World"}

    return _api

def main():
    import uvicorn
    uvicorn.run(app(), host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()

