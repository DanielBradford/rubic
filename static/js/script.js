$(document).ready(function () {
  // materialise js
  $("select").formSelect();
  $(".collapsible").collapsible();
  $(".dropdown-trigger").dropdown();
  $(".sidenav").sidenav();
  $(".modal").modal();
  $('.fixed-action-btn').floatingActionButton();

  //   logout confirm function
  $(".logout").click(function () {
    if (confirm("Are you sure you want to logout?")) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });
  //   /*------Delete Button Confirmation-----*/
  //   confirms the user wants to delete the recipe
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
  $(".back").click(function () {
    window.history.back();
  });

  //   remove button for saved recipes
  $(".remove-btn").click(function () {
    $(".remove").toggle("left");
  });

  //   the above presents the following to the user
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

  //   random button border add
  $("#random-btn").click(function () {
    $(".collection-item").addClass("random-border");
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
  //   all user button
  $("#all_users").click(function () {
    $("#user-table").show("slow");
    $("#types-table").hide("slow");
    $("#prodsAndTools").hide("slow");
    $("#types-table").hide("slow");
  });

  // recipes button
  $("#recipes-btn").click(function () {
    $("#recipe-table").show("slow");
    $("#user-table").hide("slow");
    $("#types-table").hide("slow");
    $("#prodsAndTools").hide("slow");
  });

  // recipe types button
  $("#types-btn").click(function () {
    $("#types-table").show("slow");
    $("#recipe-table").hide("slow");
    $("#user-table").hide("slow");
    $("#prodsAndTools").hide("slow");
  });

    // Products and Tools button
  $("#prodsAndTools-btn").click(function () {
    $("#prodsAndTools").show("slow");
    $("#recipe-table").hide("slow");
    $("#user-table").hide("slow");
    $("#types-table").hide("slow");
  });
  // email confirmation
  $("#email_link").click(function () {
    if (confirm("Would you like to Email this User?")) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });

  // delete user button
  $(".delete-user-btn").click(function () {
    if (
      confirm(
        "Are you sure you want to delete this user? This action cannot be undone!"
      )
    ) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });

  // delete type button
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
  //   delete tool /product confirm
  $("#delete-tool").click(function () {
    if (
      confirm(
        "Are you sure you want to delete this tool? This action cannot be undone!"
      )
    ) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });
  $("#delete-product").click(function () {
    if (
      confirm(
        "Are you sure you want to delete this product? This action cannot be undone!"
      )
    ) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });

  //   add type button
  $("#add_type_show").click(function () {
    //   changes drop down icon to exit icon
    $(".fa-chevron-down").toggle();
    $(".fa-times").toggle();
    $("#add_type").slideToggle("slow");
  });

  //add product
  $("#add-product-btn").click(function () {
    //   changes drop down icon to exit icon
    $(".fa-chevron-down").toggle();
    $(".fa-times").toggle();
    $("#add_product").slideToggle("slow");
  });
  //add tool
  $("#add-tool-btn").click(function () {
    //   changes drop down icon to exit icon
    $(".fa-chevron-down").toggle();
    $(".fa-times").toggle();
    $("#add_tool").slideToggle("slow");
  });

  //   searchbars
  $(".search").click(function () {
    $("#search-glass").toggle("medium");
    $(".fa-times").toggle("medium");
    $(".inner-search").fadeToggle("medium");
  });
});
