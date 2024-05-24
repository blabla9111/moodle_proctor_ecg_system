<?php
/**
 * Simple file test.php to drop into root of Moodle installation.
 * This is the skeleton code to print a downloadable, paged, sorted table of
 * data from a sql query.
 */
require_once ('../../config.php');
require_once ($CFG->libdir . '/tablelib.php');
require_once ($CFG->dirroot . '/proctor_ecg/proctor_ecg_table_download/index.php');
require_once ($CFG->dirroot . '/proctor_ecg/proctor_ecg_init/form.php');

$context = context_system::instance();

$PAGE->set_context($context);
$PAGE->set_url('/proctor_ecg/proctor_ecg_table_download/index.php');

$download = optional_param('download', '', PARAM_ALPHA);

$table = new table_sql('uniqueid');
$table->is_downloading($download, 'test', 'testing123');
if (!$table->is_downloading()) {
    $PAGE->set_title('Results');
    $PAGE->set_heading('Таблица с результатами прохождения прокторинга по ЭКГ');
    $PAGE->navbar->add('Testing table class', new moodle_url('/proctor_ecg/proctor_ecg_table_download/test.php'));
    echo $OUTPUT->header();
}
$roleid = $DB->get_field('role', 'id', ['shortname' => 'editingteacher']);
$isteacheranywhere = $DB->record_exists('role_assignments', ['userid' => $USER->id, 'roleid' => $roleid]);
if (isloggedin() && $isteacheranywhere) {
    $mform = new simplehtml_form();
    $mform->addButton();
    if ($mform->is_cancelled()) {
    } else if ($fromform = $mform->get_data()) {

        // проверяю что данный пользователь зарегистрирован на этот курс
        try {

            $course_name = $fromform->course_name;
            $course = $DB->get_record('course', ['fullname' => $course_name]);
            $quiz_name = $fromform->quiz_name;
            // print_r($course);
            $quiz = $DB->get_record('quiz', ['course' => $course->id, 'name' => $quiz_name]);
            $context = context_course::instance($course->id);
            // is_enrolled($context, $USER->id, '', true);
            echo "<p><a href=" . $CFG->wwwroot . "/proctor_ecg/proctor_ecg_table_download/test2.php?quiz_id=" . $quiz->id . " >Подробнее о непрошедших идентификацию по ЭКГ</a></p>";
            $where = "p.quiz_id = " . $quiz->id;
            $table->set_sql('p.start_time, p.end_time,p.proctor_result as is_bad, u.username, u.firstname, u.lastname, u.email', "{proctor_user} p inner join {user} u on p.user_id=u.id", $where);

            $table->define_baseurl("$CFG->wwwroot/proctor_ecg/proctor_ecg_table_download/test.php?quiz_id=" . $quiz->id);

            $table->out(40, true);
            $table->finish_output();

        } catch (Exception $e) {
            print_r($e->getMessage() . "Проверьте на корректность введенные значения");
        }

    } else {
        $mform->set_data($toform);
        $mform->display();
    }
} else {
    echo "<p>У Вас нет прав на просмотр этой странице. Если Вы считаете, что это ошибка, то обратитеcь с администратору сайта.</p>";
}


if (!$table->is_downloading()) {

    echo $OUTPUT->footer();
}


?>