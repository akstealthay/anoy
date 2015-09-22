var tagapiClass = function(areaId) {
    
    var rawContent          = null;

    this.getAreaId = function() {
        return areaId;
    };

    this.getRawContent = function() {
        return rawContent;
    };

    this.setRawContent = function(content) {
        rawContent = content.replace(/\n/g, '<br/>');
        $(areaId).html(rawContent);
    };

    this.addProfile = function(profileName) {
        if (!profileName) {
            alert('Please enter name of the profile');
            return;
        }

        $.post( "/act/" + profileName, {action:'add'},function( response ) {
            if (response.error) {
                showError(response);
                return;
            }
            $('#profiles').append($('<option>').html(profileName));
            $('#new-profile-entry').val(null);

        });
    };

    this.addTag = function(tagName, profileName) {
        if (!tagName) {
            alert('Please enter appropriate value of the tag');
            return;
        }

        if (!profileName) {
            alert('No profile selected. Select a profile first.');
            return;
        }

        $.post( "/act/" + profileName + '/' + tagName, {action:'add'},function( response ) {
            if (response.error) {
                showError(response);
                return;
            }

            $('#new-tag-entry').val(null);
            $('#tags ul').append($('<li>').addClass('tag').html(tagName));

            updateContextMenu();

        });
    };
};