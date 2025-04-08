import re

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            local = re.sub(r'\+.*', '', local)  # Remove everything after the first '+'
            local = local.replace('.', '')      # Remove all '.'
            unique_emails.add(local + '@' + domain)
        
        return len(unique_emails)
