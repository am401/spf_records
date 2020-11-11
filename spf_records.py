import dns.resolver
import re

def get_spf_record(domain):
    myResolver = dns.resolver.Resolver()
    myAnswers = myResolver.resolve(domain,"TXT")
    validate_ip_regex = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}")

    for rdata in myAnswers:
        records = rdata.to_text().split()
        for i in records:
            x = re.findall(validate_ip_regex, i)
            if x:
                print(x[0])

print("SPF2 MailGun")
get_spf_record("spf2.mailgun.org")
print("SPF1 MailGun")
get_spf_record("spf1.mailgun.org")
print("Sendgrid")
get_spf_record("sendgrid.net")
