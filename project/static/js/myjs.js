/**
 * Created by user on 06.08.15.
 */
$(function(){
    $("#category tr:not(:first, .level-0)").hide();
    $("#category tr:not(:first).level-0").click(function() {
        $(this).nextUntil(".level-0").filter(".level-1").slideDown().click(function() {
            $(this).nextUntil(".level-1").filter(".level-2").slideDown();
            $("#category tr:not(:first, .level-0, :animated):visible.level-2").slideUp();
        });
        $("#category tr:not(:first, .level-0, :animated):visible").slideUp();
    });

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

