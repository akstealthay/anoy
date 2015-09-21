var showError = function(response) {
    alert(response.error);
};

var showWaiting = function(targetElement) {
    targetElement.html('<i class="fa fa-spinner fa-spin"></i>');
}

var removeWaiting = function(targetElement) {
    targetElement.html(null);
}

var showDialog = function() {
    $('body').bPopup();
};

var updateContextMenu = function() {
    // Add it to context menu
    var listTags = [];
    $.each($('#tags ul').children(), function(index, value) {
        listTags.push({
            text: value.textContent,
            action: function(event) {
                var range = window.getSelection().getRangeAt(0);
                var selectionContents = range.extractContents();
                var div = document.createElement("span");
                div.style.color = "red";
                div.appendChild(selectionContents);
                range.insertNode(div);
            }
        });
    });
    context.attach('#content', listTags);
};