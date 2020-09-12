$(document).ready(function () {
  $("select").formSelect();
  $(".collapsible").collapsible();
  $(".dropdown-trigger").dropdown();
  $(".sidenav").sidenav();
  $("#logout").click(function () {
    if (confirm("Are you sure you want to logout?")) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });
  /*------Delete Button Confirmation-----*/
  $(".delete-btn").click(function () {
    if (
      confirm(
        "Are you sure you want to DELETE this recipe? This action cannot be undone!"
      )
    ) {
      alert("RECIPE HAS BEEN SUCCESSFULLY DELETED");
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });

  //   back button for breadcrumb nav

  $("#back").click(function () {
    window.history.back();
  });

  $("#save-btn").click(function () {
    alert("This recipe has been SAVED successfully!");
    $(".lever").addAttribute("selected");
    $("#save-text").text("SAVED");
  });

  //   remove button for saved recipes
  $(".remove-btn").click(function () {
    $(".remove").toggle("left");
  });

  $(".remove").click(function () {
    if (
      confirm(
        "Are you sure you want to REMOVE this recipe from the SAVED RECIPES? This action cannot be undone!"
      )
    ) {
      alert("RECIPE HAS BEEN SUCCESSFULLY REMOVED");
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });

  //   button pulse function
  $("button").mouseover(function () {
    $(this).addClass("pulse");
  });
  $("button").mouseout(function () {
    $(this).removeClass("pulse");
  });

  // Shows all recipes
  $("#allRecipes").click(function () {
    $(".recipe-cards").attr("hidden", false);
  });

  //   Recipe types menu to be shown
  $("#types-btn").click(function () {
    $("#recipeTypeCards").slideToggle("slow");
    $("#all_recipes").hide("slow");
  });
  //   Shows all Vegan Recipes
  $("#vegan").click(function () {
    $("#all_recipes").toggle("slow");
  });

  //   management template
  $("#all_users").click(function () {
    $("#user-table").toggle("slow");
    $("#types-table").hide("slow");
  });

  $("#recipes-btn").click(function () {
    $("#recipe-table").toggle("slow");
    $("#user-table").hide("slow");
    $("#types-table").hide("slow");
  });

  $("#types-btn").click(function () {
    $("#types-table").show("slow");
    $("#recipe-table").hide("slow");
    $("#user-table").hide("slow");
  });

  $("#email_link").click(function () {
    if (confirm("Would you like to Email this User?")) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });
  $("#delete-user-btn").click(function () {
    if (
      confirm(
        "Are you sure you want to delete this user? This action cannot be undone!"
      )
    ) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });
  $("#delete-type-btn").click(function () {
    if (
      confirm(
        "Are you sure you want to delete this recipe type? This action cannot be undone!"
      )
    ) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });
  $("#add_type_show").click(function () {
    $("#add_type").slideToggle("slow");
  });

  //   searchbars
  $(".search").click(function () {
    $(".inner-search").slideToggle("slow");
  });

});
