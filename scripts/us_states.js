// grab info from http://www.geonames.org/US/administrative-division-united-states.html
$('#subdivtable1 tr').each(function(idx, elt){
    var code = $(elt).find('span[id*="isoSpan"]').text();
    if (code) {
        var link = $(elt).find('span[id*="nameSpan"] a');
        var href = link.attr('href');
        if (href) {
            var gid = href.split('/')[3];
            var name = link.text();
            console.log("'"+code+"': {'code': '"+code+"', 'name': '"+name+"', 'geonameid': "+gid+"},");
        }
    }
});
