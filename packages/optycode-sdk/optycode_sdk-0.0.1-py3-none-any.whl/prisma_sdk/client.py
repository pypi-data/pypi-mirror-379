import requests
from datetime import datetime
import urllib.parse

class OptycodeAPI:
    def __init__(self, auth_token: str, timeout: int = 30):
        """
        Initialize the client with an auth token.
        If base_url is not provided, will try PRISMA_API_URL env var.
        """
        enncoded_base_url = "https%3A%2F%2Fmwuamhsio56zkuxyerq62fdzom0vxeeh.lambda-url.us-east-2.on.aws%2F"
        base_url = urllib.parse.unquote(enncoded_base_url)
        endpoint_encoded = "https%3A%2F%2Felpaimpmp7bw7rol5yv7ggtreq0zuvos.lambda-url.us-east-2.on.aws%2F"
        endpoint = urllib.parse.unquote(endpoint_encoded)

        self.auth_token = auth_token
        self.base_url = base_url
        self.endpoint = endpoint
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.auth_token}"})

        # Optional: verify token immediately
        self._verify_token()

    def _verify_token(self):
        """Verify the token with the server once at initialization"""
        try:
            response = self.session.get(self.base_url, timeout=self.timeout)
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"Token verification failed: {e}")

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

