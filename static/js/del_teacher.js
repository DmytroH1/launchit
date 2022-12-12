$(document).ready(() => {

    console.log('del_teacher -> Start');

    $('.del-btn').click((event) => {
        let delTeacherId = $(event.target).prev().val();
        $.ajax({
            url: '/teachers/ajax_del_teacher',
            data: 'del_teacher_id=' + delTeacherId,
            success: (response) => {
                alert(response.report);
                window.location = '/teachers/index';
            }
        });
    });
});