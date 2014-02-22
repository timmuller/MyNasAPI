var SystemInfo = {
    init: function(){
        SystemInfo.reloadData();
        setInterval(SystemInfo.reloadData, 5000);
    },
    reloadData:function(self){
        SystemInfo.retrieveData()
    },
    retrieveData: function(){
        $.get('/api/v1/systeminfo', function(data){
            for(i in data){
                $("#text_" + i).text(data[i]);
            }
        });
    }
}


$(document).ready(function(){
   SystemInfo.init()
});
