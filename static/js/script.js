$(document).ready(function () {
  // materialise js
  $("select").formSelect();
  $(".collapsible").collapsible();
  $(".sidenav").sidenav();
  $(".modal").modal();

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
        "Are you sure you want to delete this user? This action cannot be undone! ALL RECIPES CONTRIBUTED BY THE USER WILL REMAIN IN THE SYSTEM"
      )
    ) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });

  // delete type button
  $(".delete-type-btn").click(function () {
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
  $(".delete-tool-btn").click(function () {
    if (
      confirm(
        "Are you sure you want to delete this tool? This action cannot be undone!"
      )
    ) {
    } else {
      return false; //----On cancel user returns to current screen------//
    }
  });
  $(".delete-product-btn").click(function () {
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

//   copy discount code confirmation
  $("#copy").click(function () {
    $("#copy").hide();
    $("#tick").show();

  });

//   resets copy confirmation
  $("#thanks").click(function(){
       $("#copy").show();
    $("#tick").hide();

  })
});

// fixed action button and menu made clickable for responsive desgin
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".fixed-action-btn");
  var instances = M.FloatingActionButton.init(elems, {
    direction: "top",
    hoverEnabled: false,
  });
});

//   code from w3 schools https://www.w3schools.com/howto/howto_js_copy_clipboard.asp
// copy the discount code function
function copyCode() {
  /* Get the text field */
  var copyText = document.getElementById("code");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /*For mobile devices*/

  /* Copy the text inside the text field */
  document.execCommand("copy");

  /* Alert the copied text */
  alert("Copied the text: " + copyText.value);
}
