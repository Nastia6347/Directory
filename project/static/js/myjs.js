/**
 * Created by user on 06.08.15.
 */
$(function(){
    $(".unclickable").on("click", function() {
        SendingRequest();
        return false;
    });
    $("#category tr:not(:first, .level-0)").hide();
    $("#search").on('submit', function() {
        $("#category tr:not(:first, .level-0)").hide();
        var search = $("#search_input").val();
        $.ajax({
            type: "GET",
            url: "/search/?q="+search,
            cache: false,
            success: function (response) {
                $("#resSearch").html(response);
            }
        });
        return false;
    });
});


function countRabbits(element, level) {
    $(element).parents(".level-"+level).each( function() {
        $(this).css("background-color", "#cceecc").nextUntil(".level-"+level).filter(".level-"+(level+1)).slideDown();
        $(this).siblings(":visible").css("background-color", "#ffffff")
            .not(":animated, :first, .level-0, .level-"+level).not(".level-"+(level-1)).slideUp();
    });
}


function SendingRequest() {
    alert($(this));
    //$.ajax({
    //    type: "GET",
    //    url: "???",
    //    cache: false,
    //    success: function (response) {
    //        $("#resSearch").html(response);
    //        }
    //    });
}