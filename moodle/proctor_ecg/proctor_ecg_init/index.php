<?php
require_once ('../../config.php');
global $CFG, $DB, $USER, $OUTPUT;
require_once ($CFG->dirroot . '/proctor_ecg/proctor_ecg_init/form.php');
require_once ($CFG->dirroot . '/proctor_ecg/ecgproctor.php');
$PAGE->set_title('ECG_Proctor');
echo $OUTPUT->header();

echo "<h1>Прокторинг по ЭКГ</h1>";

// только зарегистрированные пользователи видят информацию
if (isloggedin()) {
    $mform = new simplehtml_form();
    $mform->addButton();

    if ($mform->is_cancelled()) {
    } else if ($fromform = $mform->get_data()) {

        // проверяю, что данный пользователь зарегистрирован на этот курс
        try {
            $course_name = $fromform->course_name;
            $course = $DB->get_record('course', ['fullname' => $course_name]);
            $quiz_name = $fromform->quiz_name;
            $quiz = $DB->get_record('quiz', ['course' => $course->id, 'name' => $quiz_name]);
            $context = context_course::instance($course->id);
            if (is_enrolled($context, $USER->id, '', true) and $quiz) {
                $req = new Request($CFG->wwwproctorecg . "/take_code");
                $data = array('user_id' => $USER->id, 'quiz_id' => $quiz->id);
                $json = json_encode($data);
                $data_2 = array('json' => $json);
                if (empty($req->httpPost($CFG->wwwproctorecg . "/take_code", $data_2))) {
                    print_r("Сервер недоступен. Зайдите позже(");
                } else {
                    print_r("Введите в приложение " . $req->httpPost($CFG->wwwproctorecg . "/take_code", $data_2));
                }

            }
        } catch (Exception $e) {
            print_r($e->getMessage());
        }

    } else {
        $mform->set_data($toform);
        $mform->display();
    }

}
echo $OUTPUT->footer();
?>