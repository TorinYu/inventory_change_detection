/**
 * Created by zhututu on 10/24/14.
 */
var csrfToken;

$(document).ready(function() {
    csrfToken = $('#search input[name=csrfmiddlewaretoken]').val();
    $('.new-comment').submit(ajaxPostComment);

});

var ajaxPostComment = function(e) {
    e.preventDefault();

    var commentForm = $(this);
    commentForm.children('input[name="csrfmiddlewaretoken"]').val(csrfToken);

    $.ajax({
        type: commentForm.attr('method'),
        url: commentForm.attr('action'),
        data: commentForm.serialize(),
        dataType : "html",
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(errorThrown);
        },
        success: function(html) {
//            alert(html)

            var commentList;
            if (commentForm.siblings('.comments').length === 0) {
                var commentClass = createCommentClass();
                commentForm.parent().children('.post').after(commentClass);
                commentList = commentClass;
            } else {
                commentList = commentForm.siblings('.comments');
            }

            commentList.append(html);

            commentForm.find('textarea').val("")

        }
    });
};
//var ajaxPostComment = function(e) {
//    e.preventDefault();
//
//    var commentForm = $(this);
//    commentForm.children('input[name="csrfmiddlewaretoken"]').val(csrfToken);
//
//    $.ajax({
//        type: commentForm.attr('method'),
//        url: commentForm.attr('action'),
//        data: commentForm.serialize(),
//        error: function(jqXHR, textStatus, errorThrown) {
//            console.log(errorThrown);
//        },
//        success: function(data, textStatus, jqXHR) {
//            if (data.success === false) {
//                alert(data.error);
//                return ;
//            }
//            var responseData = data.responseData;
//            console.log(responseData);
//
//            var comments;
//            if (commentForm.siblings('.comments').length === 0) {
//                var commentClass = createCommentClass();
//                commentForm.parent().children('.post').after(commentClass);
//                commentList = commentClass;
//            } else {
//                commentList = commentForm.siblings('.comments');
//            }
//
//            commentList.append(createCommentContent(responseData));
//
//            commentForm.find('textarea').val("")
//        }
//    });
//};
//
//
var createCommentClass = function() {
    return $('<div class="comments"></div>')
}

//var createCommentContent = function(responseData){
//    return $('<div class="row"></div>').append(createUserPhoto(responseData.userId)).append(createUserComment(responseData.userId, responseData.userName, responseData.commentContent));;
//}
//var createUserPhoto = function(userId) {
//     return $('<div class="col-sm-1"></div>').append('<p></p>').append(
//        $('<img/>').attr({'src':"/photo/" + userId, 'height':"40", 'width':"40", 'alt':"User avatar"})
//     );
//}
//var createUserComment = function(userId, userName, commentContent) {
//    var userInfo =
//                        $('<a></a>').attr('href', "/profile/" + userId).append(
//                            $('<h5></h5>').text(userName)
//                        )
//                    ;
//    var content = $('<h5></h5>').html(
//                            commentContent
//                         );
//
//    return $('<div class="col-sm-11"></div>').append(userInfo).append(content);
//}
//
