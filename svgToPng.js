    function styles(dom) {
        var css = "";
        var sheets = document.styleSheets;
        for (var i = 0; i < sheets.length; i++) {
            var rules = sheets[i].cssRules;
            
            if (rules == null)
                return null;

            for (var j = 0; j < rules.length; j++) {
                var rule = rules[j];
                if (typeof(rule.style) != "undefined") {
                    css += rule.selectorText + " { " + rule.style.cssText + " }\n";
                }
            }
        }

        var s = document.createElement('style');
        s.setAttribute('type', 'text/css');
        s.innerHTML = "<![CDATA[\n" + css + "\n]]>";

        var defs = document.createElement('defs');
        defs.appendChild(s);
        return defs;
    }

    function svgSrcToPngSrc(svgSrc, callback){
        var img = new Image();
        img.src = svgSrc;

        var canvas = document.createElement("canvas");
        canvas.width = img.width;
        canvas.height = img.height;

        var context = canvas.getContext("2d");
        context.drawImage(img, 0, 0);

        var pngSrc = canvas.toDataURL("image/png");
        document.body.appendChild(canvas);

        callback(pngSrc);
    }

    function inlineImages(callback) {
        var images = document.querySelectorAll('svg image');
    
        var left = images.length;
        if (left == 0) {
            callback();
        }
        for (var i = 0; i < images.length; i++) {
            (function(image) {
    
                if (image.getAttribute('xlink:href')) {
                    var href = image.getAttribute('xlink:href').value;
                    var attrHref = 'xlink:href'
    
                    if (/^http/.test(href) && !(new RegExp('^' + window.location.host).test(href)))
                        throw new Error("Cannot render embedded images linking to external hosts.");
                }
                else if (image.getAttribute('href')) {
                    var href = image.getAttribute('href').value;
                    var attrHref = 'href'
    
                    if (/^http/.test(href) && !(new RegExp('^' + window.location.host).test(href)))
                        throw new Error("Cannot render embedded images linking to external hosts.");
                }

                svgSrcToPngSrc(image.getAttribute(attrHref), function(pngSrc) {
                    image.setAttribute(attrHref, pngSrc);

                    left--;
                    if (left == 0)
                        callback();
                });
            })(images[i]);
        }
    }


