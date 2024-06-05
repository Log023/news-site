// JavaScript код для добавления комментария с помощью AJAX
$(document).ready(function() {
    $('#add-comment form').submit(function(e) {
        e.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Получаем данные из формы
        var formData = $(this).serialize();

        // Отправляем AJAX запрос
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: formData,
            success: function(response) {
                // Обновляем содержимое комментариев без перезагрузки страницы
                $('#comments').html(response);
                // Очищаем форму после успешного добавления комментария
                $('#add-comment form')[0].reset();
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // Выводим ошибку в консоль
                // Оповещаем пользователя об ошибке
                alert('Произошла ошибка при отправке комментария. Пожалуйста, попробуйте еще раз.');
            }
        });
    });
});
