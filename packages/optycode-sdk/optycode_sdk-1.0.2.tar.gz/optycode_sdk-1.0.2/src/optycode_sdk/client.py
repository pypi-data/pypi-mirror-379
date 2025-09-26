import requests
from datetime import datetime
import urllib.parse

class OptycodeAPI:
    def __init__(self, auth_token: str, timeout: int = 30):
        """
        Initialize the client with an auth token.
        If base_url is not provided, will try PRISMA_API_URL env var.
        """
        base_url = "https://ut35ueyqjf.execute-api.us-east-2.amazonaws.com/prod/send-data"
        endpoint = "https://ut35ueyqjf.execute-api.us-east-2.amazonaws.com/prod/eval_layer"
        self.auth_token = auth_token
        self.base_url = base_url
        self.endpoint = endpoint
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.auth_token}"})
        # Optional: verify token immediately
        self._verify_token()

    def _verify_token(self):
        """Verify the token with a lightweight POST to the API Gateway endpoint."""
        try:
            payload = {"verify": True, "timestamp": datetime.now().isoformat()}
            response = self.session.post(self.base_url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            return {"status": "ok", "code": response.status_code}
        except requests.RequestException as e:
            return {"status": "failed", "error": str(e)}


    def send_model_data(self, question: str, answer: str, model_id: int) -> dict:
        """
        Send model data (question, answer, model_number) to the server.
        If `url` is provided, overrides the base_url for this request.
        """

        payload = {
            "timestamp": datetime.now().isoformat(),
            "question": question,
            "answer": answer,
            "model_id": model_id,
        }

        try:
            response = self.session.post(self.endpoint, json=payload, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Failed to send model data: {e}")

    def send_model_data_async(self, question: str, answer: str, model_id: int):
        payload = {
            "timestamp": datetime.now().isoformat(),
            "question": question,
            "answer": answer,
            "model_id": model_id,
        }

        # Don't wait for server response — just send and close connection
        try:
            self.session.post(
                self.endpoint,
                json=payload,
                timeout=0.5  # very short timeout
            )
        except requests.exceptions.ReadTimeout:
            # This is expected — we don’t care about the response
            pass

        return True

