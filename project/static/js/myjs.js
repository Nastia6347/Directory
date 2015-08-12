/**
 * Created by user on 06.08.15.
 */
$(function(){
    $("#category tr:not(:first, .level-0)").hide();
    $("#search").on('submit', function() {
        var search = $("#search_input").val();
        $.ajax({
            type: "GET",
            url: "/search/",
            data: {"q": search},
            cache: false,
            success: function (response) {
                $("#resSearch").html(response);
            }
        });
        return false;
    });
});
function countRabbits(element, level, slug) {
    $(element).nextUntil(".level-"+level).filter(".level-"+(level+1)).slideDown();
    $(element).siblings(":visible").not(":animated, :first, .level-0, .level-"+level).not(".level-"+(level-1)).slideUp();
    $.ajax({
        type: "GET",
        url: slug,
        cache: false,
        success: function (response) {
            $("#resSearch").html(response);
            }
        });
    }

