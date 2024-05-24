<?php
// This file is part of Moodle - http://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Moodle is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Moodle.  If not, see <http://www.gnu.org/licenses/>.

/**
 * Lists all the users within a given course.
 *
 * @copyright 1999 Martin Dougiamas  http://dougiamas.com
 * @license http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 * @package core_user
 */

require_once ('../../config.php');
require_once ($CFG->dirroot . '/user/lib.php');
require_once ($CFG->dirroot . '/course/lib.php');
require_once ($CFG->dirroot . '/notes/lib.php');
require_once ($CFG->libdir . '/tablelib.php');
require_once ($CFG->libdir . '/filelib.php');
require_once ($CFG->dirroot . '/enrol/locallib.php');
require_once ($CFG->dirroot . '/proctor_ecg/proctor_ecg_init/form.php');
global $CFG, $DB, $USER, $OUTPUT;

use core_table\local\filter\filter;
use core_table\local\filter\integer_filter;
use core_table\local\filter\string_filter;




$PAGE->set_title('ECG_Proctor');
echo $OUTPUT->header();


$roleid = $DB->get_field('role', 'id', ['shortname' => 'editingteacher']);
$isteacheranywhere = $DB->record_exists('role_assignments', ['userid' => $USER->id, 'roleid' => $roleid]);
if (isloggedin() && $isteacheranywhere) {
    echo "<h1>Прокторинг по ЭКГ</h1>";
    echo "<p>Добавить\Удалить прокторинг по ЭКГ</p>";

    $mform = new simplehtml_form();
    $mform->addProctor_ECG();
    $mform->addButton();
    if ($mform->is_cancelled()) {
    } else if ($fromform = $mform->get_data()) {

        // проверяю, что данный пользователь зарегистрирован на этот курс
        try {
            $course_name = $fromform->course_name;
            $course = $DB->get_record('course', ['fullname' => $course_name]);
            $quiz_name = $fromform->quiz_name;
            $quiz = $DB->get_record('quiz', ['course' => $course->id, 'name' => $quiz_name]);
            $select_item = $fromform->proctor_ecg;
            $record = new stdclass;
            $record->quiz_id = $quiz->id;
            $record->proctor_ecg_flag = $select_item;

            $proctor_ecg_course = $DB->get_record('proctor_ecg_course', ['quiz_id' => $quiz->id]);
            if (empty($proctor_ecg_course)) {
                $result = $DB->insert_record('proctor_ecg_course', $record);
                print_r("insert");
            } else {
                $sql = $DB->execute('update mdl_proctor_ecg_course set proctor_ecg_flag= ? where quiz_id = ?', ['proctor_ecg_flag' => $select_item, 'quiz_id' => $quiz->id]);

                if (!$sql) {
                    echo "<p>Ошибка при выполнении запроса.</p>";
                } else {
                    echo "<p>Запрос выполнен. Изменения сохранены.</p>";
                }

            }



        } catch (Exception $e) {
            print_r($e->getMessage());
        }

    } else {
        $mform->set_data($toform);
        $mform->display();

    }
} else {
    echo "<p>У Вас нет прав на просмотр этой странице. Если Вы считаете, что это ошибка, то обратитеcь с администратору сайта.</p>";
}

echo $OUTPUT->footer();
?>