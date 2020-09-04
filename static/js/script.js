$(document).ready(function () {
  $("select").formSelect();
  $(".collapsible").collapsible();
  $(".sidenav").sidenav();
  $("#logout").click(function () {
    if (confirm("Are you sure you want to logout?")) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });
  /*------Delete Button Confirmation-----*/
  $('.delete-btn').click(function () {
    if (confirm("Are you sure you want to DELETE this recipe? This action cannot be undone!")) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });
});
