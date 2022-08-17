# nameserver-validation

Given one or more input files, will return domains which do not use at least one of the list of valid nameservers.

```
$ python validate.py example.txt
example.org
example.net
example.com
```

Requires the `dnspython` package.