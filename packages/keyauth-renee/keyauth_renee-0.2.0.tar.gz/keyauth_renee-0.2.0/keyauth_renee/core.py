from fastapi import Request, HTTPException

class KeyAuth:
    def __init__(self, validation_url: str):
        self.url = validation_url

    def check(self, key: str) -> bool:
        import requests
        try:
            response = requests.get(self.url, params={"key": key})
            return response.json().get("valid", False)
        except Exception:
            return False

    def verify(self):
        async def dependency(request: Request):
            key = request.query_params.get("key")
            if not key or not self.check(key):
                raise HTTPException(status_code=403, detail="Invalid API key")
        return dependency