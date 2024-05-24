<?php
require_once ('../../config.php');
global $CFG, $DB, $USER, $OUTPUT;
$PAGE->set_title('ECG_Proctor');
echo $OUTPUT->header();

echo '<h1>Прокторинг по ЭКГ</h1>';

$roleid = $DB->get_field('role', 'id', ['shortname' => 'editingteacher']);
$isteacheranywhere = $DB->record_exists('role_assignments', ['userid' => $USER->id, 'roleid' => $roleid]);
if (isloggedin() && $isteacheranywhere) {
    $url_result = $CFG->wwwroot . '/proctor_ecg/proctor_ecg_table_download/';
    $url_edit = $CFG->wwwroot . '/proctor_ecg/proctor_ecg_proct_edit/';
    echo "<p><a href=" . $url_result . ">Перейти к просмотру результатов прокторинга по ЭКГ</a></p>";

    echo "<p><a href=" . $url_edit . ">Редактировать ...</a></p>";

} else {
    echo "<p>У Вас нет прав на просмотр этой странице. Если Вы считаете, что это ошибка, то обратитель с администратору сайта.</p>";
}


echo $OUTPUT->footer();

?>