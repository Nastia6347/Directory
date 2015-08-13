/**
 * Created by user on 06.08.15.
 */
$(function(){
    $("#category a").on("click", function(e) {
        var uri = $(this).attr("href");
        SendingRequest(uri);
        e.preventDefault();
    });

    $("#paginator a").on("click", function(e) {
        var uri = $(this).attr("href");
        SendingRequest(uri);
        e.preventDefault();
    });

    $("#category tr:not(:first, .level-0)").hide();
    $("#search").on('submit', function() {
        $("#category tr:not(:first, .level-0)").hide();
        var search = $("#search_input").val();
        var uri = "/search/?q="+search
        SendingRequest(uri)
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


function SendingRequest(uri) {
    history.pushState('', '', uri);
    $.ajax({
        type: "GET",
        url: uri,
        cache: false,
        success: function (response) {
            $("#resSearch").html(response);
            }
        });
}