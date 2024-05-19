APP_THEME = ["sun-valley", "light"]
ECG_PROCTOR_SERVER_URL = "http://127.0.0.1:8000"
FIND_CODE_URL = "/find_code"
SEND_INIT_ECG_URL = "/send_init_ecg"
CHECK_ECG_URL = "/check_ecg"
CLOSE_DESKTOP_URL = "/close_desktop"
REQUEST_RARAMS_DICT = {"code":"code",
                       "id_transaction":"id_transaction",
                       "ecg_data":"ecg_data"}
APP_NAME = "ECG proctor APP"
APP_END_CODE = "602"
APP_TEXT_DICT = {"enter_code":"Введите код из Moodle",
                 "enter_code_button":"Отправить",
                 "start_ecg":"Для начала непрерывной идентификации\nподключите датчики ЭКГ и нажмите на кнопку ",
                 "start_ecg_button":"Начать снимать ЭКГ",
                 "ecg_in_progress":"Непрерывная идентификация началась. \nМожете приступать к выполнению теста. \nПосле завершения теста идентификация завершится сама. ",
                 "ecg_end":"Непрерывная идентификация по ЭКГ завершена. Можете закрыть приложение."}