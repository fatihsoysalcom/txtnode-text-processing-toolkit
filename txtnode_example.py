import re

class TxtNode:
    def __init__(self, text):
        self.text = text

    def find_all(self, pattern):
        # Finds all occurrences of a pattern in the text.
        return re.findall(pattern, self.text)

    def replace_all(self, pattern, repl):
        # Replaces all occurrences of a pattern with a replacement string.
        return TxtNode(re.sub(pattern, repl, self.text))

    def split_by(self, pattern):
        # Splits the text into a list of strings based on a pattern.
        return self.text.split(pattern)

    def extract_between(self, start_pattern, end_pattern):
        # Extracts text between specified start and end patterns.
        matches = []
        # Use a non-greedy match for the content between delimiters
        regex = re.compile(f'{re.escape(start_pattern)}(.*?){re.escape(end_pattern)}', re.DOTALL)
        for match in regex.finditer(self.text):
            matches.append(match.group(1))
        return matches

    def __str__(self):
        return self.text

# --- Example Usage ---

# Sample text data
log_data = """
[2023-10-27 10:00:01] INFO: User 'alice' logged in.
[2023-10-27 10:01:15] WARN: Disk space low.
[2023-10-27 10:02:30] INFO: Processing request #12345.
[2023-10-27 10:03:05] ERROR: Database connection failed.
"""

# Create a TxtNode instance
log_node = TxtNode(log_data)

# 1. Find all log levels
log_levels = log_node.find_all(r'\[(.*?)\]')
print("Log Levels:", log_levels)

# 2. Replace all INFO messages with DEBUG
debug_log = log_node.replace_all(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] INFO:', '[DEBUG]')
print("\nLog after replacing INFO with DEBUG:\n", debug_log)

# 3. Split the log into individual lines
lines = log_node.split_by('\n')
print("\nIndividual Log Lines:")
for line in lines:
    if line.strip(): # Avoid printing empty lines
        print(f"- {line}")

# 4. Extract messages between square brackets (excluding the timestamp part)
# This demonstrates extracting specific structured data.
message_contents = log_node.extract_between('[', ']')
print("\nExtracted content within brackets:", message_contents)

# A more specific extraction: get messages after 'INFO:'
info_messages = log_node.extract_between('INFO: ', '.')
print("\nExtracted INFO messages:", info_messages)
