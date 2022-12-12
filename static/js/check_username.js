$(document).ready(() => {
    console.log('check_username.js -> OK');

    console.log('script -> start');
    let usernameIsValid = false;
    let emailIsValid = false;
    let password1IsValid = false;
    let password2IsValid = false;


    // Login:
    // ========================================================================
    const usernameInput = $('#floatingusername');
    usernameInput.blur(() => {
        console.log('username -> blur');
        let username = usernameInput.val();
        let pattern = /^[a-zA-Z][a-zA-Z0-9_\-\.]{5,15}$/;
        let message = 'Логін довжиною від 6 до 16 символів, перший - буква,';
        message += ' інші - букви(великі або маленькі), цифри, ';
        message += ' знаки(_, -, .) ';
        //
        if (pattern.test(username)) {
            // !!! Перевірка зайнятості логіну:
            // ================================
            console.log('pattern -> ok');
            $.ajax({
                url: '/account/ajax_check_username',
                data:  'username=' + username,
                success: function(response) {
                    console.log('ajax -> check_username');
                    console.log('message -> ', response.message_username);
                    console.log('ajax_message ->', response.ajax_message)
                    console.log('quntity ->', response.quntity)
                    let result = response.ajax_message;
                    if (result === 'Ok') {
                        console.log('result = Ok')
                        $('#error-username').text('Логін зайнятий');
                        usernameInput.css('box-shadow', '0 0 10px red');
                        usernameIsValid = false;
                    } else {
                        console.log('result = not Ok')
                        usernameInput.css('box-shadow', '0 0 10px green');
                        $('#error-username').text('');
                        // Якщо логіна немає в базі даних, то success нічого не повертає і не діє
                        $('#error-username').text('Логін не зайнятий');
                        usernameIsValid = true;
                    }
                }
            });
        } else {
            console.log('pattern -> not ok');
            usernameInput.css('box-shadow', '0 0 10px red');
            $('#error-username').text(message);
            usernameIsValid = false;
        }
    });

    // Email:
    // ========================================================================
    const emailInput = $('#floatingemail');
    emailInput.blur(() => {
        console.log('email -> blur');
        let email = emailInput.val();
        let pattern = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
        let message = ' Перша частина - букви(великі або маленькі), знаки ';
        message += ' (_, -, .), цифри, обов`язково знак @! Друга частина - ';
        message += ' букви(маленькі), знак(.), букви(маленькі)';
        //
        if (pattern.test(email)) {
            // !!! Перевірка зайнятості пошти:
            // ================================
            $.ajax({
                url: '/account/ajax_check_email',
                data: 'email=' + email,
                success: function(response) {
                    console.log('ajax -> check_email');
                    console.log('message -> ', response.message_email);
                    console.log('ajax_message ->', response.ajax_message)
                    console.log('quntity ->', response.quntity)
                    let result = response.ajax_message;
                    if (result === 'Ok') {
                        console.log('result = Ok')
                        $('#error-email').text('Пошта зайнята');
                        emailInput.css('box-shadow', '0 0 10px red');
                        emailIsValid = false;
                    } else {
                        console.log('result = not Ok')
                        emailInput.css('box-shadow', '0 0 10px green');
                        $('#error-email').text('');
                        // Якщо пошти немає в базі даних, то success нічого не повертає і не діє
                        $('#error-email').text('Пошта не зайнята');
                        emailIsValid = true;
                    }
                }
            });
        } else {
            console.log('pattern -> not ok');
            emailInput.css('box-shadow', '0 0 10px red');
            $('#error-email').text(message);
            emailIsValid = false;
        }
    });

    // Pass1:
    // ========================================================================
    const password1Input = $('#floatingpassword1');
    password1Input.blur(() => {
        console.log('password1 -> blur');
        let password1 = password1Input.val();
        let pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9_\-\.]{8,}$/;
        let message = 'Пароль довжиною від 8 символів, хоча б одна велика';
        message += ' літера, хоча б одна маленька літера, хоча б одна цифра, ';
        message += ' інші - букви(великі або маленькі), цифри, _, -, .';
        //
        if (pattern.test(password1)) {
            password1Input.css('box-shadow', '0 0 10px green');
             $('#error-password1').text('');
             password1IsValid = true;
        } else {
            password1Input.css('box-shadow', '0 0 10px red');
            $('#error-password1').text(message);
            password1IsValid = false;
        }
    });

    // Pass2:
    // ========================================================================
    const password2Input = $('#floatingpassword2');
    password2Input.blur(() => {
        console.log('password2 -> blur');
        let password1 = password1Input.val();
        let password2 = password2Input.val();
        let message = 'Паролі не співпадають!';
        //
        if (password1 === password2) {
            password2Input.css('box-shadow', '0 0 10px green');
             $('#error-password2').text('');
             password2IsValid = true;
        } else {
            password2Input.css('box-shadow', '0 0 10px red');
            $('#error-password2').text(message);
            password2IsValid = false;
        }
    });


    // Submit:
    // ========================================================================
    $('#submit').click((event) => {
        console.log('submit -> click');
        console.log(usernameIsValid);
        console.log(password1IsValid);
        console.log(password2IsValid);
        console.log(emailIsValid);
        if (usernameIsValid && password1IsValid && password2IsValid && emailIsValid) {
            console.log('OK');
        } else {
            console.log('FAILED');
            event.preventDefault();
            alert('Відправка даних заблокована валідатором!');
        }
    });

});
