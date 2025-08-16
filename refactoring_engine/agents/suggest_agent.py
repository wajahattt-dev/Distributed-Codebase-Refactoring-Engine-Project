# GPT-suggested refactor plans


from .base import BaseAgent
import openai

class SuggestAgent(BaseAgent):
    def run(self, patterns):
        import astor
        suggestions = {}
        openai.api_key = getattr(self.settings, 'openai_api_key', None)
        for path, data in patterns.items():
            code_metrics = data.get('metrics', {})
            tree = data.get('tree')
            code = astor.to_source(tree) if tree else ''
            prompt = (
                f"You are an expert Python software architect and refactoring specialist.\n"
                f"Analyze the following file for maintainability, modularity, and code quality.\n"
                f"File path: {path}\n"
                f"Code metrics: {code_metrics}\n"
                f"Code:\n{code}\n"
                "\nInstructions:\n"
                "1. Identify code smells, anti-patterns, and opportunities for advanced refactoring (e.g., design patterns, SOLID, DRY, KISS, modularization, dependency injection, etc).\n"
                "2. For each issue, provide a clear, actionable suggestion with a short code snippet or pseudocode if possible.\n"
                "3. Prioritize suggestions that improve testability, extensibility, and readability.\n"
                "4. If the code is already well-structured, explain why.\n"
                "5. Respond in markdown with a summary table, then detailed sections for each suggestion.\n"
            )
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are an expert Python software architect and refactoring specialist."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=1024
                )
                plan = response.choices[0].message['content'].strip()
            except Exception as e:
                plan = f"[OpenAI API error: {e}]"
            suggestions[path] = {'plan': plan, 'tree': tree}
        return suggestions
