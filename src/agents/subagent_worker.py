class SubAgentWorker:

    def execute_task(self, task):

        print(f"[SubAgent] Executing step -> {task}")

        # Simulated execution logic
        result = f"Completed: {task}"

        return result
