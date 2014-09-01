$("path").each(function(i){
    var path = this;
    var len = path.getTotalLength();
    var p=path.getPointAtLength(0);
    stp=p.x+","+p.y
    for(var i=1; i<len; i++){
        p=path.getPointAtLength(i);
        stp=stp+","+p.x+","+p.y;
    }
    $(path).replaceWith('<polygon points="' +  stp + '" />');
});
