<?php
require_once ("$CFG->libdir/formslib.php");

class simplehtml_form extends moodleform
{

    // Add elements to form.
    public function definition()
    {
        // A reference to the form is stored in $this->form.
        // A common convention is to store it in a variable, such as `$mform`.
        $mform = $this->_form; // Don't forget the underscore!

        // Add elements to your form.

        $mform->addElement('text', 'course_name', 'Название курса');

        // Set type of element.
        $mform->setType('course_name', PARAM_NOTAGS);

        // Default value.
        $mform->setDefault('course_name', 'Test1_course');

        $mform->addElement('text', 'quiz_name', 'Название теста');

        // Set type of element.
        $mform->setType('quiz_name', PARAM_NOTAGS);

        // Default value.
        $mform->setDefault('quiz_name', 'Входной тест');
    }

    public function addProctor_ECG()
    {
        $mform = $this->_form;
        $mform->addElement('select', 'proctor_ecg', 'Добавить прокторинг по ЭКГ', array('Удалить', 'Добавить'));
        $mform->setType('proctor_ecg', PARAM_NOTAGS);
    }

    public function addButton()
    {
        $this->add_action_buttons(false, 'Отправить');
    }
    function validation($data, $files)
    {
        return [];
    }
}
?>