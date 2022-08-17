import dns.resolver

import sys


VALID_NAMESERVERS = {
    "ns1.valcato.com.",
    "ns2.valcato.com.",
    "ns3.valcato.com.",
}

domains = set()

for input_filename in sys.argv[1:]:
    with open(input_filename) as input_f:
        domains = domains.union({l.strip() for l in input_f})

invalid_domains = []

for domain in domains:
    records = dns.resolver.resolve(domain, "NS")
    records = {record.to_text() for record in records}
    if records.intersection(VALID_NAMESERVERS) == set():
        invalid_domains.append(domain)

print("\n".join(invalid_domains))
