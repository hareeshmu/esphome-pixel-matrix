import requests
import os
import json
import yaml

os.makedirs("icons", exist_ok=True)

with open('lametric_icons.json') as f:
    json_data = json.load(f)

for icon in json_data['icons']:
    r = requests.get("https://developer.lametric.com/content/apps/icon_thumbs/" + str(icon['lameid']), timeout=10.0)
    if r.status_code == 200:
        print(f"Downloading icon {icon['id']}")
        with open(f"icons/{icon['lameid']}_{icon['id']}.gif", "wb") as f:
            f.write(r.content)
    else:
        print(f"Failed to download icon {icon['id']}. Status: {r.status_code}")

yaml_data = [{'id': icon['id'], 'file': f"esphome-pixel-matrix/icons/{icon['lameid']}_{icon['id']}.gif"} for icon in json_data['icons']]

with open('icons.yaml', 'w') as f:
    yaml.dump(yaml_data, f)


# import requests
# import concurrent.futures

# def download_icon(i):
#     try:
#         r = requests.get("https://developer.lametric.com/content/apps/icon_thumbs/" + str(i), timeout=4.0)
#         if r.status_code == 200:
#             print(f"Downloading icon {i}")
#             with open(f"icons/{i}.png", "wb") as f:
#                 f.write(r.content)
#         else:
#             print(f"Failed to download icon {i}. Status: {r.status_code}")
#     except Exception as e:
#         print(f"Error downloading icon {i}: {e}")

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(download_icon, range(1, 100000))