class Evaluator:

    def evaluate(
        self,
        agent,
        case,
    ):

        answer = agent.run(
            case.user_input
        )

        trace = agent.tracer.get_events()

        answer_passed = self.check_answer(
            case,
            answer,
        )

        tools_passed = self.check_tools(
            case,
            trace,
        )

        return {
            "name": case.name,
            "answer": answer_passed,
            "tools": tools_passed,
            "passed": (
                answer_passed
                and tools_passed
            ),
        }

    def check_answer(
        self,
        case,
        answer,
    ):

        if case.expected_answer is None:
            return True

        return (
            case.expected_answer.lower()
            in answer.lower()
        )

    def check_tools(
        self,
        case,
        trace,
    ):

        if not case.expected_tools:
            return True

        actual_tools = []

        for event in trace:

            if event["event"] == "TOOL_START":

                actual_tools.append(
                    event["data"]["tool"]
                )

        return actual_tools == case.expected_tools
    
    def run_all(
        self,
        agent,
        cases,
    ):

        results = []

        for case in cases:

            print(
                f"\nRunning: {case.name}"
            )

            result = self.evaluate(
                agent,
                case,
            )

            results.append(result)

            status = (
                "PASS"
                if result["passed"]
                else "FAIL"
            )

            print(
                f"{case.name}: {status}"
            )

        self.print_summary(results=results)

        return results

    def print_summary(self, results):

        passed = sum(
            result["passed"]
            for result in results
        )

        total = len(results)

        print("\n" + "=" * 40)
        print("EVALUATION SUMMARY")
        print("=" * 40)

        print(
            f"Passed: {passed}/{total}"
        )

        print(
            f"Failed: {total - passed}/{total}"
        )

        print(
            f"Score: {passed / total:.1%}"
        )