/**
 * Created by user on 06.08.15.
 */
$(function(){
    $("#search").on('submit', function() {
        var search = $("#search_input").val();
        //$("#bread_crumbs").html('Результаты поиска по запросу: '+search);
        $.ajax({
            type: "GET",
            url: "/search/",
            data: {"q": search},
            cache: false,
            success: function (response) {
                $("#resSearch").html(response);
            }
        });
        //var resSearch = $("#resSearch");
        //save(search, resSearch);
        return false;
    });
});

//function save(search, resSearch) {
//    if (window.localStorage) {
//        localStorage.loan_search = search;
//        localStorage.loan_resSearch = resSearch;
//    };
//};
//
//window.onload = function onload() {
//    if (window.localStorage && localStorage.loan_search) {
//        $("#bread_crumbs").html('Результаты поиска по запросу: '+localStorage.loan_search);
//        $("#resSearch").html(localStorage.loan_resSearch.html());
//    };
//};