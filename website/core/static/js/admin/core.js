function activeClickDelete(url, title)
{
    iziToast.question({
        timeout: 20000,
        close: false,
        overlay: true,
        toastOnce: true,
        zindex: 999,
        title: 'Hey',
        message: gettext('Are you sure to delete <b>') + title + '</>?',
        position: 'center',
        buttons: [
            ['<button><b>' + gettext('Yes') + '</b></button>', function (instance, toast) {
                instance.hide(toast, { transitionOut: 'fadeOut' }, 'button');
                window.location = url;
            }, true],
            ['<button>' + gettext('No') + '</button>', function (instance, toast) {
                instance.hide(toast, { transitionOut: 'fadeOut' }, 'button');
            }]
        ],
    });
}
