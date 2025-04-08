class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = {}
        
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            cleaned_email = local + '@' + domain
            unique_emails[cleaned_email] = True
        
        return len(unique_emails)
