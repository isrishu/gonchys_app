from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'gonchys.urls', name='www'), # Or a dedicated 'frontend' app
    host(r'crm', 'crm.urls', name='crm'),
    host(r'erp', 'erp.urls', name='erp'),
    host(r'accounting', 'accounting.urls', name='accounting'),
    host(r'marketing', 'marketing.urls', name='marketing'),
)