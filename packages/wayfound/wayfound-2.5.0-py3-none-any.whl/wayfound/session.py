import os
import requests
import json
import warnings

# https://packaging.python.org/en/latest/tutorials/packaging-projects/

class Session:
    WAYFOUND_HOST = "https://app.wayfound.ai"
    WAYFOUND_SESSION_CREATE_URL = WAYFOUND_HOST + "/api/v2/sessions"
    WAYFOUND_APPEND_TO_SESSION_URL = WAYFOUND_HOST + "/api/v2/sessions"

    def __init__(self,
                 session_id=None,
                 wayfound_api_key=None, 
                 agent_id=None, 
                 application_id=None,
                 visitor_id=None, 
                 visitor_display_name=None, 
                 account_id=None, 
                 account_display_name=None,
                 ):
        super().__init__()

        self.session_id = session_id
        self.wayfound_api_key = wayfound_api_key or os.getenv("WAYFOUND_API_KEY")
        self.agent_id = agent_id or os.getenv("WAYFOUND_AGENT_ID")
        self.application_id = application_id
        self.visitor_id = visitor_id
        self.visitor_display_name = visitor_display_name
        self.account_id = account_id
        self.account_display_name = account_display_name
        
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.wayfound_api_key}",
            "X-SDK-Language": "Python",
            "X-SDK-Version": "2.5.0"
        }

    def create(self, messages=None, is_async=True):
        if (self.session_id is not None):
            raise Exception("Session already created. Use append_to_session to add more messages.")

        if messages is None:
            messages = []

        recording_url = self.WAYFOUND_SESSION_CREATE_URL
        payload = {
            "agentId": self.agent_id,
            "messages": messages,
            "async": is_async,
        }

        if self.visitor_id:
            payload["visitorId"] = self.visitor_id

        if self.visitor_display_name:
            payload["visitorDisplayName"] = self.visitor_display_name

        if self.account_id:
            payload["accountId"] = self.account_id

        if self.account_display_name:
            payload["accountDisplayName"] = self.account_display_name

        if self.application_id:
            payload["applicationId"] = self.application_id

        try:
            response = requests.post(recording_url, headers=self.headers, data=json.dumps(payload))
            if response.status_code != 200:
                print(f"The request failed with status code: {response.status_code} and response: {response.text}")
                raise Exception(f"Error creating session: {response.status_code}")

            parsed_response = response.json()
            self.session_id = parsed_response["id"]

            return parsed_response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error creating session: {e}")

    def complete_session(self, messages=None, is_async=True,):
        warnings.warn(
            "complete_session is deprecated and will be removed in a future version. Use create() instead.",
            DeprecationWarning,
            stacklevel=2
        )
        return self.create(messages, is_async)

    def append_to_session(self, messages, is_async=True):
        if self.session_id is None:
            raise Exception("No session_id available. Complete a session first before appending.")
        
        if messages is None:
            messages = []

        append_url = f"{self.WAYFOUND_APPEND_TO_SESSION_URL}/{self.session_id}"
        payload = {
            "messages": messages,
            "async": is_async,
        }
            
        try:
            response = requests.put(append_url, headers=self.headers, data=json.dumps(payload))
            if response.status_code != 200:
                print(f"The request failed with status code: {response.status_code} and response: {response.text}")
                raise Exception(f"Error appending to session: {response.status_code}")
            
            parsed_response = response.json()
            return parsed_response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error appending to session: {e}")
