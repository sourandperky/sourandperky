from django_hosts import host, patterns

host_patterns = patterns(
    "snp.urls",
    host(r"admin", "admin", name="admin"),
    host(r"api", "api", name="api"),
    host(r"", "root", name="root"),
)
