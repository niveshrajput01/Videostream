$(document).ready(function(){
 $.getJSON("/displayallcategoryjson",function(data){
    $.each(data,function(index,item){
       $('#cid').append($('<option>').text(item[1]).val(item[0]))

    } )
 })

  $('#cid').change(function(){
     $('#sid').empty()
     $('#sid').append($('<option>').text("-Select Show-"))
     $.getJSON("/displayallshowjson",{cid:$('#cid').val()},function(data){
       $.each(data,function(index,item){
         $('#sid').append($('<option>').text(item[2]).val(item[1]))
       })

     })

  })

    $('#st').keyup(function() {
      $.getJSON("/searching", {st: $('#st').val()}, function (data) {
          htm=''
          $.each(data, function (index, item) {

            htm+="<a href='#'><img src='/static/"+item[11]+"' class='zoom' style='width: 115px;margin:5px;border-radius: 5px;' /></a>"

          })
           $('#search').html(htm)
      })
  })



})