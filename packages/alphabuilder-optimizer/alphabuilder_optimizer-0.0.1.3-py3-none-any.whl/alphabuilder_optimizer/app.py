import requests

class OptimizerClient:
    def __init__(self, api_key: str, api_url: str = "https://optimizer.alphabuilder.xyz/"):
        self.api_url = api_url
        self.api_key = api_key
        
    def optimize(self, 
                 idempotency_key, 
                 assets, 
                 expected_returns, 
                 covariance, 
                 risk_free_rate=0.0, 
                 constraint="equal_weighted"):
        
        payload = {
            "idempotency_key": idempotency_key,
            "assets": assets,
            "expected_returns": expected_returns,
            "covariance": covariance,
            "risk_free_rate": risk_free_rate,
            "constraint": constraint
        }
        
        headers = {"x-api-key": self.api_key}
        
        response = requests.post(f"{self.api_url}/optimize", json=payload, headers=headers)
        
        if response.status_code != 200:
            raise Exception(response.json())
        return response.json()
    
    def get_items(self):
        headers = {"x-api-key": self.api_key}
        response = requests.get(f"{self.api_url}/items", headers=headers)
        return response.json()
    
client = OptimizerClient(api_key="supersecret123")