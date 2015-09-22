var uiModulesClass = function() {
    /*
     *  uiModulesClass: Class that defines the UI Modules
     *  Contains all the methods that would enable showing errors,
     *  show waiting ticker, context menu .. etc.
     */

    this.showError = function(response) {
        alert(response.error);
    };

    this.showWaiting = function(targetElement) {
        targetElement.html('<i class="fa fa-spinner fa-spin"></i>');
    }

    this.removeWaiting = function(targetElement) {
        targetElement.html(null);
    }

    this.updateContextMenu = function() {
        // Add it to context menu
        var listTags = [];
        $.each($('#tags ul').children(), function(index, value) {
            listTags.push({
                text: value.textContent,
                action: function(event) {
                    var range = window.getSelection().getRangeAt(0);
                    var selectionContents = range.extractContents();
                    
                    if(selectionContents.textContent.length == 0 ) {
                        /* If nothing is selected then directly return */
                        return;
                    }

                    var div = document.createElement("span");
                    div.style.color = "red";
                    div.appendChild(selectionContents);
                    range.insertNode(div);

                    // Notify the save method
                }
            });
        });
        context.attach('#content', listTags);
    };
};