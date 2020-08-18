
  // function api_like() {
  //     var api_url = "{% url 'blog:api_like' blog.pk %}";
  //     var btn = document.getElementById("like");
  //     var request = new XMLHttpRequest();
  //     request.onreadystatechange = function () {
  //         if (request.readyState === 4 && request.status === 200) {
  //             var received_data = JSON.parse(request.responseText);
  //             btn.innerText = received_data.like;
  //         }
  //     }
  //     request.open("GET",api_url);
  //     request.send();
  // }

$(function(){
  $(".nav-button").click(function(){
    $(this).toggleClass("active"),
    $(".nav-menu").toggleClass("active");
  });
});
