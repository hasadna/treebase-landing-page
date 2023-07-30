import requests
import json

QUERIES = [(
    'tree_count',
    '''SELECT count(1) as val FROM trees_compact'''
), (
    'avg_canopy_cover',
    '''SELECT 100*avg(canopy_area_ratio) as val FROM munis'''
), (
    'count_munis',
    '''SELECT count(1) as val FROM munis'''
), (
    'count_munis_more_than_10',
    '''SELECT count(1) as val FROM munis where canopy_area_ratio > 0.1'''
), (
    'count_contributing_munis',
    '''select count(distinct muni_code) as val from trees_processed where "meta-collection-type"='סקר רגלי' and "meta-source-type"='מוניציפלי' '''
)]

def get_data(query):
    URL = 'https://api.digital-forest.org.il/api/query'
    result = requests.get(URL, params={'query': query}).json()
    if not result['success']:
        print(result)
    return result['rows'][0]['val']

if __name__ == '__main__':
    indicators = dict(
        (name, get_data(query)) for name, query in QUERIES
    )
    indicators = json.dumps(indicators, indent=2)
    with open('projects/treebase/src/app/indicators.ts', 'w') as out:
        out.write(f'export const indicators = {indicators};')
