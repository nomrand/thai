const IS_FIT_AR_ON_MARKER = false;
const ORG_MARKER_SIZE = 512;

function createAllMarker(data, sceneElement) {
    let assetsElement = $("<a-assets>");
    sceneElement.append(assetsElement);

    for (let i = 0; i < data.length; i++) {
        // idnum will be 3 digit
        let idnum = "000" + i;
        idnum = idnum.substring(idnum.length - 3, idnum.length);

        // a-marker
        let amarker = null;
        if (typeof data[i].barcode !== "undefined") {
            // for barcode marker
            // markers created by "http://au.gmented.com/app/marker/marker.php"
            let barcodeValue = data[i].barcode;
            amarker = $("<a-marker type='barcode' value='" + barcodeValue + "'>");
        }
        else if (typeof data[i].patt !== "undefined") {
            // for pattern marker
            // markers&patterns created by "https://jeromeetienne.github.io/AR.js/three.js/examples/marker-training/examples/generator.html"
            let patternName = data[i].patt;
            amarker = $("<a-marker type='pattern' url='" + patternName + "'>");
        }
        sceneElement.append(amarker);

        // asset
        let assetName = data[i].img;
        if (assetName.endsWith(".jpeg") || assetName.endsWith(".jpg") || assetName.endsWith(".gif")
            || assetName.endsWith(".bmp") || assetName.endsWith(".png")) {
            // image asset
            let img = $("<img crossorigin='anonymous'>");
            let idstr = "img" + idnum;
            img.attr("id", idstr);
            img.attr("src", assetName);

            img.on("load", function () {
                // a-image using asset
                // to get width/height, creation must start after asset loaded
                let aimage = $("<a-image>");
                aimage.attr("src", "#" + idstr);

                // image rotation
                let rotate = data[i].rotate ? data[i].rotate : "-90 0 0";
                aimage.attr("rotation", rotate);

                if (!IS_FIT_AR_ON_MARKER) {
                    // get width / height ratio(AR image will have same size as marker)
                    let h = this.height / ORG_MARKER_SIZE;
                    let w = this.width / ORG_MARKER_SIZE;
                    h = Math.round(h * 100) / 100;
                    w = Math.round(w * 100) / 100;
                    aimage.attr("width", w);
                    aimage.attr("height", h);
                }

                amarker.append(aimage);
            });
            assetsElement.append(img);
        }
        else if (assetName.endsWith(".glb") || assetName.endsWith(".gltf")) {
            // 3d asset
            let asset = $("<a-asset-item>");
            asset.attr("id", "obj" + idnum);
            asset.attr("src", assetName);
            assetsElement.append(asset);

            let primitive = $("<a-entity gltf-model=#obj" + idnum + " />");
            amarker.append(primitive);
        }
    }
}
