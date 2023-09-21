import requests

res = requests.get('https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json').json()

ids = []
def id_taker(content):
    for check in ['revoked','x_mitre_deprecated']:
        if check in content:
            if content[check] == True:return None

    if 'kill_chain_phases' not in content:return None
       
    if len(content['kill_chain_phases']) > 1:
        id_path = content['external_references'][0]['external_id']
        ids.append(id_path)

for content in res['objects']:
    id_taker(content)  
                
result = [i for i in ids if i[0] == 'T']
result = sorted(result)
print(result)
