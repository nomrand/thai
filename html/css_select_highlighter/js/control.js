$(document).ready(function () {
    $("#inputCSS").on("keyup", function () {
        selectHTML($("#inputCSS").val());
    });

    $("#inputHTML").on("keyup", function () {
        inToHTML();

        selectHTML($("#inputCSS").val());
    });

    $("#fileUpload").on("change", function () {
        var file = $(this).prop('files')[0];
        if (file && window.FileReader) {
            var reader = new FileReader();
            reader.onload = function () {
                $("#drawContents").html(reader.result)
                htmlToIN();
                htmlChanged();
            }

            reader.readAsText(file);
        }
    });

    htmlToIN();
    htmlChanged();
});

function htmlToIN() {
    let htmlVal = $("#drawContents").html();
    $("#inputHTML").val(htmlVal);
    $("#inputHTML").format({ method: 'xmlmin' });
    $("#inputHTML").format({ method: 'xml' });
}

function inToHTML() {
    let inval = $("#inputHTML").val();
    $("#drawContents").html(inval);

    htmlChanged();
}

function htmlChanged() {
    $("#drawContents *").each(function () {
        let name = this.tagName;
        if (this.id) {
            name += "#" + this.id;
        }
        if (this.className) {
            name += " class='" + this.className + "'";
        }

        $(this).prop('title', name);
    });
}

function selectHTML(selector) {
    $("*").removeClass("selectedHTML");
    try {
        $(selector).addClass("selectedHTML");
    } catch (e) {
        return false;
    }
    return true;
}
