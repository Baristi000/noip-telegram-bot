import requests
import base64


def get_ip():
  r = requests.get("https://httpbin.org/ip")
  return r.json()["origin"]

def update_ip_domain(
  username,
  password,
  domain,
  ip
):
  __title__ = "Baristi"
  __version__ = "1.0.0"
  __author__ = "Baristi Trieu"
  __email__ = "ltqtrieu.0204@gmail.com"
  
  auth_str = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")

  r = requests.get(
    url=f"http://dynupdate.no-ip.com/nic/update?hostname={domain}&myip={ip}",
    headers= {
      "Authorization": f"Basic {auth_str}",
      "User-Agent": f"{__title__}/{__version__} ltqtrieu.0204@gmail.com"
    }
  )
  return r.status_code

ip = get_ip()
res = (update_ip_domain(
  "Baristi000",
  "Trieukute_2420",
  "idp-server.ddns.net",
  ip
))

