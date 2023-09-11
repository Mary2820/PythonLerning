import datetime
import os

from requests import Response


class Logger:
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    print('Это родительский путь ' + parent_directory)
    file_name = f"log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"
    # file_name = f"log.log"
    file_path = os.path.join(parent_directory, file_name)
    print(file_path)

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_path, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)
            # print('Это родительский путь ' + cls.parent_directory)
            # print('Это текущий путь ' + cls.current_directory)
            # print('Это путь ' + cls.file_path)




    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        # cls.current_directory = test_name
        # cls.parent_directory = os.path.dirname(cls.current_directory)
        # cls.file_path = os.path.join(cls.parent_directory, cls.file_name)

        data_to_add = f'\n-----\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Time: {str(datetime.datetime.now())}\n'
        data_to_add += f'Request method: {method}\n'
        data_to_add += f'Request URL: {url}\n'
        data_to_add += '\n'

        cls.write_log_to_file(data_to_add)
        print("jdivjlij")

    @classmethod
    def add_response(cls, result: Response):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f'Response code: {result.status_code}\n'
        data_to_add += f'Response text: {result.text}\n'
        data_to_add += f'Response headers: {headers_as_dict}\n'
        data_to_add += f'Response cookies: {cookies_as_dict}\n'
        data_to_add += f'\n-----\n'

        cls.write_log_to_file(data_to_add)