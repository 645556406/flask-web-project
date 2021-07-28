/**
  扩展一个 mymod 模块
**/

layui.define(function(exports){ //提示：模块也可以依赖其它模块，如：layui.define('mod1', callback);
  var $ = layui.jquery;
  var obj = {
    hello: function(str){
      alert('Hello '+ (str||'mymod'));
    },
    getQueryVariable: function(variable) {
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
    },
    selectNav: function() {
        var navobjs = $("#nav a");
        $.each(navobjs, function () {
        var href = $(this).attr("href");
        if (pathname.indexOf(href) != -1) {
            $(this).parent().addClass('layui-this');
        }
    });
    }
  };

  //输出 mymod 接口
  exports('mymod', obj);
});