import requests


class Test_new_joke:

    def __init__(self):
        pass

    @staticmethod
    # def create_random_joke():
    #     url = 'https://api.chucknorris.io/jokes/random'
    #     print(url)
    #     result = requests.get(url)
    #     print('Статус код: ' + str(result.status_code))
    #     assert 200 == result.status_code
    #     print('Успешно!!! Мы получили новую шутку!')
    #     result.encoding = 'utf-8'
    #     # print(result.text)
    #     check = result.json()
    #     check_info_value = check.get('value')
    #     print(check_info_value)
    #     name = 'Chuck'
    #     if name in check_info_value:
    #         print('Имя Chuck присутствует')
    #     else:
    #         print('Имя Chuck отсутствует')

    def create_random_categories_joke():
        category = 'sport'
        url = 'https://api.chucknorris.io/jokes/random?category=' + category
        print(url)
        result = requests.get(url)
        print('Статус код: ' + str(result.status_code))
        assert 200 == result.status_code
        print('Успешно!!! Мы получили новую шутку!')
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get('categories')
        print(check_info)
        assert  check_info == ["sport"]
        print('Категория верна')


        # check_info_value = check.get('value')
        # print(check_info_value)
        # name = 'Chuck'
        # if name in check_info_value:
        #     print('Имя Chuck присутствует')
        # else:
        #     print('Имя Chuck отсутствует')

# random_joke = Test_new_joke()
# random_joke.create_random_joke()

sport_joke = Test_new_joke()
sport_joke.create_random_categories_joke()
