import os
import requests

class TokenCutClient:
    def __init__(self, api_key: str, base_url: str = "https://api.tokencut.ai/v1"):
        self.api_key = api_key or os.getenv("TOKENCUT_API_KEY")
        if not self.api_key:
            raise ValueError("No API key provided. Pass api_key or set TOKENCUT_API_KEY env var.")
        self.base_url = base_url.rstrip("/")

    def chat(self, messages: list[dict], model: str = "gpt-4o-mini", session_id: str = "default") -> dict:
        """Call the TokenCut API /chat endpoint"""
        resp = requests.post(
            f"{self.base_url}/chat",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"model": model, "messages": messages, "session_id": session_id},
            timeout=30,
        )
        if resp.status_code == 401:
            raise ValueError("Invalid API key.")
        if resp.status_code != 200:
            raise RuntimeError(f"API error {resp.status_code}: {resp.text}")
        return resp.json()
