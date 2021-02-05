import dns.resolver
import re

def get_spf_record(domain):
    myResolver = dns.resolver.Resolver()
    myAnswers = myResolver.resolve(domain,"TXT")
    validate_ip_regex = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}")

    try:
        for rdata in myAnswers:
            records = rdata.to_text().split()
            for i in records:
                x = re.findall(validate_ip_regex, i)
                if x:
                    print(x[0])
    except dns.resolver.NoAnswer:
        print(domain + ": No answer.")



print("=" * 10 + " MailGun " + "=" * 10 + "\n")
get_spf_record("spf2.mailgun.org")
get_spf_record("spf1.mailgun.org")
print("\n" + "=" * 10 + " Sendgrid " + "=" * 10 + "\n")
get_spf_record("sendgrid.net")
print("\n" + "=" * 10 + " MailChannel " + "=" * 10 + "\n")
get_spf_record("spf1.mailchannels.net")
get_spf_record("spf2.mailchannels.net")
get_spf_record("spf3.mailchannels.net")
