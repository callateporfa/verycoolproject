import requests
import json


def get_data(page_id, token):
    """Функция получает из паблика все комментарии, возвращает список текстов"""
    posts = requests.get(
        'https://api.vk.com/method/wall.get',
        params={
            "owner_id": page_id,
            "v": "5.92",
            "count": 100,
            "access_token": token
        }
    ).json()['response']['items']
    comments_strings = []
    for post in posts:
        comments = requests.get('https://api.vk.com/method/wall.getComments',
                                params={
                                    "owner_id": page_id,
                                    "v": "5.92",
                                    "post_id": post['id'],
                                    "access_token": token
                                }).json()
        for comment in comments['response']['items']:
            try:
                comments_strings.append(comment['text'])
            except KeyError:
                continue
    return comments_strings


if __name__ == '__main__':
    pages = {
        'Типография НИУ ВШЭ': -163106783, 'Медуза': -76982440,
        'Лентач': -29534144, 'капризный ленгвист': -116496582,
        'ПостНаука': -36507793, 'CLIQUE': -66687279, 'КБ': -67580761,
        'Калик)': -179625476, 'абстрактные мемы для элиты всех сортов | АМДЭВС': -92337511,
        '4ch': -45745333, 'Реализм кухонной раковины': -193675952, 'Астрофотография': -59516873
    }
    token = 'e0ae8496e0ae8496e0ae849618e0d92d7bee0aee0ae849680230dd7fb731f57503a5cc7'
    page_comments = {}
    for name, page_id in pages.items():
        page_comments[name] = get_data(page_id, token)
    with open('results.json', 'w', encoding='utf-8') as file:
        json.dump(page_comments, file, ensure_ascii=False, indent=2)
