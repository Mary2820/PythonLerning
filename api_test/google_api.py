import requests


class Test_new_location:

    def test_create_new_location(self):

        base_url = 'https://rahulshettyacademy.com'
        key = '?key=qaclick123'

        post_resource = '/maps/api/place/add/json'
        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
             ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)
        print('Статус код: ' + str(result_post.status_code))
        assert 200 == result_post.status_code
        print('Успешно!!! Создана новая локация!')

        check_post = result_post.json()
        check_post_info = check_post.get('status')
        print('Статус код-ответа: ' + check_post_info)
        assert check_post_info == 'OK'
        print('Статус ответа верен')

        place_id = check_post.get('place_id')
        print('Place_id: ' + place_id)

        get_resource = '/maps/api/place/get/json'
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)

        print('Статус код: ' + str(result_get.status_code))
        assert 200 == result_get.status_code
        print('Проверка создания новой локации прошла успешно !')

        put_resource = '/maps/api/place/update/json'
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_location)
        print(result_put.text)

        print('Статус код: ' + str(result_put.status_code))
        assert 200 == result_put.status_code
        print('Проверка изменения адреса локации прошла успешно !')

        check_put = result_put.json()
        check_put_info = check_put.get('msg')
        print('Сообщение: ' + check_put_info)
        assert check_put_info == 'Address successfully updated'
        print('Сообщение верно!')

        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        print(delete_url)

        json_for_delete_location = {
                "place_id": place_id
        }

        result_delete = requests.delete(delete_url, json=json_for_delete_location)
        print(result_delete.text)

new_place = Test_new_location()
new_place.test_create_new_location()
