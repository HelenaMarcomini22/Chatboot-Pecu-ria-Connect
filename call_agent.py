from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types


def call_agent(agent, message_text): 
    session_service = InMemorySessionService()
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    session_service.create_session(app_name=agent.name, user.id="user1", session_id="session1")
    
    user_message = types.Content(role="user", parts=[types.Part(text=message_text)])
    response_text = ""
    
    for event in runner.run(user.id="user1", session_id="session1", new_message=user_message):
        if event.is_final_response():
            response_text += ''.join(part.text + "\n" for part in event.content.parts if part.text)
            return response_text.strip()