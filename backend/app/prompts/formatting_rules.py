"""
Formatting rules for DocuMind AI responses.

These rules define how every answer should be structured,
regardless of the question being asked.
"""

FORMATTING_RULES = """
========================
RESPONSE STYLE
========================

Always format the response using Markdown.

Follow these rules:

1. Start with a clear title (# Heading) whenever appropriate.

2. Organize the answer into logical sections using
   level-2 headings (##).

3. Use bullet points for lists.

4. Use numbered lists for procedures or steps.

5. Preserve code examples exactly as they appear
   inside fenced code blocks.

6. Use tables whenever they improve readability.

7. If the answer is long, finish with a short summary.

8. Never return one huge paragraph.

9. Keep spacing clean and readable.

10. Do not repeat the same information.
"""