import dns.resolver

import sys
import time


VALID_NAMESERVERS = {
    "ns1.valcato.com.",
    "ns2.valcato.com.",
    "ns3.valcato.com.",
}

domains = set()

for input_filename in sys.argv[1:]:
    with open(input_filename) as input_f:
        domains = domains.union({l.strip() for l in input_f})


def get_ns_records(domain):
    try:
        records = dns.resolver.resolve(domain, "NS")
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
        return None


for domain in domains:
    while True:
        try:
            records = get_ns_records(domain)
            break
        except dns.resolver.LifetimeTimeout:
            time.sleep(60)
    if records is None:
        continue
    records = {record.to_text() for record in records}
    if records.intersection(VALID_NAMESERVERS) == set():
        print(domain)
