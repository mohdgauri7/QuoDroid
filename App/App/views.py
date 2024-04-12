# views.py
from django.http import JsonResponse
from robot.api import TestSuiteBuilder
from io import StringIO
import sys
import json

def execute_tests(request):
    if request.method == 'POST':
        # Receive instructions from POST API
        data = json.loads(request.body)
        instructions = data.get('tests')

        # Convert instructions to Robot Framework format
        robot_test_case = ""
        for test in instructions:
            robot_test_case += f"* Test Cases *\n{test['title']}\n"
            for step in test['steps']:
                robot_test_case += f"    {step}\n"


        # Execute instructions using Robot Framework
        output_stream = StringIO()
        sys.stdout = output_stream  # Redirect stdout to capture output
        try:
            suite = TestSuiteBuilder().build(StringIO(robot_test_case))
            suite.run()
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

        # Restore stdout
        sys.stdout = sys._stdout_

        # Get captured output
        output = output_stream.getvalue()

        return JsonResponse({'output': output})

    return JsonResponse({'error': 'Method not allowed'}, status=405)