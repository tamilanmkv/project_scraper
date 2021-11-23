from urllib.parse import urlparse
import itertools as it

url = {'https://www.hackerone.com/security-at/2021', 'http://purl.org/rss/1.0/modules/content/', 'https://fast.wistia.com/assets/external/E-v1.js', 'http://ogp.me/ns#', 'http://www.w3.org/2004/02/skos/core#', 'http://xmlns.com/foaf/0.1/', 'http://schema.org/', 'https://ma.hacker.one/thank-you-for-contacting-us.html', 'https://www.googletagmanager.com/ns.html?id=GTM-KLQXL8V', 'https://www.hackerone.com/resources/customer-story/how-hired-builds-customer-trust-with-hackerone-pentest', 'https://hackerone.com/users/sign_in', 'cdn.jsdelivr.net/npm/js-cookie@3.0.1/dist/js.cookie.min.js', 'http://rdfs.org/sioc/ns#', 'https://docs.hackerone.com/', "https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f)", 'https://hackerone.com/leaderboard', 'cdnjs.cloudflare.com/ajax/libs/fancybox/3.5.7/jquery.fancybox.min.js', 'cdn.jsdelivr.net/npm/chart.js', 'https://hackerone.com/leaderboard/all-time', 'http://www.w3.org/2001/XMLSchema#', 'http://purl.org/dc/terms/', 'https://www.drupal.org', 'https://hackerone.com/hacktivity', 'https://www.facebook.com/Hacker0x01', 'https://hackerone.com/directory/programs?order_direction=DESC&amp;order_field=resolved_report_count', 'app-sj17.marketo.com/js/forms2/js/forms2.min.js', 'http://rdfs.org/sioc/types#', 'https://www.hackerone.com/', 'https://www.hackerone.com/resources/e-book/hacker-powered-security-for-aws-applications', 'https://www.hackerone.com/history-of-hacker-powered-security', 'http://www.w3.org/2000/svg', 'https://fast.wistia.com/embed/medias/tgau2nci1n/swatch', 'http://www.w3.org/2000/01/rdf-schema#', 'https://www.hackerone.com/resources/hyatt', 'https://docs.hackerone.com', 'https://www.linkedin.com/company/hackerone', 'https://hackerone.com/att', 'https://hackerone.com/newrelic', 'https://www.instagram.com/hacker0x01', 'consent.truste.com/notice?domain=hackerone.com&c=teconsent&js=nj&noticeType=bb', 'https://hackerone.com/line', 'https://www.twitter.com/Hacker0x01', 'https://www.hackerone.com/resources'}

domain = {'a.ns.hackerone.com', 'gslink.hackerone.com', 'mta-sts.forwarding.hackerone.com', 'zendesk1.hackerone.com', 'info.hackerone.com', 'b.ns.hackerone.com', 'www.hackerone.com', 'zendesk2.hackerone.com', 'o1.email.hackerone.com', 'zendesk4.hackerone.com', 'support.hackerone.com', 'api.hackerone.com', 'forwarding.hackerone.com', 'events.hackerone.com', 'mta-sts.hackerone.com', 'links.hackerone.com', 'mta-sts.managed.hackerone.com', '3d.hackerone.com', 'zendesk3.hackerone.com', 'cover-photos-user-content.hackerone.com', 'docs.hackerone.com', 'email.gh-mail.hackerone.com', 'resources.hackerone.com', 'hackerone.com', 'profile-photos-user-content.hackerone.com', 'go.hackerone.com'}
internal = set()
external = set()


for i,j in it.product(url,domain):
    flag = False
    k = urlparse(i).netloc
    if str(k) == str(j):
        internal.add(k)
    elif k not in domain :
        external.add(k)


print(internal)
print("\n\n\n",external)
