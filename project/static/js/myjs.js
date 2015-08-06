/**
 * Created by user on 06.08.15.
 */
$(function(){
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