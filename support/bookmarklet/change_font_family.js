/**
 * Change Page Font-Family to specific google-fonts family name.
 * ex.
 *  changeFontFamilyGF('Kanit');
 *  changeFontFamilyGF('Sarabun');
 *  changeFontFamilyGF('Pridi');
 * @param {*} ff font-family(for google-fonts)
 */
function changeFontFamilyGF(ff) {
    var head = document.getElementsByTagName('head');

    var link = document.createElement('link');
    link.setAttribute('href', 'https:\/\/fonts.googleapis.com\/css?family=' + ff);
    link.setAttribute('rel', 'stylesheet');

    var style = document.createElement('style');
    style.setAttribute('type', 'text\/css');
    style.innerHTML = '* {font-family: ' + ff + ' !important;}';

    head[0].appendChild(link);
    head[0].appendChild(style);
}

