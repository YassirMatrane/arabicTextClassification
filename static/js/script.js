$(function() {
 
  $("#process").click(function(){
    xhr = new XMLHttpRequest()
    comment = $("#comment").val()
    xhr.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200) {
      resp = JSON.parse(xhr.response)

      $("#result_text").html(resp['comment'])
      $("#hate_value").html('Hate: ' + resp['hate'])
      $("#offense_value").html('Offense: ' + resp['offense'])
    }
    if (this.status === 204 || this.status === 205) {
      console.log("nothing to parse")
    }
    };
    xhr.open("GET", "/classifier/"+comment, true)
    xhr.send()
  })

})

