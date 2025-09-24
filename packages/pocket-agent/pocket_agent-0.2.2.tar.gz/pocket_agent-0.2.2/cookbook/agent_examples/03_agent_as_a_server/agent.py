import asyncio
import os
from pocket_agent import PocketAgent, AgentConfig


#########################################################
# Simple Agent (to be used as the main agent)
#########################################################
class SimpleAgent(PocketAgent):

    async def run_user_input_loop(self) -> dict:
        while True:
            user_input = input("Your input: ")
            if user_input.lower() == 'quit':
                break
            await self.run(user_input)
        return {"status": "completed"}



#########################################################
# Initialize the simple agent
#########################################################
def create_simple_agent():
    # MCP config for the simple agent to give it access to the utilities server's tools and the weather agent running as a server
    simple_agent_mcp_config = {
        "mcpServers": {
            "utilities": {
                "transport": "stdio",
                "command": "python",
                "args": ["server.py"],
                "cwd": os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "servers", "simple_utilities")
            },
            "weather": {
                "transport": "stdio",
                "command": "python",
                "args": ["agent_server.py"],
                "cwd": os.path.join(os.path.dirname(os.path.abspath(__file__))),
                "env": {
                    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
                }
            }
        }
    }

    # Agent config for the simple agent
    simple_agent_config = AgentConfig(
        llm_model="gpt-5-nano",
        system_prompt="You are a helpful assistant who answers user questions and uses provided tools when applicable"
    )

    # Create and return the simple agent instance
    simple_agent = SimpleAgent(
        agent_config=simple_agent_config,
        mcp_config=simple_agent_mcp_config
    )
    return simple_agent


async def main():
    simple_agent = create_simple_agent()
    await simple_agent.run_user_input_loop()


if __name__ == "__main__":
    asyncio.run(main())