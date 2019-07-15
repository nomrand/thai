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
                let modResult = reader.result;
                modResult = modResult.replace(/>[\s]+</g, "><").replace(/^[\s]+</, "<").replace(/>[\s]+$/, ">");
                // inside body only
                modResult = modResult.replace(/[\s\S]*<body>/, "").replace(/<\/body>[\s\S]*/, "");
                // toHTML & delete no displayed tags (ex. scripts)
                $("body>div>#drawContents").html(modResult);
                htmlToIN();

                // format
                inToHTML();
                htmlToIN();
            }

            reader.readAsText(file);
        }
    });

    htmlToIN();
    htmlChanged();
});

function htmlToIN() {
    let htmlVal = $("body>div>#drawContents").html();
    htmlVal = htmlVal.trim();
    $("#inputHTML").val(htmlVal);
    $("#inputHTML").format({ method: 'xmlmin' });
    $("#inputHTML").format({ method: 'xml' });
}

function inToHTML() {
    let inval = $("#inputHTML").val();
    $("body>div>#drawContents").html(inval);
    $("body>div>#drawContents script, body>div>#drawContents link").remove();

    htmlChanged();
}

function htmlChanged() {
    $("body>div>#drawContents *").each(function () {
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
        $("body>div>#drawContents " + selector).addClass("selectedHTML");
    } catch (e) {
        return false;
    }
    return true;
}
