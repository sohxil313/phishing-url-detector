import re
import tldextract

def extract_url_features(url):
    f = {}
    f['url_length']  = len(url)
    f['has_ip']      = 1 if re.search(r'(\d{1,3}\.){3}\d{1,3}', url) else 0
    f['count_at']    = url.count('@')
    f['count_dash']  = url.count('-')
    f['count_dot']   = url.count('.')
    f['count_slash'] = url.count('/')
    f['https']       = 1 if url.startswith('https') else 0
    ext = tldextract.extract(url)
    f['domain_length']  = len(ext.domain)
    f['suspicious_tld'] = ext.suffix in ['xyz','top','click','link','club']
    return f
