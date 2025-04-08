class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = []
        
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            cleaned_email = local + '@' + domain
            if cleaned_email not in unique_emails:
                unique_emails.append(cleaned_email)
        
        return len(unique_emails)
