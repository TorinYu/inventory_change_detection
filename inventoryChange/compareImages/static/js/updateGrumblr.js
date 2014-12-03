/**
 * Created by zhututu on 10/25/14.
 */
var csrfToken;

$(document).ready(function() {
    csrfToken = $('#search input[name=csrfmiddlewaretoken]').val();
    setInterval(updateGrumblr, 10000)

});

var updateGrumblr = function() {
    var data = {}
    if ($('.grumblrs').children().length > 0) {
        var url = $('.grumblrs').children().first().find('.new-comment').attr('action');
        var currentGrumblrId = url.split('/')[2];
        data.currentGrumblrId = parseInt(currentGrumblrId);
    }
    $.ajax({
        type: 'GET',
        url: "/update_grumblr",
        data: data,
        dataType: 'html',
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(errorThrown);
        },
        success: function(html) {

            $('.grumblrs').prepend(html);
            if ($('.grumblrs').children().length > 0) {
                var url = $('.grumblrs').children().first().find('.new-comment').attr('action');
                currentGrumblrId = url.split('/')[2];
                currentGrumblrId = parseInt(currentGrumblrId);
            }
            $('.new-comment').submit(e, ajaxPostComment);

        }
    })
}