from mcp.bedrock_provider import BedrockProvider
from skills.planner_skill import create_execution_plan
from skills.summarizer_skill import summarize_text
from agents.subagent_worker import SubAgentWorker
from tools.s3_tool import S3Tool


class OrchestratorAgent:

    def __init__(self):

        self.llm_provider = BedrockProvider()
        self.subagent = SubAgentWorker()
        self.s3_tool = S3Tool()

    def handle_request(self, user_task):

        print("\n[Agent] Creating execution plan using Skill layer...")
        plan = create_execution_plan(user_task)

        print("[Agent] Execution Plan:", plan)

        print("\n[Agent] Delegating work to SubAgents...")
        execution_results = []

        for step in plan:
            result = self.subagent.execute_task(step)
            execution_results.append(result)

        combined_result = " ".join(execution_results)

        print("\n[Agent] Calling MCP (AWS Bedrock)...")
        ai_response = self.llm_provider.invoke_llm(
            f"Summarize this execution output:\n{combined_result}"
        )

        summary = summarize_text(ai_response)

        print("\n[Agent] Calling AWS Tool (S3)...")
        buckets = self.s3_tool.list_buckets()

        return {
            "task": user_task,
            "execution_output": combined_result,
            "ai_summary": summary,
            "s3_buckets": buckets
        }
