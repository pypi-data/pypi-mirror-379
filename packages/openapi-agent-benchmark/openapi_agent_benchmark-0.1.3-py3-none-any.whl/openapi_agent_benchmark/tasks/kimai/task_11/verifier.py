import requests


def verify(agent_output: str, base_url: str, authenticated_session: requests.Session) -> bool:
    response = authenticated_session.get(f"{base_url}/api/customers")
    customers = [customer['name'] for customer in response.json()]
    return set(customers) == {'Google', 'OpenAI', 'Microsoft'}
