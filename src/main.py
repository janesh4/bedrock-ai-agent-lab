from agents.orchestrator_agent import OrchestratorAgent


def main():

    agent = OrchestratorAgent()

    user_task = "Design a scalable AI agent system using cloud services"

    response = agent.handle_request(user_task)

    print("\n=========== FINAL RESPONSE ===========")
    print(response)


if __name__ == "__main__":
    main()
