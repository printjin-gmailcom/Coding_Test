class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        return len({local.split('+')[0].replace('.', '') + '@' + domain 
                    for local, domain in (email.split('@') for email in emails)})
