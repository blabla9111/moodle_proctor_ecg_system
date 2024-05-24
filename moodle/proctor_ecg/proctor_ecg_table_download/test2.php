<?php
/**
 * Simple file test.php to drop into root of Moodle installation.
 * This is the skeleton code to print a downloadable, paged, sorted table of
 * data from a sql query.
 */
require_once ('../../config.php');
require_once ($CFG->libdir . '/tablelib.php');
require_once ($CFG->dirroot . '/proctor_ecg/proctor_ecg_init/form.php');

$context = context_system::instance();

$PAGE->set_context($context);
$PAGE->set_url('/proctor_ecg/proctor_ecg_table_download/test2.php');

$download = optional_param('download', '', PARAM_ALPHA);

$table = new table_sql('uniqueid');
$table->is_downloading($download, 'test', 'testing123');
if (!$table->is_downloading()) {
    $PAGE->set_title('Results');
    $PAGE->set_heading('Таблица с неуспешными прохождениями прокторинга');
    $PAGE->navbar->add('Testing table class', new moodle_url("/proctor_ecg/proctor_ecg_table_download/test2.php?quiz_id=" . $query['quiz_id']));
    echo $OUTPUT->header();
}
$roleid = $DB->get_field('role', 'id', ['shortname' => 'editingteacher']);
$isteacheranywhere = $DB->record_exists('role_assignments', ['userid' => $USER->id, 'roleid' => $roleid]);
if (isloggedin() && $isteacheranywhere) {

    $url = $_SERVER['REQUEST_URI'];
    $parts = parse_url($url);
    parse_str($parts['query'], $query);
    $where = "u.quiz_id = " . $query['quiz_id'];
    $table->set_sql('p.curr_time, mu.username, mu.firstname, mu.lastname, mu.email', "{proctor_bad_result_info} p inner join {proctor_user} u on p.id_transaction=u.id_transaction inner join {user} mu ON u.user_id=mu.id", $where);

    $table->define_baseurl("$CFG->wwwroot/proctor_ecg/proctor_ecg_table_download/test2.php?quiz_id=" . $query['quiz_id']);

    $table->out(40, true);
    $table->finish_output();


} else {
    echo "<p>У Вас нет прав на просмотр этой странице. Если Вы считаете, что это ошибка, то обратитеcь с администратору сайта.</p>";
}

if (!$table->is_downloading()) {

    echo $OUTPUT->footer();
}


?>